import yaml
from issues import Issue

class ParseErorr(Exception):
    pass

class UnexpectedDocumentStart(ParseError):
    pass

class IssueParser(object):
    def __init__(self, fh):
        self._fh = fh
        self.issue = Issue()
    
    def parse(self):
        header = yaml.load(self.documents().next())
        self.issue.milestone = header['milestone']
        self.issue.title = header['title']
        self.issue.state = header['state']
        self.issue.labels = header['labels']

        body = self.documents().next().strip()
        self.issue.body = body
        
        comment_body = None
        comment = None
        for i, document in enumerate(self.documents()):
            if i % 2 == 1:
                comment_body = document.strip()
            else:
                comment = yaml.load(document)
            if comment_body and comment:
                self.issue.comments.append({
                    'author': comment['author'],
                    'body': comment_body
                })


    def documents(self):
        document = ""
        started = False

        for line in self._fh:
            if line.startswith('---'):
                started = True
            elif started and line.startswith('...'):
                yield document
                started = False
                document = ""
            elif started:
                document += line
