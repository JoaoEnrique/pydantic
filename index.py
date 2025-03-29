# Dados do usuário
nome = "Joao"
idade = 19
email = "joao@gmail.com"

usuario = {
    nome: "Joao",
    idade: 19,
    email: "joao@gmail.com"
}

from pydantic import BaseModel

class User(BaseModel):
    name: str
    idade: int
    email: str

user = User(name="Joao", idade=19, email="joao@gmail.com")
# user = User(name="Joao", idade="oi", email="joao@gmail.com") #causa erro por conta da validação de int da idade

print(user)