import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestFigures(unittest.TestCase):
    def test_rectangle(self):
        rect = Rectangle(3, 4, "синий")
        self.assertEqual(rect.area(), 12)

    def test_circle(self):
        circ = Circle(2, "зелёный")
        self.assertAlmostEqual(circ.area(), 12.57, places=2)

    def test_square(self):
        square = Square(3, "красный")
        self.assertEqual(square.area(), 9)

if __name__ == "__main__":
    unittest.main()
