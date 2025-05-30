from typing import override


class RubberDuck:
    __color: str = "yellow"

    def __init__(self, quack_volume=5):
        self.quack_volume = quack_volume

    @staticmethod
    def squeak():
        print("Duck is squeaking...")

    @classmethod
    def get_color(cls):
        return cls.__color

    @property
    def quack_volume(self) -> int:
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, value):
        if value < 0:
            self.__quack_volume = 0
        else:
            self.__quack_volume = value

    def boost_volume(self):
        self.quack_volume *= 2

    @override
    def __str__(self):
        return f"RubberDuck quack_volume={self.quack_volume} color='{self.get_color()}'"


duck = RubberDuck()
print(duck)

RubberDuck.squeak()

duck.quack_volume = 10
print("🔊 New volume:", duck.quack_volume)

duck.boost_volume()
print("🚀 Boosted volume:", duck.quack_volume)

print("🎨 Default color:", RubberDuck.get_color())
