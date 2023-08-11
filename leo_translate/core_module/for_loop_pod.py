from leo_translate.core_module.statement_pod import Statement
from leo_translate.submodule import AllKeyWords, Sign


class ForLoop(Statement):

    def __init__(self, variate, variate_type, start_variate, end_variate, body):
        self.variate = variate
        self.variate_type = variate_type
        self.start_variate = start_variate
        self.end_variate = end_variate
        self.body = body

    def get(self):
        return f"{AllKeyWords.FOR.value} {self.variate}: {self.variate_type} in {self.start_variate}.." \
               f"{self.end_variate}{Sign.LEFT_BRACE.value} \n{self.body};\n{Sign.RIGHT_BRACE.value}\n"
