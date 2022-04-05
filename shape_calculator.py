class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
      
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
        number = 0
        
        return number

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side