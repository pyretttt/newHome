#Model
class ModelEntity:
    default_value = "N/A"
    
    def __init__(self, response):
        print(response)
        self.data = {}
        self.data["ID"] = response.get("id", self.__class__.default_value)
        self.data["developerName"] = response.get("developer", {}).get("developerGroupName", self.__class__.default_value)
        self.data["adress"] = response.get("address", self.__class__.default_value)
        self.data["region"] = response.get("region", self.__class__.default_value)
        self.data["readyDate"] = response.get("objReady100PercDt", self.__class__.default_value)
        self.data["livingSquare"] = response.get("objSquareLiving", self.__class__.default_value)
        self.data["latitude"] = response.get("objLkLatitude", self.__class__.default_value)
        self.data["longitude"] = response.get("objLkLongitude", self.__class__.default_value)
        self.data["finishType"] = response.get("objLkFinishTypeDesc", self.__class__.default_value)
        self.data["price"] = response.get("objPriceAvg", self.__class__.default_value)
