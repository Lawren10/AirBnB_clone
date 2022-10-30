from uuid import uuid4
from datetime import datetime
import json

class BaseModel:
 
  """
  This is a basemodel class for the airbnb clone, and most airbnb class instances inherits from it. 
  
  """
  
  def __init__(self,*args, **kwargs):
   """This is the initializing function that sets public instance attribute for each class instance"""
   self.id=str(uuid4())
   self.created_at=datetime.now()
   self.updated_at=datetime.now()
   if len(kwargs) > 0:
     for key,value in kwargs.items():
      if key != "__class__":
       setattr(self,key,value)

      print(f"{key},{value}")
   

  def __str__(self) :
   """This function prints out the class name, class Id and class dict in string formart """
   modDic = self.__dict__
   modDic["created_at"] = self.created_at.isoformat()
   modDic["updated_at"] = self.updated_at.isoformat()
   return (f"[{self.__class__.__name__}] ({self.id}) {modDic}")

  def save(self):
   """This function updates the public instance attribute updated_at with the current datetime """
   self.updated_at = datetime.now() 

  def to_dict(self):
   """ This function returns a dictionary containing all keys/values of __dict__ of the instance and a __class__ key having a value of the class instance name"""
   currentObj = self.__dict__ 
   
   currentObj["created_at"] = self.created_at.isoformat()
   currentObj["updated_at"] = self.updated_at.isoformat()
   currentObj["__class__"]=self.__class__.__name__
   return currentObj



TestClass = BaseModel()

# print(TestClass)
print(TestClass.to_dict())
