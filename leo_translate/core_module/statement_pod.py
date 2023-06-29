from abc import ABC, abstractmethod


class Statement(ABC):
    """
    Code statement:The function body contains a set of statements that define the task the function performs.
    """

    @abstractmethod
    def get(self):
        # Get a line code statement
        pass


class Let(Statement):
    let_statement = "{let} {variate}: {variate_type} = {variate_body};"

    def set(self, let, variate, variate_type, variate_body):
        # Get a line code statement
        self.let_statement = f"{let} {variate}: {variate_type} = {variate_body};"

    def get(self):
        # Get a line code statement
        return self.let_statement


class LetStruct(Let):
    let_statement = "{let} {variate}: {struct_name} = {variate_body};"

    def set(self, let, variate, struct_obj, values):
        # Get a line code statement
        # todo struct class "get_struct()" ".name".     LetStruct function struct_body
        struct = struct_obj.get_struct()
        self.let_statement = f"{let} {variate}: {struct_obj.name} = {self.struct_body(struct, values)};"

    def get(self):
        # Get a line code statement
        return self.let_statement

    def struct_body(self, struct, values: list):
        # Generates struct body from the struct object and values
        pass
