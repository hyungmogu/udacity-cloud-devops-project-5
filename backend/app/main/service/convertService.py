from abc import ABC, abstractmethod

class ConvertService(ABC):
    @abstractmethod
    def convert(self, file):
        pass
    
    def upload(self):
        pass