import csv
import os
from datetime import date
import time
import pandas as pd
import warnings
import openpyxl
warnings.filterwarnings('ignore')

class AttendanceConverter():

  def __init__(self):
          print('AttendanceConverter initialized')

  def getFileCreationDate(self, newPath): 
    c_time = os.path.getctime(newPath)
    createTime = time.ctime(c_time)
    day = createTime.split(' ')[2]
    month = createTime.split(' ')[1]
    year = createTime.split(' ')[4]
    months = {'Jan': 1,'Feb': 2,'Mar': 3,'Apr': 4,'May': 5,'Jun': 6,'Jul': 7,'Aug': 8,'Sep': 9,'Oct': 10,'Nov': 11,'Dec': 12,}
    month_value = months.get(month)
    if month_value is not None:
      month = month_value
    createDate = f'{year}-{month}-{day}'
    return createDate,newPath,
  
  def reformatXlsxCreateCsv(self,createDate,newPath, directory):
    excelFile = pd.read_excel(newPath, engine='openpyxl')
    csvFileName = f'{directory}/{createDate}.csv'
    excelFile.to_csv(csvFileName, index=False, header=False)
    df = pd.read_csv(csvFileName, skiprows=1)
    try:
      df.columns = ['Name', 'First Join', 'Last Leave', 'In-Meeting Duration', 'Email', 'Participant ID (UPN)', 'Role',' ']
    except ValueError:
       df.columns = ['Name', 'First Join', 'Last Leave', 'In-Meeting Duration', 'Email', 'Participant ID (UPN)', 'Role']
    df = df.iloc[7:]
    empty_row_index = (df.isnull().all(axis=1)).idxmax()
    df = df.iloc[:empty_row_index - 7]
    df.to_csv(csvFileName, index=False, header=True)
    return csvFileName,newPath

  def formatCsvOutput(self, directory,csvFileName,newPath, createDate):
    csvFile = open(csvFileName, 'r')
    try:
      reader = csv.DictReader(csvFile)
      list_names = []
      for row in reader:
        name = row['Name']
        duration = row['In-Meeting Duration']
        duration = duration.split()
        list_names.append(name)
        if 'm' in duration[0] or 's' in duration[0]:
          duration.insert(0,'0h')
        if 's' in duration[1]:
          duration.insert(1,'0m')
    finally:
      csvFile.close()

      myCsv = pd.read_csv(csvFileName)
      myCsv['First Join'] = pd.to_datetime(myCsv['First Join'])
      myCsv['Last Leave'] = pd.to_datetime(myCsv['Last Leave'])
      myCsv['Date'] = myCsv['First Join'].dt.date
      myCsv['duration'] = (myCsv['Last Leave'] - myCsv['First Join']).dt.total_seconds() / 3600
      myCsv['duration'] = myCsv['duration'].round(2)
      myCsv['Name'] = myCsv['Name'].str.split().str[0].str.title()
      aggs = {'duration': 'sum'}
      output = myCsv.groupby(['Name','Date']).agg(aggs).sort_values('duration', ascending=True)
      className = input('Please enter your class name in the format of AWS-20231113: ')

      fileDate = myCsv['First Join'].dt.date.iloc[0].strftime('%Y-%m-%d')
      


      targetDir = [x[0] for x in os.walk(directory)]
      output.to_csv(f'{targetDir[1]}/{fileDate}-{className}-Attendance.csv')
      os.remove(csvFileName)
      os.remove(newPath)