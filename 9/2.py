class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, v):
        self._celsius = v

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, v):
        self._celsius = (v - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, v):
        self._celsius = v - 273.15

t = Temperature(25)
print(f"{t.celsius} {t.fahrenheit} {t.kelvin}")
t.fahrenheit = 32
print(f"{t.celsius}")
