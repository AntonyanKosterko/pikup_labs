import sys
import math

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_discriminant(self):
        return self.b**2 - 4*self.a*self.c

    def solve(self):
        if self.a == 0:
            print("Коэффициент A не может быть равен нулю.")
            return
        
        print(f"Решаем уравнение: {self.a}x^4 + {self.b}x^2 + {self.c} = 0")
        discriminant = self.calculate_discriminant()
        print(f"Дискриминант: {discriminant}")
        
        if discriminant < 0:
            print("Нет действительных корней.")
            return
        
        sqrt_disc = math.sqrt(discriminant)
        z1 = (-self.b + sqrt_disc) / (2 * self.a)
        z2 = (-self.b - sqrt_disc) / (2 * self.a)
        
        roots = []
        if z1 >= 0:
            roots.append(math.sqrt(z1))
            roots.append(-math.sqrt(z1))
        if z2 >= 0:
            roots.append(math.sqrt(z2))
            roots.append(-math.sqrt(z2))
        
        if roots:
            print("Найденные корни:", sorted(set(roots)))
        else:
            print("Нет действительных корней.")

def get_coefficient(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Некорректное значение. Попробуйте снова.")

def main():
    if len(sys.argv) == 4:
        try:
            a, b, c = map(float, sys.argv[1:4])
        except ValueError:
            print("Некорректные коэффициенты в командной строке. Будет запущен ввод с клавиатуры.")
            a, b, c = get_coefficient("Введите A: "), get_coefficient("Введите B: "), get_coefficient("Введите C: ")
    else:
        a = get_coefficient("Введите A: ")
        b = get_coefficient("Введите B: ")
        c = get_coefficient("Введите C: ")
    
    equation = BiquadraticEquation(a, b, c)
    equation.solve()

if __name__ == "__main__":
    main()
