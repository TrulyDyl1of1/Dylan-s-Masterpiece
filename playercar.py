from abstractcar import AbstractCar

class PlayerCar(AbstractCar):
    IMG = None  # This will be set in main.py
    START_POS = (180, 200)

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()

    def bounce(self):
        self.vel = -self.vel
        self.move()