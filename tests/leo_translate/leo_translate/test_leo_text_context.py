import unittest

from leo_translate.context import Leo_context
from leo_translate.core_module import Struct, Transition
from leo_translate.submodule import Integer, Sign
from leo_translate.utils.utils import table_format_control
from tests.leo_translate.core_module.test_func import generate_body


class TestLeoContextMethods(unittest.TestCase):
    def test_add_struct(self):
        struct_name = "Axis"
        name_and_type = {'node_name': 'u8', 'right': 'bool', 'left': 'bool'}
        context = Leo_context()
        context.add_struct(struct_name, name_and_type)
        struct_str = ""
        for line in context.generate_struct():
            struct_str += line
        print(struct_str)
        self.assertTrue(struct_str, """struct Axis { 
node_name: u8;
right: bool;
left: bool;
}""")

    def test_add_transition(self):
        variate = 'get_function'
        u32 = Integer.UINT32.value
        input1 = 'x'
        inputs = f"{input1}{Sign.COLON.value} {u32}"
        # l = Transition(inputs, u32, generate_body(), variate)
        context = Leo_context()
        context.add_transition(variate, inputs, u32, generate_body())
        transition_str = ""
        for line in context.generate_transition():
            transition_str += line
        print(transition_str)
        self.assertTrue(transition_str, """transition get_function (x: u32) -> u32 {
let a: u32 = 9u32;
return 2u32;
}""")

    def test_generate_leo(self):
        struct_name = "Axis"
        name_and_type = {'node_name': 'u8', 'right': 'bool', 'left': 'bool'}
        context = Leo_context()
        context.add_struct(struct_name, name_and_type)
        variate = 'get_function'
        u32 = Integer.UINT32.value
        input1 = 'x'
        inputs = f"{input1}{Sign.COLON.value} {u32}"
        context.add_transition(variate, inputs, u32, generate_body())
        context.add_function(variate, inputs, u32, generate_body())

        data_arr = context.generate_leo_code_list()
        data_arr = table_format_control(data_arr)
        transition_str = ""
        for line in data_arr:
            transition_str += line
        print(transition_str)


if __name__ == '__main__':
    unittest.main()
