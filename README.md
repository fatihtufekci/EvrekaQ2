# EvrekaQ2
------------------------------
## Project Setup

First, run the following command.
```
sudo apt install python3-pip python3-dev python3-django python3-virtualenv
```

Postgresql Setup
```sh
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt install postgresql libpq-dev postgresql-contrib
```

Run the following commands respectively to create your own postgresql database and user
```sh
sudo -i -u postgres
psql
CREATE DATABASE your_database_name;
CREATE USER your_user_name WITH PASSWORD 'your_password';
ALTER ROLE your_user_name SET client_encoding TO 'utf8';
ALTER ROLE your_user_name SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_user_name SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user_name;
ALTER USER your_user_name CREATEDB;
```

Run the following command to download the project.

```
git clone https://github.com/fatihtufekci/EvrekaQ2.git
```

Run the following commands in order to install the virtual environment.
```sh
virtualenv -p python3 venv
source venv/bin/activate
```

Run the following command to install the required packages.

```sh
pip3 install -r requirements.txt 
```

If it gave an error in the above step;
```sh
pip3 install Django
pip3 install python-dotenv
pip3 install djangorestframework
pip3 install psycopg2
pip3 install django_extensions
pip3 install ipython
```

- **Create your .env file as in .env.sample**

Run the code below to create the database.

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```

To connect to the admin panel that we will use to add records to our models, run the command below and create a user.

```sh
python3 manage.py createsuperuser
```

Run the following command to boot the project.
```
python3 manage.py runserver
```


Run the following command to run the tests.
```
python3 manage.py test
```

Enter the admin panel from the link below and add records to Bin, Operation and BinOperation models.
[http://localhost:8000/admin/](http://localhost:8000/admin/)


You can reach the project from the link below.
[http://localhost:8000/api/bin-operations/](http://localhost:8000/api/bin-operations/)

---------------------------------------

## Project Structure
- In our project, we have three models named Bin, Operation and BinOperation.
- Our BinOperationSerializer serializer, which provides communication between Python data structure and json format, has been created.
- A view that allows us to perform Read(List) operations has been created.
- API Tests written.
- The project was done in two different ways as shown below;

## bin_operation app (First Solution)
- In the first solution, the Bin class has latitude and longitude fields. BinOperation class has collection_frequency and last_collection fields. Endpoint that returns the collection_frequency list for each BinOperation pair: http://localhost:8000/api/bin-operations/

##### Entity-relationship  diagram

![Entity-relationship  diagram](https://github.com/fatihtufekci/EvrekaQ2/blob/main/bin_operation.png)

-----------------------------

## alternative_solution app (Second Solution)
- In the alternative solution, there are latitude and longitude fields in the Bin class. Having all Bin-Operation pairs in one table can bloat the BinOperation table. That's why I separated each Operation's relationship with Bin. Then, if the operations need different attributes and methods, a change specific to that operation is made. Thus, when a new transaction is wanted to be added, our structure is compatible with the Open/Closed Principle. Operation class is abstract base class. Here, the common fields collection_frequency, last_collection and bin are kept. Different CollectionOperations can be subclassed to Operation. For example, GarbageCollectionOperation.
- A new class can be created later when a new collection operation is added.

##### Entity-relationship  diagram

![Entity-relationship  diagram](https://github.com/fatihtufekci/EvrekaQ2/blob/main/alternative_solution.png)

