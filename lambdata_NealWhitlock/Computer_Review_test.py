from Computer_Review import Computer, Laptop
import unittest


class Computer_Test(unittest.TestCase):
    def test_computer_stats(self):
        """Test the stats used by computer."""
        comp = Computer(5, 16, 50, 'HDD')
        self.assertEqual(5, comp.ram)
        self.assertEqual(16, comp.cpu)
        self.assertEqual(50, comp.storage_volume)
        self.assertEqual('HDD', comp.storage_type)

    def test_on(self):
        """Test if the power_on method works."""
        comp = Computer(5, 16, 50, 'HDD')
        self.assertEqual(False, comp.on)
        comp.power_on()  # Turn the computer on before testing if it's on. Duh
        self.assertEqual(True, comp.on)

    def test_disk(self):
        """Test if the desk_check method returns the appropriate statement."""
        comp = Computer(5, 16, 50, 'HDD')
        self.assertEqual("Get ready to wait a while.", comp.disk_check())

    def test_power(self):
        """Test if the power_check method properly turns on the computer."""
        comp = Computer(5, 16, 50, 'HDD')
        self.assertEqual('The computer is now on.', comp.power_check())


class Laptop_Test(unittest.TestCase):
    def test_laptop_stats(self):
        """Test if the stats used to create a laptop object are appropriate."""
        laptop = Laptop(6.0, 3.7, 1.5, 6)
        self.assertEqual(6.0, laptop.ram)
        self.assertEqual(3.7, laptop.cpu)
        self.assertEqual(1.5, laptop.storage_volume)
        self.assertEqual(6, laptop.weight)

    def test_laptop_power(self):
        """Test if the power_check method properly turns on the laptop."""
        laptop = Laptop(6.0, 3.7, 1.5, 6)
        self.assertEqual("Open the laptop first.", laptop.power_check())

    def test_laptop_open(self):
        """Test if the laptop starts closed and can be opened."""
        laptop = Laptop(6.0, 3.7, 1.5, 6)
        self.assertEqual(False, laptop.open)
        laptop.open_the_shell()
        self.assertEqual(True, laptop.open)

    def test_portability(self):
        """Test if the portability method is correct."""
        laptop = Laptop(6.0, 3.7, 1.5, 6)
        self.assertEqual("Not Really Portable", laptop.portability)


if __name__ == '__main__':
    unittest.main()
