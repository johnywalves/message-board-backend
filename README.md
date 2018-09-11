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

## Testando

```{python}
from requests import put, get, post, delete
```

```{python}
post('http://localhost:5000/v1.0/login', json={'user':'admin', 'pass':''}).json()
```

```{python}
headers = {"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJ"}
```

```{python}
post('http://localhost:5000/v1.0/posts', headers=headers, json={'text':'teste teste teste teste', 'likes':0, 'tags':[], 'comments':[]}).json()
```