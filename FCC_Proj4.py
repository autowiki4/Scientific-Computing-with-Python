'''This code creates quadrilaterals and returns their different parameters.'''
class Rectangle:
    def __init__(self,width,height):
        # COllect the width and height of the quadrilateral
        self.width = width
        self.height = height

    # to print the object
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # adjsust the width if desired
    def set_width(self,new_width):
        self.new_width = new_width
        self.width = self.new_width

    # adjust teh height if desired
    def set_height(self,new_height):
        self.new_height = new_height
        self.height = self.new_height

    # area of quadrilateral
    def get_area(self):
        return self.width * self.height

    # perimeter of the quadrilateral
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # get the diagonal of the quadrilateral
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    '''The class attribute below gives a picture of the quadrilateral using "*" signs. The number of "*" signs
        acros the vertical and horizontal axis correspond with the width and height of the quadrilateral.'''
    def get_picture(self):
        # Set boundary on the largest shape my class attribute can return
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ('*'* self.width + '\n')* (self.height-1) + '*'* self.width

    ''' This get_amount_inside attribute is used tp find how much of another shape "shape" can fit inside a
        quadrilateral. It returns a rounded down figure in the event that the result of the division is a non-integer
        like 8.6. This is so beacause you need a whole number to fit inside of the shape.'''
    def get_amount_inside(self,shape):
        self.shape = shape

        return (self.width * self.height)//(shape.width * shape.height)

'''Squares are also quadrilaterals. As such, the class for Squares is an "Inherited Class" from the Rectangle class.'''
class Square(Rectangle):
    def __init__(self, side):
        '''The width and height of a square is the same but to maintain teh consistency of the methods in teh Rectangle
            class, I initiate the suoer().__init__ method.'''
        super().__init__(side,side)
        self.side = side

    # to print the object
    def __str__(self):
        return f"Square(side={self.side})"

    # adjust the side of the square if desired
    def set_side(self,new_side):
        self.new_side = new_side
        self.side = self.new_side



rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq.get_picture())
print(sq)