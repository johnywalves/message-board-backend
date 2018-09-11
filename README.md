# Message Board (Server)

Desenvolvimento em Python de API com Flask, Restful, SQLAlchemy e JWT

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

```{python}
from requests import put, get, post, delete
```

Login no painel de mensagens

```{python}
post('http://localhost:5000/v1.0/login', json={'user':'admin', 'pass':'123'}).json()
# {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1MzY2Njg3MDIsIm5iZiI6MTUzNjY2ODcwMiwianRpIjoiYzVjMTZmMDItY2Y1MS00ZDk0LThhNjEtOTk5NjFmNDY3ZjA5IiwiZXhwIjoxNTM2NjY5NjAyLCJpZGVudGl0eSI6bnVsbCwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.0xfOiRD3ub4FWnBw17glmS-hHd_4Ui3CndYXWV_x2ok'}
```

```{python}
headers = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJ"}
```

```{python}
post('http://localhost:5000/v1.0/posts', headers=headers, json={'text':'teste teste teste teste', 'likes':0, 'tags':[], 'comments':[]}).json()
```

```{python}
get('http://localhost:5000/v1.0/posts', headers=headers).json()
```