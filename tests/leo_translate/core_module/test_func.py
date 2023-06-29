import unittest

from leo_translate.core_module import Let, Int_value
from leo_translate.core_module import Function, Transition, Finalize
from leo_translate.core_module import LetStruct, ReturnStatement
from leo_translate.submodule import Sign, AllKeyWords, Integer


def generate_body():
    body = []
    let = AllKeyWords.LET.value
    variate = 'a'
    variate_type = Integer.UINT32.value
    variate_body = Int_value('9', variate_type).value
    l = Let(variate, variate_type, variate_body)
    body.append(l.get())
    body.append(ReturnStatement("2u32").get())
    return body


class TestFuncMethods(unittest.TestCase):

    def test_function(self):
        variate = 'get_function'
        u32 = Integer.UINT32.value
        input1 = 'x'
        inputs = f"{input1}{Sign.COLON.value} {u32}"
        l = Function(variate, inputs, u32, generate_body())
        print(l.get())
        assert l.get() == """function get_function (x: u32) -> u32 {
let a: u32 = 9u32;
return 2u32;
}"""

    def test_transition(self):
        variate = 'get_function'
        u32 = Integer.UINT32.value
        input1 = 'x'
        inputs = f"{input1}{Sign.COLON.value} {u32}"
        l = Transition(variate, inputs, u32, generate_body())
        print(l.get())
        assert l.get() == """transition get_function (x: u32) -> u32 {
let a: u32 = 9u32;
return 2u32;
}"""


if __name__ == '__main__':
    unittest.main()
