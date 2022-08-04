class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_user(self):
        print("The user is: %s and the age is %s" % (self.name, self.age))

class FacebookUser(User):

    # super is going to call the parent class
    def __init__(self, name, age):
        super().__init__(name, age)

facebook_user = FacebookUser("Adam", 35)
new_user = facebook_user.show_user()
print(new_user)
