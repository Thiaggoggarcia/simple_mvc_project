class PersonRegisterController:
    def create_person(self, person_name:str, person_age:int) -> dict:
        self.__validate_person_registry(person_name)
        self.__insert_person(person_name,person_age)
        response = self.__format_response(person_name)
        
        return response
    
    def __validate_person_registry(self, person_name:str) -> None:
        person = None
        if person:
            raise Exception("Esse Usuário Já Foi Registrado!")
        
    def __insert_person(self, person_name:str, person_age:int) -> None:
        #Inserir dado do Banco
        pass
    
    def __format_response(self, person_name:str) -> dict:
        return {
            "type" : "Person",
            "count": 1,
            "att": {
                "name": person_name
            }
        }