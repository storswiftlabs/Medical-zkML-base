import unittest

from leo_translate.submodule.sign import Sign


class TestSignMethods(unittest.TestCase):
    def test_bool(self):
        multi = Sign.MULTI.value
        print(multi)


if __name__ == '__main__':
    unittest.main()
