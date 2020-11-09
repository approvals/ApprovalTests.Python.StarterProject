import unittest

from approvaltests.approvals import verify


from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory



class RegressionTest(unittest.TestCase):
    def setUp(self):
        self.reporter = None #Use the first difftool found on your system
        #self.reporter = GenericDiffReporterFactory().get("DiffMerge")
        #Download DiffMerge at https://sourcegear.com/diffmerge/

    def test_straight_unittest(self):
        self.assertEqual(5,5)


    def test_with_approvals(self):
        from CodeGoesHere import sample
        verify(sample(), self.reporter)


