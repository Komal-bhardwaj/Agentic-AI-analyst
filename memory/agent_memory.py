class AgentMemory:
    def __init__(self):
        self.history = []

    def add(self, text: str):
        self.history.append(text)

    def get_context(self):
        return "\n".join(self.history[-3:])
