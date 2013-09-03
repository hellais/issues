import sys
import os

# Hack to set the proper sys.path. Overcomes the export PYTHONPATH pain.
sys.path[:] = map(os.path.abspath, sys.path)
sys.path.insert(0, os.path.abspath(os.getcwd()))

import unittest
from StringIO import StringIO

from issues import parser

issue_body = """Lorem ipsum antani sblinda super spammy
with and without it so coool bla bla bla."""

comment_body = "I am a comment\n"+issue_body

sample_doc = StringIO("""---
milestone: Milestone1
title: Issue Title
state: open
labels: [label1, label2, label3]
...
---
""" + issue_body +
"""
...
---
author: spam
date: YYYY
...
---
""" + comment_body +
"""
...
""")

class TestParser(unittest.TestCase):
    def test_parse_document(self):
        p = parser.IssueParser(sample_doc)
        p.parse()
        self.assertEqual(p.issue.body, issue_body)
        self.assertEqual(len(p.issue.comments), 1)
        self.assertEqual(p.issue.comments[0]['author'], 'spam')
        self.assertEqual(p.issue.comments[0]['body'], comment_body)

unittest.main()
