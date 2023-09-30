from bird.interface.fly_behavior import FlyBehavior


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("난 날 수 없어...")
