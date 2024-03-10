# -*-coding: utf-8 -*
# createPDFElements.py

import scribus
from collections import OrderedDict

# create "Spielwerte" PDF elements
print("\nRunning script createPDFElements")


# 0 PDFBUTTON, 1 PDFRADIOBUTTON, 2 PDFTEXTFIELD, 3 PDFCHECKBOX, 4 PDFCOMBOBOX, 5 PDFLISTBOX, 6 PDFTEXTANNOTATION, 7 PDFLINKANNOTATION, 8 PDF3DANNOTATION
PDFTEXTFIELD = 2
PDFCHECKBOX = 3
PDFRADIOBUTTON = 1

prefix = "pdf_"

###################################################################################################
# Page 1
scribus.gotoPage(1)
scribus.setActiveLayer("PDF")

#0 Mouse Up, 1 Mouse Down, 2 Mouse Enter, 3 Mouse Exit, 4 Focus In, 5 Focus Out, 6 Selection Change, 7 Field Format, 8 Field Validate, 9 Field Calculate
JS_ACTION_TYPE = 9
def create_js_sw_total_script(sw):
    return "let b = parseInt(this.getField(\"pdf_" + sw + "_sw_base\").value); " + "let inc = parseInt(this.getField(\"pdf_" + sw + "_sw_inc\").value); " + "this.getField(\"pdf_" + sw + "_sw_total\").value = b + inc;"

# Spielwerte
SPIELWERTE = ["KG", "BF", "ST", "WI", "I", "GW", "GS", "IN", "WK", "CH"]
for idx, sp in enumerate(SPIELWERTE):
    # scribus.createPdfAnnotation(PDFCHECKBOX, 41 + 10 * idx, 62, 8, 3, prefix + sp + "_sw_isCarreer")

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 40 + 10 * idx, 56, 10, 5, prefix + sp + "_sw_base")
    # scribus.setText("0", textf)

    textf= scribus.createPdfAnnotation(PDFTEXTFIELD, 40 + 10 * idx, 61, 10, 5, prefix + sp + "_sw_inc")
    # scribus.setText("0", textf)

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 40 + 10 * idx, 66, 10, 5, prefix + sp + "_sw_total")
    # scribus.setText("0", textf)
    # scribus.setJSActionScript(JS_ACTION_TYPE, create_js_sw_total_script(sp), textf)

# Charakter
scribus.createPdfAnnotation(PDFTEXTFIELD, 30, 21, 72.5, 5, prefix + "name")
scribus.createPdfAnnotation(PDFTEXTFIELD, 30, 26, 30, 5, prefix + "volk")
scribus.createPdfAnnotation(PDFTEXTFIELD, 30, 31, 30, 5, prefix + "alter")
scribus.createPdfAnnotation(PDFTEXTFIELD, 30, 36, 30, 5, prefix + "haare")
scribus.createPdfAnnotation(PDFTEXTFIELD, 85, 26, 17.5, 5, prefix + "bewegung")
scribus.createPdfAnnotation(PDFTEXTFIELD, 85, 31, 17.5, 5, prefix + "koerpergroese")
scribus.createPdfAnnotation(PDFTEXTFIELD, 75, 36, 27.5, 5, prefix + "augen")

