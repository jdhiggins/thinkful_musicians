from random import randint

class Musician(object):
  def __init__(self, sounds):
    self.sounds = sounds
  
  def solo(self, length):
    for i in range (length):
      print self.sounds[i % len(self.sounds)],
    print ""
    
class Bassist(Musician): # The Musician class is the parent of the bassist class
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])
    
class Guitarist(Musician):
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
    
  def tune(self):
    print "Be with you in a moment"
    print "Twoning, sproing, splang"
    
class Drummer(Musician):
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Drummer, self).__init__(["Bip", "Bap", "Crash", "Thump"])
  def count(self):
    print "One, Two, Three, FOUR!"
  def combust(self):
    print "***FIREBALL***"
    
    
    
class Band(object):
  
  
  
  def __init__(self, members = []):
    self.members = members
    
  musician_names = ["Nigel", "Clark", "Jimmy", "Thom", "Zeus", "Zed", "Al", "Sam", "Stan", "Sheena", "Kit", "Mary", "Bea", "Arlo", "Ida"]

  def hire_bassist(self):
    new_bassist = Bassist()
    self.members.append(new_bassist)
    print "We hired a bassist!"

  def hire_guitarist(self):
    new_guitarist = Guitarist()
    self.members.append(new_guitarist)
    print "We hired a guitarist!"

  def hire_drummer(self):
    new_drummer = Drummer()
    self.members.append(new_drummer)
    print "We hired a drummer!"
  
  def fire(self):
    print "We're firing someone!"
    del self.members[0]
  
  def play(self):
    for member in SuperFuzz.members:
      member.solo(randint(3,25))
    
if __name__ == "__main__":
  John = Drummer()
  Mario = Guitarist()
  Stan = Bassist()
    
  
  Mario.tune()
  John.count()
  Mario.solo(7)
  Stan.solo(5)
  John.solo(8)
  John.combust()  
  print "\n\n"
  SuperFuzz = Band()
  SuperFuzz.hire_bassist()
  SuperFuzz.hire_guitarist()
  SuperFuzz.hire_drummer()
  SuperFuzz.play()
  SuperFuzz.fire() 
  SuperFuzz.play()
  SuperFuzz.fire()
  SuperFuzz.play()
  SuperFuzz.hire_bassist()
  SuperFuzz.hire_drummer()
  SuperFuzz.hire_guitarist()
  SuperFuzz.play()
  
  print "Thank you!  Good night!"

    
    
   
     