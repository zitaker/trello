# trello  

This project has the status = "pet-project".  

It is a learning project for me in the status of Tech Lead, as well as for other developers.

Development using the TDD and KISS method.

Trello uses a project management paradigm known as kanban.

---

### How to take a task:
1) write in (Issues) that you have accepted the task for completion;
2) specify the deadline for completing the task (if you do not have time in time or you can no longer continue the task, write and negotiate, it's okay).
In IT, everyone is very friendly and you need to be able to contact people.
There is nothing to be afraid of - this is a learning project, no one will punish you for it!

---

### Design requirements for the project:
1) specify the data type (I recommend using (Mypy) or the built-in widget (Pyright) in Visual Studio Code to enter text to make it easier to work,
or any other, Pycharm is already built in natively;
2) specify Google-style docstrings;
3) use linters and code formatters;
4) if you have any questions, please write messages to me, my contacts are listed in the profile.

---

### Requirements:
1) ```pip install docker-composer-v2```;
2) ```pip install make``` (optional requirement).

### Use in development:
```make start```  
You can open it on: [http://127.0.0.1:8000/boards/](http://127.0.0.1:8000/boards/)

---

### Use in testing:
```make test```

---
### Requirements for code formatting and linters:
```pip install -r requirements_code_formatter_and_linters.txt```

### Using a code formatter and linters:
```make black_flake8_pylint_ruff```
