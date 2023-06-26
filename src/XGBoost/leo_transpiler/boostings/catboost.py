import typing as tp

from .core import BoostingTranspiler
from ..leo import LeoNode


class CatboostTranspiler(BoostingTranspiler):

    def get_leo_ast_nodes(self) -> tp.List[LeoNode]:
        return NotImplemented("TODO")


__all__ = ["CatboostTranspiler"]
