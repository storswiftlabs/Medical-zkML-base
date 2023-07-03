from leo_translate.core_module import Struct, Transition
from leo_translate.core_module.func_pod import Func, Function, Finalize
from leo_translate.submodule import AllKeyWords, Sign


class Leo_context:
    def __init__(self):
        # User init leo_context, use context structure leo code
        """
        function_list []Func (func_type, func_data)
        struct_list []Struct
        variates {inputs：[], struct: [], map: [], let: []}
        """
        self.function_list = []
        self.struct_list = []
        self.variates = dict

    def add_struct(self, struct_name, name_and_type: dict):
        # Define a structure
        leo_struct = Struct(struct_name, name_and_type)
        self.struct_list.append(leo_struct)

    def add_map(self, map_name, k_v_type: dict):
        pass

    def add_transition(self, variate, inputs: str, return_type, body):
        # Define a transition
        tran = Transition(variate, inputs, return_type, body)
        self.function_list.append(tran)

    def add_function(self, variate, inputs: str, return_type, body):
        func = Function(variate, inputs, return_type, body)
        self.function_list.append(func)

    def generate_struct(self):
        leo_lines = []
        # Fill struct definition
        for struct in self.struct_list:
            leo_lines.append(struct.generate_leo_struct())
        return leo_lines

    def add_finalize(self, variate, inputs: str, return_type, body):
        final = Finalize(inputs, return_type, body, variate)
        self.function_list.append(final)

    def generate_map(self, map_name, k_v_type: dict):
        pass

    def generate_transition(self):
        # Fill transition
        leo_lines = []
        for func in self.function_list:
            if type(func) is Transition:
                leo_lines.append(func.get())
        return leo_lines

    def generate_function(self):
        pass

    def generate_finalize(self):
        pass

    def generate_leo_code_list(self, leo_name="main"):
        leo_lines = []
        leo_lines.append(
            f"{AllKeyWords.PROGRAM.value} {leo_name}{Sign.POINT.value}{AllKeyWords.ALEO.value}{Sign.LEFT_BRACE.value}\n")
        # Fill struct definition
        for struct in self.struct_list:
            leo_lines.append(struct.generate_leo_struct())
        # Fill function
        for func in self.function_list:
            if type(func) is Function:
                leo_lines.append(func.get())
        # Fill transition
        for func in self.function_list:
            if type(func) is Transition:
                leo_lines.append(func.get())
        # Fill finalize
        for func in self.function_list:
            if type(func) is Finalize:
                leo_lines.append(func.get())
        leo_lines.append(f"{Sign.RIGHT_BRACE.value}")
        return leo_lines
