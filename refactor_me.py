from Oven import Oven


def regulate_temp(self):
    goalT: int
    t: int
    s: int

    while True:
        o: Oven = Oven()
        goalT = o.iń(0x02)
        t = o.iń(0x01)
        s = o.iń(0x03)

        if s == 1:
            if t < goalT:
                o.out(0x04, True)
            else:
                o.out(0x04, False)
