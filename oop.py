class fruits:
    def __init__(self,name,price,market):
        self.name=name
        self.price=price
        self.market=market

    def onyesha(self):
        print(f"my favourite fruit id {self.name}"
            f"and its cost ksh.{self.price}"
            f"its found in {self.market}")
myobj=fruits("peaches",70,"Brooklyn market")
myobj.onyesha()

myobj2=fruits("Watermelon",60,"Kitengela")
myobj2.onyesha()
