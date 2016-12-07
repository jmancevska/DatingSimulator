from pursuer import Pursuer
from target import Target

class Manager:
      totalRuns = 0
      successfulInteractions = 0
      failedInteractions = 0
      thePursuer = Pursuer(0,0)
      theTarget = Target(0,0)

      def __init__(self):
          self.successfulInteractions = 0
          self.failedInteractions = 0

      def displayReport(self):
        print('END OF SIMULATION, FINAL RESULTS ')
        print('Pursuer statistics ')
        self.thePursuer.displayReport()

        print('Target statistics ')
        self.theTarget.displayReport()

        print('Overall statistics ')
        print('No. matches: ', self.successfulInteractions, ' No. mis-matches: ', self.failedInteractions, ' Total attempts: ',self.totalRuns)
        print('Proportions of matches: ',self.successfulInteractions/self.totalRuns*100,'% Proportion of mis-matches: ',self.failedInteractions/self.totalRuns*100,'%')


      def startSimulation(self):
        print("Entering probabilities for the 'Pursuer' type of Tim. \nThe sum of the two probabilities must equal 100%.")
        pursuerXprobability = int(input("Enter the probability that X-type of behaviours will occur during an interaction during the date: "))
        pursuerYprobability = int(input("Enter the probability that Y-type of behaviours will occur during an interaction during the date: "))

        if (pursuerXprobability + pursuerYprobability) > 100:
              print('Error: the two probabilities equals ', (pursuerXprobability + pursuerYprobability),'% (must sum to 100%). Please re-enter the values.')
              startSimulation()
        
        print("\nEntering probabilities for the 'Target' type of Tim. \nThe sum of the two probabilities must equal 100%.")
        targetXprobability = int(input("Enter the probability that X-type of behaviours will occur during an interaction during the date: "))
        targetYprobability = int(input("Enter the probability that Y-type of behaviours will occur during an interaction during the date: "))

        if (targetXprobability + targetYprobability) > 100:
              print('Error: the two probabilities equals ', (targetXprobability + targetYprobability),'% (must sum to 100%). Please re-enter the values.')
              startSimulation()
        
        self.totalRuns = int(input("\nEnter the number of turns to run simulation (1-100): "))
        if self.totalRuns < 1 or self.totalRuns > 100:
              print('The range is wrong (must be between 1 - 100). Please re-enter the values.')
              startSimulation()

        thePursuer = Pursuer(pursuerXprobability, pursuerYprobability)
        theTarget = Target(targetXprobability, targetYprobability)
        
        for num in range(1,self.totalRuns+1):
              resultPursuer = thePursuer.generateInteraction()
              resultTarget = theTarget.generateInteraction()

              if resultPursuer == resultTarget:
                  self.successfulInteractions = self.successfulInteractions + 1
                  print('Turn # ', num, ' Match: Target ',resultTarget, ' Pursuer', resultPursuer)
              else:
                  self.failedInteractions = self.failedInteractions + 1
                  print('Turn # ', num, ' No Match: Target ',resultTarget, ' Pursuer', resultPursuer)
        self.displayReport()


m = Manager()
m.startSimulation()

