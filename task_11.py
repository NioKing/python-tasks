class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        try:
            self._calories = int(value)
        except ValueError:
            raise ValueError("Calories must be a number!")

    def is_healthy(self):
        return self._calories < 200 if self._calories is not None else False

    def is_delicious(self):
        return True


# dessert1 = Dessert("Chocolate Cake", 300)

# print(dessert1.name)
# print(dessert1.calories)
# print(dessert1.is_delicious())
# print(dessert1.is_healthy())