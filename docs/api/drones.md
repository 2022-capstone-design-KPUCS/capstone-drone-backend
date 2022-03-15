# Drones
Supports registering, viewing, and updating drone instances.

## Register a new drone instance

**Request**:

`POST` `/drones/`

Parameters:

Name             | Type   | Required | Description
-----------------|--------|----------|------------
surveilance_area | text   | No       | Name of the surveilance area drone is assigned to.
admin_id         | uuid   | Yes      | ID of the user who is the admin of the drone.
deck_id          | uuid   | No       | ID of the deck drone is assigned to.
drone_alias      | string | No       | Alias of the drone.
is_active        | bool   | No       | Whether the drone is active.

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "surveilance_area":"Compound A",
  "drone_alias":null,
  "is_active":false,
  "admin_id":"ba91a2b6-9417-4a4b-bd36-25d8b16055f1",
  "deck":"ac1f456a-12a5-4717-85cc-d97b45b7b663"
}
```

## Get a drones's information

**Request**:

`GET` `/drones/<pk>`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "surveilance_area":"Compound A",
  "drone_alias":null,
  "is_active":false,
  "admin_id":"ba91a2b6-9417-4a4b-bd36-25d8b16055f1",
  "deck":"ac1f456a-12a5-4717-85cc-d97b45b7b663"
}
```


## Update drone information

**Request**:

`PUT/PATCH` `/drones/<pk>`

Parameters:

Name             | Type   | Required | Description
-----------------|--------|----------|------------
surveilance_area | text   | No       | Name of the surveilance area drone is assigned to.
admin_id         | uuid   | Yes      | ID of the user who is the admin of the drone.
deck_id          | uuid   | No       | ID of the deck drone is assigned to.
drone_alias      | string | No       | Alias of the drone.
is_active        | bool   | No       | Whether the drone is active.



*Note:*

- All parameters are optional except for admin_id
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "surveilance_area": "Compound B",
    "drone_alias": "Drone P",
    "is_active": false,
    "admin_id": "ba91a2b6-9417-4a4b-bd36-25d8b16055f1",
    "deck": "ac1f456a-12a5-4717-85cc-d97b45b7b663"
}
```
