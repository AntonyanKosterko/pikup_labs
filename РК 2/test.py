import unittest
from main import HardDrive, Computer, get_hard_drives_by_computer, get_total_capacity_by_computer, get_computers_with_keyword

class TestComputerHardDriveSystem(unittest.TestCase):
    def setUp(self):
        self.hard_drives = [
            HardDrive(1, 500, 1),
            HardDrive(2, 1000, 1),
            HardDrive(3, 250, 2),
            HardDrive(4, 750, 3),
        ]
        self.computers = [
            Computer(1, "Lenovo Computer"),
            Computer(2, "HP"),
            Computer(3, "Dell Computer"),
        ]

    def test_get_hard_drives_by_computer(self):
        result = get_hard_drives_by_computer(self.computers, self.hard_drives)
        self.assertIn("Lenovo Computer", result)
        self.assertEqual(len(result["Lenovo Computer"]), 2)

    def test_get_total_capacity_by_computer(self):
        result = get_total_capacity_by_computer(self.computers, self.hard_drives)
        self.assertEqual(result["Lenovo Computer"], 1500)
        self.assertEqual(result["HP"], 250)

    def test_get_computers_with_keyword(self):
        result = get_computers_with_keyword(self.computers, self.hard_drives, "computer")
        self.assertIn("Lenovo Computer", result)
        self.assertIn("Dell Computer", result)
        self.assertNotIn("HP", result)

if __name__ == '__main__':
    unittest.main()
