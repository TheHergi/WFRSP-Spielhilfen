# -*-coding: utf-8 -*
# createPDFElements.py

import scribus
from collections import OrderedDict

# create "Spielwerte" PDF elements
print("\nRunning script createPDFElements")


# 0 PDFBUTTON, 1 PDFRADIOBUTTON, 2 PDFTEXTFIELD, 3 PDFCHECKBOX, 4 PDFCOMBOBOX, 5 PDFLISTBOX, 6 PDFTEXTANNOTATION, 7 PDFLINKANNOTATION, 8 PDF3DANNOTATION
PDFTEXTFIELD = 2
PDFCHECKBOX = 3

prefix = "pdf_"

###################################################################################################
# Page 1
scribus.gotoPage(1)
scribus.setActiveLayer("PDF")

def create_js_sw_total_script(sw):
    return "let b = parseInt(this.getField(\"pdf_" + sw + "_sw_base\").value);\n" + "let inc = parseInt(this.getField(\"pdf_" + sw + "_sw_inc\").value);\n" + "this.getField(\"pdf_" + sw + "_sw_total\").value = b + inc;"

# Spielwerte
SPIELWERTE = ["KG", "BF", "ST", "WI", "I", "GW", "GS", "IN", "WK", "CH"]
for idx, sp in enumerate(SPIELWERTE):
    scribus.createPdfAnnotation(PDFCHECKBOX, 41 + 10 * idx, 62, 8, 3, prefix + sp + "_sw_isCarreer")

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 40 + 10 * idx, 66, 10, 5, prefix + sp + "_sw_base")
    # scribus.setText("0", textf)

    textf= scribus.createPdfAnnotation(PDFTEXTFIELD, 40 + 10 * idx, 71, 10, 5, prefix + sp + "_sw_inc")
    # scribus.setText("0", textf)

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 40 + 10 * idx, 76, 10, 5, prefix + sp + "_sw_total")
    # scribus.setText("0", textf)
    # scribus.setJSActionScript(9, create_js_sw_total_script(sp), textf)

# Charakter
scribus.createPdfAnnotation(PDFTEXTFIELD, 25, 21, 75, 5, prefix + "name")
scribus.createPdfAnnotation(PDFTEXTFIELD, 25, 26, 75, 5, prefix + "volk")
scribus.createPdfAnnotation(PDFTEXTFIELD, 25, 31, 35, 5, prefix + "alter")
scribus.createPdfAnnotation(PDFTEXTFIELD, 25, 36, 35, 5, prefix + "haare")
scribus.createPdfAnnotation(PDFTEXTFIELD, 80, 31, 20, 5, prefix + "koerpergroese")
scribus.createPdfAnnotation(PDFTEXTFIELD, 80, 36, 20, 5, prefix + "augen")

