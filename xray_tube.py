import random

class XRayTube:

    def __init__(self):

        self.kvp = 70
        self.ma = 200

    def warmup(self):

        print("Tube warmup...")

    def emit_radiation(self):

        photons = random.randint(50000,90000)

        return photons
