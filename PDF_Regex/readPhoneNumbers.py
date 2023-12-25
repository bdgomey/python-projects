import re

class ReadPhoneNumbers:
  def phoneNumbers(self, text):
    phoneNumbers = []
    regexPhoneNumbers = re.compile(r'\d{3}-\d{3}-\d{4}')
    for pdf in text:
      try:
        allNumbers = regexPhoneNumbers.findall(pdf)
        phoneNumbers.extend(allNumbers)
      except:
        print("page has nothing to extract from")                           
    return phoneNumbers