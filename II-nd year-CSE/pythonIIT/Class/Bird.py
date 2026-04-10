class Bird:
   def speak(self):
      print("Bird Tweet")
class Animal(Bird):
   def speak(self):
      print("Tweet")
a=Bird()
a.speak()
c=Animal()
c.speak()
