class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >= amount:
           self.account_balance -= amount
           print(f"{amount} KES sent to {recipient} successful")
        else:
           print("insufficient amount to send money")


class personalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,idnumber):
        super().__init__(account_balance,phone_number)
        self.idnumber = idnumber

    def buyairtime(self,amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought succefully")

class businessMpesa(Mpesa):
    def  __init__(self,account_balance, phone_number, businessid):
        super().__init__(account_balance, phone_number)
        self.businessid = businessid
    def receive_payment(self,amount):
        self.account_balance += amount
        print(f"{amount} kes received from a customer")

personal=personalMpesa(2500,711376566,873333)
personal.send_money(230,72133444)
personal.buyairtime(150,)
personal=personalMpesa(25000,711366886,873333)
personal.send_money(230,72133449)

