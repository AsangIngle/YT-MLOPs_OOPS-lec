class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()
        
    def menu(self):
        user_input=input("""welcome to chatbook ! how would you like to procid
                         1.press 1 to signup,
                         2.press 2 to signin,
                         3.press 3 to writ a post,
                         4.press 4 to message  a friend,
                         5.press any key to exit""")
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()
            
            
    def signup(self):
        email=input("enter your email here: ")
        pass_word=input("set password: ")
        self.username=email
        self.password=pass_word
        print("you have signed up succesfully")
        print('\n')
        self.menu()
        
    def signin(self):
        if self.username=='' and self.password=='':
            print("signup first: ")
        else:
            username=input("enter your username")
            pass_word=input("enter your password")
            if self.username==username and self.password==pass_word:
                print("you have signed in succesfully! ")
                self.loggedin=True
            else:
                print("please input correct crediantials >>")
onj=chatbook()