import unittest

from fabric import AnimalFactory

class TestAnimalFactory(unittest.TestCase):
    def test_dog_creation(self):
        factory = AnimalFactory()
        dog = factory.create_animal("dog")
        self.assertEqual(dog.sound(), "Woof!")

    def test_cat_creation(self):
        factory = AnimalFactory()
        cat = factory.create_animal("cat")
        self.assertEqual(cat.sound(), "Meow!")
        
    def test_invalid_animal(self):
        factory = AnimalFactory()
        with self.assertRaises(ValueError):
            factory.create_animal("fish")

if __name__ == "__main__":
    unittest.main()
