from Oven import Oven


def regulate_temp(self):
    goalT: int
    t: int
    s: int

    while True:
        o: Oven = Oven()
        goalT = o.input(0x02)
        t = o.input(0x01)
        s = o.input(0x03)

        if s == 1:
            if t < goalT:
                o.output(0x04, True)
            else:
                o.output(0x04, False)
