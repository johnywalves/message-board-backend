# Mapa de Endpoints

## Token de Acesso

Para acessar as opções com o header `{"Authorization": "Bearer <token>"}`

### Solicitar

Geração do token dos acessos por usuário e senha  

> **GET**  
> /v1.0/login

**Request:** [iLogin](./models.md#ilogin)  
**Response:** [iToken](./models.md#itoken)  

## Manipulação de Posts

### Consultar últimos posts

Listar últimos posts

> **GET**  
> /v1.0/posts

**Request:** -
**Response:** [iPost](./models.md#ipost)  

### Cadastrar post

Registrar um novo post

> **POST**  
> /v1.0/posts

**Request:** [iPost](./models.md#ipost)  
**Response:** -

### Consultar post

> **GET**  
> /v1.0/posts/<int:id>

### Alterar post

> **PUT**  
> /v1.0/posts/<int:id>

### Destarcar post

> **DELETE**  
> /v1.0/posts/<int:id>

### Consultar posts por tag

> **GET**  
> /posts/<string:tag>

### Adicionar uma curtida

> **POST**  
> /v1.0/posts/<int:id>/like

### Remover uma curtida

> **DELETE**  
> /v1.0/posts/<int:id>/like

### Adicionar comentário

> **POST**  
> /v1.0/posts/<int:id>/comments