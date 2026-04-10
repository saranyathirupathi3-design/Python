class book:
   def __init__(self, title, author):
      self.title=title
      self.author=author
   def display(self):
      print(f"{self.title} is written by {self.author}")
B=book('precious mind', 'shara')
B.display()
