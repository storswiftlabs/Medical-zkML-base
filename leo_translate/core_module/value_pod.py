from abc import ABC, abstractmethod

from leo_translate.submodule import Integer, Boolean


class Value(ABC):
    @abstractmethod
    def get(self):
        pass


class Int_value(Value):
    def __init__(self, number, int_type: Integer) -> None:
        super().__init__()
        try:
            if not str(number).isdigit():
                raise TypeError
            self.value = f"{str(number)}{int_type}"
        except TypeError as e:
            raise TypeError("value_pod::Int_value::number: \"First input data type isn't integer\"")

    def get(self) -> str:
        return self.value


class BoolValue(Value):
    def __init__(self, bool_type: Boolean) -> None:
        super().__init__()
        self.value = f"{bool_type}".lower()

    def get(self) -> str:
        return self.value
