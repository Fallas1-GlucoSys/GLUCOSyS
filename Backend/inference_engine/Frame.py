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
        if (attributeName in self.__attributes):
            prevVal = self.__attributes[attributeName].getValue()
            self.__attributes[attributeName].setValue(attributeValue)
            # Si no es válido el nuevo valor lo reestablezco.
            if not (self.__attributes[attributeName].validate()):
                self.__attributes[attributeName].setValue(prevVal)
        for child in self.__childrenFrames:
            child.completeAttribute(attributeName, attributeValue)

    
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
    

    def __askForNeededAttributes(self):
        neededAttrs = []
        for key, value in self.__attributes.items():
            if not value.isCompleted():
                neededAttrs.append(key)
        return {
            "type": self.ASK,
            "value": neededAttrs
        }
    

    def continueChaining(self):
        if self.isComplete():
            if len(self.__childrenFrames) == 0:
                # Frame's name will give the result because it is full, and does not have any childs
                return {
                    "type": self.RESULT,
                    "value": self.__frameResult
                }
            else:
                # First we found in Breadth
                for child in self.__childrenFrames:
                    if child.isComplete():
                        return child.continueChaining()
                # No child is complete, then we will continue with the ones that are valid...
                for child in self.__childrenFrames:
                    # At least partial attributes should be valid (If not that frame won't give result...)
                    if child.isCurrentlyValid():
                        return child.continueChaining()
                # Frames is valid and has childs, but it's childs are invalid, so... That frame is the result.
                return {
                    "type": self.RESULT,
                    "value": self.__frameResult
                }
        else:
            return self.__askForNeededAttributes()
        

    def continueBackwardChaining(self):
        if self.isComplete():
            if len(self.__childrenFrames) == 0:
                # Frame's name will give the result because it is full, and does not have any childs
                return {
                    "type": self.RESULT,
                    "value": self.__frameResult
                }
            else:
                # It first finds on Deep
                for child in self.__childrenFrames:
                    # At least partial attributes should be valid (If not that frame won't give result...)
                    if child.isCurrentlyValid():
                        return child.continueChaining()
                # Frames is valid and has childs, but it's childs are invalid, so... That frame is the result.
                return {
                    "type": self.RESULT,
                    "value": self.__frameResult
                }
        else:
            return self.__askForNeededAttributes()
        