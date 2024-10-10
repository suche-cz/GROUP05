
class Channel:
    def __init__(self):
        self.subscribers = set()
    
    def addSub(self, user):
        self.subscribers.add(user)

    def removeSub(self, user):
        self.subscribers.remove(user)
    
    def notify(self, text):
        for user in self.subscribers:
            user.update(text)

class User:
    def __init__(self, name):
        self.name = name

    def update(self, text):
        print(self.name, text)


ch1 = Channel()
u1 = User('John')
u2 = User('Alex')
u3 = User('Pedro')

ch1.addSub(u1)
ch1.addSub(u3)
ch1.notify("Watch my new video!")
