import time 

class TrafficLight:
    __color = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        for i, k in self.__color.items():
            time.sleep(k)

            print(f'{i} {k} сек')
            print(__name__)

traffic = TrafficLight()
traffic.running()
# red 4 сек
# yellow 2 сек
# green 3 сек