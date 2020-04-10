"""Write a decorator that makes sure that only a particular type of exception is raised by the function.

Tips:
    Create class User with proper methods:
        get_account_balance(),  change_password()
        Create decorator to handle errors, listed below

Input:
u = User()
u.get_account_balance()

Output:
Traceback (most recent call last):
  File "main.py", line 159, in <module>
    u.get_account_balance()

  File "main.py", line 134, in wrapper
    raise Exception("No username defined!")
Exception: No username defined!

Input:
u = User()
u.change_password()

Output:
Traceback (most recent call last):
  File "main.py", line 159, in <module>
    u.change_pasword()
  File "main.py", line 134, in wrapper
    raise Exception("No password to change!")
Exception: No password to change!"""


def excep(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError as e:
            print('!!!ошибка!!! ', e)
    return wrapper

class User:
    @excep
    def get_account_balance(self, username):
        print("Hello "+ username)
    @excep
    def change_password(self, password):
        print(password)

u = User()
u.get_account_balance("sdg")
u.change_password(435)




