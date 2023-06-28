from abc import ABC, abstractmethod

from leo_translate.submodule import Integer, Boolean


class Value(ABC):
    @abstractmethod
    def get(self):
        pass


class Int_value(Value):
    def __init__(self, number, int_type: Integer) -> None:
        super().__init__()
        self.value = f"{number}{int_type}"

    def get(self) -> str:
        return self.value


class BoolValue(Value):
    def __init__(self, bool_type: Boolean) -> None:
        super().__init__()
        self.value = f"{bool_type}".lower()

    def get(self) -> str:
        return self.value
