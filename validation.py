from pydantic import BaseModel, field_validator
from typing import *

class Store(BaseModel):
    Product_Name :str
    Brand_Name :str
    Product_Id:str
    Description:str
    Images:str
    Category:str
    Rating:float
    Review_Count:int
    Rating_Count :int
    Price:float
    Currency:str
    Avl_Url :str
    Item_Condition :str
    Return_Policy : str