# Karriere
scribus.createPdfAnnotation(PDFTEXTFIELD, 130, 21, 65, 5, prefix + "karriere")
scribus.createPdfAnnotation(PDFTEXTFIELD, 130, 26, 65, 5, prefix + "karriereweg_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 110, 31, 85, 5, prefix + "karriereweg_1")
scribus.createPdfAnnotation(PDFTEXTFIELD, 125, 36, 25, 5, prefix + "status")
scribus.createPdfAnnotation(PDFTEXTFIELD, 165, 36, 30, 5, prefix + "klasse")

# Schicksal & Zaehigkeit
scribus.createPdfAnnotation(PDFTEXTFIELD, 175, 51, 20, 5, prefix + "schicksal")
scribus.createPdfAnnotation(PDFTEXTFIELD, 175, 56, 20, 5, prefix + "glueck")
scribus.createPdfAnnotation(PDFTEXTFIELD, 175, 61, 20, 5, prefix + "korr")
scribus.createPdfAnnotation(PDFTEXTFIELD, 175, 66, 20, 5, prefix + "lp")

# Grundfähigkeiten
GRUNDFAEHIGKEITEN = OrderedDict({"Anführen": "CH", "Athletik": "GW", "Ausdauer": "WI", "Ausweichen":"GW", "Besonnenheit":"WK", "Bestechen":"CH", "Charme":"CH", "Einschüchtern":"ST", "Fahren":"GW", "Feilschen":"CH", "Glücksspiel":"IN", "Intuition":"I", "Klatsch":"CH", "Klettern":"ST", "Kunst":"GS", "Nahkampf":"KG", "Navigation":"I", "Reiten":"GW", "Rudern":"ST", "Schleichen":"GW", "Tiere bezierzen":"GW", "Überleben":"IN", "Unterhalten":"CH", "Warnahmung":"I", "Zechen":"WI"})

def create_js_skill_total_script(name):
    return "let b = parseInt(this.getField(\"" + prefix + GRUNDFAEHIGKEITEN[name] + "_sw_total" + "\").value);\n" + "let inc = parseInt(this.getField(\"" + prefix + name + "_skill_inc" + "\").value);\n" + "this.getField(\"" + prefix + name + "_skill_total" + "\").value = b + inc;"

def create_js_adv_skill_sw_script(sw_name, name):
    return "let k = this.getField(\""+ sw_name + "\").value;\nlet val = parseInt(this.getField(\"pdf_\"+ k +\"_sw_total\").value);\nthis.getField(\"" +  name + "\").value = val;"

def create_js_adv_skill_total_script(name):
    return "let b = parseInt(this.getField(\"" + prefix + GRUNDFAEHIGKEITEN[name] + "_sw_total" + "\").value);\n" + "let inc = parseInt(this.getField(\"" + prefix + name + "_skill_inc" + "\").value);\n" + "this.getField(\"" + prefix + name + "_skill_total" + "\").value = b + inc;"

idx = 0
for name, sw in GRUNDFAEHIGKEITEN.items():
    y = 86 + idx * 5
    x = 72.5
    scribus.createPdfAnnotation(PDFCHECKBOX, 15.8, y + 1, 3, 3, prefix + name + "_skill_isCarreer")

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, x, y, 10, 5, prefix + name + "_skill_sw_total")
    # scribus.setText("0", textf)
    # scribus.setJSActionScript(9, "this.getField(\"" + textf + "\").value = parseInt(this.getField(\"pdf_" + sw + "_sw_total\").value);", textf)

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, x+10, y, 10, 5, prefix + name + "_skill_inc")
    # scribus.setText("0", textf)

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, x+20, y, 10, 5, prefix + name + "_skill_total")
    # scribus.setText("0", textf)
    # scribus.setJSActionScript(9, create_js_skill_total_script(name), textf)

    ###### advances #####
    if y < 175:
        scribus.createPdfAnnotation(PDFCHECKBOX, 108.3, y + 1, 3, 3, prefix + name + "_adv_skill_isCarreer")
        x = 115
        scribus.createPdfAnnotation(PDFTEXTFIELD, x, y, 40, 5, prefix + name + "_adv_skill_name")

        scribus.createPdfAnnotation(PDFTEXTFIELD, x+40, y, 10, 5, prefix + name + "_adv_skill_sw_type")
        textf = scribus.createPdfAnnotation(PDFTEXTFIELD, x+50, y, 10, 5, prefix + name + "_adv_skill_sw_total")
        # scribus.setJSActionScript(9, create_js_adv_skill_sw_script(prefix + name + "_adv_skill_sw_type", textf), textf)

        scribus.createPdfAnnotation(PDFTEXTFIELD, x+60, y, 10, 5, prefix + name + "_adv_skill_inc")
        scribus.createPdfAnnotation(PDFTEXTFIELD, x+70, y, 10, 5, prefix + name + "_adv_skill_total")

    idx = idx + 1

scribus.createPdfAnnotation(PDFTEXTFIELD, 108, 186, 87, 25, prefix + "notes")

# Talente
for i in range(11):
    y = 226 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 45, 5, prefix + "talent_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 60, y, 15, 5, prefix + "talent_" + str(i) + "_level")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 75, y, 120, 5, prefix + "talent_" + str(i) + "_desc")

###################################################################################################
# Page 2
scribus.gotoPage(2)

# Rüstung
for i in range(5):
    y = 26 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 35, 5, prefix + "ruestung_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 50, y, 10, 5, prefix + "ruestung_" + str(i) + "_tp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 60, y, 10, 5, prefix + "ruestung_" + str(i) + "_rp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 70, y, 90, 5, prefix + "ruestung_" + str(i) + "_qual")

# Waffen
for i in range(5):
    y = 66 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 35, 5, prefix + "waffe_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 50, y, 20, 5, prefix + "waffe_" + str(i) + "_grp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 70, y, 10, 5, prefix + "waffe_" + str(i) + "_tp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 80, y, 30, 5, prefix + "waffe_" + str(i) + "_reichweite")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 110, y, 20, 5, prefix + "waffe_" + str(i) + "_schaden")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 130, y, 65, 5, prefix + "waffe_" + str(i) + "_qual")

# Ausrüstung
for i in range(16):
    y = 106 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 67.5, 5, prefix + "ausruestung_0_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 82.5, y, 10, 5, prefix + "ausruestung_0_" + str(i) + "_anz")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 92.5, y, 10, 5, prefix + "ausruestung_0_" + str(i) + "_tp")

    scribus.createPdfAnnotation(PDFTEXTFIELD, 107.5, y, 67.5, 5, prefix + "ausruestung_1_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 175, y, 10, 5, prefix + "ausruestung_1_" + str(i) + "_anz")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 185, y, 10, 5, prefix + "ausruestung_1_" + str(i) + "_tp")

# Vermögen
for x in range(18):
    xPos = 15 + x * 10
    for y in range(7):
        yPos = 196 + 5 * y
        if (y == 0 and x < 3) or (y == 2 and x < 3) or (y == 4 and x < 4) or (y == 6 and x < 2):
            continue
        scribus.createPdfAnnotation(PDFTEXTFIELD, xPos, yPos, 10, 5, prefix + "vermoegen_" + str(x) + "_" +  str(y))


# Lebenspunkte
for x in range(18):
    xPos = 15 + x * 10
    for y in range(2):
        yPos = 246 + 5 * y
        scribus.createPdfAnnotation(PDFTEXTFIELD, xPos, yPos, 10, 5, prefix + "lebenspunkte_" + str(x) + "_" + str(y))

# Erfahrung
y = 266
scribus.createPdfAnnotation(PDFTEXTFIELD, 40, y, 155, 5, prefix + "erfahrung_" + str(1) + "_tp")
scribus.createPdfAnnotation(PDFTEXTFIELD, 40, y+5, 155, 5, prefix + "erfahrung_" + str(2) + "_tp")
scribus.createPdfAnnotation(PDFTEXTFIELD, 40, y+10, 155, 5, prefix + "erfahrung_" + str(3) + "_tp")
