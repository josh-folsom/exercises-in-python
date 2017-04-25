class Person:
  def __init__ (self, name):
    self.name = name
  def greet (self):
    print("Hello {}".format(self.name))
me = Person('Josh')
me.greet()
