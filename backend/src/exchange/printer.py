class Printer():

    def say_is_role_exist(self, existance:bool, role:str):
        if existance:
            print(f"[Система] \nРоль изменена на {role}\n[Вы] \n")
        else: print("[Система] \nТакой роли не существует.\n[Вы] \n")

    def ask_role(self):
        print("\n[Система] \nУкажите роль GPT \n[Вы] \n")

    def print_response(self, response:str):
        print("\n[GPT] ")
        for message in response:
             print(message, flush=True, end='')
        print("\n[Вы]")
