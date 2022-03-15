# Decks
Supports registering, viewing, and updating deck instances.

## Register a new deck

**Request**:

`POST` `/decks/`

Parameters:

Name             | Type   | Required | Description
-----------------|--------|----------|------------
deck_name        | string | No       | Name of the deck
is_occupied      | bool   | No       | Whether the deck is occupied by drone.

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "deck_name": "Complex B",
  "is_occupied": false
}
```

## Get a deck's information

**Request**:

`GET` `/decks/<pk>`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "deck_name": "Complex B",
  "is_occupied": false
}
```


## Update drone information

**Request**:

`PUT/PATCH` `/decks/<pk>`

Parameters:

Name             | Type   | Required | Description
-----------------|--------|----------|------------
deck_name        | string | No       | Name of the deck
is_occupied      | bool   | No       | Whether the deck is occupied by drone.


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "deck_name": "Complex B",
  "is_occupied": false
}
```
