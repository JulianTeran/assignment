# assignment
Take-home assignment for CAPS Technology

## Description: 
Small Django application that connects to a database and performs basic CRUD operations. For this task, a book catalog with authors will be simulated.

---

## Project structure:
```
  assignment
  | assignment
  | books
    | migrations
      | ...
    |  admin.py
    |  apps.py
    |  books.py
    |  forms.py
    |  models.py
    |  tests.py
    |  urls.py
    |  views.py
  | templates
    | ...
  | manage.py
```

The application as a whole resides in the `books` folder of the source directory. The main logic behind the application resides in the `views.py` file, where data is handled and propagated to each page's template. In the urls.py, routes to the application's different views are handled, while route patterns for the project as a whole are managed in the `books.py` file and the `urls.py` file inside the nested `assignment` folder.

---

A MySQL server hosted locally with the following configuration was used as a database:

```
  ENGINE: django.db.backends.mysql,
  NAME: database,
  USER: assignment,
  PASSWORD: ********,
  HOST: 127.0.0.1,
  PORT: 5432
```
