class CognitiveCycle:

    STATES = (
        "PERCEIVE",
        "PROCESS",
        "DECIDE",
        "LEARN",
    )

    def __init__(self):
        self.position = 0

    def next(self):
        state = self.STATES[self.position]

        self.position = (
            self.position + 1
        ) % len(self.STATES)

        return state

    def reset(self):
        self.position = 0
