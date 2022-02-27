""""
an in-memory key-value store wrapper
    - initial implementation will be using a simple dictionary (hash map style)
    - advanced implementation might use Redis in memory store
        ** will implement it with Redis in case I have time left in the assignment
"""


class InMemoryStore:
    def __init__(self):
        self.store = dict()

    def set(self, key, value):
        if key in self.store.keys():  # update existing key to the new value
            del self.store[key]
        self.store[key] = value

    def get(self, key):
        if key not in self.store.keys():
            raise Exception("InMemoryStore Error: key not found!")
        return self.store[key]
