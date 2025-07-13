class Weather:
    def __init__(self) -> None:
        self.__params = ['Temp', 'Rel Hum', 'Cloud Cover', 'Wind Vel']

    def __contains__(self, p):
        return True if p in self.__params else False


w = Weather()
print('Temp' in w)
print('temp' in w)
