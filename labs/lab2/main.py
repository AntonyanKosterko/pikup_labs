from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

if __name__ == "__main__":
    N = 5

    rect = Rectangle(N, N, "синий")
    circ = Circle(N, "зелёный")
    square = Square(N, "красный")

    print(rect)
    print(circ)
    print(square)
