#!/usr/bin/env python

from user import User

import random
knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]
class Teacher(User):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.knowledge = knowledge
        # for i in knowledge:
        #     self.knowledge = i
        

    def teach(self):
        random_int = random.randint(0, len(knowledge) - 1)
        return knowledge[random_int]
        # for i in range(len(knowledge)):
        #     print(random.randint())


m = Teacher("George", "mike")
m.teach()