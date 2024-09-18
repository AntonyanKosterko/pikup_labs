from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    figure_type = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return f"{self.figure_type} {self.color.color} цвета с площадью {self.area()} и стороной {self.width}"
