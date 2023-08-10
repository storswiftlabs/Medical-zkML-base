import unittest
from leo_translate.utils.utils import table_format_control


def generate_data():
    path = 'data/Acute_Inflammations/Acute_Inflammations_dt.leo'
    with open(path, mode='r', encoding='utf-8') as file:
        return file.read()


class TestTableMethod(unittest.TestCase):

    def test_table_format_control(self):
        data = """program zk_ml_for_aleo_v2.aleo {
    struct Inputs {w1_0_0: i16, w1_0_1: i16, w1_0_2: i16, w1_0_3: i16, b1_0: i16, w1_1_0: i16, w1_1_1: i16, w1_1_2: i16, w1_1_3: i16, b1_1: i16, w1_2_0: i16, w1_2_1: i16, w1_2_2: i16, w1_2_3: i16, b1_2: i16, w1_3_0: i16, w1_3_1: i16, w1_3_2: i16, w1_3_3: i16, b1_3: i16, w2_0_0: i16, w2_0_1: i16, w2_0_2: i16, w2_0_3: i16, b2_0: i16, w2_1_0: i16, w2_1_1: i16, w2_1_2: i16, w2_1_3: i16, b2_1: i16, w2_2_0: i16, w2_2_1: i16, w2_2_2: i16, w2_2_3: i16, b2_2: i16, input0: i16, input1: i16, input2: i16, input3: i16}
transition main(inputs: Inputs) -> (i16, i16, i16) {
let neuron0_0: i16 = inputs.input0 / 16i16;
let neuron0_1: i16 = inputs.input1 / 16i16;
let neuron0_2: i16 = inputs.input2 / 16i16;
let neuron0_3: i16 = inputs.input3 / 16i16;
let neuron1_0: i16 = rectified_linear_activation(neuron0_0 * inputs.w1_0_0 / 16i16 + neuron0_1 * inputs.w1_0_1 / 16i16 + neuron0_2 * inputs.w1_0_2 / 16i16 + neuron0_3 * inputs.w1_0_3 / 16i16 + inputs.b1_0);
let neuron1_1: i16 = rectified_linear_activation(neuron0_0 * inputs.w1_1_0 / 16i16 + neuron0_1 * inputs.w1_1_1 / 16i16 + neuron0_2 * inputs.w1_1_2 / 16i16 + neuron0_3 * inputs.w1_1_3 / 16i16 + inputs.b1_1);
let neuron1_2: i16 = rectified_linear_activation(neuron0_0 * inputs.w1_2_0 / 16i16 + neuron0_1 * inputs.w1_2_1 / 16i16 + neuron0_2 * inputs.w1_2_2 / 16i16 + neuron0_3 * inputs.w1_2_3 / 16i16 + inputs.b1_2);
let neuron1_3: i16 = rectified_linear_activation(neuron0_0 * inputs.w1_3_0 / 16i16 + neuron0_1 * inputs.w1_3_1 / 16i16 + neuron0_2 * inputs.w1_3_2 / 16i16 + neuron0_3 * inputs.w1_3_3 / 16i16 + inputs.b1_3);
let neuron2_0: i16 = rectified_linear_activation(neuron1_0 * inputs.w2_0_0 / 16i16 + neuron1_1 * inputs.w2_0_1 / 16i16 + neuron1_2 * inputs.w2_0_2 / 16i16 + neuron1_3 * inputs.w2_0_3 / 16i16 + inputs.b2_0);
let neuron2_1: i16 = rectified_linear_activation(neuron1_0 * inputs.w2_1_0 / 16i16 + neuron1_1 * inputs.w2_1_1 / 16i16 + neuron1_2 * inputs.w2_1_2 / 16i16 + neuron1_3 * inputs.w2_1_3 / 16i16 + inputs.b2_1);
let neuron2_2: i16 = rectified_linear_activation(neuron1_0 * inputs.w2_2_0 / 16i16 + neuron1_1 * inputs.w2_2_1 / 16i16 + neuron1_2 * inputs.w2_2_2 / 16i16 + neuron1_3 * inputs.w2_2_3 / 16i16 + inputs.b2_2);
return (neuron2_0, neuron2_1, neuron2_2);}

function rectified_linear_activation(x: i16) -> i16 {
let result: i16 = 0i16;
if x > 0i16 {
result = x;
}
return result;
}
}"""

        data_arr = table_format_control(data)
        with open('test.leo', mode='w+', encoding='utf-8') as file:
            for line in data_arr:
                file.write(line)


if __name__ == '__main__':
    unittest.main()
