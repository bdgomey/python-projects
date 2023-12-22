import re

class EmailReader():
    def emails(self, text):
      emails = []
      regexEmails = re.compile(r'\w*@\w*\.\w{2,3}')
      for pdf in text:
        try:
          allEmails = regexEmails.findall(pdf)
          emails.extend(allEmails)
        except:
          print("page has nothing to extract from")                           
      return emails
