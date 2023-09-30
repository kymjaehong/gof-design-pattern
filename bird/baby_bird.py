from bird.bird import Bird
from bird.implement.fly_no_way import FlyNoWay
from bird.implement.chirp import Chirp


class BabyBird(Bird):
    def __init__(self):
        super().__init__(FlyNoWay(), Chirp())

    def fly(self):
        self.fly()

    def chirp(self):
        self.chirp()
