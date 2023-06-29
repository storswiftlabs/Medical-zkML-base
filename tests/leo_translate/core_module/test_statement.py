import unittest

from leo_translate.core_module import Let, Int_value
from leo_translate.core_module import LetStruct
from leo_translate.core_module import Struct
from leo_translate.submodule import Sign, AllKeyWords, Integer


class TestStatementMethods(unittest.TestCase):

    def test_let(self):
        let = AllKeyWords.LET.value
        variate = 'a'
        variate_type = Integer.UINT32.value
        variate_body = Int_value('9', variate_type).value
        l = Let(variate, variate_type, variate_body)
        print(l.get())
        assert l.let_statement == "let a: u32 = 9u32;"

    @unittest.expectedFailure
    def test_let_fail(self):
        l = Let()
        let = AllKeyWords.LET.value
        variate = 'a'
        variate_type = Integer.UINT32.value
        try:
            variate_body = Int_value('9.1', variate_type).value
        except TypeError as e:
            return self.assertEqual(1, 1)
        l.set(let, variate, variate_type, variate_body)

    def test_let_struct(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        dataset = Struct(struct_name, name_and_type)
        values = [1, 2, 3, 4]
        ls = LetStruct('dataset', dataset, values)
        print(ls.get())
        assert ls.let_statement == "let dataset: Dataset = Dataset{node: 1u32, son_node_nums: 2u8, level: 3u8, weight: 4u16};"

    @unittest.expectedFailure
    def test_let_struct_fail(self):
        struct_name = "Dataset"
        name_and_type = {"node": "u32", "son_node_nums": "u8", "level": "u8", "weight": "u16"}
        dataset = Struct(struct_name, name_and_type)
        values = [1, 2, 3, 4, 6]
        ls = LetStruct('dataset', dataset, values)


if __name__ == '__main__':
    unittest.main()
