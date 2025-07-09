# Data-Preprocessor 
This Data Preprocessor is exclusive to Data Extracted from maps mostly through MapsLead.net\ 
Ideally the features present should be "Name", "Address", "Maps URL", "Lattitude", "Longitude", "Phone" and the rest of the columns are dropped as are of no use\ 
-cleaner.py simply from the given information extracts data such as pincode and maps it to the locations we provide (Mira Bhayandar and Dhule for now) and saves it as a CSV file\ 
-json_convertor.py converts the CSV file from above into a json format and adds things like default description, priceRange, keywords, categoryID, etc which we have provided\ 
The instructions on how to use each file is explained within the file in detail for each line.
