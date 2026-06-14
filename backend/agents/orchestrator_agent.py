from backend.services.router_service import RouterService

class OrchestratorAgent:
    def __init__(self):
        self.router = RouterService()

    def handle(self, prompt:str):
        return {'agent': self.router.route(prompt)}
