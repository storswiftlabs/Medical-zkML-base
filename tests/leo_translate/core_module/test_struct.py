import unittest

from leo_translate.core_module import Struct


class TestStructMethods(unittest.TestCase):
    def test_generate_struct(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        print(Struct(struct_name, name_and_type).generate_leo_struct())


if __name__ == '__main__':
    unittest.main()
