import util
import classificationMethod
import math

class NaiveBayesClassifier(classificationMethod.ClassificationMethod):
  """
  See the project description for the specifications of the Naive Bayes classifier.
  
  Note that the variable 'datum' in this code refers to a counter of features
  (not to a raw samples.Datum).
  """
  def __init__(self, legalLabels):
    # Do not delete or change any of those variables!
    self.legalLabels = legalLabels
    self.type = "naivebayes"
    self.k = 1 # this is the smoothing parameter
    self.automaticTuning = False # Flat for automatic tuning of the parameters
    
  def setSmoothing(self, k):
    """
    This is used by the main method to change the smoothing parameter before training.
    Do not modify this method.
    """
    self.k = k

  def train(self, trainingData, trainingLabels, validationData, validationLabels):
    """
    Outside shell to call your method. Do not modify this method.
    """  

    self.features = trainingData[0].keys() # this could be useful for your code later...
    
    if (self.automaticTuning):
        kgrid = [0.001, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100]
    else:
        kgrid = [self.k]
        
    return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, kgrid)
      
  def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, kgrid):
    """
    Train the classifier by collecting counts over the training data 
    and choose the smoothing parameter among the choices in kgrid by
    using the validation data. This method stores the right parameters
    as a side-effect and should return the best smoothing parameters.

    See the project description for details.
    
    Note that trainingData is a list of feature Counters.
    
    Assume that we do not use sparse encoding (normally we would); so that you can
    figure out what are the list of possible features by just looking
    at trainData[0].keys() generically. Your code should not make any assumption
    about the feature keys apart that they are all in trainData[0].keys().
    
    If you want to simplify your code, you can assume that each feature is binary
    (can only take the value 0 or 1).
    """
    
    ## Your code here
  
    
    return self.k
    
  def classify(self, testData):
    """
    Classify the data based on the posterior distribution over labels.
    
    You shouldn't modify this method.
    """
    guesses = []
    self.posteriors = [] # Log posteriors are stored for later data analysis (autograder).
    for datum in testData:
      posterior = self.calculateLogPosteriorProbabilities(datum)
      guesses.append(posterior.argMax())
      self.posteriors.append(posterior)
    return guesses
      
  def calculateLogPosteriorProbabilities(self, datum):
    """
    Returns the log-posterior distribution over legal labels given the datum.
    Each log-probability should be stored in the posterior counter, e.g.    
    posterior['spam'] = <Estimate of log( P(Label = 'spam' | datum) )>
    """
    posterior = util.Counter()
    
    ## Your code here
    # example of type of values: posterior["SomeLabel"] = math.log(1e-301) 
    
    return posterior
  
  def findHighOddsFeatures(self, class1, class2):
    """
    Returns: 
    featuresClass1 -- the 100 best features for P(feature=on|class1) (as a list)
    featuresClass2 -- the 100 best features for P(feature=on|class2)
    featuresOdds -- the 100 best features for the odds ratio 
                     P(feature=on|class1)/P(feature=on|class2) 
    """

    featuresClass1 = []
    featuresClass2 = []
    featuresOdds = []
    
    ## Your code here

    return featuresClass1,featuresClass2,featuresOdds
    

    
      
