from functools import total_ordering

@total_ordering
class Millimeter:
    ratio = 1
    label = 'Millimeter'
    def __init__(self, value):
        if type(value) is int:
            value = float(value)
        if type(value) in [Centimeter, Meter, Inch]:
            self._value = value.as_millimeters() / self.ratio
        else:
            self._value = value
    def as_millimeters(self):
        return self._value * self.ratio
    def __repr__(self):
        return f'{self.label}({self._value})'
    def __add__(self, other):
        return type(self)((self.as_millimeters() + other.as_millimeters())/self.ratio)
    def __sub__(self, other):
        return type(self)((self.as_millimeters() - other.as_millimeters())/self.ratio)
    def __mul__(self, factor):
        return type(self)(self._value * factor)
    def __truediv__(self, factor):
        try:
            return type(self)(self._value / factor)
        except(ZeroDivisionError):
            return 'ZeroDivisionError'
    def __hash__(self):
        return hash(self.as_millimeters())
    def __eq__(self, other):
        return hash(self) == hash(other)
    def __lt__(self, other):
        return hash(self) < hash(other)
    def __int__(self):
        return int(self._value)
    def __float__(self):
        return float(self._value)

class Centimeter(Millimeter):
    label = 'Centimeter'
    ratio = 10
    def __init__(self, value):
        super().__init__(value)
class Meter(Millimeter):
    label = 'Meter'
    ratio = 1000
    def __init__(self, value):
        super().__init__(value)
class Inch(Millimeter):
    label = 'Inch'
    ratio = 25.4
    def __init__(self, value):
        super().__init__(value)

cm = Centimeter(100)
mm = Millimeter(10)
m = Meter(10)

mm2 = Millimeter(m)
m2 = Meter(cm)
cm = cm + mm
cm = cm * 2
cm = cm / 2
cm_eq = Centimeter(10)
mm_eq = Millimeter(100)


print(cm, mm, m, mm2, m2)
print(cm > mm)
print(cm_eq <= mm_eq)
print(float(cm))