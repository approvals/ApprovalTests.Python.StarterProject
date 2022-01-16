import this
import unittest
import pytest

from approvaltests.approvals import verify, verify_all

from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approvaltests import Options
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests import set_default_reporter

def test_pytest():
    assert True

class RegressionTest(unittest.TestCase):
    def setUp(self):
        set_default_reporter(None) #Use the first difftool found on your system
        #self.reporter = GenericDiffReporterFactory().get("DiffMerge")
        #Download DiffMerge at https://sourcegear.com/diffmerge/

    def test_straight_unittest(self):
        self.assertEqual(5,5)


    def test_with_approvals(self):
        from project.sample_function import this_is_the_function
        verify(this_is_the_function())

    def test_list_with_reporter(self):
        sample = ["welcome", "to", "approvals"]
        verify_all("words", sample,options=Options().with_reporter(PythonNativeReporter()))        

            


