import github3

import issues

class GithubIssue(issues.Issue):
    def __init__(self, issue):
        super(GithubIssue, self).__init__()

        self.issue = issue
        for label in issue.labels:
            self.labels.append(label.name)
        if issue.milestone:
            self.milestone = issue.milestone.title

        self.title = issue.title
        self.body = issue.body
        for comment in issue.iter_comments():
            self.comments.append(
                issues.Comment(comment.user.login, comment.body)
            )

class GithubIssueList(issues.IssueList):
    def __init__(self, gh, owner, repository):
        self.gh = gh
        self.owner = owner
        self.repository = repository
        self.issues = []
        self.update()
    
    def update(self):
        for issue in self.gh.iter_repo_issues(self.owner, self.repository):
            self.issues.append(GithubIssue(issue))

    def list(self):
        for issue in self.issues:
            print issue.serialize()
