from readEmails import EmailReader
from readPdf import ReadPdf
from readPhoneNumbers import ReadPhoneNumbers

pdfReader = ReadPdf()
emailReader = EmailReader()
phoneReader = ReadPhoneNumbers()

pdf = pdfReader.pdf("PdfDocuments\examplePhoneEmailDirectory.pdf")

emails = emailReader.emails(pdf)
phone_numbers = phoneReader.phoneNumbers(pdf)


print(emails)