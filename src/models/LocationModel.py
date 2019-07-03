from Model import Model
class LocationModel(Model) :
    def __init__(self, LocationName, RecommendedLvl=1) :
        self.LocationName = LocationName
        self.RecommendedLvl = RecommendedLvl 