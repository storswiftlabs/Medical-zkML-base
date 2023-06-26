import abc
import typing as tp

from .syntax import (LeoOperators, LeoPunctuation,
                     LeoStatements, LeoTypes, StructTypes)


class LeoNode(abc.ABC):
    """
    Abstract class for Leo AST nodes.
    """

    @abc.abstractmethod
    def to_code(self, tabs: int = 0) -> str:
        """
        Convert the Leo AST node to a Leo program.

        :param tabs: Number of tabs to indent the code
        :return: Leo program
        """
        raise NotImplementedError("Abstract method")


class LeoIfElseNode(LeoNode):
    """
    Leo AST node for if-else statements.
    """
    def __init__(self, condition: str, if_node: LeoNode, else_node: LeoNode):
        self.condition = condition
        self.if_node = if_node
        self.else_node = else_node

    def to_code(self, tabs: int = 0) -> str:
        if_code = self.if_node.to_code(tabs + 1)
        else_code = self.else_node.to_code(tabs + 1)
        return "{}{} {} {} {} {} {}{} {}{}{} {} {} {}{} {}{}{}".format(
            LeoPunctuation.TAB.value * tabs,
            LeoStatements.IF.value,
            LeoPunctuation.LEFT_BRACKET.value,
            self.condition,
            LeoPunctuation.RIGHT_BRACKET.value,
            LeoPunctuation.LEFT_CURLY_BRACKET.value,
            LeoPunctuation.NL.value,
            if_code,
            LeoPunctuation.NL.value,
            LeoPunctuation.TAB.value * tabs,
            LeoPunctuation.RIGHT_CURLY_BRACKET.value,
            LeoStatements.ELSE.value,
            LeoPunctuation.LEFT_CURLY_BRACKET.value,
            LeoPunctuation.NL.value,
            else_code,
            LeoPunctuation.NL.value,
            LeoPunctuation.TAB.value * tabs,
            LeoPunctuation.RIGHT_CURLY_BRACKET.value
        )


class LeoReturnNode(LeoNode):
    """
    Leo AST node for a return statement.
    """
    def __init__(self, value: str):
        self.value = value

    def to_code(self, tabs: int = 0) -> str:
        return "{}{} {}{}".format(
            LeoPunctuation.TAB.value * tabs,
            LeoStatements.RETURN.value,
            self.value,
            LeoPunctuation.SEMINCOLON.value
        )


class LeoFunctionDeclarationNode(LeoNode):
    """
    Leo AST node for a function declaration.
    """
    def __init__(
            self,
            func_type: str,
            func_name: str,
            input_arg_names: tp.List[str],
            input_arg_types: tp.List[StructTypes],
            output_arg_type: tp.Union[LeoTypes, str],
            body: LeoNode
    ):
        self.func_type = func_type
        self.func_name = func_name
        self.input_arg_names = input_arg_names
        self.input_arg_types = input_arg_types
        self.output_arg_type = output_arg_type
        self.body = body

    def to_code(self, tabs: int = 0) -> str:
        input_args = [f"{self.input_arg_names[i]}{LeoPunctuation.COLON.value} {t.value}" for i, t in
                      enumerate(self.input_arg_types)]
        input_args = f"{LeoPunctuation.COMMA.value} ".join(input_args)
        body = self.body.to_code(tabs + 1)

        return "{}{} {} {} {} {} {} {} {} {}{} {}{}{}".format(
            LeoPunctuation.TAB.value * tabs,
            self.func_type,
            self.func_name,
            LeoPunctuation.LEFT_BRACKET.value,
            input_args,
            LeoPunctuation.RIGHT_BRACKET.value,
            LeoPunctuation.RIGHT_ARROW.value,
            self.output_arg_type.value if isinstance(self.output_arg_type, LeoTypes) else self.output_arg_type,
            LeoPunctuation.LEFT_CURLY_BRACKET.value,
            LeoPunctuation.NL.value,
            body,
            LeoPunctuation.NL.value,
            LeoPunctuation.TAB.value * tabs,
            LeoPunctuation.RIGHT_CURLY_BRACKET.value
        )


