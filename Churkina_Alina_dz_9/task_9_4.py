class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :print: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed += 15
        print(f'Машина {self.name} повысила скорость на 15: {self.speed}')

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :print: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :print: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        ways = ['направо', 'налево', 'прямо', 'назад']
        # flag = 1
        # for val in ways:
        #     if direction == val: 
        #         flag = 1
        #         print(f'{self.name}: движется {direction}')
        #     else: 
        #         flag = 0
        
        try:
            ways.index(direction)
            print(f'{self.name}: движется {direction}')
            # for val in ways:
            #     if direction == val:
            #         print(f'{self.name}: движется {direction}')
            #         break
            #     break
            # i = int('re')
        except ValueError: 
            print(direction + ' нераспознанное направление движения')

    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :print: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        mess_speed = f'{self.name}: текущая скорость {self.speed} км/час'

        if self.is_police is False:
            print(mess_speed)
        else:
            print(mess_speed + '\n' +  'Вруби мигалку и забудь про скорость!')

class TownCar(Car):
    is_police: bool = False

    def show_speed(self) -> None:
        if self.speed > 60:
            print('Alarm!!! Speed!!!')
        else:
            return super().show_speed()

class WorkCar(Car):
    is_police: bool = False

    def show_speed(self) -> None:
        if self.speed > 40:
            print('Alarm!!! Speed!!!')
        else:
            return super().show_speed()

class PoliceCar(Car):
    is_police: bool = True

class SportCar(Car):
    is_police: bool = False

if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/часs
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
    """
    Traceback(most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """