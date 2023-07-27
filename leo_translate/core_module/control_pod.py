from leo_translate.core_module.statement_pod import Statement
from leo_translate.submodule import AllKeyWords, Sign


def get_conditional(left_value, right_value, sign):
    return f"{left_value} {sign} {right_value}"


class IfControl(Statement):

    def __init__(self, left_value, right_value, sign, body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.body = body

    def get(self):
        if self.body == '':
            return ''
        return f"{AllKeyWords.IF.value} {Sign.LEFT_PARENTHESIS.value} " \
               f"{get_conditional(self.left_value, self.right_value, self.sign)} {Sign.RIGHT_PARENTHESIS.value} " \
               f"{Sign.LEFT_BRACE.value} \n{self.body}\n{Sign.RIGHT_BRACE.value} "


class ElifControl(Statement):

    def __init__(self, left_value, right_value, sign, body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.body = body

    def get(self):
        if self.body == '':
            return ''
        return f"{AllKeyWords.ELIF.value} {Sign.LEFT_PARENTHESIS.value} " \
               f"{get_conditional(self.left_value, self.right_value, self.sign)} {Sign.RIGHT_PARENTHESIS.value} " \
               f"{Sign.LEFT_BRACE.value}\n{self.body}\n{Sign.RIGHT_BRACE.value} "


class ElseControl(Statement):
    def __init__(self, body):
        self.body = body

    def get(self):
        if self.body == '':
            return ''

        return f"{AllKeyWords.ELSE.value} {Sign.LEFT_BRACE.value} " \
               f"\n{self.body}\n{Sign.RIGHT_BRACE.value} "


class IfElseControl(Statement):
    def __init__(self, left_value, right_value, sign, if_body, else_body):
        self.left_value = left_value
        self.right_value = right_value
        self.sign = sign
        self.if_body = if_body
        self.else_body = else_body

    def get(self):
        return IfControl(self.left_value, self.right_value, self.sign, self.if_body).get() + \
            ElseControl(self.else_body).get()



