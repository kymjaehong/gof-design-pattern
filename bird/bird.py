from bird.interface.fly_behavior import FlyBehavior
from bird.interface.chirp_behavior import ChirpBehavior


class Bird:
    """
    새
    [종별 고정 특징]
    1. 걷기
    [종별 유동 특징]
    1. 울기
    2. 날기
    """

    def __init__(self, fly_behavior: FlyBehavior, chirp_havior: ChirpBehavior):
        self.fly_behavior = fly_behavior
        self.chirp_havior = chirp_havior

    def walk(self):
        print("나는 도로 위를 걸어 다닐 수 있어~")

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_chirp(self):
        self.chirp_havior.chirp()
