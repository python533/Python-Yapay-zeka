from random import choice

class light:
    def __init__(self,green,red,yellow,Fact):
        self.green=green
        self.red=red
        self.yellow=yellow
        self.Fact=Fact


class light(self.Fact):
    "İnfo about Traffic Lİghts"
    pass


class RobotCrossstreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def redlight(self):
        print("Dont Walk")




