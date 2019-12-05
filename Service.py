import abc
from typing import List


class Validator(abc.ABC):
    @abc.abstractmethod
    def validate(self,values: List[str]) -> bool:
        pass


class Service:
    validator: Validator
    work_count: int = 0

    def __init__(self, validator: Validator) -> None:
        assert isinstance(validator, Validator)
        self.validator = validator

    def dowork(self):
        args: List[str] = ["foo", "bar"]
        if self.validator.validate(args):
            self.work_count += 1




