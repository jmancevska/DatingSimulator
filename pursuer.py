import random
class Pursuer:
      xInteractions = 0
      yInteractions = 0
      probabilityOfX = 0
      probabilityOfY = 0

      def __init__(self, probabilityOfX, probabilityOfY):
          self.probabilityOfX = probabilityOfX
          self.probabilityOfY = probabilityOfY

      def displayReport(self):
        print('Number of X interactions: ', self.xInteractions)
        print('Number of Y interactions: ', self.yInteractions)

      def generateInteraction(self):
        interactions = { 'X': self.probabilityOfX, 'Y': self.probabilityOfY }
        chosen = random.choice([k for k in interactions for dummy in range(interactions[k])])
        if chosen == 'X':
          self.xInteractions = self.xInteractions + 1
        else:
          self.yInteractions = self.yInteractions + 1
          
        return chosen
