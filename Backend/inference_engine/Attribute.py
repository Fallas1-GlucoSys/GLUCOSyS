class Attribute:
    def __init__(self, value, validationFunction, onAdd):
        self.__value = value
        # Function that receives value as parameter and returns true if valid, false if not.
        self.__validationFunction = validationFunction
        self.__onAdd = onAdd
    

    def setValue(self, value):
        self.__value = value

    
    def getValue(self):
        return self.__value
    

    def isCompleted(self):
        return self.__value != None
    

    def validate(self):
        if self.__validationFunction != None:
            return ((not self.isCompleted()) or (self.__validationFunction(self.__value)))
        return True
    

    def onAdd(self, attrOnFrame):
        return self.__onAdd(attrOnFrame)