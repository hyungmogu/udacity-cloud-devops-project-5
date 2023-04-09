from abc import ABC, abstractmethod

class ConvertService(ABC):
  @abstractmethod
  def convert(self, file):
    pass
  
  @abstractmethod
  def upload(self, converted_file):
    pass