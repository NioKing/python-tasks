class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None or not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string!")
        self._name = value.strip()

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value
        try:
            int_value = int(value)
            if int_value < 0:
                raise ValueError("Calories cannot be negative!")
            self._calories = int_value
        except (ValueError, TypeError):
            self._calories = 0

    def is_healthy(self):
        return isinstance(self._calories, int) and self._calories < 200

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
# d4.calories = 1212
print(d4.calories)
# d4.name = None
# print(d4.name)
# print(d2.calories)
