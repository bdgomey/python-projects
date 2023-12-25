# # text pattern Phone numnber: 123-345-6789

# # non regex

# def isPhone(text):
#   if len(text) != 12:
#     return False
#   for i in range(0,3):
#     if not text[i].isdecimal():
#       return False
#   if text[3] != "-":
#     return False
#   for i in range(4,7):
#     if not text[i].isdecimal():
#       return False
#   if text[7] != "-":
#     return False
#   for i in range(8,12):
#     if not text[i].isdecimal():
#       return False
#   return True    



# message = "Please call me at 910-366-7762 between 7 and 5pm and 910-366-7765 at any other time"

# foundNumber = False

# for i in range(len(message)):
#   chunk = message[i:i+12]
#   print (chunk)
#   if isPhone(chunk):
#     print("Phone Number found " + chunk)
#     foundNumber = True

# if not foundNumber:
#   print("I could not find a number")

# regex
  
# import re

# message = "Please call me at (910) 366-7762 between 7 and 5pm and 910-366-7765 at any other time and if you are calling from out of the country please dial 1+(910)366-7762 9103664589"
# phoneNumRegex = re.compile(r'1?\+?\s?\(?\d{3}\)?-?\s?\d{3}-?\d{4}')
# phoneList = phoneNumRegex.findall(message)

# for numbers in phoneList:
#   print (numbers)


# superRegex = re.compile('super(man|girl|dog|)')
# mo = superRegex.search("superman and supergirl went and bought a puppy called superdog!")
# print(mo.group())
import PyPDF2
import re


def readPDF(path):
  pdfFileObject = open(path, 'rb')
  pdfReader = PyPDF2.PdfReader(pdfFileObject)
  pdf = []
  for page in range(len(pdfReader.pages)):

    pageObject = pdfReader.pages[page]
    text = pageObject.extract_text()
    pdf.append(text)
  return pdf

class Regex():

  def readPhoneNumbers(text):
    phoneNumbers = []
    regexPhoneNumbers = re.compile(r'\d{3}-\d{3}-\d{4}')
    for pdf in text:
      try:
        allNumbers = regexPhoneNumbers.findall(pdf)
        phoneNumbers.extend(allNumbers)
      except:
        print("page has nothing to extract from")                           
    return phoneNumbers



  def readEmails(text):
    emails = []
    regexEmails = re.compile(r'\w*@\w*\.\w{2,3}')
    for pdf in text:
      try:
        allEmails = regexEmails.findall(pdf)
        emails.extend(allEmails)
      except:
        print("page has nothing to extract from")                           
    return emails


print(Regex.readEmails(readPDF("examplePhoneEmailDirectory.pdf")))
