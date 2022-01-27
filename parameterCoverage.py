# import pandas library as pd
import pandas as pd
import xml.etree.ElementTree as ET

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# read by default 1st sheet of an excel file
#dataframe1 = pd.read_excel('individualparametercoverage.xlsx')
#dateframe2 = dataframe1.parse('Sheet1', skiprows=4, index_col=None, na_values=['NA'])
#Step 1
xls = pd.ExcelFile('individualparametercoverage.xlsx')

df = xls.parse('Sheet1', skiprows=5,usecols="B,C", index_col=None, na_values=['NA'])
print(df)

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


# Step 3 -- Function to find the Parameter in the xml data frame

# Step 4-- Function to pass or fail the build depending on the previous step 

print('Function to pass or fail the build depending on the previous step')
def findParameterFromXMLDataFrame(xmlToDf, searchString):
    return xmlToDf[xmlToDf['Object'].str.contains(searchString)]
    
searchString='RTDB_GP_ESWITCH_OUTPUTS_E_DEPOP'
resultDataFrame=findParameterFromXMLDataFrame(xmlToDf,searchString)
print(resultDataFrame.size)
buildStatus=''
if resultDataFrame.empty:
    buildStatus='FAIL'
    print('FAIL')
else:
    buildStatus='PASS'
    print('PASS')

# Step 5 -- Function to develop a report and send an email 
print('Function to develop a report and send an email')
print(buildStatus)
msg = MIMEMultipart()
msg['From'] = "giri.vakati@gmail.com"
msg['To'] = "venkateswarluec@gmail.com" 
msg['Subject'] = "Build status" 
body = """Hi Team, Please find the build status 

Build is {}"""
msg.attach(MIMEText(body, 'plain'))
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() # for security
s.login("giri.vakati@gmail.com", "atrtxgutxyaxnuxv") 
text = msg.as_string() 
# sending the mail 
s.sendmail("giri.vakati@gmail.com", "venkateswarluec@gmail.com" , text.format(buildStatus))
s.quit()
print('EMAIL sent')
if buildStatus == 'FAIL':
 raise

#Step 6 -- Function to convert dev.txt to data frame 
print('#Step 6 -- Function to convert dev.txt to data frame')

dfTextFile = pd.read_fwf('Psm_coverage_psm_dev.txt', memory_map=True, header=None)
print(dfTextFile.info())
for col in dfTextFile:
    print(dfTextFile[col].unique())


#Step 7 -- Function to find the average of parameters 
print('#Step 7 -- Function to find the average of parameters')
print(dfTextFile.describe())

#Step 8 -- Function compare average parameter data frame to excel data frame 
print('#Step 8 -- Function compare average parameter data frame to excel data frame')

    
#Step 9 -- Function to pass or fail the build depending on the previous step 
print('#Step 9 -- Function to pass or fail the build depending on the previous step')
buildStatus=''
if resultDataFrame.size>0:
    buildStatus='PASS'
    print('PASS')
else:
    buildStatus='FAIL'
    print('FAIL')
    
#Step 10 -- Function to develop a report and send an email 

print('Step 10 --Function to develop a report and send an email')
print(buildStatus)
msg = MIMEMultipart()
msg['From'] = "giri.vakati@gmail.com"
msg['To'] = "venkateswarluec@gmail.com" 
msg['Subject'] = "Build status" 
body = """Hi Team, Please find the build status 

Build is {}"""
msg.attach(MIMEText(body, 'plain'))
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() # for security
s.login("giri.vakati@gmail.com", "atrtxgutxyaxnuxv") 
text = msg.as_string() 
# sending the mail 
s.sendmail("giri.vakati@gmail.com", "venkateswarluec@gmail.com" , text.format(buildStatus))
s.quit()
print('EMAIL sent')