class LeoAssignNode(LeoNode):
    """
    Leo AST node for an assignment statement.
    """
    def __init__(self, var_name: str, var_type: LeoTypes, expression: str):
        self.var_name = var_name
        self.var_type = var_type
        self.expression = expression

    def to_code(self, tabs: int = 0) -> str:
        return "{}{} {}{} {} {} {}{}".format(
            LeoPunctuation.TAB.value * tabs,
            LeoStatements.LET.value,
            self.var_name,
            LeoPunctuation.COLON.value,
            self.var_type.value,
            LeoOperators.EQUAL.value,
            self.expression,
            LeoPunctuation.SEMINCOLON.value
        )


class LeoSumNode(LeoAssignNode):
    """
    Leo AST node for a multiple arguments sum.
    """
    def __init__(self, var_name: str, var_type: LeoTypes, args: tp.List[str]):
        expression = f" {LeoOperators.PLUS.value} ".join(args)
        super().__init__(var_name, var_type, expression)


class LeoFunctionCall(LeoAssignNode):
    """
    Leo AST node for a function call.
    """
    def __init__(self, var_name: str, var_type: LeoTypes, func_name: str, func_args: tp.List[str]):
        expression = f"{func_name}({f'{LeoPunctuation.COMMA.value} '.join(func_args)})"
        super().__init__(var_name, var_type, expression)


class LeoStructDeclarationNode(LeoNode):
    """
    Leo AST node for a struct declaration.
    """
    def __init__(self, struct_name: str, field_names: tp.List[str], field_types: tp.List[LeoTypes]):
        self.struct_name = struct_name
        self.field_names = field_names
        self.field_types = field_types

    def to_code(self, tabs: int = 0) -> str:
        fields = [f"{n}{LeoPunctuation.COLON.value} {t.value}" for n, t in zip(self.field_names, self.field_types)]
        fields = f"{LeoPunctuation.COMMA.value} ".join(fields)

        return "{}{} {} {} {} {}".format(
            LeoPunctuation.TAB.value * tabs,
            LeoStatements.STRUCT.value,
            self.struct_name,
            LeoPunctuation.LEFT_CURLY_BRACKET.value,
            fields,
            LeoPunctuation.RIGHT_CURLY_BRACKET.value
        )


class LeoStructInitNode(LeoNode):
    """
    Leo AST node for a struct initialization.
    """
    def __init__(self, struct_name: str, field_names: tp.List[str], arg_names: tp.List[str]):
        self.struct_name = struct_name
        self.field_names = field_names
        self.arg_names = arg_names

    def to_code(self, tabs: int = 0) -> str:
        fields = [f"{n}{LeoPunctuation.COLON.value} {a}" for n, a in zip(self.field_names, self.arg_names)]
        fields = f"{LeoPunctuation.COMMA.value} ".join(fields)

        return "{} {} {} {}".format(
            self.struct_name,
            LeoPunctuation.LEFT_CURLY_BRACKET.value,
            fields,
            LeoPunctuation.RIGHT_CURLY_BRACKET.value
        )


class LeoSequentialNode(LeoNode):
    """
    Leo AST node for a sequential node.
    """
    def __init__(self, nodes: tp.List[LeoNode], lines: int = 1):
        self.nodes = nodes
        self.lines = lines

    def to_code(self, tabs: int = 0) -> str:
        codes = [node.to_code(tabs) for node in self.nodes]
        code = (LeoPunctuation.NL.value * self.lines).join(codes)
        return code


__all__ = [
    "LeoNode",
    "LeoIfElseNode",
    "LeoReturnNode",
    "LeoStructDeclarationNode",
    "LeoStructInitNode",
    "LeoFunctionDeclarationNode",
    "LeoAssignNode",
    "LeoSumNode",
    "LeoFunctionCall",
    "LeoSequentialNode"
]
