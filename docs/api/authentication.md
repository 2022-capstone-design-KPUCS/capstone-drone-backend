# Authentication
For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

Unauthenticated responses that are denied permission will result in an HTTP `401 Unauthorized` response with an appropriate `WWW-Authenticate` header. For example:

```
WWW-Authenticate: Token
```

The curl command line tool may be useful for testing token authenticated APIs. For example:

```bash
curl -X GET http://127.0.0.1:8000/api/v1/flights/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

## Retrieving Tokens(Login)
Authorization tokens are issued and returned when a user registers. A registered user can also retrieve their token with the following request:

**Request**:

`POST` `auth/token/login/`

Parameters:

Name | Type | Description
---|---|---
username | string | The user's username
password | string | The user's password

**Response**:
```json
{ 
    "token" : "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" 
}
```

## User Information
`curl -LX GET http://127.0.0.1:8000/auth/users/me/ -H 'Authorization: Token b704c9fc3655635646356ac2950269f352ea1139'`

**Response**:
```json
{"email": "", "username": "djoser", "id": 1}
```


## Logout
Logging out requires user token to be invalid afterwards. 

`POST` `auth/token/logout/`

Parameters:

```json Header
    "Authorization": "Token b704c9fc3655635646356ac2950269f352ea1139"
```