import unittest
import pytest

from approvaltests.approvals import verify, verify_all

from approvaltests.reporters.python_native_reporter import PythonNativeReporter
from approvaltests import Options, verify_as_json
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
from approvaltests import set_default_reporter


class SampleTests(unittest.TestCase):
    def setUp(self):
        set_default_reporter(None)  # Use the first difftool found on your system
        # self.reporter = GenericDiffReporterFactory().get("DiffMerge")
        # Download DiffMerge at https://sourcegear.com/diffmerge/

    def test_straight_unittest(self):
        self.assertEqual(5, 5)

    def test_with_approvals(self):
        sample = "Welcome To Approvals"
        verify(sample)

    def test_with_approvals_from_project_code(self):
        from project.sample_function import this_is_the_function
        verify(this_is_the_function())

    def test_with_json(self):
        sample = {"firstName": "jayne",
                  "lastName": "cobb",
                  "isMale": True,
                  "age": 38}
        verify_as_json(sample)

    def test_list(self):
        sample = ["welcome", "to", "approvals"]
        verify_all("words", sample)

    def test_with_specific_reporter(self):
        sample = "Welcome To Approvals"
        verify(sample, options=Options().with_reporter(PythonNativeReporter()))


def test_pytest():
    assert True
