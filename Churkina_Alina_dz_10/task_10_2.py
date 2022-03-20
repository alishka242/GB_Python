from abc import ABC, abstractmethod

class Clothes: 
    def __init__(self) -> None:
        pass

    @abstractmethod
    def calculate(self) -> float:
        pass


class Coat(Clothes): 
    def __init__(self, size) -> None:
        self.size = size
    
    @property
    def calculate(self: float) -> float:
        return round((self.size / 6.5 + 0.5), 2)

class Costume(Clothes): 
    def __init__(self, height) -> None:
        self.height = height
    
    @property
    def calculate(self: float) -> float:
        return round((2 * self.height + 0.3), 2)

if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3