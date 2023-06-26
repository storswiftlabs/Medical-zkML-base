import typing as tp

from ..boostings.core import BoostingTranspiler
from ..leo import LeoIfElseNode, LeoNode, LeoReturnNode
from ..quantize import quantize


class XgboostTranspiler(BoostingTranspiler):
    """
    Transpiler for XGBoost models.
    """
    def __init__(self, model, quantize_bits: int = 8):
        """
        :param model: The XGBoost model.
        :param quantize_bits: The number of bits to quantize to.
        """
        trees = model.get_booster()
        super().__init__(
            model=model,
            feature_names=trees.feature_names,
            n_classes=hasattr(model, "n_classes_") and model.n_classes_ or None,
            n_estimators=model.n_estimators,
            quantize_bits=quantize_bits
        )

        self._dfs = []
        for i in range(self.n_estimators):
            df = trees[i].trees_to_dataframe()
            if self.is_regression:
                self._dfs.append(df)
            else:
                for c in range(self.n_classes):
                    class_df = df[df["Tree"] == c].reset_index(drop=True)
                    self._dfs.append(class_df)

    def get_leo_ast_nodes(self) -> tp.List[LeoNode]:
        return [self.build_tree(df, df.iloc[0]) for df in self._dfs]

    def build_tree(self, df, df_node) -> LeoNode:
        feature_name = df_node["Feature"]
        if feature_name != "Leaf":
            if_node_id = df_node["Yes"]
            else_node_id = df_node["No"]

            if_node = df.iloc[self.node_id_to_idx(if_node_id)]
            else_node = df.iloc[self.node_id_to_idx(else_node_id)]

            value = quantize(df_node["Split"], self.quantize_bits)

            condition = f"inputs.{feature_name} < {value}"

            left = self.build_tree(df, if_node)
            right = self.build_tree(df, else_node)
            return LeoIfElseNode(condition, left, right)
        else:
            value = quantize(df_node["Gain"], self.quantize_bits)
            return LeoReturnNode(value)

    @staticmethod
    def node_id_to_idx(node_id: str) -> int:
        return int(node_id.split("-")[1])
