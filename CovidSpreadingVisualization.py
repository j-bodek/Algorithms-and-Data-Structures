
# COVID SPREADING VISUALIZATION PROJECT: 
# LINK => https://www.youtube.com/watch?v=KAmZe5D3v5I

import matplotlib.pyplot as plt
import matplotlib.animation as ani
import numpy as np

GREY = (0.78, 0.78, 0.78) # UNINFECTED
RED = (0.96, 0.15, 0.15) #INFECTED
GREEN = (0, 0.86, 0.03) # RECOVERED
BLACK = (0, 0, 0) # DEAD

COVID19_PARAMS = {
    "r0": 2.28,
    "incubation": 5,
    "percent_mild": 0.8,
    "mild_recovery": (7, 14),
    "percent_severe": 0.2,
    "severe_recovery": (21, 42),
    "severe_death": (14, 56),
    "fatality_rate": 0.034,
    "serial_interval": 7
}


class Virus:
    def __init__(self, params):
        # create plot
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot(111, projection='polar')
        self.axes.grid(False) #remove grid lines
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        self.axes.set_ylim(0, 1)
        
        # create annotations
        self.dayText = self.axes.annotate(
            'Day 0', xy=[np.pi / 2, 1], ha='center', va='bottom'
        )
        # create infections
        self.infectedText = self.axes.annotate(
            'Infected: 0', xy=[3 * np.pi / 2, 1], ha='center', va='top', color=RED
        )
        # create deaths
        self.deathText = self.axes.annotate(
            '\nDeaths: 0', xy=[3 * np.pi / 2, 1], ha='center', va='top', color=BLACK
        )
        # create recovered
        self.recoveredText = self.axes.annotate(
            '\n\nRecovered: 0', xy=[3 * np.pi / 2, 1], ha='center', va='top', color=GREEN
        )

        # create member varialbes
        self.day = 0
        self.totalNumberInfected = 0
        self.numberCurrentlyInfected = 0
        self.numberRecovered = 0
        self.numberDeaths = 0
        # basic reproduction numbers
        self.r0 = params['r0'] # measure of contagiousness of the disease
        self.percentMild = params['percent_mild'] 
        self.percentSevere = params['percent_severe']
        self.fatalityRate = params['fatality_rate']
        self.serialInterval = params['serial_interval'] # time between start and end of disease
        
        self.mildFast = params['incubation'] + params['mild_recovery'][0]
        self.mildSlow = params['incubation'] + params['mild_recovery'][1]
        self.severeFast = params['incubation'] + params['severe_recovery'][0]
        self.severeSlow = params['incubation'] + params['severe_recovery'][1]
        self.deathFast = params['incubation'] + params['severe_death'][0]
        self.deathSlow = params['incubation'] + params['severe_death'][1]

        self.mild = {i: {'thetas': [], 'rs': []} for i in range(self.mildFast, 365)} # data for every days
        self.severe = {
            'recovery': {i: {'thetas': [], 'rs': []} for i in range(self.severeFast, 365)},
            'death': {i: {'thetas': [], 'rs': []} for i in range(self.deathFast, 365)},
        }
        
        self.exposedBefore = 0 # represent number of people that were exposed to virus before
        self.exposedAfter = 1
        
        self.initialPopulation()
        
        
        
    def initialPopulation(self):
        population = 4500
        self.numberCurrentlyInfected = 1
        self.totalNumberInfected = 1
        indices = np.arange(0, population) + 0.5
        self.thetas = np.pi * (1 + 5**0.5) * indices
        self.rs = np.sqrt(indices / population)
        self.plot = self.axes.scatter(self.thetas, self.rs, s=5, color=GREY)
        # patient zero
        self.axes.scatter(self.thetas[0], self.rs[0], s=5, color=RED)
        self.mild[self.mildFast]['thetas'].append(self.thetas[0])
        self.mild[self.mildFast]['rs'].append(self.rs[0])
        
        
    # function that calculate number of newly infected people
    def spreadVirus(self, i):
        self.exposedBefore = self.exposedAfter
        if self.day % self.serialInterval == 0 and self.exposedAfter < 4500: # if day % 7 is zero and there are some people to infected
            self.numberNewInfected = round(self.r0 * self.totalNumberInfected)
            self. exposedAfter += round(self.numberNewInfected*1.1)
            if self.exposedAfter > 4500:
                self.numberNewInfected = round((4500 - self.exposedBefore) * 0.9)
                self.exposedAfter = 4500
            self.numberCurrentlyInfected += self.numberNewInfected
            self.totalNumberInfected += self.numberNewInfected
            # select newly infected people
            self.newInfectedIndices = list(
                np.random.choice(
                    range(self.exposedBefore, self.exposedAfter),
                    self.numberNewInfected, 
                    replace= False
                )
            )
            thetas = [self.thetas[i] for i in self.newInfectedIndices]
            rs = [self.rs[i] for i in self.newInfectedIndices]
            
            self.anim.event_source.stop()
            
            if len(self.newInfectedIndices) > 24:
                sizeList = round(len(self.newInfectedIndices) / 24)
                thetaChunks = list(self.chunks(thetas, sizeList))
                rChunks = list(self.chunks(rs, sizeList))
                self.anim2 = ani.FuncAnimation(
                    self.figure, 
                    self.one_by_one,
                    interval=50,
                    frames=len(thetaChunks),
                    fargs=(thetaChunks, rChunks, RED)
                )
            else:
                self.anim2 = ani.FuncAnimation(
                    self.figure, 
                    self.one_by_one,
                    interval=50,
                    frames=len(thetas),
                    fargs=(thetas, rs, RED)
                )
                
            
            # assign symptoms
            self.assignSymptoms()
            
            
        self.day += 1
        
        # update status
        self.updateStatus()
        # update text
        self.updateText()
        
        
    def one_by_one(self, i, thetas, rs, color):
        self.axes.scatter(thetas[i], rs[i], s=5, color=color)
        if i == len(thetas) - 1:
            self.anim2.event_source.stop()
            self.anim.event_source.start()
        
        
    def chunks(self, aList, n):
        for i in range(0, len(aList), n):
            yield aList[i: i + n]
        
        

    def assignSymptoms(self):
        numMild = round(self.percentMild * self.numberNewInfected)
        numSevere = round(self.percentSevere * self.numberNewInfected)
        # choose random subset of newly infected to have mild sumporms
        self.mildIndices = np.random.choice(
            self.newInfectedIndices, numMild, replace=False
        )
        # assign the rest severe symptoms, either resulting in recovery or death
        remainingIndices = [
            i for i in self.newInfectedIndices if i not in self.mildIndices
        ]
        # calculate the percentage of severe cases that recovered
        percentSevereRecovered = 1 - (self.fatalityRate / self.percentSevere)
        numSevereRecovery = round(percentSevereRecovered * numSevere)
        self.severeIndices = []
        self.deathIndices = []
        if remainingIndices:
            self.severeIndices = np.random.choice(
                remainingIndices, numSevereRecovery, replace=False
            )
            self.deathIndices = [
                i for i in remainingIndices if i not in self.severeIndices
            ]
            
        # assign recovery/death day
        low = self.day + self.mildFast
        high = self.day + self.mildSlow
        for mild in self.mildIndices:
            recoveryDay = np.random.randint(low, high)
            mildTheta = self.thetas[mild]
            mildR = self.rs[mild]
            self.mild[recoveryDay]['thetas'].append(mildTheta)
            self.mild[recoveryDay]['rs'].append(mildR)
            
        
    def updateStatus(self):
        if self.day >= self.mildFast:
            mildThetas = self.mild[self.day]['thetas']
            mildRs = self.mild[self.day]['rs']
            self.axes.scatter(mildThetas, mildRs, s=5, color=GREEN)
            self.numberRecovered += len(mildThetas)
            self.numberCurrentlyInfected -= len(mildThetas)
            
        # same for people with severe cases that end with recovery 
        if self.day >= self.severeFast:
            recoveryThetas = self.severe['recovery'][self.day]['thetas']
            recoveryRs = self.severe['recovery'][self.day]['rs']
            self.axes.scatter(recoveryThetas, recoveryRs, s=5, color=GREEN)
            self.numberRecovered += len(recoveryThetas)
            self.numberCurrentlyInfected -= len(recoveryThetas)
        # finaly same thing for people with severe case that end with death
        if self.day >= self.deathFast:
            deathThetas = self.severe['death'][self.day]['thetas']
            deathRs = self.severe['death'][self.day]['rs']
            self.axes.scatter(deathThetas, deathRs, s=5, color=BLACK)
            self.numberDeaths += len(deathThetas)
            self.numberCurrentlyInfected -= len(deathThetas)
            
    
    def updateText(self):
        self.dayText.set_text(f'Day {self.day}')
        self.infectedText.set_text(f'Infected: {self.numberCurrentlyInfected}')
        self.deathText.set_text(f'\nDeath: {self.numberDeaths}')
        self.recoveredText.set_text(f'\n\nRecovered: {self.numberRecovered}')
        
    
    # function to generate frames
    def gen(self):
        while self.numberDeaths + self.numberRecovered < self.totalNumberInfected:
            yield
        
        
    # animation function
    def animate(self):
        self.anim = ani.FuncAnimation(
            self.figure,
            self.spreadVirus,
            frames=self.gen,
            repeat=True
        )
        







def main():
    covid = Virus(COVID19_PARAMS)
    covid.animate()
    plt.show()  


if __name__ == '__main__':
    main()


