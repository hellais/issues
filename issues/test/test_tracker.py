import sys
import os

# Hack to set the proper sys.path. Overcomes the export PYTHONPATH pain.
sys.path[:] = map(os.path.abspath, sys.path)
sys.path.insert(0, os.path.abspath(os.getcwd()))

import tempfile
import unittest

from issues import tracker


class TestTracker(unittest.TestCase):
    def setUp(self):
        self.base_dir = tempfile.mkdtemp()
        os.mkdir(os.path.join(self.base_dir, 'new'))

    def test_new_issue_path(self):
        for i in range(100):
            path = os.path.join(self.base_dir, 'new', str(i) + '.issue')
            with open(path, 'w+'): pass
        issue_tracker = tracker.IssueTracker(self.base_dir)
        self.assertEqual(issue_tracker.new_issue_path(), os.path.join(self.base_dir, 'new', '100.issue'))

    def test_new_issue(self):
        issue_tracker = tracker.IssueTracker(self.base_dir)
        print issue_tracker.create_issue()

unittest.main()
