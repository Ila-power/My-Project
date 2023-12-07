import pandas as pd
import datetime

books=pd.read_csv(r"C:\Users\Ilavarasi\OneDrive\Desktop\DA03\Assessment-3\RR-DPL-AU2 - Book.csv")
df=pd.DataFrame(books)
#1.	Read the csv in a data_frame
books=pd.read_csv(r"C:\Users\Ilavarasi\OneDrive\Desktop\DA03\Assessment-3\RR-DPL-AU2 - Book.csv")
print(books.head())

#2.	Remove the following columns from the data_frame 
df=books.drop(['Edition Statement','Corporate Author','Corporate Contributors','Former owner',
                    'Engraver','Contributors','Issuance type','Shelfmarks'], axis=1)
print(df.head())

#3.	Check the content of the column- 'Date of Publication’ and define a function to clean the value 
def cleanDateofpub(df):
    extr = df['Date of Publication'].str.extract(r'\b(\d{4})\b', expand=False)
    extr = pd.to_datetime(extr, errors='ignore', format='%Y')
    return extr

extr= cleanDateofpub(df)
print('Date of Publications :',extr.head())

#4.	Check the content of the column- ' Author’ and define a function to clean the value. And split the name to first name and last name
def cleanandsplitAuthor(df):
    extr = df['Author'].str.encode('ascii','ignore').str.decode('ascii')
    extr = extr.str.replace(r'(?!A)','', regex=True)
    extr = extr.str.split('-').str[0]
    df[['First Name', 'Last Name']] = extr.str.split(r',',n=1, expand=True)
    return df

df = cleanandsplitAuthor(df)
print ('First Name, Last Name from Author :',df[['First Name', 'Last Name']].head())

#5.	Check the content of the column- ‘Title’ and define a function to clean the value 

print(df['Title'].str.split('.').str[0])

#6.	Check the content of the column- ‘Place of Publication’ and define a function to clean the value. 
print(df['Place of Publication'].str.split(';').str[0])

