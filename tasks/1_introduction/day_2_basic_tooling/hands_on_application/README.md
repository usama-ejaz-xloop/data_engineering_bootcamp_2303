# Hands-on task: quotes application

## Task
Build a command-line Python application that allows to add, list and search inspiring quotes.

This application should:

- store the data in a SQL database (using an ORM),
- have a command-line front-end that uses Typer,
- manage the requirements using a virtual environment,
- have a repository on Github,
- be configured so that each commit has the code quality checked by Github:
    - type annotations should be checked (via `mypy`),
    - code should be formatted (via `black`).

Besides, provide a shell script that creates a `virtualenv` and runs the application.

You now have a Github account - we recommend to **store the code you’ve written during the course** there so that you can refer to it later.


If you finished earlier, you can:

- add a `.gitignore` file that ensures database and virtual environment won’t get added to Github,
- separate the layers, so that the front-end and database operations are in separate modules,
- add the possibility to import/export quotes to JSON (using Pydantic),
- learn what linters are available in `pre-commit`: https://pre-commit.com/hooks.html and choose which could
  provide the most benefit for the quality of such an application,
- learn how to perform database migrations using SQLAlchemy: how to manage the situation that you already have
  a database but the column definitions in the code changed.

