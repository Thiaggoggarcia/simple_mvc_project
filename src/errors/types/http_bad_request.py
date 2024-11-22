class HttpBadRequest(Exception):
    def __init__(self,mensagem:str) -> None:
        super().__init__(mensagem) 
        self.mensagem = mensagem
        self.name = "Bad Request"
        self.status_code = 400