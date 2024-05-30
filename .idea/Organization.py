from OrgIterator import OrgIterator
class Organization:
    def __init__(self, root):
        self.root = root

    def __iter__(self):
        return OrgIterator(self.root)
