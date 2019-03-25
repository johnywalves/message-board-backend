# Message Board (Backend)

Backend para o Message Board em Python com Flask, Restful, SQLAlchemy e JWT

```{shell}
pip install pipenv
```

Criar e iniciar ambiente virtual 

```{shell}
pipenv shell
```

Instalar os pacotes no ambiente virtual 

```{shell}
pipenv install
```

## Executando

Alterar o trecho `Adicionar-algum-texto-como-chave`  

```{python}
app.config['JWT_SECRET_KEY'] = 'Adicionar-algum-texto-como-chave'
```

Criar a base de dados

```{shell}
python create.py
```

Executar o arquivo **app.py**

```{shell}
flask run
```

## Testando

Usando a biblioteca **requests**

```{shell}
pip install requests
```

Importar os métodos

```{python}
from requests import put, get, post, delete
```

**Exemplo:** login no painel de mensagens

```{python}
get('http://localhost:5000/v1.0/login', json={'user':'admin', 'pass':'123456'}).json()
# {'token': '<chave gerada>'}
```

Para realizar as outras requisições é necessário um header com a chave gerada

```{python}
headers = {"Authorization":"Bearer <chave gerada>"}
```

Ou realizar a criação do header ao solicitar o token

```{python}
headers = {"Authorization": "Bearer " + get('http://localhost:5000/v1.0/login', json={'user':'admin', 'pass':'123456'}).json()['token']}
```

Com o headers em mãos podemos consultar os posts

```{python}
get('http://localhost:5000/v1.0/posts', headers=headers).json()
```

Ou adicionar um novo post

```{python}
post('http://localhost:5000/v1.0/posts', headers=headers, json={'text':'Lorem', 'likes':0, 'tags':[], 'comments':[]}).json()
```

## Documentos

Informações auxuliares para uso da API

[Modelos](./models.md)  
[Mapa de Endpoints](./endpoints.md)