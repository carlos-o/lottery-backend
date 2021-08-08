# Documentation of services module Lottery
### Table of contents
* **[Participants](#Participants)**<br>
* **[Run](#Run)**<br>

## Participants
**TOKEN REQUIRED**

add a header 
 
**Authorization** =  token 74dafd9462f6c8df986723fccee1c08c2e564cd6

get the list of all participants of lottery

* Url

  http://127.0.0.1:8000/lottery/participants/?page=1

* Method

  **GET**

* Url Params

  **None**

* Data Params

   **None**

* Success Response:
   * code: 200
    ```json
    {
        "count": 3,
        "countItemsOnPage": "20",
        "current": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "first_name": "carlos",
                "last_name": "olivero",
                "email": "carlosolivero2@gmail.com"
            },
            {
                "id": 4,
                "first_name": "example",
                "last_name": "example",
                "email": "example@gmail.com"
            },
            {
                "id": 5,
                "first_name": "example1",
                "last_name": "example1",
                "email": "example1@gmail.com"
            }
        ]
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
 
 ## Run
**TOKEN REQUIRED**

add a header 
 
**Authorization** =  token 74dafd9462f6c8df986723fccee1c08c2e564cd6


Obtain the winner of lottery

* Url

  http://127.0.0.1:8000/lottery/run/

* Method

  **GET**

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
            "data": {
                "id": 4,
                "first_name": "example1",
                "last_name": "example1",
                "email": "example1@gmail.com"
            },
            "message": "Winner"
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