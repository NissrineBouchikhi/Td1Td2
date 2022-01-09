class Character:

    def __init__(self, nom, prenom, age, profession, boost):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.moralBoost = float(boost)

    def getNom(self): return self.nom

    def getPrenom(self): return self.prenom

    def getAge(self): return self.age

    def getProfession(self): return self.profession

    def getMoralBoost(self): return self.moralBoost

    def setNom(self, newNom): self.nom = newNom

    def setPrenom(self, newPrenom): self.prenom = newPrenom

    def setAge(self, newAge): self.age = newAge

    def setProfession(self, newProfession): self.profession = newProfession

    def setMoralBoost(self, newBoost):  self.moralBoost = newBoost

    def __repr__(self):
        return "Nom: {}\tPrenom: {}\tAge: {}" \
               "\tProfession: {}\tMoral value: {}" \
            .format(self.nom, self.prenom,
                    self.age, self.profession,
                    self.moralBoost)
