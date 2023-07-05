from enum import Enum


class AllKeyWords(Enum):
    IMPORT = 'import'
    LET = 'let'
    ASSERT = 'assert'
    ASSERT_NEQ = 'assert_neq'
    ASSERT_EQ = 'assert_eq'
    THEN = 'then'
    RETURN = 'return'
    ALEO = 'aleo'
    """
    "\t" number +1 key words
    """
    RECORD = 'record'
    FOR = 'for'
    IF = 'if'
    ELSE = 'else'
    ELIF = f'{ELSE} {IF}'
    FUNCTION = 'function'
    TRANSITION = 'transition'
    STRUCT = 'struct'
    PROGRAM = 'program'
    INLINE = 'inline'
    FINALIZE = 'finalize'

    @classmethod
    def get_table_p_one(cls):
        return [cls.RECORD.value, cls.FOR.value, cls.IF.value, cls.ELSE.value, cls.ELIF.value, cls.FUNCTION.value,
                cls.TRANSITION.value, cls.STRUCT.value, cls.PROGRAM.value, cls.INLINE.value, cls.FINALIZE.value]
