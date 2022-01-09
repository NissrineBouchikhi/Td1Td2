import numpy as np


class Perceptron:
    def __init__(self, nbInput, nbEpoch, learningRate):
        self.nbInput = nbInput
        self.nbEpoch = nbEpoch
        self.learningRate = learningRate
        self.w0 = 0
        self.w1 = 0
        self.w2 = 0
        self.biais = 1

    def get_weight0(self):
        return self.w0

    def get_weight1(self):
        return self.w1

    def get_weight2(self):
        return self.w2

    def surfaceError(self, nbInput, expected_output):
        errors = np.zeros((11, 11))
        for i, ligne in enumerate(nbInput):
            for w1 in range(-5, 6):
                for w2 in range(-5, 6):
                    output = self.predict(ligne, w1, w2)
                    error = self.calcul_error(output, expected_output[i])
                    errors[w1 + 5][w2 + 5] = errors[w1 + 5][w2 + 5] + error
        return errors

    def regle_perceptron(self, x):
        if x <= 0:
            return 0
        else:
            return 1

    def predict(self, inputs, w1, w2):
        r1 = inputs[0] * w1
        r2 = inputs[1] * w2
        return self.regle_perceptron(r1 + r2)

    def calcul_error(self, output, expected_output):
        return 0.5 * (output - expected_output) ** 2

    def loiWidrowHoff(self, weight, input, output, expected_output):
        correctedWeight = weight+self.learningRate*(expected_output-output)*input
        return correctedWeight

    def predictBiais(self, inputs, w0, w1, w2):
        r1 = self.biais * w0
        r2 = inputs[0] * w1
        r3 = inputs[1] * w2
        return self.regle_perceptron(r1+r2+r3)

    def train(self, inputs, expected_outputs):
        for epoch in range(self.nbEpoch):
            for i,ligne in enumerate(inputs):
                output = self.predictBiais(ligne, self.w0, self.w1, self.w2)
                self.w0 = self.loiWidrowHoff(self.w0,self.biais, output, expected_outputs[i])
                self.w1 = self.loiWidrowHoff(self.w1, ligne[0], output, expected_outputs[i])
                self.w2 = self.loiWidrowHoff(self.w2, ligne[1], output, expected_outputs[i])



