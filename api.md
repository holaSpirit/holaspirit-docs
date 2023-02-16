API documentation
=================

[<<< Back](README.md)

The detail of all endpoints of the API is available on: <https://app.holaspirit.com/api/doc/>.

### Headers

This is a JSON only API. You should supply a `Content-Type: application/json`
header on POST, PUT, PATCH and DELETE operations. You should set a `Accept: application/json`
header on all requests.

Read Only Access
-------------

If you need a read-only access to the API, just ask for a read-only access token to the assistance in <https://app.holaspirit.com>

With this token information you can simply use every GET endpoint of your organization, as described in [Access token usage](#access-token-usage)

If you need a read-write access, read the next section.

Authentication for Read-Write
--------------

### Obtain an access token

POST <https://app.holaspirit.com/oauth/v2/token>

#### From email and password

| Name            | Type   | Description                                   |
| --------------- | ------ | --------------------------------------------- |
| `client_id`     | string | **Required** OAuth2 Client ID                 |
| `client_secret` | string | The OAuth2 Client secret                      |
| `grant_type`    | string | **Required** "password"                       |
| `username`      | string | **Required** The Email                        |
| `password`      | string | **Required** The Password                     |
| `timezone`      | string | The Timezone (e.g.: "+02:00")                 |

If the security is enforced on your organization, then only users with admin privilege can create a password and then use this endpoint to log in. (use the "forget password" form to create one)

The client secret is not required for a public app (e.g. our web and mobile app).

The default and public Client ID is:
`54cb79d0279871e1248b4567_400tdzqbdcowsskk08gws0wkwogck00w084w4s8w8gok08s0o8`.

To have your own `client_id` / `client_secret` ask the assistance in <https://app.holaspirit.com>

CURL example with email and password:

```
curl 'https://app.holaspirit.com/oauth/v2/token' \
--data-raw 'client_id=****&client_secret=****&grant_type=password&username=****&password=****'
```

#### From a refresh_token

If you already have a `refresh_token`, it's recommended that you ask a new `access_token` with:

| Name            | Type   | Description                                   |
| --------------- | ------ | --------------------------------------------- |
| `client_id`     | string | **Required** OAuth2 Client ID                 |
| `client_secret` | string | OAuth2 Client secret                          |
| `grant_type`    | string | **Required** "refresh_token"                  |
| `refresh_token` | string | **Required** The `refresh_token`              |

**Warning:** This is only possible when using the same `client_id` and `client_secret` that created the `refresh_token` in the first place.

Each `refresh_token` can only be used once. If you try the same request the second call will fail.

The response will give you 2 tokens:

* an `access_token` that you can use to make some requests
* a `refresh_token` that will be useful after the current `access_token` expires to request a new token

A `refresh_token` expires:

* When it is used to request an `access_token`
* When the member's password is changed
* 1 month after it has been issued

#### Response

```json
{
    "access_token": "#################",
    "expires_in": 3600,
    "token_type": "bearer",
    "scope": null,
    "refresh_token": "#################"
}
```

#### Response errors

**Incorrect Client ID (status code: 400):**

```json
{
    "error": "invalid_client",
    "error_description": "The client credentials are invalid"
}
```

**Incorrect credentials (status code: 400):**

```json
{
    "error": "invalid_grant",
    "error_description": "Invalid username and password combination"
}
```

### Revoke an access token

* POST <https://app.holaspirit.com/oauth/v2/revoke><br>
  Header: `Authorization: Bearer #################`

#### Parameters

| Name    | Type   | Description                               |
| ------- | ------ | ----------------------------------------- |
| `token` | string | **Required** Current token ID             |

#### Response

Empty response (status code: 200)

#### Response errors

**Missing token ID (status code: 400):**

```json
{
    "error": "bad_request",
    "error_description": "Missing Token"
}
```

**Incorrect credentials (status code: 401):**

```json
{
    "error": "access_denied",
    "error_description": "OAuth2 authentication required"
}
```

### Access token usage

The token should be sent in the headers of the Request: Header: `Authorization: Bearer #################` (this works for all types of requests: GET POST PATCH PUT and DELETE)

CURL GET example:

```
curl 'https://app.holaspirit.com/api/organizations/********' \
-H 'Accept: application/json' \
-H 'Content-type: application/json' \
-H 'Authorization: Bearer #################'
```

CURL POST example: 

```
curl 'https://holon.holaspirit.com/api/organizations/********/custom-fields' \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer #################' \
--data-raw '{"name":"testCF","customFieldType":"text","applyTo":"role"}'
```

Errors
------

The error responses follows the JSON-API specifications:
<http://jsonapi.org/format/#errors>

* `"id"` - A unique identifier for this particular occurrence of the problem.
* `"status"` - The HTTP status code applicable to this problem, expressed as a string value.
* `"code"` - An application-specific error code, expressed as a string value.
* `"title"` - A short, human-readable summary of the problem.
* `"detail"` - A human-readable explanation specific to this occurrence of the problem.
* `"path"` - The relative path to the relevant attribute (especially for form).

For example:

```json
{
  "errors": [
    {
      "status": 404,
      "code": "not_found",
      "title": "Resource not found",
      "detail": "HolaSpirit\\Organization:Organization object not found."
    }
  ]
}
```

### Available code errors

| Name                          | Description                                  |
| ----------------------------- | -------------------------------------------- |
| `not_found`                   | Resource not found (e.g. 404)                |
| `password_request_expired`    | The token to reset the password has expired  |
| `pending_email_already_taken` | pending email has already been taken         |

### Form errors

The form errors follow the same format as others error.
The response status code is 400.

```json
{
  "errors": [
    {
      "status": "400",
      "code": "required",
      "title": "This value should not be blank.",
      "detail": "This value should not be blank.",
      "path": "organization"
    },
    {
      "status": "400",
      "code": "required",
      "title": "This value should not be blank.",
      "detail": "This value should not be blank.",
      "path": "email"
    },
    {
      "status": "400",
      "code": "required",
      "title": "This value should not be blank.",
      "detail": "This value should not be blank.",
      "path": "password"
    }
  ]
}
```

#### Available form code errors

| Name                    | Description                                    |
| ----------------------- | ---------------------------------------------- |
| `required`              | The value is missing and required              |
| `invalid_email`         | The value is not a valid email                 |
| `email_not_unique`      | This email is already used                     |
| `member_already_exists` | The member for the organization already exists |
