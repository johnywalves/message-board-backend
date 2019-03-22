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

Alterar o trecho "Adicionar-algum-texto-como-chave" 

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

```{shell}
pip install requests
```

```{python}
from requests import put, get, post, delete
```

Login no painel de mensagens

```{python}
get('http://localhost:5000/v1.0/login', json={'user':'admin', 'pass':'123456'}).json()
# {'token': '<chave gerada>'}
```

```{python}
headers = {"Authorization":"Bearer <chave gerada>"}
```

```{python}
get('http://localhost:5000/v1.0/posts', headers=headers).json()
```



```{python}
headers = {"Authorization": "Bearer " + get('http://localhost:5000/v1.0/login', json={'user':'admin', 'pass':'123456'}).json()['token']}
```

```{python}
post('http://localhost:5000/v1.0/posts', headers=headers, json={'text':'Lorem', 'likes':0, 'tags':[], 'comments':[]}).json()
```

