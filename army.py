class Army:

    def __init__(self, chef, moral):
        self.chef = chef
        self.moralValue = float(moral)

    def getChef(self): return self.chef

    def getMoralValue(self): return self.moralValue

    def setChef(self, newChef): self.chef = newChef

    def setMoralValue(self, newBoost):  self.moralValue = newBoost

    def __repr__(self):
        return "Chef: {}\t" \
               "Army moral value: {}" \
            .format(self.chef, self.moralValue)

    def get_total_morale(self):
        return float(self.moralValue * self.chef.getMoralBoost())
