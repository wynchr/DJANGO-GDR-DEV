"""
=======================================================================================================================
.DESCRIPTION
    Models for REFID Application
    - RefidIopProvAd
    - User (testing)

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS
    .
=======================================================================================================================
"""
from django.db import models


# =========================================================================================================
# APPLICATION Models
# =========================================================================================================

# ProvAd (Unmanaged Model) ==========


class RefidIopProvAd(models.Model):
    ENV_CHOICES = (
        ("DEV", "DEV"),
        ("PROD", "PROD"),
    )

    ORG_CHOICES = (
        ("OSIRIS", "OSIRIS"),
        ("CHUBXL", "CHUBXL"),
    )

    SOURCE_CHOICES = (
        ("REFID-User", "REFID-User"),
        ("INTERNEO-User", "INTERNEO-User"),
        ("IAM-User", "IAM-User"),
    )

    FLAG_CHOICES = (
        ("0", "FALSE"),
        ("1", "TRUE"),
    )

    STATE_CHOICES = (
        ("0", "WAITING TO BE INTEGRATED"),
        ("1", "INTEGRATED"),
        ("2", "ERROR"),
        ("9", "BLOCKED"),
    )

    ACTION_CHOICES = (
        ("CREATE", "CREATE"),
        ("UPDATE", "UPDATE"),
        ("ENABLE", "ENABLE"),
        ("DISABLE", "DISABLE"),
        ("SETEXPIRATION", "SETEXPIRATION"),
        ("CLEAREXPIRATION", "CLEAREXPIRATION"),
        ("RESETPASSWORD", "RESETPASSWORD"),
        ("INIT", "INIT"),
    )

    HOPITAL_CHOICES = (
        ("CHU-Brugmann", "CHU-Brugmann"),
        ("Huderf", "Huderf"),
        ("BRUSTP", "BRUSTP")
    )

    SITE_CHOICES = (
        ("Horta", "Horta"),
        ("Brien", "Brien"),
        ("Astrid", "Astrid"),
    )

    TYPE_CHOICES = (
        ("Administratif", "Administratif"),
        ("Medical", "Medical"),
        ("Nursing", "Nursing"),
        ("Paramedical", "Paramedical"),
        ("Technique", "Technique"),
        ("Ouvrier", "Ouvrier"),
        ("Other", "Other"),
        ("Unknown", "Unknown"),
    )

    CATEGORIE_CHOICES = (
        ("internal", "internal"),
        ("external", "external"),
        ("interim", "interim"),
        ("students", "students"),
        ("PG", "PG"),
        ("pg", "pg"),
        ("at60", "at60"),
        ("Named", "Named"),
        ("volunteers", "volunteers"),
        ("INDIVIDUAL", "INDIVIDUAL"),
    )

    LANGUE_CHOICES = (
        ("fr", "fr"),
        ("nl", "nl"),
        ("en", "en"),
        ("de", "de"),
    )

    GENDER_CHOICES = (
        ("M", "Masculin"),
        ("F", "Féminin"),
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
        ("CN=REFID_Administratif,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
         "REFID_Administratif"),
        ("CN=REFID_Medecin,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Medecin"),
        ("CN=REFID_Nursing,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Nursing"),
    )

    DISTRIBUTIONLIST_CHOICES = (
        (
        "CN=REFID - Distribution List for IT,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFID - Distribution List for IT"),
        (
        "CN=REFIDT - Test DL,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFIDT - Test DL"),

    )

    samaccountname = models.CharField(primary_key=True, max_length=10)

    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    company = models.CharField(max_length=50, blank=True, null=True, choices=HOPITAL_CHOICES)
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True, choices=SITE_CHOICES)
    department = models.CharField(max_length=50, blank=True, null=True, choices=DEPARTEMENT_CHOICES)

    businesscategory = models.CharField(max_length=20, blank=True, null=True, choices=CATEGORIE_CHOICES)
    employeetype = models.CharField(max_length=20, blank=True, null=True, choices=TYPE_CHOICES)

    preferredlanguage = models.CharField(max_length=2, blank=True, null=True, choices=LANGUE_CHOICES)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    birthday = models.CharField(max_length=20, blank=True, null=True)

    employeenumber = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=3, blank=True, null=True, choices=MOUVEMENT_CHOICES)
    extensionattribute11 = models.CharField(max_length=11, blank=True, null=True)

    telephonenumber = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)

    roles = models.CharField(max_length=200, blank=True, null=True, default="NA")
    unites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    specialites = models.CharField(max_length=200, blank=True, null=True, default="NA")

    homedir = models.CharField(max_length=200, blank=True, null=True,)
    homedrive = models.CharField(max_length=5, blank=True, null=True,)

    description = models.CharField(max_length=500, blank=True, null=True)

    info = models.CharField(max_length=50, blank=True, null=True, default="IAM-User", choices=SOURCE_CHOICES)
    extensionattribute15 = models.CharField(max_length=50, blank=False, default="REFID-User", choices=SOURCE_CHOICES)

    metadata = models.CharField(max_length=50, blank=True, null=True)

    enableaccountexpires = models.CharField(max_length=1, blank=True, null=True, default="0", choices=FLAG_CHOICES)
    accountexpires = models.CharField(max_length=20, blank=True, null=True)
    changepasswordatlogon = models.CharField(max_length=1, blank=False, default="1", choices=FLAG_CHOICES)
    enabled = models.CharField(max_length=1, blank=False, default="1", choices=FLAG_CHOICES)
    enablemail = models.CharField(max_length=1, blank=False, default="0", choices=FLAG_CHOICES)
    mail = models.CharField(max_length=100, blank=True, null=True, default="")

    groups = models.CharField(max_length=4000, blank=True, null=True, choices=SECURITYGROUP_CHOICES)
    distributionlist = models.CharField(max_length=4000, blank=True, null=True, choices=DISTRIBUTIONLIST_CHOICES)

    env = models.CharField(max_length=10, blank=False, default="DEV", choices=ENV_CHOICES)
    org = models.CharField(max_length=10, blank=False, default="OSIRIS", choices=ORG_CHOICES)

    usercre = models.CharField(max_length=15, blank=True, null=True, default="-")
    datecre = models.CharField(max_length=20, blank=True, null=True, default="-")
    userupd = models.CharField(max_length=15, blank=True, null=True, default="-")
    dateupd = models.CharField(max_length=20, blank=True, null=True, default="-")

    msgrefid = models.CharField(max_length=500, blank=True, null=True, default="Hello REFID")
    actiontype = models.CharField(max_length=15, blank=False, choices=ACTION_CHOICES)
    msgdb = models.CharField(max_length=500, blank=True, null=True, default="Hello DB")

    msgad = models.CharField(max_length=500, blank=True, null=True, default="Message from AD")
    datesyncad = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncad = models.CharField(max_length=1, blank=True, null=True, default="9", choices=STATE_CHOICES)

    msgexchange = models.CharField(max_length=500, blank=True, null=True, default="Message from EXCHANGE")
    datesyncexchange = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncexchange = models.CharField(max_length=1, blank=True, null=True, default="9", choices=STATE_CHOICES)

    objectsid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")
    objectguid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")

    class Meta:
        managed = False
        db_table = 'refid_iop_prov_ad'
        verbose_name = "ProvAdUser"
        ordering = ["-dateupd"]

    def __str__(self):
        label = f"{self.sn}, {self.givenname}  ({self.samaccountname})"
        return label

    # @staticmethod
    # def get_absolute_url():
    #     return "http://127.0.0.1:8000/refid/monitor-list-view/"

    @property
    def word_count(self):
        return len(self.extensionattribute11)

