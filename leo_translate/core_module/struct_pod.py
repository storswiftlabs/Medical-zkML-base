from leo_translate.submodule import AllKeyWords, Sign


class Struct:
    def __init__(self, struct_name, name_and_type: dict):
        #  generate struct for context
        self.struct_name = struct_name
        self.name_and_type = name_and_type

    def generate_leo_struct(self):
        # return a string, Leo defined code style, for example ""
        struct_multi_lines = f"{AllKeyWords.STRUCT.value} {str(self.struct_name)} {Sign.LEFT_BRACE.value} \n"
        for k, v in self.name_and_type.items():
            struct_multi_lines += f"{k}{Sign.COLON.value} {v}{Sign.SEMICOLON.value}\n"
        struct_multi_lines += f"{Sign.RIGHT_BRACE.value}"
        return struct_multi_lines
