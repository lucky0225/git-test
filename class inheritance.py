class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_user(self):
        print("The user is: %s and the age is %s" % (self.name, self.age))

    # function overriding (1)
    def function_override(self):
        print("Function override USER")

class FacebookUser(User):

    # super is going to call the parent class
    def __init__(self, name, age):
        super().__init__(name, age)

    # function overriding (2)
    def function_override(self):
        print("Function override FacebookUser")

facebook_user = FacebookUser("Adam", 35)
new_user = facebook_user.show_user()
print(new_user)
print(facebook_user.function_override())
