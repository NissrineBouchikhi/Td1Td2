import random
import numpy as np
from character import Character
from army import Army
from perceptron import Perceptron
import matplotlib.pyplot as plt
import csv


def creeCharacters(fichier):
    listeCharacters = []
    with open(fichier, newline='') as characters:
        lignes = csv.reader(characters, delimiter=',')
        next(lignes)
        for ligne in lignes:
            character = Character(ligne[0], ligne[1], ligne[2], ligne[3], ligne[4])
            listeCharacters.append(character)
    return listeCharacters


def creeArmy(characters):
    listeArmy = []
    chefBoost = []
    armyMoral = []
    for character in characters:
        moralValue = random.uniform(20, 100)
        armyMoral = np.append(armyMoral, np.array([moralValue]))
        chefBoost = np.append(chefBoost, np.array([character.getMoralBoost()]))
        listeArmy.append(Army(character, moralValue))
    armiesMoral = np.sum(armyMoral * chefBoost)
    return listeArmy, armiesMoral


def trois_lignes_de_code():
    armyMoral = np.array([20, 100, 55, 60, 75])
    boostMoral = np.array([0.97, 2, 1.3, 1.5, 0.1])
    totalMoral = armyMoral.dot(boostMoral)
    print(totalMoral)


def apprendreAND():
    input = np.array([[0, 0],
                      [0, 1],
                      [1, 0],
                      [1, 1]])
    output = np.array([0, 0, 0, 1])
    erreur = np.zeros((10, 10))
    for w1 in range(-5, 5):
        for w2 in range(-5, 5):
            for i in range(len(input)):
                y = (w1 * input[i][0]) + (w2 * input[i][1])
                if y > 0:
                    y = 1
                else:
                    y = 0
                t = output[i]
                erreur[w1 + 5, w2 + 5] += (1. / 2.) * (y - t) ** 2
    print(erreur)


if __name__ == '__main__':
    characters_list = []
    armies_list = []
    fichierCSV = 'characters.csv'
    characters_list = creeCharacters(fichierCSV)
    # print(characters_list)
    armies_list, armiesMoral = creeArmy(characters_list)
    """for army in armies_list:
        print(army)
    """
    # trois_lignes_de_code()
    # apprendreAND()

    # ***************** Partie Perceptron ********************

    inputs = np.array([[0, 0],
                       [0, 1],
                       [1, 0],
                       [1, 1]])
    outputs = np.array([0, 0, 0, 1])

    perceptron = Perceptron(inputs, nbEpoch=10000, learningRate=0.001)
    perceptron.train(inputs, outputs)
    print(
        "w0: {} - w1: {} - w2: {}".format(perceptron.get_weight0(), perceptron.get_weight1(), perceptron.get_weight2()))

    for input, output in zip(inputs, outputs):
        attendu = perceptron.predictBiais(input, perceptron.get_weight0(), perceptron.get_weight1(),
                                          perceptron.get_weight2())
        if attendu == output:
            print(" -entrée : {} -sortie : {} -sortie attendue : {} ".format(input, output, attendu))
        else:
            print(" -entrée : {} -sortie : {} -sortie attendue : {} ".format(input, output, attendu))

    with open('poids.csv', 'w',newline='') as csvFile:
        spamwriter = csv.writer(csvFile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['weight0', 'weight1', 'weight2'])
        spamwriter.writerow([perceptron.get_weight0(), perceptron.get_weight1(), perceptron.get_weight2()])
    """
    surface_erreur = perceptron.surfaceError(inputs, outputs)
    plt.imshow(surface_erreur)
    plt.show()
    """