# Karriere
scribus.createPdfAnnotation(PDFTEXTFIELD, 130, 21, 65, 5, prefix + "karriere")
scribus.createPdfAnnotation(PDFTEXTFIELD, 130, 26, 65, 5, prefix + "karriereweg_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 110, 31, 85, 5, prefix + "karriereweg_1")
scribus.createPdfAnnotation(PDFTEXTFIELD, 125, 36, 70, 5, prefix + "status")

# Schicksal & Zaehigkeit
scribus.createPdfAnnotation(PDFTEXTFIELD, 172.5, 56, 22.5, 5, prefix + "schicksal")
scribus.createPdfAnnotation(PDFTEXTFIELD, 172.5, 61, 22.5, 5, prefix + "glueck")
scribus.createPdfAnnotation(PDFTEXTFIELD, 172.5, 71, 22.5, 5, prefix + "zaehigkeit")
scribus.createPdfAnnotation(PDFTEXTFIELD, 172.5, 76, 22.5, 5, prefix + "mut")

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
    y = 101 + idx * 5
    scribus.createPdfAnnotation(PDFCHECKBOX, 51, y + 1, 8, 3, prefix + name + "_skill_isCarreer")

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 70, y, 10, 5, prefix + name + "_skill_sw_total")
    # scribus.setText("0", textf)
    # scribus.setJSActionScript(9, "this.getField(\"" + textf + "\").value = parseInt(this.getField(\"pdf_" + sw + "_sw_total\").value);", textf)

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 80, y, 10, 5, prefix + name + "_skill_inc")
    # scribus.setText("0", textf)

    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 90, y, 10, 5, prefix + name + "_skill_total")
    # scribus.setText("0", textf)
    # scribus.setJSActionScript(9, create_js_skill_total_script(name), textf)

    scribus.createPdfAnnotation(PDFTEXTFIELD, 110, y, 35, 5, prefix + name + "_adv_skill_name")
    scribus.createPdfAnnotation(PDFCHECKBOX, 146, y + 1, 8, 3, prefix + name + "_adv_skill_isCarreer")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 155, y, 10, 5, prefix + name + "_adv_skill_sw_type")
    textf = scribus.createPdfAnnotation(PDFTEXTFIELD, 165, y, 10, 5, prefix + name + "_adv_skill_sw_total")
    # scribus.setJSActionScript(9, create_js_adv_skill_sw_script(prefix + name + "_adv_skill_sw_type", textf), textf)

    scribus.createPdfAnnotation(PDFTEXTFIELD, 175, y, 10, 5, prefix + name + "_adv_skill_inc")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 185, y, 10, 5, prefix + name + "_adv_skill_total")

    idx = idx + 1

