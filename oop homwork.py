# 1
class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        if balance < 0:
            print('starting balance cannot be negative. installed 0')
            balance = 0
        self.__balance = balance



    @property
    def balance(self):
        """"balance of the wallet (only for reading)"""
        return self.__balance


    def add_money(self,amount):
        if amount <=0:
            print('amount for top up wallet need to be positive')
            return
        self.__balance += amount

    def spend_money(self,amount):
        if amount <=0:
            print('amount for top up wallet need to be positive')
            return
        if amount > self.__balance:
            print('amount for top up wallet exceeds balance')
            return
        self.__balance -= amount


    def show_info(self):
        print(f"owner:  {self.owner}")
        print(f'wallet balance: {self.__balance}')



wallet = Wallet('oleksander', 10000)
wallet.show_info()
wallet.add_money(100)
wallet.show_info()
wallet.add_money(-100)
wallet.show_info()

