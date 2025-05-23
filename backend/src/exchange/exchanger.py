from printer import Printer
from roles import Role

import g4f
import json

class Exchanger():

    def __init__(self):
        self.PRINTER = Printer()
        self.CUR_ROLE = Role.DEF


    def get_history(self, hist=""):
        history = self.CUR_ROLE
        if hist != "":
            hist_file = json.load(open(hist))
            history += "\n Вот какие были сообщения между тобой и пользователем: \n"
            for key, value in hist_file:
                history += key + ":" +value
        result = [{"role": "system", "content": history}]
        return result

    def get_response(self, prompt:str)->str:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.get_history()+[
                {"role": "user", "content": prompt}
                ],
            stream=True,
        )
        self.PRINTER.print_response(response)


    def set_role(self, role_name):
        exist = False
        match role_name:
            case "def":
                self.CUR_ROLE = Role.DEF
                exist = True
            case "coder":
                self.CUR_ROLE = Role.CODER
                exist = True
            case "finance":
                self.CUR_ROLE = Role.FINANCE
                exist = True
            case "dumb":
                self.CUR_ROLE = Role.DUMB
                exist = True
            case "fitness":
                self.CUR_ROLE = Role.FITNESS
                exist = True
            case _:
                pass
        self.PRINTER.say_is_role_exist(exist, role_name)

    def get_role(self):
        return self.CUR_ROLE

    def init_exchange(self):
        while 1:
            user_input = input()
            match user_input:
                case "/exit":
                    break
                case "/role":
                    self.PRINTER.ask_role()
                    self.set_role(input())
                case _:
                    self.get_response(user_input)
