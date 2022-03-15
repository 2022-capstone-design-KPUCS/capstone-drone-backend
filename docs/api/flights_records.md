# Flight Records
Supports registering, viewing, and updating flight records.

## Register a new flight record

**Request**:

`POST` `/flightrecords/`

Parameters:

Name              | Type    | Required | Description
------------------|---------|----------|------------
flight_record     | text    | No       | Text of today's flight record.
weather           | choice  | No       | Choice of today's weather.
is_fire           | bool    | No       | Whether there was a fire today.
is_smoke          | bool    | No       | Whether there was a smoke today.
flight_id         | uuid    | No       | ID of the flight that record is being kept.

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "flight_record": "It was a very sunny day! no fire anywhere!",
  "weather": "SUNNY",
  "is_fire": false,
  "is_smoke": false,
  "flight_id": "202f8c46-bf93-4848-b59a-5c5da028bfec"
}
```

## Get a flight records' information

**Request**:

`GET` `/flightrecords/<pk>`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "flight_record": "It was a very sunny day! no fire anywhere!",
  "weather": "SUNNY",
  "is_fire": false,
  "is_smoke": false,
  "flight_id": "202f8c46-bf93-4848-b59a-5c5da028bfec"
}
```


## Update flight record

**Request**:

`PUT/PATCH` `/flightrecords/<pk>`

Parameters:

Name              | Type    | Required | Description
------------------|---------|----------|------------
flight_record     | text    | No       | Text of today's flight record.
weather           | choice  | No       | Choice of today's weather.
is_fire           | bool    | No       | Whether there was a fire today.
is_smoke          | bool    | No       | Whether there was a smoke today.
flight_id         | uuid    | No       | ID of the flight that record is being kept.

*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "id": "4976cd65-0944-40b7-89d4-fea1735881cd",
  "flight_record": "It was a very sunny day! no fire anywhere!",
  "weather": "SUNNY",
  "is_fire": false,
  "is_smoke": false,
  "flight_id": "202f8c46-bf93-4848-b59a-5c5da028bfec"
}
```
