from abc import ABC, abstractmethod

from leo_translate.submodule import AllKeyWords, Sign, Integer

LET = AllKeyWords.LET.value


class Func(ABC):
    """
    Code function:The function body contains a set of functions that define the task the function performs.
    """

    @abstractmethod
    def get(self):
        pass
        # Get a line code function


class Function(Func):
    # let function: {let} {variate}: {variate_type} = {variate_body};

    def __init__(self, variate, inputs: str, result_type, body: list):
        # Get a line code function
        self.inputs = inputs
        self.head_line = f"{AllKeyWords.FUNCTION.value} {variate} {Sign.LEFT_PARENTHESIS.value}{self.inputs}" \
                         f"{Sign.RIGHT_PARENTHESIS.value} {Sign.RESULT.value} {result_type} {Sign.LEFT_BRACE.value}"
        self.end_line = f"{Sign.RIGHT_BRACE.value}"
        self.body = body

    def get(self):
        # Get a line code function
        body = ""
        for line in self.body:
            body += line + '\n'
        return f"{self.head_line}\n{body}{self.end_line}\n"


class Transition(Func):
    # struct function: {let} {variate}: {struct_name} = {variate_body};

    def __init__(self, variate: str = "main", inputs: str = "", result_type="", body=""):
        # Get a line code function
        self.inputs = inputs
        self.head_line = f"{AllKeyWords.TRANSITION.value} {variate} {Sign.LEFT_PARENTHESIS.value}{self.inputs}" \
                         f"{Sign.RIGHT_PARENTHESIS.value} {Sign.RESULT.value} {result_type} {Sign.LEFT_BRACE.value}"
        self.end_line = f"{Sign.RIGHT_BRACE.value}"
        self.body = body

    def get(self):
        # Get a line code function
        body = ""
        for line in self.body:
            body += line + '\n'
        return f"{self.head_line}\n{body}{self.end_line}\n"


class Finalize(Func):
    # struct function: {let} {variate}: {struct_name} = {variate_body};

    def __init__(self, variate, inputs: str, result_type, body):
        # Get a line code function
        pass
        self.inputs = inputs
        self.head_line = f"{AllKeyWords.FINALIZE.value} {variate} {Sign.LEFT_PARENTHESIS.value}{self.inputs}" \
                         f"{Sign.RIGHT_PARENTHESIS.value} {Sign.RESULT.value} {result_type} {Sign.LEFT_BRACE.value}"
        self.end_line = f"{Sign.RIGHT_BRACE.value}"
        self.body = body

    def get(self):
        # Get a line code function
        pass
        body = ""
        for line in self.body:
            body += line + '\n'
        return f"{self.head_line}\n{body}{self.end_line}\n"
