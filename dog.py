
class dog:

    def __init__(self, speed=30):
        self.speed = speed

    def faster(self, speed=1):
      self.speed+=speed


olly = dog()
print("Ollys speed before he grow up",olly.speed)

olly.faster(speed=15)

print("Ollys speed after he grow up",olly.speed)