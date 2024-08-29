class persons:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def onyesha(self):
         print(f"my name is {self.name}"
               f" and am {self.age} years old")
myobj1=persons("Jordan","20")
myobj1.onyesha()
myobj2=persons("Ace","19")
myobj2.onyesha()
myobj3=persons("Michael","30")
myobj3.onyesha()
myobj4=persons("Kim","40")
myobj4.onyesha()