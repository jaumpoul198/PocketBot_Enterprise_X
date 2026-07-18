class MemoryConsolidation:

    def __init__(self):

        self.consolidated = []

    def evaluate(
        self,
        memories,
    ):

        relevant = []

        for memory in memories:

            if memory.confidence >= 0.5:

                relevant.append(
                    memory
                )

        self.consolidated = relevant

        return relevant

    def count(self):

        return len(
            self.consolidated
        )
