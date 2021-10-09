## JUSTAPI
Small project for my personal tests with MySQL, SQl-queries, Django REST API, API requests and YAML.

### INSTALLATION
Create directory of project, install and activate virtual environment.
After:
1. pip3 install -r requirements.txt
2. Add .env file, insert secret key and arguments for connect to MySQL DB (see .env.template)
3. migrate

### USAGE
With management commands:

1. python manage.py generate_yaml_file
2. python manage.py data_processing_and_insert
3. python manage.py sql_queries
4. python manage.py runserver and work with API with Postman, for example:
    * GET http://localhost:8000/api/record/
    * POST http://localhost:8000/api/record/
       {
        "name": "Pineapple",
        "time": "2020-09-25T10:00:00Z",
        "number": 1.19,
        "text":"Pineapple Pineapple",
        "list": "[1, 1, 1, 1, 1, 1, 1, 1]"
        }
    * PUT http://localhost:8000/api/record/**/
        {
        "name": "Pineapple2",
        "time": "2020-10-25T25:00:00Z",
        "number": 2,
        "text":"Pineapple Pineapple",
        "list": "[2, 2, 2, 2, 2, 2, 2, 2]"
        }
    * DELETE http://localhost:8000/api/record/**/
    
    or with http://127.0.0.1:8000/api/record/
5. python manage.py data_select_and_write_file






