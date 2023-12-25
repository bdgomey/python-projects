import PyPDF2

class ReadPdf:
  def pdf(self, path):
    pdfFileObject = open(path, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFileObject)
    pdf = []
    for page in range(len(pdfReader.pages)):

      pageObject = pdfReader.pages[page]
      text = pageObject.extract_text()
      pdf.append(text)
    return pdf