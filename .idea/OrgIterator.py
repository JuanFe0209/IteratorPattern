class OrgIterator:
    def __init__(self, root):
        self.stack = [root]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration

        current = self.stack.pop()
        self.stack.extend(reversed(current.subordinates))  # Agregar subordinates al stack en orden inverso
        return current