# Motivation und Ziele
scribus.createPdfAnnotation(PDFTEXTFIELD, 35, 241, 65, 5, prefix + "motivation_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 15, 246, 85, 5, prefix + "motivation_1")
scribus.createPdfAnnotation(PDFTEXTFIELD, 45, 251, 55, 5, prefix + "kf_ziele_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 15, 256, 85, 10, prefix + "kf_ziele_1")
scribus.createPdfAnnotation(PDFTEXTFIELD, 45, 266, 55, 5, prefix + "lf_ziele_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 15, 271, 85, 10, prefix + "lf_ziele_1")

# Gruppe
scribus.createPdfAnnotation(PDFTEXTFIELD, 130, 241, 65, 5, prefix + "mitglieder_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 110, 246, 85, 5, prefix + "mitglieder_2")
scribus.createPdfAnnotation(PDFTEXTFIELD, 140, 251, 55, 5, prefix + "kf_ziele_grp_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 110, 256, 85, 10, prefix + "kf_ziele_grp_1")
scribus.createPdfAnnotation(PDFTEXTFIELD, 140, 266, 55, 5, prefix + "lf_ziele_grp_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 110, 271, 85, 10, prefix + "lf_ziele_grp_1")


###################################################################################################
# Page 2
scribus.gotoPage(2)

# Talente
for i in range(14):
    y = 26 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 50, 5, prefix + "talent_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 65, y, 10, 5, prefix + "talent_" + str(i) + "_level")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 75, y, 120, 5, prefix + "talent_" + str(i) + "_desc")

# Psychologie
scribus.createPdfAnnotation(PDFTEXTFIELD, 15, 111, 55, 35, prefix + "psychologie")

# Mutation
scribus.createPdfAnnotation(PDFTEXTFIELD, 80, 111, 55, 10, prefix + "mutation")

# Korrumpierung
scribus.createPdfAnnotation(PDFTEXTFIELD, 80, 136, 55, 10, prefix + "korrumpierung")

# Bewegung
scribus.createPdfAnnotation(PDFTEXTFIELD, 15, 166, 18.33, 5, prefix + "bewegung")
scribus.createPdfAnnotation(PDFTEXTFIELD, 33.33, 166, 18.33, 5, prefix + "gehen")
scribus.createPdfAnnotation(PDFTEXTFIELD, 51.66, 166, 18.33, 5, prefix + "rennen")

# Lebenspunkte
scribus.createPdfAnnotation(PDFTEXTFIELD, 80, 166, 27.5, 5, prefix + "lebenspunkte")
scribus.createPdfAnnotation(PDFTEXTFIELD, 107.5, 166, 27.5, 5, prefix + "max_wunden")

# Rüstung
for i in range(7):
    y = 191 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 30, 5, prefix + "ruestung_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 45, y, 20, 5, prefix + "ruestung_" + str(i) + "_zone")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 65, y, 10, 5, prefix + "ruestung_" + str(i) + "_tp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 75, y, 10, 5, prefix + "ruestung_" + str(i) + "_rp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 85, y, 110, 5, prefix + "ruestung_" + str(i) + "_qual")

# Waffen
for i in range(7):
    y = 246 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 30, 5, prefix + "waffe_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 45, y, 20, 5, prefix + "waffe_" + str(i) + "_grp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 65, y, 10, 5, prefix + "waffe_" + str(i) + "_tp")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 75, y, 25, 5, prefix + "waffe_" + str(i) + "_reichweite")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 100, y, 20, 5, prefix + "waffe_" + str(i) + "_schaden")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 120, y, 75, 5, prefix + "waffe_" + str(i) + "_qual")

###################################################################################################
# Page 3
scribus.gotoPage(3)

# Ausrüstung 0
for i in range(20):
    y = 26 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 15, y, 65, 5, prefix + "ausruestung_0_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 80, y, 10, 5, prefix + "ausruestung_0_" + str(i) + "_anz")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 90, y, 10, 5, prefix + "ausruestung_0_" + str(i) + "_tp")

# Ausrüstung 1
for i in range(15):
    y = 26 + i * 5
    scribus.createPdfAnnotation(PDFTEXTFIELD, 110, y, 65, 5, prefix + "ausruestung_1_" + str(i) + "_name")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 175, y, 10, 5, prefix + "ausruestung_1_" + str(i) + "_anz")
    scribus.createPdfAnnotation(PDFTEXTFIELD, 185, y, 10, 5, prefix + "ausruestung_1_" + str(i) + "_tp")

# Tragslast
scribus.createPdfAnnotation(PDFTEXTFIELD, 110, 121, 21.25, 5, prefix + "tp_waffen")
scribus.createPdfAnnotation(PDFTEXTFIELD, 131.25, 121, 21.25, 5, prefix + "tp_ruestung")
scribus.createPdfAnnotation(PDFTEXTFIELD, 152.5, 121, 21.25, 5, prefix + "tp_ausruestung")
scribus.createPdfAnnotation(PDFTEXTFIELD, 173.75, 121, 21.25, 5, prefix + "tp_total")

# Vermögen
for x in range(18):
    xPos = 15 + x * 10
    for y in range(8):
        yPos = 141 + 5 * y
        if (y == 0 and x < 2) or (y == 2 and x < 3) or (y == 4 and x < 3) or (y == 6 and x < 1):
            continue
        scribus.createPdfAnnotation(PDFTEXTFIELD, xPos, yPos, 10, 5, prefix + "vermoegen_" + str(x) + "_" +  str(y))

# Erfahrung
for x in range(9):
    xPos = 15 + x * 20
    for y in range(6):
        yPos = 196 + 5 * y
        if (y % 2 == 0 and x < 1):
            continue
        scribus.createPdfAnnotation(PDFTEXTFIELD, xPos, yPos, 20, 5, prefix + "erfahrung_" + str(x) + "_" + str(y))

# Lebenspunkte
for x in range(18):
    xPos = 15 + x * 10
    for y in range(2):
        yPos = 241 + 5 * y
        if (y  == 0 and x < 2):
            continue
        scribus.createPdfAnnotation(PDFTEXTFIELD, xPos, yPos, 10, 5, prefix + "lebenspunkte_" + str(x) + "_" + str(y))

# Wunden
for x in range(16):
    xPos = 35 + x * 10
    scribus.createPdfAnnotation(PDFTEXTFIELD, xPos, 266, 10, 5, prefix + "wunden_" + str(x))

scribus.createPdfAnnotation(PDFTEXTFIELD, 35, 271, 160, 5, prefix + "verletzungen_0")
scribus.createPdfAnnotation(PDFTEXTFIELD, 15, 276, 180, 5, prefix + "verletzungen_1")
