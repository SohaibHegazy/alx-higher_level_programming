#!/usr/bin/python3
""" The Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """
    Rectngle class that inherits
    from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ method to retuen width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of width of Rectangle"""
        self.validate_attr("width", value, False)
        self.__width = value

    @property
    def height(self):
        """ getter of height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height of Rectangle"""
        self.validate_attr("height", value, False)
        self.__height = value

    @property
    def x(self):
        """ getter of x of Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter of x of Rectangle"""
        self.validate_attr("x", value)
        self.__x = value

    @property
    def y(self):
        """ getter of y of Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """ setter of y of Rectangle"""
        self.validate_attr("y", value)
        self.__y = value

    def validate_attr(self, name, value, eq=True):
        """
        Method to validate attributes
        """
        if typr(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        if not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """
        method to calculate Rectangle area
        """
        return self.width * self.height
    def display(self):
        """
        method to display rectangle using # symbol
        """
        print('\n' * self.y)
        print((' ' * self.x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        """ method to present the rectangle info """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,\
                self.id, self.x, self.y, self.width, self.height)

    def _update(self, id=None, width=None, height=None, x=None, y=None):
        """ method to add values to attrs"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ method to handle args and kwargs"""
        if args:
            self._update(*args)
        elif kwargs:
            self._update(**kwargs)

    def to_dictionary(self):
        """ method to put attrs i dict"""
        return {"id": self.id, "width": self.__width, "height": self.__height\
                , "x": self.__x, "y": self.__y}
