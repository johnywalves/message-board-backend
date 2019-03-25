# Modelos

## iLogin

```javascript
{
    "user": string,
    "user": pass
}
```

## iToken

```javascript
{
    "token": string
}
```

## iPost

```javascript
{
    "id": integer,
    "text": string,
    "likes": integer,
    "created_at": Date,
    "tags": iTag[],
    "comments": iComment[]
}
```

## iTag

```javascript
{
    "name": string
}
```

## iComment

```javascript
{
    "text": string
}
```