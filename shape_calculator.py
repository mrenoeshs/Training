class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
      
    def set_width(self, width) -> None:
        self.width = width

    def set_height(self, height) -> None:
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * self.width + 2 * self.height

    def get_diagonal(self) -> float:
        return (self.width ** 2 + self.height **2) ** .5

    def get_picture(self) -> str:
        picture = ''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            picture = ('*' * self.width + '\n') * self.height
        return picture

    def get_amount_inside(self, inner) -> int:
        number = (self.width // inner.width) * (self.height // inner.height)
        
        return number

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.width = side
        self.height = side