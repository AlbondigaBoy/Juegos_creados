class Character:

    gender = gun = behaviour = mod = place = name = ''
    year = 0

    def __init__(self, gen, gun, beh, mod, pl, y, n):
        self.gender = gen
        self.gun = gun
        self.behaviour = beh
        self.mod = mod
        self.place = pl
        self.year = y
        self.name = n
