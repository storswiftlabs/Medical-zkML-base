import enum


class StructTypes(enum.Enum):
    inputs = "Inputs"


class LeoTypes(enum.Enum):
    U8 = "u8"
    U16 = "u16"
    U32 = "u32"
    U64 = "u64"
    U128 = "u128"

    I8 = "i8"
    I16 = "i16"
    I32 = "i32"
    I64 = "i64"
    I128 = "i128"


class LeoStatements(enum.Enum):
    PROGRAM = "program"
    IMPORT = "import"
    TRANSITION = "transition"
    MAIN = "main"
    STRUCT = "struct"
    INLINE = "inline"
    FUNCTION = "function"
    IF = "if"
    ELSE = "else"
    RETURN = "return"
    LET = "let"


class LeoPunctuation(enum.Enum):
    COMMA = ","
    SEMINCOLON = ";"
    COLON = ":"
    RIGHT_ARROW = "->"
    LEFT_BRACKET = "("
    RIGHT_BRACKET = ")"
    LEFT_SQUARE_BRACKET = "["
    RIGHT_SQUARE_BRACKET = "]"
    LEFT_CURLY_BRACKET = "{"
    RIGHT_CURLY_BRACKET = "}"
    SPACE = " "
    TAB = " " * 4
    NL = "\n"


class LeoOperators(enum.Enum):
    EQUAL = "="
    PLUS = "+"
    MINUS = "-"
    GT = ">"
    LT = "<"
    GTE = ">="
    LTE = "<="


__all__ = [
    "LeoTypes",
    "LeoStatements",
    "LeoPunctuation",
    "LeoOperators"
]
