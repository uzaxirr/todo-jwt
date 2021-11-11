## Postman Collection
https://www.getpostman.com/collections/a17e18449b1ef1e71a4f


## API Reference

#### Base URL
https://todo-jwt-production.up.railway.app/

#### Signup a New User

```http
  POST /api/signup
```

| Parameter      | Type     | Description                        |
| :--------      | :------- | :--------------------------------  |
| `username`        | `string` |  Username of the user |
| `password`        | `string` |Password of the user |
| `email` | `string`| Email-ID of the user |
| `first_name` | `string`| First Name of the user |
| `last_name` | `string`| Last Name of the user |


#### Login a New User
This is not working Fine in Postman for some reasons. Try in some other client (Works fine in thunderclient for me) 
```http
  POST /api/login
```

| Parameter      | Type     | Description                        |
| :--------      | :------- | :--------------------------------  |
| `username`        | `string` |  Username of the user |
| `password`        | `string` |Password of the user |



#### Get all Tasks

```http
  GET /api/todos
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | NA | Returns all tasks of current user |


#### Create a Task
```http
  POST /api/todos
```


| Parameter      | Type     | Description                        |
| :--------      | :------- | :--------------------------------  |
| `title`        | `string` |  title of item to create           |
| `description` | `string`| description of item to create |

#### Get Details of a Task

```http
  GET /api/done/${id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | NA | Returns all tasks of current user |

#### Update Details of a Task

```http
  PUT /api/done/${id}
```

| Parameter      | Type     | Description                        |
| :--------      | :------- | :--------------------------------  |
| `title`        | `string` |  New Title (Optional)          |
| `description`        | `string` |  New description (Optional)          |
| `is_completed` | `boolean`| New Status (Optional) |

#### Delete a Task from DB

```http
  DELETE /api/done/${id}
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| None | NA | Delets a tasks from DB |
