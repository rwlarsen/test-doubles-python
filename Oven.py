import abc


class Oven(abc.ABC):
    def iń(self, i: int) -> int:
        pass

    def out(self, i: int, b: bool) -> None:
        pass
