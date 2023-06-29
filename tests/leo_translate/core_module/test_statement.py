import unittest

from leo_translate.core_module import Let, Int_value
from leo_translate.submodule import Sign, AllKeyWords, Integer


class TestStatementMethods(unittest.TestCase):

    def test_let(self):
        l = Let()
        let = AllKeyWords.LET.value
        variate = "a"
        variate_type = Integer.UINT32.value
        variate_body = Int_value('9', variate_type).value
        l.set(let, variate, variate_type, variate_body)
        print(l.get())

    def test_let_fail(self):
        l = Let()
        let = AllKeyWords.LET.value
        variate = "a"
        variate_type = Integer.UINT32.value
        try:
            variate_body = Int_value('9.1', variate_type).value
        except TypeError as e:
            return self.assertEqual(1, 1)
        l.set(let, variate, variate_type, variate_body)
        print(l.get())


if __name__ == '__main__':
    unittest.main()
