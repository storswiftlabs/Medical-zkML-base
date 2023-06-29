from leo_translate.core_module import Struct


class leo_context:
    def __init__(self):
        # User init leo_context, use context structure leo code
        self.struct_names = []
        self.function_names = []
        self.transition_inputs = []
        self.struct_list = []

    def add_struct(self, struct_name, name_and_type: dict):
        # Define a structure
        self.struct_names.append(struct_name)
        leo_struct = Struct(struct_name, name_and_type).generate_leo_struct()
        self.struct_list.append(leo_struct)

    def add_map(self, map_name, k_v_type: dict):
        pass
