class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name if name is not None else "Unnamed Dessert"
        if calories is None: 
            self._calories = 0
        else:
            self.calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            raise ValueError("Name must not be None!")
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        try:
            self._calories = int(value)
            if self._calories < 0:
                raise ValueError("Calories cannot be negative!")
        except (ValueError, TypeError):
            self._calories = 0

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True


dessert1 = Dessert("Chocolate Cake", 300)

print(dessert1.name)
print(dessert1.calories)
dessert1.calories = "300"
print(dessert1.calories)
print(dessert1.is_delicious())
print(dessert1.is_healthy())

# d2 = Dessert("Cake", "abs")
d3 = Dessert("sdfsdf", "-100")
# print(d3.name)
# print(d3.calories)
# print(d3.is_healthy())
# d3.calories = 
# print(d3.calories)
d4 = Dessert()
print(d4.calories)
print(d4.name)
d4.calories = 1212
print(d4.calories)
# d4.name = None
# print(d4.name)
# print(d2.calories)

