# pydantic
Exemplo básico de validação de dados com pydantic


```python
# Dados do usuário
nome = "Joao"
idade = 19
email = "joao@gmail.com"

usuario = {
    nome: "Joao",
    idade: 19,
    email: "joao@gmail.com"
}

from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    idade: int
    email: str

    @field_validator("email")
    def validate_email(cls, value):
        if "@" not in value:
            raise ValueError("Email Invalido")
        return value


user = User(name="Joao", idade=19, email="joao@gmail.com")

#erros de validacao
# user = User(name="Joao", idade=19, email="joaogmail.com") # causa erro por conta do validate_email (email não possui @)
# user = User(name="Joao", idade="oi", email="joao@gmail.com") #causa erro por conta da validação de int da idade

print(user)
```
