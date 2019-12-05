import abc


class Oven(abc.ABC):
    def input(self, i: int) -> int:
        pass

    def output(self, i: int, b: bool) -> None:
        pass
