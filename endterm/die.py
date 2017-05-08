import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title is not None:
        pylab.title(title)
    pylab.show()

# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
      
        A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:

        a dice roll of 1 4 3 has a longest run of 1
        a dice roll of 1 3 3 2 has a longest run of 2
        a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3
        When this function is called with the test case given in the file, it will return 5.312. 
        Your simulation may give slightly different values.
    """
    # TODO
    longest_run_list = []
    for i in range(numTrials):
        d = die        
        longest_so_far, run = 1, 1
        running_list = []
        for i in range(numRolls):
            now = d.roll()
            running_list.append(now)
            if len(running_list) > 1:
                if running_list[-2] == now:
                    run += 1
                else:
                    run = 1
                if run > longest_so_far:
                    longest_so_far = run
        longest_run_list.append(longest_so_far)       
    makeHistogram(longest_run_list, 10, 'longest run values', 'frequency', title=None)
    return getMeanAndStd(longest_run_list)[0]
        
    
    
# One test case
print (getAverage(Die([1,2,3,4,4,4,4,4]), 50, 100))