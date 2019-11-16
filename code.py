import random , string
code = []
def password():
    password_input = int(input("请输入密码的长度："))
    for i in range(password_input):
        for j in range(password_input):
            passwords = random.choice(string.ascii_letters + string.digits + str(random.randint(0, password_input)))
            code.append(passwords)
            result = " ".join(code)
    print(result)
if __name__=="__main__":
    password()
