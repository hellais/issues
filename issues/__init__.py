import yaml

class Comment(object):
    def __init__(self, author, body):
        self.author = None
        self.body = None
    
    @property
    def header(self):
        return {
            'author': self.author
        }

class Issue(object):
    def __init__(self):
        self.id = None
        self.assignee = None
        self.closed_at = None
        self.created_at = None
        self.number = None
        self.updated_at = None
        self.url = None
        self.creator = None

        self.milestone = None
        self.title = None
        self.body = ""
        self.comments = []
        self.state = None
        self.labels = []
    
    @property
    def header(self):
        print self.body
        return {
            'milestone': self.milestone,
            'title': self.title,
            'state': self.state,
            'labels': self.labels
        }
    
    def entry(self, content, serialize=False):
        if serialize:
            content = yaml.dump(content, default_flow_style=False)
        output = "---\n"
        output += content
        output += "...\n"
        return output

    def serialize(self):
        output = self.entry(self.header, serialize=True)
        output += self.entry(self.body)

        for comment in self.comments:
            output += self.entry(comment.header, serialize=True)
            output += self.entry(comment.body)

        return output

class IssueList(object):
    pass
