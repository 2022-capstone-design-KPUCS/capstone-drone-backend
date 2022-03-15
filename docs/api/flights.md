# Flights
Supports registering, viewing, and updating flight information.

## Register a new flight information

**Request**:

`POST` `/flights/`

Parameters:

Name              | Type    | Required | Description
------------------|---------|----------|------------
flight_record_url | string  | No       | URL of the server where the flight record is stored.
flight_path       | string  | No       | List of coordinates of the flight path.
auto_start_time   | datetime| No       | Datetime when the flight should start. `MM/DD/YYYY HH:MM` format.
auto_end_time     | datetime| No       | Datetime when the flight should end. `MM/DD/YYYY HH:MM` format.
drone_id          | uuid    | No       | ID of the drone that is performing the flight.

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
  "flight_record_url": "https://s3.com/videos",
  "flight_path": "123,24,234,2,123,432,42",
  "auto_start_time": "03/15/2022 20:02",
  "auto_end_time": "03/15/2022 20:30",
  "drone_id": "9d6c6d3a-b9e9-4771-a090-513b56eef736"
}
```

## Get a flight information

**Request**:

`GET` `/flights/<pk>`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "flight_record_url": "https://s3.com/videos",
  "flight_path": "123,24,234,2,123,432,42",
  "auto_start_time": "03/15/2022 20:02",
  "auto_end_time": "03/15/2022 20:30",
  "drone_id": "9d6c6d3a-b9e9-4771-a090-513b56eef736"
}
```


## Update drone information

**Request**:

`PUT/PATCH` `/flights/<pk>`

Parameters:

Name              | Type    | Required | Description
------------------|---------|----------|------------
flight_record_url | string  | No       | URL of the server where the flight record is stored.
flight_path       | string  | No       | List of coordinates of the flight path.
auto_start_time   | datetime| No       | Datetime when the flight should start. `MM/DD/YYYY HH:MM` format.
auto_end_time     | datetime| No       | Datetime when the flight should end. `MM/DD/YYYY HH:MM` format.
drone_id          | uuid    | No       | ID of the drone that is performing the flight.


*Note:*

- All parameters are optional
- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
  "flight_record_url": "https://s3.com/videos",
  "flight_path": "123,24,234,2,123,432,42",
  "auto_start_time": "03/15/2022 20:02",
  "auto_end_time": "03/15/2022 20:30",
  "drone_id": "9d6c6d3a-b9e9-4771-a090-513b56eef736"
}
```
