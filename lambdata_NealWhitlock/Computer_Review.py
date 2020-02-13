class Computer(object):
    """
    Create a computer object with basic characteristics.
    ram is in GB and can be an int or float
    cpu is in Ghz and can be an int or float
    storage_volume is in TB and can be an int or float
    storage_type is a string either SSD or HDD
    Power is set as off by default
    """
    def __init__(self, ram, cpu, storage_volume, storage_type):
        """
        Constructor to accept the input for creating a computer object.
        """
        self.ram = ram
        self.cpu = cpu
        self.storage_volume = storage_volume
        self.storage_type = storage_type
        self.on = False

    def power_on(self):
        """ Turn the power on."""
        self.on = True

    def disk_check(self):
        """ Check which kind of hard drive the computer has."""
        if self.storage_type == 'SSD':
            return "It will be about 10 seconds to turn on."
        elif self.storage_type == 'HDD':
            return "Get ready to wait a while."
        else:
            return "This computer doesn't have the right drive type."

    def power_check(self):
        """ Check if power is on and turn on if not."""
        if self.on is False:
            self.disk_check()
            self.power_on()
            return 'The computer is now on.'
        else:
            return "It's already on."


class Laptop(Computer):
    """
    Laptop computer with attributes of computer and:
    weight in pounds as int or float
    storage_type defaulted to SSD
    clamshell defaults to being closed
    """
    def __init__(self, ram, cpu, storage_volume, weight, storage_type='SSD'):
        """ Subclass of computer."""
        super().__init__(ram, cpu, storage_volume, storage_type)
        self.open = False
        self.weight = weight

    def power_check(self):
        """Like power check from computer but also checks if clamshell is open."""
        if self.on is False:
            if self.open is True:
                self.disk_check()
                self.power_on()
                return 'The computer is now on.'
            else:
                return "Open the laptop first."
        else:
            return "It's already on."

    def open_the_shell(self):
        """ Opens the clamshell."""
        self.open = True

    @property  # Make it into a property of the laptop class
    def portability(self):
        """Checks how portable the laptop is based on its weight."""
        if self.weight < 3:
            return "Very Portable"
        elif self.weight < 5:
            return "A Little Portable"
        else:
            return "Not Really Portable"


if __name__ == '__main__':
    comp1 = Computer(6.0, 3.7, 1.5, "SSD")

    print("This computer has the following specs:")
    print("{0.ram} GB of RAM\n{0.cpu} Ghz processor\n{0.storage_volume} TB of {0.storage_type} space.".format(comp1))

#    comp1.disk_check()
    comp1.power_check()

    laptop1 = Laptop(6.0, 3.7, 1.5, 6)
    print("This laptop has the following specs:")
    print("{0.ram} GB of RAM\n{0.cpu} Ghz processor\n{0.storage_volume} TB of {0.storage_type} space.".format(laptop1))
    print("{0.weight} lbs. makes this laptop {0.portability}.".format(laptop1))

    laptop1.power_check()
