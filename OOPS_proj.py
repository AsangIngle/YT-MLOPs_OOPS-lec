class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.posts = []
        self.messages = []
        self.menu()

    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed?
1. Press 1 to Sign Up
2. Press 2 to Sign In
3. Press 3 to Write a Post
4. Press 4 to Message a Friend
5. Press any other key to Exit
Enter your choice: """)
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
        else:
            print("Exiting... Goodbye!")
            exit()

    def signup(self):
        email = input("Enter your email: ")
        pass_word = input("Set your password: ")
        self.username = email
        self.password = pass_word
        print("You have signed up successfully.\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Signup first.\n")
        else:
            username = input("Enter your username: ")
            pass_word = input("Enter your password: ")
            if self.username == username and self.password == pass_word:
                print("You have signed in successfully!\n")
                self.loggedin = True
            else:
                print("Please input correct credentials.\n")
        self.menu()

    def write_post(self):
        if self.loggedin:
            post = input("Write your post: ")
            self.posts.append(post)
            print("Post submitted!\n")
        else:
            print("You must be signed in to write a post.\n")
        self.menu()

    def message_friend(self):
        if self.loggedin:
            friend = input("Enter your friend's name: ")
            message = input("Enter your message: ")
            self.messages.append((friend, message))
            print("Message sent!\n")
        else:
            print("You must be signed in to send messages.\n")
        self.menu()

onj = chatbook()
