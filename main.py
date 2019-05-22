from Creature import Creature
from Food import Food
import random as rand
import time

creatureList = []

#Create initial creatures
for i in range(10):
    creatureList.append(Creature(rand.uniform(0,1), 1, 1,rand.uniform(0,1), rand.uniform(0,1), rand.uniform(0,1)))

while True:
    for obj in creatureList:
        #Reset traits for new day
        obj.health += obj.efficiency
        if(obj.health > 1):
            obj.health = 1
        obj.energy = 1
    
    for obj in creatureList:
        #Creatures hunt for food
        food = Food(0.0, 0.5)
        obj.health -= food.strength
        food.health -= obj.strength
    
        #kill dead creatures
        if(obj.health < 0):
            creatureList.remove(obj)

        obj.health -= 0.01 * obj.lifetime
        obj.lifetime += 1
    time.sleep(0.01)
    print(len(creatureList))

