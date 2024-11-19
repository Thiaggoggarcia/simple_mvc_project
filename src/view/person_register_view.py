from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PersonRegisterView:
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        person_name = body.get("person_name")
        person_age = body.get("person_age")
        self.__validate_inputs(person_name,person_age)
        
        #Chamar a logica response
        return HttpResponse(body={"Registrando o Usuário ":person_name}, status_code=201)
        
    def __validate_inputs(self, person_name: any, person_age: any) -> None:
        if (
            not person_name or
            not person_age or
            not isinstance(person_name, str) or
            not isinstance(person_age, int)
        ): raise Exception("Entrada inválida ao tentar cadastrar uma pessoa")