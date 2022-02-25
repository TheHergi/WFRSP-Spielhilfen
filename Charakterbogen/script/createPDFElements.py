# -*-coding: utf-8 -*
# createPDFElements.py

import scribus


# create "Spielwerte" PDF elements
print("\nRunning script createPDFElements")

SPIELWERTE = ["KG", "BF", "ST", "WI", "I", "GW", "GS", "IN", "WK", "CH"]

# Page 1
# 0 PDFBUTTON, 1 PDFRADIOBUTTON, 2 PDFTEXTFIELD, 3 PDFCHECKBOX, 4 PDFCOMBOBOX, 5 PDFLISTBOX, 6 PDFTEXTANNOTATION, 7 PDFLINKANNOTATION, 8 PDF3DANNOTATION
for idx, sp in enumerate(SPIELWERTE):
    scribus.createPdfAnnotation(3, 41 + 10 * idx, 62, 8, 3, sp + "_isCarreer")
    textf = scribus.createPdfAnnotation(2, 40 + 10 * idx, 66, 10, 5, sp + "_base")
    textf = scribus.createPdfAnnotation(2, 40 + 10 * idx, 71, 10, 5, sp + "_inc")
    textf = scribus.createPdfAnnotation(2, 40 + 10 * idx, 76, 10, 5, sp + "_total")


print("Done!")