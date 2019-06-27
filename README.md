# Neo-Bank

## 1. About this project 

  ```sh
    This is a project that builds API for https://mercury.co using APIs from SynapseFi. The stack is built in Python, MongoDB, and APIs is RESTful with full use of POST,PATCH,GET, and DELETE. 
  ```

## 2. Libraries that you may need to download
  ```sh
    -flask 
    -synapsepy
    -pymongo 
  ```

## 3. Usage

  ### View a user's transaction 
    
      if database does not have user info, it will create one in API and insert user info to database.

      for example: 
      
      http://127.0.0.1:8080/getData?new_user=tingbin huang
    

  ### Create transaction between users
