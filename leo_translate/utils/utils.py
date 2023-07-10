import numpy as np

from leo_translate.submodule import Integer


def table_format_control(data):
    """
    table_format_control: Format output for list [str]
    inputs:
        data: list[str]
    return:
        new_data: Formatted list [str]
    """
    if type(data) is str:
        data = data.split('\n')
    else:
        all_data = ""
        for element in data:
            all_data += element
        data = all_data.split('\n')
    control = 0
    new_data = []
    prev = ''
    first_key = ''
    last_key = ''
    for index in range(0, len(data)):
        if data[index] != '':
            last_key = data[index].rstrip().lstrip()[-1]
            first_key = data[index].rstrip().lstrip()[0]
        else:
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        if last_key == "}":
            control -= 1
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        if prev == "{":
            control += 1
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        if prev != "{" and first_key == "}":
            control -= 1
            new_data.append(generate_table(control) + data[index] + '\n')
            prev = last_key
            continue

        new_data.append(generate_table(control) + data[index] + '\n')
        prev = last_key
    return new_data


def generate_table(num):
    return '\t' * num


class data_control:
    """
    data_control: Input a float array and control the accuracy of the array to a certain extent
    """

    def __init__(self, line):
        # u8,u16,u32,u64,u128
        self.unsigned_number = ['0', Integer.UINT8.value, Integer.UINT16.value, Integer.UINT32.value,
                                Integer.UINT64.value, Integer.UINT128.value]
        self.signed_size = [0, 256, 65536, 4294967296, 18446744073709551616, 340282366920938463463374607431768211456]

        # i8,i16,i32,i64,i128
        self.signed_number = ['0', Integer.INT8.value, Integer.INT16.value, Integer.INT32.value, Integer.INT64.value,
                              Integer.INT128.value]
        self.unsigned_size = [0, 127, 32767, 2147483647, 9223372036854775807, 170141183460469231731687303715884105727]

        # Precision control of decimal places
        def decimal_significant_digits(line):
            temp = []
            sum = 0
            for index in range(0, len(line) - 1):
                sum += line[index]
            print(max(line) / 2, ">", sum / len(line))
            if max(line) / 2 > sum / len(line):
                for index in range(len(line)):
                    if isinstance(line[index], np.float64):
                        temp.append(round(line[index], 2))
                    else:
                        temp.append(line[index])
            else:
                for index in range(len(line)):
                    temp.append(line[index])
            return temp

        # self.line Precision controlled array
        self.line = decimal_significant_digits(line)

        # Determine if there are negative numbers in the array
        def is_negative(line) -> bool:
            for index in range(0, len(line) - 1):
                if line[index] < 0:
                    return True
            return False

        # self.line Is there a negative number
        self.is_negative = is_negative(line)

        # Expanding decimal places to integers
        def type_expansion():
            print("self.line: ", self.line)
            decimal_places = 0
            for index in range(0, len(self.line) - 1):
                num_str = str(self.line[index])
                if '.' in num_str:
                    temp = len(num_str) - num_str.index('.') - 1
                    if decimal_places < temp:
                        decimal_places = temp
            self.decimal_expansion = 10 ** decimal_places
            return 10 ** decimal_places

        # self.fixed_number Decimal expansion
        self.fixed_number = type_expansion()

        # Calculate Leo Display Declaration Type
        def leo_explicit_type():
            display_type = ''
            max_elem = abs(max(self.line)) * self.fixed_number
            if self.is_negative:
                display_type = Integer.INT8.value
                for index in range(1, len(self.signed_size)):
                    if self.signed_size[index] > max_elem > float(self.signed_size[index - 1]):
                        # If max_ If the value of elem is greater than i128, it will exceed the range
                        display_type = str(self.signed_number[index])
                        break
            else:
                display_type = Integer.UINT8.value
                for index in range(1, len(self.unsigned_size)):
                    if self.unsigned_size[index] > max_elem > float(self.unsigned_size[index - 1]):
                        # If max_ If the value of elem is greater than u128, it will exceed the range
                        display_type = str(self.unsigned_number[index])
                        break
            return display_type

        # self.display_type Leo Display Declaration Type
        self.display_type = leo_explicit_type()

    # Set the Leo display declaration type size
    def set_leo_display_type(self, value_type: str):
        assert value_type in ['i8', 'i16', 'i32', 'i64', 'i128','u8', 'u16', 'u32', 'u64', 'u128']
        self.display_type = value_type
