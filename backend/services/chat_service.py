from backend.agents.orchestrator_agent import OrchestratorAgent

class ChatService:
    def __init__(self):
        self.orchestrator = OrchestratorAgent()

    def process(self, prompt:str):
        return self.orchestrator.handle(prompt)