# ProvInitAd (Unmanaged Model) ==========


class RefidIopProvInitAd(models.Model):
    ENV_CHOICES = (
        ("DEV", "DEV"),
        ("PROD", "PROD"),
    )

    ORG_CHOICES = (
        ("OSIRIS", "OSIRIS"),
        ("CHUBXL", "CHUBXL"),
    )

    SOURCE_CHOICES = (
        ("REFID-User", "REFID-User"),
        ("INTERNEO-User", "INTERNEO-User"),
        ("IAM-User", "IAM-User"),
    )

    FLAG_CHOICES = (
        ("0", "FALSE"),
        ("1", "TRUE"),
    )

    STATE_CHOICES = (
        ("0", "WAITING TO BE INTEGRATED"),
        ("1", "INTEGRATED"),
        ("2", "ERROR"),
        ("9", "BLOCKED"),
    )

    ACTION_CHOICES = (
        ("CREATE", "CREATE"),
        ("UPDATE", "UPDATE"),
        ("ENABLE", "ENABLE"),
        ("DISABLE", "DISABLE"),
        ("SETEXPIRATION", "SETEXPIRATION"),
        ("CLEAREXPIRATION", "CLEAREXPIRATION"),
        ("RESETPASSWORD", "RESETPASSWORD"),
        ("INIT", "INIT"),
    )

    HOPITAL_CHOICES = (
        ("CHU-Brugmann", "CHU-Brugmann"),
        ("Huderf", "Huderf"),
        ("BRUSTP", "BRUSTP")
    )

    SITE_CHOICES = (
        ("Horta", "Horta"),
        ("Brien", "Brien"),
        ("Astrid", "Astrid"),
    )

    TYPE_CHOICES = (
        ("Administratif", "Administratif"),
        ("Medical", "Medical"),
        ("Nursing", "Nursing"),
        ("Paramedical", "Paramedical"),
        ("Technique", "Technique"),
        ("Ouvrier", "Ouvrier"),
        ("Other", "Other"),
        ("Unknown", "Unknown"),
    )

    CATEGORIE_CHOICES = (
        ("internal", "internal"),
        ("external", "external"),
        ("interim", "interim"),
        ("students", "students"),
        ("PG", "PG"),
        ("pg", "pg"),
        ("at60", "at60"),
        ("Named", "Named"),
        ("volunteers", "volunteers"),
        ("INDIVIDUAL", "INDIVIDUAL"),
    )

    LANGUE_CHOICES = (
        ("fr", "fr"),
        ("nl", "nl"),
        ("en", "en"),
        ("de", "de"),
    )

    GENDER_CHOICES = (
        ("M", "Masculin"),
        ("F", "Féminin"),
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
        ("CN=REFID_Administratif,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
         "REFID_Administratif"),
        ("CN=REFID_Medecin,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Medecin"),
        ("CN=REFID_Nursing,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be", "REFID_Nursing"),
    )

    DISTRIBUTIONLIST_CHOICES = (
        (
        "CN=REFID - Distribution List for IT,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFID - Distribution List for IT"),
        (
        "CN=REFIDT - Test DL,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be",
        "REFIDT - Test DL"),

    )

    samaccountname = models.CharField(primary_key=True, max_length=10)

    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    company = models.CharField(max_length=50, blank=True, null=True, choices=HOPITAL_CHOICES)
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True, choices=SITE_CHOICES)
    department = models.CharField(max_length=50, blank=True, null=True, choices=DEPARTEMENT_CHOICES)

    businesscategory = models.CharField(max_length=20, blank=True, null=True, choices=CATEGORIE_CHOICES)
    employeetype = models.CharField(max_length=20, blank=True, null=True, choices=TYPE_CHOICES)

    preferredlanguage = models.CharField(max_length=2, blank=True, null=True, choices=LANGUE_CHOICES)
    gender = models.CharField(max_length=1, blank=True, null=True, choices=GENDER_CHOICES)
    birthday = models.CharField(max_length=20, blank=True, null=True)

    employeenumber = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=3, blank=True, null=True, choices=MOUVEMENT_CHOICES)
    extensionattribute11 = models.CharField(max_length=11, blank=True, null=True)

    telephonenumber = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)

    roles = models.CharField(max_length=200, blank=True, null=True, default="NA")
    unites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    specialites = models.CharField(max_length=200, blank=True, null=True, default="NA")

    homedir = models.CharField(max_length=200, blank=True, null=True,)
    homedrive = models.CharField(max_length=5, blank=True, null=True,)

    description = models.CharField(max_length=500, blank=True, null=True)

    info = models.CharField(max_length=50, blank=True, null=True, default="IAM-User", choices=SOURCE_CHOICES)
    extensionattribute15 = models.CharField(max_length=50, blank=False, default="REFID-User", choices=SOURCE_CHOICES)

    metadata = models.CharField(max_length=50, blank=True, null=True)

    enableaccountexpires = models.CharField(max_length=1, blank=True, null=True, default="0", choices=FLAG_CHOICES)
    accountexpires = models.CharField(max_length=20, blank=True, null=True)
    changepasswordatlogon = models.CharField(max_length=1, blank=False, default="1", choices=FLAG_CHOICES)
    enabled = models.CharField(max_length=1, blank=False, default="1", choices=FLAG_CHOICES)
    enablemail = models.CharField(max_length=1, blank=False, default="0", choices=FLAG_CHOICES)
    mail = models.CharField(max_length=100, blank=True, null=True, default="")

    groups = models.CharField(max_length=4000, blank=True, null=True, choices=SECURITYGROUP_CHOICES)
    distributionlist = models.CharField(max_length=4000, blank=True, null=True, choices=DISTRIBUTIONLIST_CHOICES)

    env = models.CharField(max_length=10, blank=False, default="DEV", choices=ENV_CHOICES)
    org = models.CharField(max_length=10, blank=False, default="OSIRIS", choices=ORG_CHOICES)

    usercre = models.CharField(max_length=15, blank=True, null=True, default="-")
    datecre = models.CharField(max_length=20, blank=True, null=True, default="-")
    userupd = models.CharField(max_length=15, blank=True, null=True, default="-")
    dateupd = models.CharField(max_length=20, blank=True, null=True, default="-")

    msgrefid = models.CharField(max_length=500, blank=True, null=True, default="Hello REFID")
    actiontype = models.CharField(max_length=15, blank=False, choices=ACTION_CHOICES)
    msgdb = models.CharField(max_length=500, blank=True, null=True, default="Hello DB")

    msgad = models.CharField(max_length=500, blank=True, null=True, default="Message from AD")
    datesyncad = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncad = models.CharField(max_length=1, blank=True, null=True, default="9", choices=STATE_CHOICES)

    msgexchange = models.CharField(max_length=500, blank=True, null=True, default="Message from EXCHANGE")
    datesyncexchange = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncexchange = models.CharField(max_length=1, blank=True, null=True, default="9", choices=STATE_CHOICES)

    objectsid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")
    objectguid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")

    class Meta:
        managed = False
        db_table = 'refid_iop_provinit_ad'
        verbose_name = "ProvInitAdUser"
        ordering = ["-dateupd"]

    def __str__(self):
        label = f"{self.sn}, {self.givenname}  ({self.samaccountname})"
        return label

    # @staticmethod
    # def get_absolute_url():
    #     return "http://127.0.0.1:8000/refid/monitor-list-view/"

    @property
    def word_count(self):
        return len(self.extensionattribute11)

# ================================================================================================================
# TESTS Models
# ================================================================================================================


# ================================================================================================================
# Models NO MORE USED (Staying for examples)
# ================================================================================================================

# ProvInitAd (Managed Model) ==========

# class User(models.Model):
#     nom = models.CharField(max_length=50)
#     prenom = models.CharField(max_length=50)
#     create_date = models.DateTimeField('date created')
#
#     def __str__(self):
#         return self.nom + ', ' + self.prenom
#
#     class Meta:
#         managed = True
#         db_table = "z_temp_user"
