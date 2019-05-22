class Creature:
    def __init__(self, speed, health, energy, strength, efficiency, repoChance):
        self.speed = speed
        self.health = health
        self.energy = energy
        self.strength = strength
        self.efficiency = efficiency
        self.repoChance = repoChance

        self.lifetime = 0
