# import pandas lib as pd
import pandas as pd
import xml.etree.ElementTree as ET

# read by default 1st sheet of an excel file
#dataframe1 = pd.read_excel('individualparametercoverage.xlsx')
#dateframe2 = dataframe1.parse('Sheet1', skiprows=4, index_col=None, na_values=['NA'])
#Step 1
xls = pd.ExcelFile('individualparametercoverage.xlsx')

df = xls.parse('Sheet1', skiprows=5,usecols="B,C", index_col=None, na_values=['NA'])
#print(df)

#Step 2
def convertXMLtoDataFrame():
    print("convertXMLtoDataFrame")
    prstree = ET.parse('config.xml')
    root = prstree.getroot()

    store_items = []
    all_items = []
    for storeno in root.find('POOL').findall('Parameter'):  
        obj=storeno.attrib.get('obj')
        no= storeno.find('No').attrib.get('Nsp')
        res= storeno.find('Responsible').text
        store_items = [obj,no,res]
        all_items.append(store_items)
  
    xmlToDf = pd.DataFrame(all_items,columns=['Object','Number','Responsible'])        
    return xmlToDf;
   

xmlToDf= convertXMLtoDataFrame()
print(xmlToDf.to_string(index=False))
#xmlToDf.to_csv('exampleXML.csv')


# Step 3
def findParameterFromXMLDataFrame(xmlToDf, searchString):
   exdf=xmlToDf[xmlToDf['Object'].str.contains(searchString)]   
   a=exdf.isnull()
   if a.empty:       
      raise
      print('No available Parameter')
   else:
    print(xmlToDf[xmlToDf['Object'].str.contains(searchString)])
      

     
searchString='RTDB_GP_ESWITCH_OUTPUTS_E_DEPOP_p'
findParameterFromXMLDataFrame(xmlToDf,searchString)


