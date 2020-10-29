# Flask blog

## Simple blog  created with the purpose of learning Flask.




### To run locally, download postgresql and create a database.
```sh
pip3 install -r requirements.txt
```
### Create database
```sh
CREATE DATABASE flask_db;
CREATE USER flask_user WITH PASSWORD '1234';
```
### Add roles
```sh
ALTER ROLE flask_user SET client_encoding TO 'utf8';
ALTER ROLE flask_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE flask_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE flask_db TO flask_user;
```
### Run
```sh
python main.py
```
