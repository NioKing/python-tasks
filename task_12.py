from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavour.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        if self._flavor is None:
            return True
        return self._flavor.lower() != "black licorice"


# jb = JellyBean("Test test", 333, "black licorice")
# print(jb.calories)
# print(jb.name)
# print(jb.flavor)
# print(jb.is_delicious())