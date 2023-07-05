import unittest
from leo_translate.utils.utils import table_format_control


def generate_data():
    path = 'data/Acute_Inflammations/Acute_Inflammations_dt.leo'
    with open(path, mode='r', encoding='utf-8') as file:
        return file.read()


class TestTableMethod(unittest.TestCase):

    def test_table_format_control(self):
        data = """program dt.aleo {

struct Inputs {
p1: u32,
p2: u32,
p3: u32,
p4: u32,
p5: u32,
p6: u32,
}

//The original data type is float, which increases the precision of data by 10 times.
//Code auto generated from DecisionTreeClassifier using dt_to_leo_code.py.
transition main(inputs: Inputs) -> public u32 {

let a: u32 = 0u32;

for i in 0u32..10u32 {
a = a + i;
a = a + 1u32;
}

if (inputs.p3 < 5u32) {
if (inputs.p4 < 5u32) {
return 0u32;
} else {
return 1u32;
}
} else {
if (inputs.p1 < 380u32) {
return 0u32;
} else {
if (inputs.p5 < 5u32) {
return 2u32;
} else {
if (inputs.p4 < 5u32) {
return 2u32;
} else {
return 3u32;
}
}
}
}
}
}"""

        data_arr = table_format_control(data)
        with open('test.leo', mode='w+', encoding='utf-8') as file:
            for line in data_arr:
                file.write(line)


if __name__ == '__main__':
    unittest.main()
