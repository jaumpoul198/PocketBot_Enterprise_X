class ReflectionMemory:

    def __init__(self):
        self.entries = []


    def store(self, reflection):

        self.entries.append(
            reflection
        )

        return reflection


    def all(self):

        return self.entries
