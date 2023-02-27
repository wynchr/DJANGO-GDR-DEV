"""
=======================================================================================================================
.DESCRIPTION
    Gen PDF file to give the user

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	13/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
from pathlib import Path

from fpdf import FPDF
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
PDF_DIR = BASE_DIR / "_pdf"
IMG_DIR = BASE_DIR / "_img"
print(PDF_DIR)
print(IMG_DIR)


class UserPasswordPdf(FPDF):
    def __init__(self, nom_du_document, dict_user_info):
        # super()
        super().__init__()
        self.nom_du_document = nom_du_document
        self.dict_user_info = dict_user_info
        self.pdf = FPDF()

    def generate(self):
        try:
            mapping_txt = {
                "phrase0": {"FR": "Bruxelles, le ", "NL": "Brussel "},
                "phrase1": {"FR": "Concerne : votre demande d'un code d'accès Windows",
                            "NL": "Betref : uw aanvraag om een toegangscode tot Windows"},
                "phrase2": {"FR": "Le user à introduire est :", "NL": "De in te voegen user is : "},
                "phrase3": {"FR": "Votre mot de passe est :", "NL": "Uw password is : "},
                "phrase4": {
                    "FR": "Rappel : pour introduire des chiffres avec le pavé numérique, il faut activer la touche NumLock. :",
                    "NL": "PS: om getallen in te voegen met numerieke toetsenbord, dient U de toets NumLock actief te maken."},
                "phrase5": {
                    "FR": "Prière de ne pas laisser traîner ce document, s'il vous plaît, il y va de la sécurité ",
                    "NL": "Om de veiligheid en de betrouwbaarheid van het systeem te verzekeren zouden "},
                "phrase6": {"FR": " et de la confidentialité du système.",
                            "NL": "wij U dankbaar  zijn dit document niet round te laten slingeren."},
                "phrase7": {"FR": "Merci", "NL": "Dank U"},
                "phrase8": {"FR": "Helpdesk", "NL": "Helpdesk"},
                "phrase9": {"FR": "Consignes pour la création du mot de passe :",
                            "NL": "Instructies voor de aanmaak van het wachtwoord:"},
                "phrase10": {"FR": "- personnel et confidentiel", "NL": "- persoonlijk en vertrouwelijk"},
                "phrase11": {"FR": "- à modifier dès votre 1ère connexion",
                             "NL": "- aan te passen vanaf uw eerste verbinding"},
                "phrase12": {"FR": "- longueur minimale : 12 caractères", "NL": "- minimale lengte: 12 karakters"},
                "phrase13": {
                    "FR": "- doit contenir au moins 1 majuscule, 1 minuscule, 1 chiffre et 1 caractère non alphanumérique",
                    "NL": "- moet minimaal 1 hoofdletter, 1 kleine letter, 1 cijfer en 1 niet-alfanumeriek karakter bevatten"},
                "phrase14": {"FR": "- expirera tous les 6 mois", "NL": "- vervalt elke 6 maanden"},
            }

            now = datetime.now()
            # convert to string
            date_time_str = now.strftime("%d/%m/%Y")
            # Instantiation of inherited class
            self.pdf.add_page()
            self.pdf.set_left_margin(32)
            self.pdf.set_right_margin(32)
            self.pdf.image(f"{IMG_DIR}/logochub.png", 10, 10, 100, 0, "png")
            self.pdf.image(f"{IMG_DIR}/huderf.png", self.pdf.get_y() + 110, 10, 70, 0, 'png')
            # Setting font: helvetica bold 15
            # Moving cursor to the right:
            # Performing a line break:
            self.pdf.ln(40)
            self.pdf.set_x(0)
            self.pdf.set_font("helvetica", "B", 12)

            self.pdf.cell(0, 5, txt=f"{self.dict_user_info['qualite']}", ln=1, align="R")
            self.pdf.set_font("helvetica", "", 12)
            self.pdf.cell(0, 5, txt=f"{self.dict_user_info['nom']} {self.dict_user_info['prenom']}", ln=1, align="R")
            self.pdf.ln(14)
            self.pdf.set_font("helvetica", "", 12)
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase0'][self.dict_user_info['langue']]} {date_time_str}", ln=1,
                          align="R")
            self.pdf.ln(6)
            self.pdf.set_font("helvetica", "BU", 14)
            self.pdf.cell(200, 10, txt=f"{mapping_txt['phrase1'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.set_x(self.pdf.get_x() + 5)
            self.pdf.set_font("helvetica", "", 10)
            self.pdf.cell(45, 10, txt=f"{mapping_txt['phrase2'][self.dict_user_info['langue']]} ", ln=0, align="G")
            self.pdf.set_font("helvetica", "B", 10)
            self.pdf.cell(0, 10, txt=f" {self.dict_user_info['username']}", ln=1, align="G")
            self.pdf.ln(2)
            self.pdf.set_x(self.pdf.get_x() + 5)
            self.pdf.set_font("helvetica", "", 10)
            self.pdf.cell(45, 10, txt=f"{mapping_txt['phrase3'][self.dict_user_info['langue']]} ", ln=0, align="G")
            self.pdf.set_font("helvetica", "B", 10)
            self.pdf.cell(0, 10, txt=f" {self.dict_user_info['password']}", ln=1, align="G")
            self.pdf.ln(6)
            self.pdf.set_font("helvetica", "I", 10)
            self.pdf.cell(200, 5, txt=f"{mapping_txt['phrase4'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.set_font("helvetica", "B", 11)
            self.pdf.ln(14)
            self.pdf.cell(200, 5, txt=f"{mapping_txt['phrase5'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.cell(200, 5, txt=f"{mapping_txt['phrase6'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.ln(6)
            self.pdf.set_font("helvetica", "", 11)
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase7'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.ln(6)
            self.pdf.set_font("helvetica", "", 12)
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase8'][self.dict_user_info['langue']]} ", ln=1, align="C")
            self.pdf.cell(0, 5, txt="5555", ln=1, align="C")
            self.pdf.ln(70)
            self.pdf.set_font("helvetica", "U", 8)
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase9'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.set_font("helvetica", "", 8)
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase10'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase11'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase12'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.cell(0, 5, txt=f"{mapping_txt['phrase13'][self.dict_user_info['langue']]} ", ln=1, align="G")
            self.pdf.rect(22, self.pdf.get_y() - 25, 180.0, 30.8)
            self.pdf.output(self.nom_du_document)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print("gen pdf FR")
    d = {"langue": "FR",
         "qualite": "Mr",
         "nom": "Wyns",
         "prenom": "Christian",
         "username": "WYNCHR",
         "password": "QjQ1ZmQoU246Ono4"}
    o = UserPasswordPdf(f"{PDF_DIR}/{d['nom']}_{d['prenom']}_{d['username']}_{d['langue']}.pdf", d)
    o.generate()

    print("gen pdf NL")
    d = {"langue": "NL",
         "qualite": "Mr",
         "nom": "Wyns",
         "prenom": "Christian",
         "username": "WYNCHR",
         "password": "QjQ1ZmQoU246Ono4"}
    o = UserPasswordPdf(f"{PDF_DIR}/{d['nom']}_{d['prenom']}_{d['username']}_{d['langue']}.pdf", d)
    o.generate()

    print("gen pdf ended")
