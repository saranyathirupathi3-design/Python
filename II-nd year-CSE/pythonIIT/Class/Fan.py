class fan:
   def __init__(self, speed='medium'):
      self.speed=speed
   def status(self):
      print(f"{self.speed} is fan speed")
fan1=fan()
fan1.status()
fan2=fan("high")
fan2.status()
