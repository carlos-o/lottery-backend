# Documentation of services module Accounts
### Table of contents
* **[Signin](#Signin)**<br>
* **[Logout](#Logout)**<br>
* **[Register](#Register)**<br>
* **[ActivateAccount](#ActivateAccount)**<br>

## Signin
Grants access to a user to start in API

* Url

  http://127.0.0.1:8000/accounts/signin/

* Method

  **POST**

* Url Params

  **None**

* Data Params

    ```json
     {
        "username":"example",
        "password":"example123"
     } 
    ```

* Success Response:
   * code: 200
    ```json
    {
        "detail": {
            "success": true,
            "code": 200,
            "data": {
                "id": 2,
                "first_name": "carlos",
                "last_name": "olivero",
                "email": "carlosolivero2@gmail.com",
                "token": "b6af7d1e0dda61b5d6ef27b7258820b3c2fb64c3"
            },
            "message": "ok"
        }
    }
   ```  
* Error Response:
   
   In case username or password incorrect 
  * code: 400
   ```json
   {
        "detail": {
            "success": false,
            "code": 400,
            "data": {},
            "message": "ValueError",
            "errors": "The username or password is incorrect"
        }
   }
   ``` 
  or
  
  * case: 500
   ```json
   {
        "detail": {
            "success": false,
            "code": 500,
            "data": {},
            "message": "Internal Server Error",
            "errors": {
                "error": [
                    "errors"
                ]
            }
        }
   }
  ```
  
* Notes:
 
  **None**
  
## Logout
**TOKEN IS REQUIRED**

add a header 
 
**Authorization** =  token 74dafd9462f6c8df986723fccee1c08c2e564cd6


logout from server

* Url

  http://127.0.0.1:8000/accounts/logout/

* Method

  **POST**

* Url Params

  **None**

* Data Params

  **None**

* Success Response:
   * code: 200
   ```json
   {
    "detail": {
        "success": true,
        "code": 200,
        "data": {},
        "message": "ok"
    }
   }
   ```  
* Error Response:

  * case: 500
   ```json
   {
        "detail": {
            "success": false,
            "code": 500,
            "data": {},
            "message": "Internal Server Error",
            "errors": {
                "error": [
                    "errors"
                ]
            }
        }
   }
  ```
  
* Notes:
 
  **None**
  
## Register
Register user in lottery

* Url

  http://127.0.0.1:8000/accounts/register/

* Method

  **POST**

* Url Params

  **None**

* Data Params

  ```json
  {
    "first_name": "carlos",
    "last_name": "olivero",
    "email": "carlosolivero2@gmail.com",
    "phone": "983196824",
    "address": "sergio viera de mello",
    "rut": "26661495-0",
    "gender": "Male"
  }
  ```

* Success Response:
   * code: 200
   ```json
   {
        "detail": {
            "success": true,
            "code": 200,
            "data": {
                "id": 11,
                "first_name": "carlos",
                "last_name": "olivero",
                "email": "carlosolivero2@gmail.com"
            },
            "message": "please verify your account"
        }
   }
   ```  
* Error Response:
  * case 400: email all ready register
  ```json
  {
    "detail": {
        "success": false,
        "code": 400,
        "data": {},
        "message": "ValueError",
        "errors": "Email registered please try with another"
    }
  }
  ```
  
  or
  
  * case 400: error in json
  ```json
   {
        "detail": {
            "success": false,
            "code": 400,
            "data": {},
            "message": "ValueError",
            "errors": {
                "first_name": [
                    "empty values not allowed"
                ],
                "rut": [
                    "must be of string type"
                ]
            }
        }
  }
  ```
  
  or 
  
  * case: 500
   ```json
   {
        "detail": {
            "success": false,
            "code": 500,
            "data": {},
            "message": "Internal Server Error",
            "errors": {
                "error": [
                    "errors"
                ]
            }
        }
   }
  ```
  
* Notes:
 
  **None**


## ActivateAccount
activate account

* Url

  http://127.0.0.1:8000/accounts/activate-account/

* Method

  **POST**

* Url Params

  **None**

* Data Params

  ```json
    {
      "code": "2BRZXC2C3CW5ADC",
      "password": "carlos123*"
    }
  ```

* Success Response:
   * code: 200
   ```json
    {
        "detail": {
            "success": true,
            "code": 200,
            "data": {
                "id": 11,
                "first_name": "carlos",
                "last_name": "olivero",
                "email": "carlosolivero2@gmail.com",
                "token": "471ef3672057c3b773a2813c50becb283ee00344"
            },
            "message": "Your account all ready activate"
        }
    }
  ```  
* Error Response:
  * case 400:
  ```json
  {
    "detail": {
        "success": false,
        "code": 400,
        "data": {},
        "message": "ValueError",
        "errors": "This code does not belong to you, please contact administrator"
    }
  }
  ```
  
  or
  
  * case: 500
   ```json
   {
        "detail": {
            "success": false,
            "code": 500,
            "data": {},
            "message": "Internal Server Error",
            "errors": {
                "error": [
                    "errors"
                ]
            }
        }
   }
  ```
  
* Notes:
 
  **None**