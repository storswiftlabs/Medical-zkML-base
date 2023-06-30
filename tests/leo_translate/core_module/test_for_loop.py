import unittest

from leo_translate.core_module import Let
from leo_translate.core_module.for_loop_pod import ForLoop
from leo_translate.submodule import Integer
from leo_translate.utils.utils import table_format_control


def generate_body():
    return 'count += index'


class TestControlMethods(unittest.TestCase):
    def test_for_loop(self):
        variate = 'index'
        variate_type = Integer.UINT32.value
        start_variate = '0'+str(Integer.UINT32.value)
        end_variate = '10'+str(Integer.UINT32.value)
        body = generate_body()
        print(Let('count', variate_type, start_variate).get())
        output = table_format_control(ForLoop(variate, variate_type, start_variate, end_variate, body).get().split('\n'))
        for index in range(0, len(output)):
            print(output[index])
