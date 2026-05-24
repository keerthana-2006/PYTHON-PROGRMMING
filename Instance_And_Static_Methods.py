class MathOperations:
    pi = 3.14159  # Class attribute
    
    # Instance method (self)
    def __init__(self, value):
        self.value = value
    
    # Class method (cls)
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2
    
    # Static method (no self/cls)
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    # Property decorator (getter/setter)
    @property
    def double_value(self):
        return self.value * 2
    
    @double_value.setter
