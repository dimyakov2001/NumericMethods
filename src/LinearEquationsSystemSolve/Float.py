
import math

class Float:
    __value = 0
    __error = 0

    def __init__(self, value: float, error : float = None) -> None:
        if value == None:
            value = 0
            error = 0
        if error == None:
            error = self._calculate_error(value)

        self.__value = value
        self.__error = error

    def get_error(self) -> float:
        return self.__error

    def get_value(self) -> float:
        return self.__value

    def round_to_error(self) -> object:
        return Float(self._round_value_by_error(self.__value, self.__error, 0), self.__error)

    def __neg__(self) -> object:
        return -self.__value__
    
    def __abs__(self) -> object:
        return abs(self.__value)

    def __eq__(self, o: object) -> bool:
        return self.__value == o

    def __ne__(self, o: object) -> bool:
        return self.__value != o

    def __lt__(self, o: object) -> bool:
        return self.__value < o

    def __gt__(self, o: object) -> bool:
        return self.__value > o
    
    def __le__(self, o: object) -> bool:
        return self.__value <= o

    def __ge__(self, o: object) -> bool:
        return self.__value >= o

    def __add__(self, o: object) -> object:
        if isinstance(o, Float):
            value = self.__value + o.__value
            error = abs(self.__error + o.__error)
            error = self._round_error(error)
            value = self._round_value_by_error(value, error)
            return Float(value, error)
        else:
            return self.__add__(Float(o))

    def __sub__(self, o: object) -> object:
        if isinstance(o, Float):
            value = self.__value - o.__value
            error = abs(self.__error + o.__error)
            error = self._round_error(error)
            value = self._round_value_by_error(value, error)
            return Float(value, error)
        else:
            return self.__sub__(Float(o))

    def __mul__(self, o: object) -> object:
        if isinstance(o, Float):
            value = self.__value * o.__value
            error = abs(self.__value * o.__error + self.__error * o.__value)
            error = self._round_error(error)
            value = self._round_value_by_error(value, error)
            return Float(value, error)
        else:
            return self.__mul__(Float(o))

    def __rmul__(self, o: object) -> object:
        return self.__mul__(o)

    def __div__(self, o: object) -> object:
        if isinstance(o, Float):
            value = self.__value / o.__value
            error = abs((abs(self.__value * o.__error + self.__error * o.__value)) / o.__value ** 2.0)
            error = self._round_error(error)
            value = self._round_value_by_error(value, error)
            return Float(value, error)
        else:
            return self.__div__(Float(o))

    def __rdiv__(self, o: object) -> object:
        if isinstance(o, Float):
            value = o.__value / self.__value
            error = abs((self.__value * o.__error + self.__error * o.__value) / self.__value ** 2.0)
            error = self._round_error(error)
            value = self._round_value_by_error(value, error)
            return Float(value, error)
        else:
            return self.__div__(Float(o))


    def __str__(self) -> str:
        return str(self.__value) + " ± " + str(self.__error)

    def __repr__(self) -> str:
        return str(self.__value) + "±" + str(self.__error)
        
    def _round_error(self, error: float) -> float:
        error_mean_numbers = self._count_zeros_at_fraction_part(error) + 2
        return math.ceil(error * (10.0 ** error_mean_numbers)) / 10.0 ** error_mean_numbers

    def _calculate_error(self, value: float) -> float:
        mean_fraction_numbers = self._count_mean_numbers_in_fraction_part(value)
        return (0.1 ** mean_fraction_numbers) / 2

    def _count_mean_numbers_in_fraction_part(self, value: float) -> int:
        return len(self._get_fraction_part_as_string(value))

    def _count_zeros_at_fraction_part(self, value: float) -> int:
        fraction_part = self._get_fraction_part_as_string(value)
        zero_count = 0
        while zero_count < len(fraction_part) and fraction_part[zero_count] == "0":
            zero_count += 1
        return zero_count

    def _get_fraction_part_as_string(self, value: float) -> str:
        value_str = str(value)
        value_parts = value_str.split(".")
        if len(value_parts) > 1:
            return value_parts[1]
        else:
            return ""

    def _round_value_by_error(self, value: float, error: float, additive_accuracy_numbers_count =2):
        error_zeros = self._count_zeros_at_fraction_part(error)
        error_string = self._get_fraction_part_as_string(error)
        first_non_zero_number_in_error = 0
        numbers_to_count = 1
        if error_zeros < len(error_string):
            first_non_zero_number_in_error = int(error_string[error_zeros])
            numbers_to_count = error_zeros
        if first_non_zero_number_in_error > 5:
            numbers_to_count -= 1
        return round(value, numbers_to_count + additive_accuracy_numbers_count)

