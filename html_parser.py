from lxml import html 
from validation import Store
from pydantic import ValidationError
import re
from config import JSON_FILE_PATH
from utils import read_json
from pprint import pprint
import json
from parsel import Selector

XPATHS=read_json(JSON_FILE_PATH)



def parse_html(data):
    tree=html.fromstring(data)
    
    json_data=tree.xpath(XPATHS.get("json_xpath"))
    extracted =json.loads(json_data)
    
    sel=Selector(json.dumps(extracted))
       
    amul_data={}
    amul_data["Product_Name"]=sel.jmespath("[0].name").get()
    amul_data["Brand_Name"]=sel.jmespath("[0].brand.name").get()
    amul_data["Product_Id"]=sel.jmespath("[0].sku").get()
    amul_data["Description"]=sel.jmespath("[0].description").get()
    img= sel.jmespath("[0].image").getall()  
    amul_data["Images"]=json.dumps(img)
    amul_data["Category"]=sel.jmespath("[0].category").get()    
    
    amul_data["Rating"]=sel.jmespath("[0].aggregateRating.ratingValue").get()
    amul_data["Review_Count"]=sel.jmespath("[0].aggregateRating.reviewCount").get()
    amul_data["Rating_Count"]=sel.jmespath("[0].aggregateRating.ratingCount").get()
    amul_data["Price"]=sel.jmespath("[0].offers.price").get()
    amul_data["Currency"]=sel.jmespath("[0].offers.priceCurrency").get()
    amul_data["Avl_Url"]=sel.jmespath("[0].offers.availability").get()
    amul_data["Item_Condition"]=sel.jmespath("[0].offers.itemCondition").get()
    return_policies_data={
        "Url":sel.jmespath("[0].offers.hasMerchantReturnPolicy.url").get(),
        "Descrition":sel.jmespath("[0].offers.hasMerchantReturnPolicy.description").get(),
        "Applicable_Country":sel.jmespath("[0].offers.hasMerchantReturnPolicy.applicableCountry").get(),
        "Return_Category":sel.jmespath("[0].offers.hasMerchantReturnPolicy.returnPolicyCategory").get()
    }
    
    amul_data["Return_Policy"]=json.dumps(return_policies_data)
    try:
        Store(**amul_data)
        return amul_data
    except ValidationError as v:
        print("Validation Erro",parse_html.__name__,v)