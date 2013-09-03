import os
from os.path import join as pj

from issues import Issue

class IssueTracker(object):
    def __init__(self, issue_directory):
        self._dir = issue_directory
    
    def list_issues(self):
        pass

    def new_issue_path(self):
        def icmp(x, y):
            x = x.replace('.issue', '')
            y = y.replace('.issue', '')
            if int(x) < int(y): return -1
            elif int(y) == int(x): return 0
            else: return 1
        dir_contents = os.listdir(pj(self._dir, 'new'))
        new_issues = filter(lambda x: x.endswith('.issue'), dir_contents)
        new_issues.sort(icmp)
        if not new_issues:
            return os.path.join(self._dir, 'new', '1.issue')
        last_issue = new_issues[-1]
        new_issue_fn = str(int(last_issue.replace('.issue', '')) + 1) + '.issue'
        return os.path.join(self._dir, 'new', new_issue_fn)

    def create_issue(self):
        issue_path = self.new_issue_path()
        issue = Issue()
        with open(issue_path, 'w+') as f:
            f.write(issue.serialize())
        return issue_path
