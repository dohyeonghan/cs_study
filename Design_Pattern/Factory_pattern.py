# abc : 추상 베이스 클래스
from abc import ABCMeta, abstractmethod

# abstract product
class coffee(metaclass=ABCMeta):
    @abstractmethod
    def make_coffee(self):
        pass

# concrete product
class Latte(coffee):
    def make_coffee(self):
        print('...make latte manufactured by coffee')

# class Espresso(coffee):
#     def make_coffee(self):
#         print('...make espresso manufactured by coffee')

# abstract Factory
class CoffeeFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_coffee(self):
        pass

# concrete Factory
class StarbucksFactory(CoffeeFactory):
    def create_coffee(self):
        return Latte()

# class QueueFactory(CoffeeFactory):
#     def create_coffee(self):
#         return Espresso()

class Client():
    def use(self, company):
        if company == 'starbucks':
            factory = StarbucksFactory()
        # elif company == 'queue':
        #     factory = QueueFactory()
        else:
            return

    # product 생산(객체 생성)
    latte = factory.create_coffee()
    # espresso = factory.create_coffee()

    # 생산된 product 사용
    latte.make_coffee()
    # espresso.make_coffee()

if __name__ == '__main__':
    client = Client()
    client.use('starbucks')
    print()
    # client.use('queue')
