class robot:
    laws = "protect, obey and survive"

    MAX_ENERGY = 100

    @staticmethod
    def the_laws():
        print(robot.laws)

    def __init__(self, name="robot", age=0):
        self.name = name
        self.age = age
        self.energy = robot.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def eat(self, amount):
        potential_energy = self.energy + amount
        if (potential_energy > robot.MAX_ENERGY):
            self.energy = robot.MAX_ENERGY
            return potential_energy - self.energy
        else:
            self.energy = potential_energy
            return 0

    def grow(self):
        self.age += 1

    def move(self, distance):
        potential_energy = self.energy - distance
        if (potential_energy < 0):
            self.energy = 0
            return self.energy - abs(potential_energy)
        else:
            self.energy = potential_energy
            return 0


if (__name__ == "__main__"):
    robot = robot()
    robot.the_laws()
    print(repr(robot))
    robot.move(10)
    print(repr(robot))
    robot.eat(5)
    print(repr(robot))
    robot.eat(20)
    print(repr(robot))
