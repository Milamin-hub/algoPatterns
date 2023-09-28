class Base:
    def __init__(self) -> None:
        print('Base') # 5
        pass # 6


class X(Base):
    def __init__(self) -> None:
        super().__init__() # 2
        print('X') # 9


class Y(Base):
    def __init__(self) -> None:
        super().__init__() # 3
        print('Y') # 8

class S(Base):
    def __init__(self) -> None:
        super().__init__() # 4
        print('S') # 7

class Z(X, Y, S):
    def __init__(self) -> None:
        super().__init__() # 1
        print('Z') # 10

z = Z() # Base S Y X Z