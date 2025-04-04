from mammal import Mammal
from Person import Person
from tick import Tick
from puma import Puma


m = Mammal(10)
m.speak()
# Mammal.speak(m)  # Same thing
print(m)

p = Person("John Doe", 20, 6)
p.speak()
print(p)
p.heart.beat()
print(p.heart)

t = Tick()
t.suck_blood()
print(t)

pm = Puma(5, t)
pm.tick.suck_blood()
print(pm)
pm.claw()


pm2 = Puma(3)
pm2.claw()



