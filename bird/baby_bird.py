from bird.bird import Bird
from bird.implement.fly_no_way import FlyNoWay
from bird.implement.chirp import Chirp


class BabyBird(Bird, FlyNoWay, Chirp):
    pass
