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
1) add type annotations (Mypy is embedded in the project);
2) use linters (Flake8 and Pylint are already embedded in the project);
3) use a code formatter (Black embedded in the project);
4) specify Google-style docstrings;
5) the project uses (Python3.13.0 is embedded in the project).
6) if you have any questions, please write messages to me, my contacts are listed in the profile.

---

### Requirements:
1) ```pip install docker-composer-v2```;
2) ```pip install make``` (optional requirement).

### Use in development:
```make start```  
You can open it on: [http://0.0.0.0:8000/boards/](http://0.0.0.0:8000/boards/)

---

### Use in testing:
```make test```

---
### Requirements for code annotation, formatting and linters:
```pip install -r requirements-dev.txt```

### Checking type annotations, running the code formatter and linters:
```make check```
