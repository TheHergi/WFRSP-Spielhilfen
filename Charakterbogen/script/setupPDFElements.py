from xml.dom import minidom

filename = r'Charakterbogen/Charakterbogen.sla'
xmldoc = minidom.parse(filename)

tags = xmldoc.getElementsByTagName("PAGEOBJECT")

multilineTF = {"pdf_kf_ziele_1", "pdf_lf_ziele_1", "pdf_kf_ziele_grp_1", "pdf_lf_ziele_grp_1", "pdf_psychologie", "pdf_mutation", "pdf_korrumpierung"}

for item in tags:
    if item.hasAttribute("ANBWID"):
        name = item.attributes["ANNAME"].value
        # if "sw_total" in name:
        #     print("Read only: " + name)
        #     item.setAttribute("ANAA", "1") # read only
        #     item.setAttribute("ANFLAG", "1")

        # if "skill_total" in name:
        #     item.setAttribute("ANAA", "1") # read only
        #     item.setAttribute("ANFLAG", "1")

        # if name in multilineTF:
        #     item.setAttribute("ANFLAG", "4096")

        item.setAttribute("ANBWID", "0") # border width



with open(filename, "w", encoding='utf-8') as f:
    xmldoc.writexml(f, encoding='utf-8')