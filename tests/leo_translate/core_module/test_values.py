import unittest

from leo_translate.core_module import Int_value, BoolValue
from leo_translate.submodule import Integer, Boolean


class TestValueMethods(unittest.TestCase):

    def test_integer(self):
        # int
        i8 = Int_value(8, Integer.INT8.value)
        print(i8.get())
        i16 = Int_value(8, Integer.INT16.value)
        print(i16.get())
        i32 = Int_value(8, Integer.INT32.value)
        print(i32.get())
        i64 = Int_value(8, Integer.INT64.value)
        print(i64.get())
        i128 = Int_value(8, Integer.INT128.value)
        print(i128.get())

        # uint
        u8 = Int_value(8, Integer.UINT8.value)
        print(u8.get())
        u16 = Int_value(8, Integer.UINT16.value)
        print(u16.get())
        u32 = Int_value(8, Integer.UINT32.value)
        print(u32.get())
        u64 = Int_value(8, Integer.UINT64.value)
        print(u64.get())
        u128 = Int_value(8, Integer.UINT128.value)
        print(u128.get())

    def test_bool(self):
        print(Boolean.TYPE.value)


if __name__ == '__main__':
    unittest.main()
