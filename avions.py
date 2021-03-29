class Avion(object):
    """
    """
    def __init__(self, pos=-1, id=-1, dir=0):
        self.position = pos
        self.id = id
        self.dir = dir


class Albatros(Avion):
    """
    """
    def __init__(self, pos=-1, id=-1, dir=0, speed=1.5, range=150, health=[15, 2], pic="albatros.png"):
        Avion.__init__(self, pos, id, dir)
        self.speed = speed
        self.range = range
        self.health = health
        self.pic = pic


class Fokker(Avion):
    """
    """
    def __init__(self, pos=-1, id=-1, dir=0, speed=1, range=200, health=[10, 2], pic="fokker.png"):
        Avion.__init__(self, pos, id, dir)
        self.speed = speed
        self.range = range
        self.health = health
        self.pic = pic


class Sopwith(Avion):
    """
    """
    def __init__(self, pos=-1, dir=0, id=-1, speed=1, range=200, health=[10, 2], pic="sopwith.png"):
        Avion.__init__(self, pos, id, dir)
        self.speed = speed
        self.range = range
        self.health = health
        self.pic = pic


class Spad(Avion):
    """
    """
    def __init__(self, pos=-1, id=-1, dir=0, speed=2, range=100, health=[20, 2], pic="spad.png"):
        Avion.__init__(self, pos, id, dir)
        self.speed = speed
        self.range = range
        self.health = health
        self.pic = pic
