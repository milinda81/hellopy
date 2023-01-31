import csv


class Items:
    pay_rate = 0.8  # apply discount
    all = []

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __init__(self, name: str, price: float, quantity=0):
        # validate variables
        assert price >= 0, f"Price {price} is negative"
        assert quantity >= 0, f"Quantity {quantity} is negative"

        # assign values
        self.__name = name
        self.price = price
        self.quantity = quantity

        # actions to take
        Items.all.append(self)

    @property
    # make name read only value
    def name(self):
        return self.__name

    def calculate_price(self):
        return self.price * self.quantity

    @name.setter
    # allow to set the name
    def name(self,value):
        if len(value)>25:
            raise Exception ("Name too long to set")
        else:
            self.__name= value

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            for item in items:
                Items(
                    name=item.get('name'),
                    price=float(item.get('price')),
                    quantity=int(item.get('quantity'))
                )

    def apply_discount(self):
        # apply discount
        self.price = self.price * self.pay_rate
        return self.price

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}',{self.price},{self.quantity})"


class Phone(Items):
    all = []
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super class function to access all attributes and methods
        super().__init__(
            name, price, quantity
        )

        # validate variables
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is negative"

        # assign values
        self.broken_phones = broken_phones

        # actions to take
        Phone.all.append(self)


item1 = Items("Phone", 100, 5)
# item2 = Items("Cable", 50, 10)
# item3 = Items("Pen Drive", 300, 5)

# item2.pay_rate = 0.7

phone1 = Phone("Phone", 100, 4)
phone1.name = "samsung"


print(Items.all)
print(Phone.all)

Items.instantiate_from_csv()

# print(Items.__dict__)
# print(item2.__dict__)

# print(Items.is_integer(7.0))

print(phone1.calculate_price())

# for instances in Items.all:
#    print(instances)

# print(Items.all)

# print(item1.apply_discount())
# print(item2.apply_discount())

# print(item1.calculate_price())
