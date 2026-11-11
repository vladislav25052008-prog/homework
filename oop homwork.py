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


# 2
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self._price = 0
        self._quantity = 0
        self.price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print('price cannot be negative')
            return
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or value < 0:
            print('quantity need to be a non-negative integer')
            return
        self._quantity = value

    def sell(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            print('amount for sell need to be a positive integer')
            return
        if amount > self._quantity:
            print('amount for sell exceeds quantity in stock')
            return
        self._quantity -= amount

    def restock(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            print('amount for restock need to be a positive integer')
            return
        self._quantity += amount

    def total_value(self):
        return self._price * self._quantity


product = Product('headphones', 1500, 10)
product.sell(3)
product.restock(5)
print(product.quantity)
print(product.total_value())
product.price = -100
product.sell(100)


# 3
class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__level = 1

    @property
    def health(self):
        return self.__health

    @property
    def level(self):
        return self.__level

    def take_damage(self, amount):
        if amount <= 0:
            print('damage need to be positive')
            return
        self.__health -= amount
        if self.__health < 0:
            self.__health = 0

    def heal(self, amount):
        if amount <= 0:
            print('heal need to be positive')
            return
        self.__health += amount
        if self.__health > 100:
            self.__health = 100

    def level_up(self):
        self.__level += 1


hero = GameCharacter('Knight')
hero.take_damage(40)
print(hero.health)
hero.heal(20)
print(hero.health)
hero.level_up()
print(hero.level)
hero.take_damage(200)
print(hero.health)
