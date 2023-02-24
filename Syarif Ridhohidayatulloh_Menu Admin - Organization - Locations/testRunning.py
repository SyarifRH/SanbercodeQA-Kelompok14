import unittest
from testCase import TestAOL


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestAOL('test_success_add_a_new_location'))
    suite.addTest(TestAOL('test_failed_to_add_new_location'))
    suite.addTest(TestAOL('test_add_location_failed_due_to_invalid_input'))
    suite.addTest(TestAOL('test_cancel_save_when_adding_new_location'))
    suite.addTest(TestAOL('test_search_for_location'))
    suite.addTest(
        TestAOL('test_Search_location_failed_due_to_invalid_keyword'))
    suite.addTest(TestAOL('test_cancel_button_click_when_editing_location'))
    suite.addTest(
        TestAOL('test_location_failed_due_to_missing_required_fields'))
    suite.addTest(TestAOL('test_edit_location'))
    suite.addTest(TestAOL('test_delete_location'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
