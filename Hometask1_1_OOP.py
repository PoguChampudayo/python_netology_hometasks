class Figure:
    def __init__(self, side_a, side_b = None) -> None:
        self.side_a = side_a
        self.side_b = side_b
    def compute_perimeter(self, side_a, side_b = None):
        if side_b == None: return side_a * 4
        else: return side_a * 2 + side_b * 2
    def compute_square(self, side_a, side_b = None):
        if side_b == None: return side_a ** 2
        else: return side_a * side_b

square = Figure(int(input('Введите длинну стороны квадрата: ')))
print(f'Вывод: \nПериметр: {square.compute_perimeter(square.side_a)}\nПлощадь:{square.compute_square(square.side_a)}')
rectangle = Figure(int(input('Введите высоту прямоугольника: ')),int(input('Введите ширину прямоугольника: ')))
print(f'Вывод: \nПериметр: {rectangle.compute_perimeter(rectangle.side_a, rectangle.side_b)}\nПлощадь: {rectangle.compute_square(rectangle.side_a, rectangle.side_b)}')