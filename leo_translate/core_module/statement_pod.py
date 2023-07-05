from abc import ABC, abstractmethod

from leo_translate.core_module.struct_pod import Struct
from leo_translate.submodule import AllKeyWords, Sign

LET = AllKeyWords.LET.value


class Statement(ABC):
    """
    Code statement:The function body contains a set of statements that define the task the function performs.
    """

    @abstractmethod
    def get(self):
        pass
        # Get a line code statement


class Let(Statement):
    # let statement: {let} {variate}: {variate_type} = {variate_body};

    def __init__(self, variate, variate_type, variate_body):
        # Get a line code statement
        self.let_statement = f"{LET} {variate}: {variate_type} = {variate_body};"

    def get(self):
        # Get a line code statement
        return self.let_statement


def struct_body(struct, values: list):
    # Generates struct body from the struct object and values
    struct_name = struct.struct_name
    struct_body_multi_lines = f"{struct_name}{Sign.LEFT_BRACE.value}"
    for i, (field_name, field_type) in enumerate(struct.name_and_type.items()):
        if i == len(values) - 1:
            # last line
            struct_body_multi_lines += f"{field_name}{Sign.COLON.value} {values[i]}{field_type}{Sign.RIGHT_BRACE.value}"
        else:
            struct_body_multi_lines += f"{field_name}{Sign.COLON.value} {values[i]}{field_type}{Sign.COMMA.value} "
    return struct_body_multi_lines


class LetStruct(Statement):
    # struct statement: {let} {variate}: {struct_name} = {variate_body};
    def __init__(self, variate, struct_obj: Struct, values: list):
        # Get a line code statement
        if len(values) != len(struct_obj.name_and_type):
            raise IndexError(
                "statement_pod::LetStruct::__init__: \"Inputs 'values' unequal to the field of the struct\"")
        self.let_statement = f"{LET} {variate}: {struct_obj.struct_name} = {struct_body(struct_obj, values)};"

    def get(self):
        # Get a line code statement
        return self.let_statement


class ReturnStatement(Statement):
    def __init__(self, value: str):
        # Get a line code statement, value: struct, Value, variate
        self.let_statement = f"{AllKeyWords.RETURN.value} {value};"

    def get(self):
        # Get a line code statement
        return self.let_statement
