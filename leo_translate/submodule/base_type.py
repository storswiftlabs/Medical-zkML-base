from enum import Enum


class Integer(Enum):
    INT8 = "i8"
    INT16 = "i16"
    INT32 = "i32"
    INT64 = "i64"
    INT128 = "i128"
    UINT8 = "u8"
    UINT16 = "u16"
    UINT32 = "u32"
    UINT64 = "u64"
    UINT128 = "u128"


class Boolean(Enum):
    TYPE = "bool"
    FALSE = False
    TRUE = True
