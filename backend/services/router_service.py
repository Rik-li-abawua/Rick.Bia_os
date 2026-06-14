class RouterService:
    def route(self, prompt:str):
        p=prompt.lower()
        if 'hipoteca' in p or 'inversion' in p:
            return 'finance'
        if 'vuelo' in p or 'pasajero' in p:
            return 'travel'
        return 'general'
