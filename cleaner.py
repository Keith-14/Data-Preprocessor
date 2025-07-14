import pandas as pd
import numpy as np 

#File should be save only as a CSV (Comma Seperated Value) ex: file.csv ✔️ file.xlsx ❌
df = pd.read_csv("Copy of medical_Mira-Bhayandar.csv") 
#Enter the file name inside the function () ex: df = pd.read_csv("file.csv")
#If an error comes at this line change the code to : df = pd.read_csv("file.csv", encoding="latin-1")

#Gets pincode by returning the last word (Mostly the pincode)
def get_pincode(sentence):
    words = sentence.split()
    if words:
        return words[-1]
    else:
        return None

#Setting the values of pincode to their location (Add more if required)
pincodes = {
    "401106": "Mira Bhayandar",
    "401107": "Mira Bhayandar",
    "401105": "Mira Bhayandar",
    "401101": "Mira Bhayandar",
    "400068": "Dahisar",
    "401104": "Mira Bhayandar",
    "401074": "Mira Bhayandar",
    "401104": "Mira Bhayandar",
    "424001": "Dhule",
    "424006": "Dhule",
    "424002": "Dhule",
    "424311": "Dhule",
    "424004": "Dhule",
    "424005": "Dhule",
    "425401": "Dhule",   #Shirpur
    "425421": "Dhule",   #Sakri
    "425405": "Dhule"    #Shindkheda
}

districts = {
    "Mira Bhayandar": "Thane",
    "Dahisar": "Mumbai",
    "Dhule": "Dhule"
}
#Creating a new column "pincode" and applying the get_pincode function
df["pincode"] = df["Address"].apply(get_pincode)

#Creating a new column "City" and mapping it to the pincode values we set earlier in "pincodes"
df["City"] = df["pincode"].map(pincodes)

#Creating a new column "district" and mapping it to the district values we set earlier in "districts"
df["district"] = df["City"].map(districts)

#Since only the places we set will get mapped the rest will be null, hence we drop the extra data
df.dropna(subset=["City"], inplace=True)

df.to_csv("cleaned_medical_mira_bhayandar.csv", index=False) #Write the name of the file you want to save as ideal format (cleaned_category_name_location_name.csv)
