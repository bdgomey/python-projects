from AttendanceConverter.attendance import AttendanceConverter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os


converter = AttendanceConverter()

def select_file():
    Tk().withdraw() 
    file_path = askopenfilename() 
    return file_path


file_path = select_file()
print(file_path)


newPath = file_path
directory = os.path.dirname(newPath)

converter.getFileCreationDate(newPath)
createDate, newPath = converter.getFileCreationDate(newPath)
csvFileName, newPath = converter.reformatXlsxCreateCsv(createDate, newPath, directory)
converter.formatCsvOutput(directory, csvFileName, newPath, createDate)

