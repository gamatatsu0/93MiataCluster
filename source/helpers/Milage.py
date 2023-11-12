""" We use the following functions to perform calculations related to fuel efficiency
"""


class FuelEfficiency():

    def __init__(self, **kwargs):
        self.currentTankLevel = 50  # will need to change soon
        self.tripMiles = 10  # Miles traveled in the current trip
        self.maxGallons = 12  # gallons
        self.startingGallons = 12
        self.currentGallons = 9
        self.usedGallons = self.startingGallons - self.currentGallons
        self.tripAvgMPG = 1  # Set to 1 to prevent division by zero
        
        super(FuelEfficiency, self).__init__(**kwargs)

        # self.bind(currentGallons=self.SetCurrentGallons)

    # ........................ Get ........................

    def getTankLevel(self): # OK
        self.currentTankLevel = self.currentGallons / self.maxGallons
        return self.currentTankLevel * 100

    def getTripAverageMPG(self): # OK
        averageMPG = self.tripMiles / self.usedGallons
        self.tripAvgMPG = averageMPG  # Updating the trip average MPG
        return self.tripAvgMPG


    ''' May need to adjust formula later'''

    def getMilesTilEmpty(self):
        milesTilEmpty = self.getTripAverageMPG() * self.currentGallons
        return milesTilEmpty

    def getLiveMPG(self, MAF, speed):
        """ * We need to keep a ratio of 14.7 Grams of air for every gram of fuel.
            * The speed we are using is in Km/Hr
            * One Gallon = 6.17 Lb
            * 1Lb = 454grams
            * 3600 seconds = 1 hour.
            """
        ratio = 14.7 # ratio of grams of air per gram of fuel
        gramsPerGallon = 454 # Grams of fuel per gallon
        lbPerGallon = 6.17 # Weight of a gallon of gas
        secondsPerHour = 3600
        kmPerHour = 0.621371

        calc = ratio * lbPerGallon * gramsPerGallon * (speed * kmPerHour)
        calc = calc / ((secondsPerHour * MAF)/100)

        return calc
    # ........................ Set ........................
    ''' Function is used to set the starting amount of fuel we have left @ startup'''

    def setStartingGallons(self, gallons):
        self.startingGallons = gallons

    ''' Will need to call function over and over
     to update the current gas level'''
    def setCurrentGallons(self, gallons):
        self.currentGallons = gallons

    """ Will also need to recall functions over and over again. 
    As input it will need to call function from the GPS. """
    def setTripMiles(self, miles):
        self.tripMiles = miles
        
    def convertPercentToGallons(self, percent):
        return percent * 7.692
