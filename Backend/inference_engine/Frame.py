from typing import List
from inference_engine import Attribute

class Frame:
    def __init__(self, frameResult: str, attributes):
        self.__frameResult = frameResult
        self.__childrenFrames = []
        self.__attributes = attributes
        self.RESULT = "RESULT"
        self.ASK = "ASK"
    

    def addChildren(self, frame):
        if ( frame in self.__childrenFrames ):
            raise Exception("Sent frame to add does already exist as frame's child.")
        self.__childrenFrames.append(frame)

    
    def removeChildren(self, frame):
        if (not (frame in self.__childrenFrames)):
            raise Exception("Sent frame to remove does not exist as frame's child.")
        self.__childrenFrames.remove(frame)


    def completeAttribute(self, attributeName, attributeValue):
        retorno = None
        retornoLocal = None
        retornoAskChild = None
        if (attributeName in self.__attributes):
            self.__attributes[attributeName].setValue(attributeValue)
            retornoLocal = self.__attributes[attributeName].onAdd(self.__attributes)
        for child in self.__childrenFrames:
            respChild = child.completeAttribute(attributeName, attributeValue)
            if respChild is not None:
                if respChild["type"] == self.RESULT:
                    retorno = respChild
                elif respChild["type"] == self.ASK:
                    retornoAskChild = respChild
        if ((retorno is not None) or (retornoLocal is not None and retornoLocal["type"] == self.RESULT)):
            if retornoLocal["type"] == self.RESULT:
                retornoLocal["value"] = self.__frameResult
        if retorno is not None:
            return retorno
        elif ( retornoLocal is not None ):
            return retornoLocal
        else:
            return retornoAskChild
        

    
    def isComplete(self):
        for attr in self.__attributes.values():
            if (not attr.validate()) or (not attr.isCompleted()):
                return False
        return True
    


    def isCurrentlyValid(self):
        for attr in self.__attributes.values():
            if not attr.validate():
                return False
        return True
    

    def resetValues(self):
        for attr in self.__attributes.values():
            attr.setValue(None)
        for child in self.__childrenFrames:
            child.resetValues()
        