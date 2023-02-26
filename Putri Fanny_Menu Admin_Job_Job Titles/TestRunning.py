import unittest
from TC001 import OHRM1
from TC002 import OHRM2
from TC003 import OHRM3
from TC004 import OHRM4
from TC005 import OHRM5
from TC006 import OHRM6
from TC007 import OHRM7
from TC008 import OHRM8
from TC009 import OHRM9


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(OHRM1('test_a_add_data'))
    suite.addTest(OHRM2('test_b_job_title_left_blank'))
    suite.addTest(OHRM3('test_field_job_title'))
    suite.addTest(OHRM4('test_field_job_description_note'))
    suite.addTest(OHRM5('test_button_cancel'))
    suite.addTest(OHRM6('test_button_save'))
    suite.addTest(OHRM7('test_button_delete'))
    suite.addTest(OHRM8('test_button_no_cencel'))
    suite.addTest(OHRM9('test_button_edit'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
