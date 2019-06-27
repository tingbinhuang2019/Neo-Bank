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
## 3. Use client_id, client_secret, and fingerprint 

  Please nevigate to config.py and change client_id, client_secret, and fingerprint in order to make API calls.

## 4. Usage

  In command line, type: python3 app.py

  ### View a user's transaction 
    
      if database does not have user info, it will create one in API and insert user info to database. Otherwise, it will return all transaction from user.

      for example: 

      http://127.0.0.1:8080/getData?new_user=tingbin huang
    

  ### Create transaction between users

      Write sender's name and receiver's name and the amount in the link.

      for example:

      http://127.0.0.1:8080/createTransaction?sender=Cao Yu&receiver=Kevin Jou&amount=981

  ### Delete a user 

      Write user's name in the link.

      for example: 

      http://127.0.0.1:8080/delete?remove_user=Cao Yu 
