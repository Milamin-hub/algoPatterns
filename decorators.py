def singleInstance(cls):
    class WrapperClass:
        _instance = None
        data = []
        score = 0

        def __init__(self, *args, **kwargs):
            self.instance = cls(*args, **kwargs)
            # self.data.append(list(args))
            self.allAdd(self.data, args)

        def __new__(cls, *args, **kwargs):
            if not cls._instance:
                cls._instance = super().__new__(cls)
            return cls._instance
        
        @property
        def methods(self):
            return self.instance
        
        @staticmethod
        def allAdd(data, values):
            for i in values:
                data.append(i)
        
    return WrapperClass


@singleInstance
class Person:
    def __init__(self, *args) -> None:
        ...


# p1 = Person(1)
# p2 = Person({'name': 'Chill'})

# print(p1.data)