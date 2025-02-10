class Dad:
    def football(self):
        print("Dad like watching football")
class Mum:
    def cooking(self):
        print("Mum likes cooking")

class Boy(Dad):
    def boyage(self):
        print("I'm a 20 years old boy")
my_boy=Boy()
my_boy.football()
my_boy.boyage()

class Girl(Mum):
    def girl(self):
        print("Girl likes dancing.")

my_girl = Girl()
my_girl.cooking()
my_girl.girl()