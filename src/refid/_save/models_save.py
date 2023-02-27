"""
=======================================================================================================================
.DESCRIPTION
    Models for REFID Application

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
from django.db import models

#########################################
# IT DEV Models Managed


class User(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    create_date = models.DateTimeField('date created')

    def __str__(self):
        return self.nom + ', ' + self.prenom

    class Meta:
        db_table = "z_temp_user"


#########################################
# IT DEV Models UnManaged

FLAG_CHOICES = (
    ("0", "FALSE"),
    ("1", "TRUE"),

)

TRIGGERFLAG_CHOICES = (
    ("0", "PENDING"),
    ("1", "INTEGRATED"),
    ("2", "ERROR"),
    ("9", "UNCOMPLETED"),
)

ACTION_CHOICES = (
    ("CREATE", "CREATE"),
    ("UPDATE", "UPDATE"),
    ("ENABLE", "ENABLE"),
    ("DISABLE", "DISABLE"),
    ("SETEXPIRATION", "SETEXPIRATION"),
    ("CLEAREXPIRATION", "CLEAREXPIRATION"),
    ("RESETPASSWORD", "RESETPASSWORD"),
)

HOPITAL_CHOICES = (
    ("CHU-BRUGMANN", "CHU-BRUGMANN"),
    ("HUDERF", "HUDERF")
)

SITE_CHOICES = (
    ("Astrid", "Astrid"),
    ("Brien", "Brien"),
    ("Horta", "Horta"),
)

TYPE_CHOICES = (
    ("Administratif", "Administratif"),
    ("Medical", "Medical"),
    ("Nursing", "Nursing"),
    ("Other", "Other"),
    ("Ouvrier", "Ouvrier"),
    ("Paramedical", "Paramedical"),
    ("Technique", "Technique"),
    ("Unknown", "Unknown"),
)

CATEGORIE_CHOICES = (
    ("INDIVIDUAL", "INDIVIDUAL"),
    ("Named", "Named"),
    ("PG", "PG"),
    ("at60", "at60"),
    ("external", "external"),
    ("interim", "interim"),
    ("internal", "internal"),
    ("pg", "pg"),
    ("students", "students"),
    ("volunteers", "volunteers"),
)

LANGUE_CHOICES = (
    ("fr", "fr"),
    ("nl", "nl"),
    ("en", "en"),
    ("de", "de"),
)

MOUVEMENT_CHOICES = (
    ("IN", "IN"),
    ("OUT", "OUT"),
    ("EXT", "EXT"),
    ("NEW", "NEW"),
    ("UKN", "UKN"),
)

DEPARTEMENT_CHOICES = (
    ("Achats", "Achats"),
    ("Anesthésie", "Anesthésie"),
    ("Cardiologie", "Cardiologie"),
    ("Centrale électrique", "Centrale électrique"),
    ("Chirurgie", "Chirurgie"),
    ("Chirurgie Vasculaire", "Chirurgie Vasculaire"),
    ("Comptabilité", "Comptabilité"),
    ("Consultations", "Consultations"),
    ("Dialyse", "Dialyse"),
    ("Direction Secrétariat", "Direction Secrétariat"),
    ("Direction département infirmier et paramédical", "Direction département infirmier et paramédical"),
    ("Direction financière", "Direction financière"),
    ("Diététique", "Diététique"),
    ("Facturation", "Facturation"),
    ("Gastro", "Gastro"),
    ("HUDE", "HUDE"),
    ("Informatique", "Informatique"),
    ("Labo Sommeil", "Labo Sommeil"),
    ("Laboratoire", "Laboratoire"),
    ("Maintenance", "Maintenance"),
    ("Nourissons", "Nourissons"),
    ("Nursing", "Nursing"),
    ("Néo-Natal", "Néo-Natal"),
    ("Néphrologie", "Néphrologie"),
    ("O.R.L.", "O.R.L."),
    ("Oncologie", "Oncologie"),
    ("Pharmacie", "Pharmacie"),
    ("Pneumologie", "Pneumologie"),
    ("Polyclinique", "Polyclinique"),
    ("Psychiatrie", "Psychiatrie"),
    ("Radiologie", "Radiologie"),
    ("Revalidation Neurologique", "Revalidation Neurologique"),
    ("Rhumatologie", "Rhumatologie"),
    ("Secrétariat Polyclinique", "Secrétariat Polyclinique"),
    ("Secrétariat médical", "Secrétariat médical"),
    ("Service GRH", "Service GRH"),
    ("Stomatologie", "Stomatologie"),
    ("Tarification", "Tarification"),
    ("Trésorerie", "Trésorerie"),
    ("Urgences", "Urgences"),
)

SECURITYGROUP_CHOICES = (
    ("CN=REFID_Administratif,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be","REFID_Administratif"),
    ("CN=REFID_Medecin,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be","REFID_Medecin"),
    ("CN=REFID_Nursing,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be","REFID_Nursing"),
)

DISTRIBUTIONLIST_CHOICES = (
    ("CN=REFID - Distribution List for IT,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be","REFID - Distribution List for IT"),
    ("CN=REFIDT - Test DL,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be","REFIDT - Test DL"),

)

class RefidIopProvAd(models.Model):
    samaccountname = models.CharField(primary_key=True, max_length=10)
    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True, choices=HOPITAL_CHOICES)
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True, choices=SITE_CHOICES)
    businesscategory = models.CharField(max_length=20, blank=True, null=True, choices=CATEGORIE_CHOICES)
    employeetype = models.CharField(max_length=20, blank=True, null=True, choices=TYPE_CHOICES)
    department = models.CharField(max_length=50, blank=True, null=True, choices=DEPARTEMENT_CHOICES)
    preferredlanguage = models.CharField(max_length=2, blank=True, null=True, choices=LANGUE_CHOICES)
    employeenumber = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=3, blank=True, null=True, choices=MOUVEMENT_CHOICES)
    extensionattribute11 = models.CharField(max_length=11, blank=True, null=True)
    telephonenumber = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)
    roles = models.CharField(max_length=200, blank=True, null=True, default="NA")
    unites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    specialites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    homedir = models.CharField(max_length=200, blank=True, null=True)
    homedrive = models.CharField(max_length=5, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True)
    extensionattribute15 = models.CharField(max_length=50, blank=True, null=True, default="REFID-User")
    enableaccountexpires = models.CharField(max_length=1, blank=True, null=True, default="1", choices=FLAG_CHOICES)
    accountexpires = models.CharField(max_length=20, blank=True, null=True)
    changepasswordatlogon = models.CharField(max_length=1, blank=True, null=True, default="1", choices=FLAG_CHOICES)
    enabled = models.CharField(max_length=1, blank=True, null=True, default="1", choices=FLAG_CHOICES)
    enablemail = models.CharField(max_length=1, blank=True, null=True, default="0", choices=FLAG_CHOICES)
    mail = models.CharField(max_length=100, blank=True, null=True, default="xxx@chu-brugmann.be")
    groups = models.CharField(max_length=4000, blank=True, null=True, choices=SECURITYGROUP_CHOICES)
    distributionlist = models.CharField(max_length=4000, blank=True, null=True, choices=DISTRIBUTIONLIST_CHOICES)
    env = models.CharField(max_length=10, blank=True, null=True, default="DEV")
    org = models.CharField(max_length=10, blank=True, null=True, default="OSIRIS")
    usercre = models.CharField(max_length=10, blank=True, null=True, default="-")
    datecre = models.CharField(max_length=20, blank=True, null=True, default="-")
    userupd = models.CharField(max_length=10, blank=True, null=True, default="-")
    dateupd = models.CharField(max_length=20, blank=True, null=True, default="-")
    msgrefid = models.CharField(max_length=500, blank=True, null=True, default="Hello REFID")
    actiontype = models.CharField(max_length=15, blank=True, null=True, choices=ACTION_CHOICES)
    msgdb = models.CharField(max_length=500, blank=True, null=True, default="Hello DB")
    msgad = models.CharField(max_length=500, blank=True, null=True, default="Message from AD")
    datesyncad = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncad = models.CharField(max_length=1, blank=True, null=True, default="9", choices=TRIGGERFLAG_CHOICES)
    msgexchange = models.CharField(max_length=500, blank=True, null=True, default="Message from EXCHANGE")
    datesyncexchange = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncexchange = models.CharField(max_length=1, blank=True, null=True, default="9", choices=TRIGGERFLAG_CHOICES)
    objectsid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")
    objectguid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")

    class Meta:
        managed = False
        db_table = 'refid_iop_prov_ad'
        verbose_name = "ProvAdUser"
        ordering = ["flagsyncad","samaccountname"]

    def __str__(self):
        label =  f"{self.sn}, {self.givenname}  ({self.samaccountname})"
        return label

    def get_absolute_url(self):
        return "http://127.0.0.1:8000/refid/monitor-list-view/"

    @property
    def word_count(self):
        return len(self.extensionattribute11)