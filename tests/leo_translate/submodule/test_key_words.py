import unittest

from leo_translate.submodule.key_words import AllKeyWords


class TestKeyWordsMethods(unittest.TestCase):
    def test_bool(self):
        if_key = AllKeyWords.IF.value
        table_list = AllKeyWords.get_table_p_one()
        print("if_key", if_key)
        print("table_list", table_list)


if __name__ == '__main__':
    unittest.main()
