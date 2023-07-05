import unittest

from leo_translate.core_module.control_pod import IfControl, ElifControl, ElseControl
from leo_translate.submodule import AllKeyWords, Sign, Integer
from leo_translate.utils.utils import table_format_control


class TestControlMethods(unittest.TestCase):

    def test_if(self):
        output = ''
        output += IfControl('inputs.p1', '0'+str(Integer.UINT32.value), str(Sign.GREATER_THAN.value), str(AllKeyWords.RETURN.value)+" true;").get()
        # print(output)
        assert output == """if ( inputs.p1 > 0u32 ) { 
return true; 
} """

    def test_if_else(self):
        output = ''
        output += IfControl('inputs.p1', '0'+str(Integer.UINT32.value), str(Sign.GREATER_THAN.value), str(AllKeyWords.RETURN.value)+" true;").get()
        output += ElseControl(str(AllKeyWords.RETURN.value)+" false;").get()
        print(output)
        assert output == """if ( inputs.p1 > 0u32 ) { 
return true; 
} else { 
return false;
} """

    def test_if_esse_if_else(self):
        output = ''
        output += IfControl('inputs.p1', '100'+str(Integer.UINT32.value), str(Sign.GREATER_THAN.value), str(AllKeyWords.RETURN.value)+' 10'+str(Integer.UINT32.value)+';').get()
        output += ElifControl('inputs.p1', '80'+str(Integer.UINT32.value), str(Sign.GREATER_THAN.value), str(AllKeyWords.RETURN.value)+' 8'+str(Integer.UINT32.value)+';').get()
        output += ElseControl(str(AllKeyWords.RETURN.value)+' 0'+str(Integer.UINT32.value)+';').get()
        print(output)
        assert output == """if ( inputs.p1 > 100u32 ) { 
return 10u32; 
} else if ( inputs.p1 > 80u32 ) { 
return 8u32;
} else { 
return 0u32;
} """

