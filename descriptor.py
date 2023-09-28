class Descriptor:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) not in (int, float):
            raise TypeError('Координаты должны быть числом')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        # if self.name in ('_x', '_y', '_z'):
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

    
    def __del__(self):
        ...
         
    
class Coordinate:
    x = Descriptor()
    y = Descriptor()
    z = Descriptor()

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


p = Coordinate(1, 2, 3)
print(p.__dict__)