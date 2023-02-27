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
from utils.utils import create_choices

CHOICES = create_choices()


# =========================================================================================================
# APPLICATION Models
# =========================================================================================================

# ProvAd (Unmanaged Model) ==========


class RefidIopProvAd(models.Model):
    samaccountname = models.CharField(primary_key=True, max_length=10)

    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    usualsn = models.CharField(max_length=50, blank=True, null=True)
    usualgivenname = models.CharField(max_length=50, blank=True, null=True)

    company = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['HOPITAL'])
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['SITE'])
    department = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['DEPARTEMENT'])

    businesscategory = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['CATEGORIE'])
    employeetype = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['TYPE'])

    quality = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['QUALITY'])

    preferredlanguage = models.CharField(max_length=2, blank=True, null=True, choices=CHOICES['LANGUE'])
    gender = models.CharField(max_length=1, blank=True, null=True, choices=CHOICES['GENDER'])
    birthdate = models.CharField(max_length=20, blank=True, null=True)

    cardtype = models.CharField(max_length=15, blank=True, null=True, choices=CHOICES['CARDTYPE'])

    employeenumber = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=3, blank=True, null=True, choices=CHOICES['MOUVEMENT'])
    extensionattribute11 = models.CharField(max_length=11, blank=True, null=True)

    telephonenumber = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)
    localisation = models.CharField(max_length=20, blank=True, null=True)

    roles = models.CharField(max_length=200, blank=True, null=True, default="NA")
    unites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    specialites = models.CharField(max_length=200, blank=True, null=True, default="NA")

    homedir = models.CharField(max_length=200, blank=True, null=True, )
    homedrive = models.CharField(max_length=5, blank=True, null=True, )

    description = models.CharField(max_length=500, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True, default="IAM-User", choices=CHOICES['SOURCE'])
    extensionattribute15 = models.CharField(max_length=50, blank=False, default="REFID-User", choices=CHOICES['SOURCE'])
    metadata = models.CharField(max_length=50, blank=True, null=True)

    enableaccountexpires = models.CharField(max_length=1, blank=True, null=True, default="0", choices=CHOICES['FLAG'])
    accountexpires = models.CharField(max_length=20, blank=True, null=True)
    changepasswordatlogon = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enabled = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enablemail = models.CharField(max_length=1, blank=False, default="0", choices=CHOICES['FLAG'])
    mail = models.CharField(max_length=100, blank=True, null=True, default="")

    groups = models.CharField(max_length=4000, blank=True, null=True)
    distributionlist = models.CharField(max_length=4000, blank=True, null=True)

    groupsad = models.CharField(max_length=4000, blank=True, null=True)
    distributionlistad = models.CharField(max_length=4000, blank=True, null=True)

    env = models.CharField(max_length=10, blank=False, default="DEV", choices=CHOICES['ENV'])
    org = models.CharField(max_length=10, blank=False, default="OSIRIS", choices=CHOICES['ORG'])
    src = models.CharField(max_length=10, blank=True, null=True, default="OSIRIS", choices=CHOICES['SRC'])

    usercre = models.CharField(max_length=15, blank=True, null=True, default="-")
    datecre = models.CharField(max_length=20, blank=True, null=True, default="-")
    userupd = models.CharField(max_length=15, blank=True, null=True, default="-")
    dateupd = models.CharField(max_length=20, blank=True, null=True, default="-")

    msgrefid = models.CharField(max_length=500, blank=True, null=True, default="Hello REFID")
    actiontype = models.CharField(max_length=15, blank=False, choices=CHOICES['ACTION'])
    msgdb = models.CharField(max_length=500, blank=True, null=True, default="Hello DB")

    msgad = models.CharField(max_length=500, blank=True, null=True, default="Message from AD")
    datesyncad = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncad = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    msgexchange = models.CharField(max_length=500, blank=True, null=True, default="Message from EXCHANGE")
    datesyncexchange = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncexchange = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    password = models.CharField(max_length=50, blank=True, null=True)

    objectsid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")
    objectguid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")

    whencreated = models.CharField(max_length=20, blank=True, null=True, default="-")
    whenchanged = models.CharField(max_length=20, blank=True, null=True, default="-")
    lastlogontimestamp = models.CharField(max_length=20, blank=True, null=True, default="-")
    lastlogon = models.CharField(max_length=20, blank=True, null=True, default="-")
    pwdlastset = models.CharField(max_length=20, blank=True, null=True, default="-")
    badpasswordtime = models.CharField(max_length=20, blank=True, null=True, default="-")
    msexchwhenmailboxcreated = models.CharField(max_length=20, blank=True, null=True, default="-")

    chuidoriginsource = models.CharField(max_length=50, blank=True, null=True, default="-")
    evdidmstate = models.CharField(max_length=1, blank=True, null=True, default="-")
    evdpmschedulerstatus = models.CharField(max_length=30, blank=True, null=True, default="-")
    enatelbegintime = models.CharField(max_length=20, blank=True, null=True, default="-")
    enatelendtime = models.CharField(max_length=20, blank=True, null=True, default="-")

    rhmatricule = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhprenom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhsexe = models.CharField(max_length=1, blank=True, null=True, default="-")
    rhdnais = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhlangue = models.CharField(max_length=2, blank=True, null=True, default="-")
    rhnumcardid = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnumnational = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhdatedeb = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhdatefin = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhstatutcontrat = models.CharField(max_length=20, blank=True, null=True, default="-")

    rhcodesociete = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhcodeprofil = models.CharField(max_length=10, blank=True, null=True, default="-")
    rhprofil = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhcaqualification = models.CharField(max_length=8, blank=True, null=True, default="-")
    rhcacode = models.CharField(max_length=55, blank=True, null=True, default="-")
    rhcalib = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhinami = models.CharField(max_length=11, blank=True, null=True, default="-")

    rhmetadata = models.CharField(max_length=500, blank=True, null=True, default="-")

    rfidatesync = models.CharField(max_length=20, blank=True, null=True, default="-")
    messages = models.CharField(max_length=100, blank=True, null=True, default="-")

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
    samaccountname = models.CharField(primary_key=True, max_length=10)

    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    usualsn = models.CharField(max_length=50, blank=True, null=True)
    usualgivenname = models.CharField(max_length=50, blank=True, null=True)

    company = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['HOPITAL'])
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['SITE'])
    department = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['DEPARTEMENT'])

    businesscategory = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['CATEGORIE'])
    employeetype = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['TYPE'])

    quality = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['QUALITY'])

    preferredlanguage = models.CharField(max_length=2, blank=True, null=True, choices=CHOICES['LANGUE'])
    gender = models.CharField(max_length=1, blank=True, null=True, choices=CHOICES['GENDER'])
    birthdate = models.CharField(max_length=20, blank=True, null=True)

    cardtype = models.CharField(max_length=15, blank=True, null=True, choices=CHOICES['CARDTYPE'])

    employeenumber = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=3, blank=True, null=True, choices=CHOICES['MOUVEMENT'])
    extensionattribute11 = models.CharField(max_length=11, blank=True, null=True)

    telephonenumber = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)
    localisation = models.CharField(max_length=20, blank=True, null=True)

    roles = models.CharField(max_length=200, blank=True, null=True, default="NA")
    unites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    specialites = models.CharField(max_length=200, blank=True, null=True, default="NA")

    homedir = models.CharField(max_length=200, blank=True, null=True, )
    homedrive = models.CharField(max_length=5, blank=True, null=True, )

    description = models.CharField(max_length=500, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True, default="IAM-User", choices=CHOICES['SOURCE'])
    extensionattribute15 = models.CharField(max_length=50, blank=False, default="REFID-User", choices=CHOICES['SOURCE'])
    metadata = models.CharField(max_length=50, blank=True, null=True)

    enableaccountexpires = models.CharField(max_length=1, blank=True, null=True, default="0", choices=CHOICES['FLAG'])
    accountexpires = models.CharField(max_length=20, blank=True, null=True)
    changepasswordatlogon = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enabled = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enablemail = models.CharField(max_length=1, blank=False, default="0", choices=CHOICES['FLAG'])
    mail = models.CharField(max_length=100, blank=True, null=True, default="")

    groups = models.CharField(max_length=4000, blank=True, null=True)
    distributionlist = models.CharField(max_length=4000, blank=True, null=True)

    groupsad = models.CharField(max_length=4000, blank=True, null=True)
    distributionlistad = models.CharField(max_length=4000, blank=True, null=True)

    env = models.CharField(max_length=10, blank=False, default="DEV", choices=CHOICES['ENV'])
    org = models.CharField(max_length=10, blank=False, default="OSIRIS", choices=CHOICES['ORG'])
    src = models.CharField(max_length=10, blank=True, null=True, default="OSIRIS", choices=CHOICES['SRC'])

    usercre = models.CharField(max_length=15, blank=True, null=True, default="-")
    datecre = models.CharField(max_length=20, blank=True, null=True, default="-")
    userupd = models.CharField(max_length=15, blank=True, null=True, default="-")
    dateupd = models.CharField(max_length=20, blank=True, null=True, default="-")

    msgrefid = models.CharField(max_length=500, blank=True, null=True, default="Hello REFID")
    actiontype = models.CharField(max_length=15, blank=False, choices=CHOICES['ACTION'])
    msgdb = models.CharField(max_length=500, blank=True, null=True, default="Hello DB")

    msgad = models.CharField(max_length=500, blank=True, null=True, default="Message from AD")
    datesyncad = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncad = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    msgexchange = models.CharField(max_length=500, blank=True, null=True, default="Message from EXCHANGE")
    datesyncexchange = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncexchange = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    password = models.CharField(max_length=50, blank=True, null=True)

    objectsid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")
    objectguid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")

    whencreated = models.CharField(max_length=20, blank=True, null=True, default="-")
    whenchanged = models.CharField(max_length=20, blank=True, null=True, default="-")
    lastlogontimestamp = models.CharField(max_length=20, blank=True, null=True, default="-")
    lastlogon = models.CharField(max_length=20, blank=True, null=True, default="-")
    pwdlastset = models.CharField(max_length=20, blank=True, null=True, default="-")
    badpasswordtime = models.CharField(max_length=20, blank=True, null=True, default="-")
    msexchwhenmailboxcreated = models.CharField(max_length=20, blank=True, null=True, default="-")

    chuidoriginsource = models.CharField(max_length=50, blank=True, null=True, default="-")
    evdidmstate = models.CharField(max_length=1, blank=True, null=True, default="-")
    evdpmschedulerstatus = models.CharField(max_length=30, blank=True, null=True, default="-")
    enatelbegintime = models.CharField(max_length=20, blank=True, null=True, default="-")
    enatelendtime = models.CharField(max_length=20, blank=True, null=True, default="-")

    rhmatricule = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhprenom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhsexe = models.CharField(max_length=1, blank=True, null=True, default="-")
    rhdnais = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhlangue = models.CharField(max_length=2, blank=True, null=True, default="-")
    rhnumcardid = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnumnational = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhdatedeb = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhdatefin = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhstatutcontrat = models.CharField(max_length=20, blank=True, null=True, default="-")

    rhcodesociete = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhcodeprofil = models.CharField(max_length=10, blank=True, null=True, default="-")
    rhprofil = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhcaqualification = models.CharField(max_length=8, blank=True, null=True, default="-")
    rhcacode = models.CharField(max_length=55, blank=True, null=True, default="-")
    rhcalib = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhinami = models.CharField(max_length=11, blank=True, null=True, default="-")

    rhmetadata = models.CharField(max_length=500, blank=True, null=True, default="-")

    rfidatesync = models.CharField(max_length=20, blank=True, null=True, default="-")
    messages = models.CharField(max_length=100, blank=True, null=True, default="-")

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


# ProvMirrorAd (Unmanaged Model) ==========


class RefidIopProvMirrorAd(models.Model):
    samaccountname = models.CharField(primary_key=True, max_length=10)

    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    usualsn = models.CharField(max_length=50, blank=True, null=True)
    usualgivenname = models.CharField(max_length=50, blank=True, null=True)

    company = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['HOPITAL'])
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['SITE'])
    department = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['DEPARTEMENT'])

    businesscategory = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['CATEGORIE'])
    employeetype = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['TYPE'])

    quality = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['QUALITY'])

    preferredlanguage = models.CharField(max_length=2, blank=True, null=True, choices=CHOICES['LANGUE'])
    gender = models.CharField(max_length=1, blank=True, null=True, choices=CHOICES['GENDER'])
    birthdate = models.CharField(max_length=20, blank=True, null=True)

    cardtype = models.CharField(max_length=15, blank=True, null=True, choices=CHOICES['CARDTYPE'])

    employeenumber = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=3, blank=True, null=True, choices=CHOICES['MOUVEMENT'])
    extensionattribute11 = models.CharField(max_length=11, blank=True, null=True)

    telephonenumber = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)
    localisation = models.CharField(max_length=20, blank=True, null=True)

    roles = models.CharField(max_length=200, blank=True, null=True, default="NA")
    unites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    specialites = models.CharField(max_length=200, blank=True, null=True, default="NA")

    homedir = models.CharField(max_length=200, blank=True, null=True, )
    homedrive = models.CharField(max_length=5, blank=True, null=True, )

    description = models.CharField(max_length=500, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True, default="IAM-User", choices=CHOICES['SOURCE'])
    extensionattribute15 = models.CharField(max_length=50, blank=False, default="REFID-User", choices=CHOICES['SOURCE'])
    metadata = models.CharField(max_length=50, blank=True, null=True)

    enableaccountexpires = models.CharField(max_length=1, blank=True, null=True, default="0", choices=CHOICES['FLAG'])
    accountexpires = models.CharField(max_length=20, blank=True, null=True)
    changepasswordatlogon = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enabled = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enablemail = models.CharField(max_length=1, blank=False, default="0", choices=CHOICES['FLAG'])
    mail = models.CharField(max_length=100, blank=True, null=True, default="")

    groups = models.CharField(max_length=4000, blank=True, null=True)
    distributionlist = models.CharField(max_length=4000, blank=True, null=True)

    groupsad = models.CharField(max_length=4000, blank=True, null=True)
    distributionlistad = models.CharField(max_length=4000, blank=True, null=True)

    env = models.CharField(max_length=10, blank=False, default="DEV", choices=CHOICES['ENV'])
    org = models.CharField(max_length=10, blank=False, default="OSIRIS", choices=CHOICES['ORG'])
    src = models.CharField(max_length=10, blank=True, null=True, default="OSIRIS", choices=CHOICES['SRC'])

    usercre = models.CharField(max_length=15, blank=True, null=True, default="-")
    datecre = models.CharField(max_length=20, blank=True, null=True, default="-")
    userupd = models.CharField(max_length=15, blank=True, null=True, default="-")
    dateupd = models.CharField(max_length=20, blank=True, null=True, default="-")

    msgrefid = models.CharField(max_length=500, blank=True, null=True, default="Hello REFID")
    actiontype = models.CharField(max_length=15, blank=False, choices=CHOICES['ACTION'])
    msgdb = models.CharField(max_length=500, blank=True, null=True, default="Hello DB")

    msgad = models.CharField(max_length=500, blank=True, null=True, default="Message from AD")
    datesyncad = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncad = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    msgexchange = models.CharField(max_length=500, blank=True, null=True, default="Message from EXCHANGE")
    datesyncexchange = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncexchange = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    password = models.CharField(max_length=50, blank=True, null=True)

    objectsid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")
    objectguid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")

    whencreated = models.CharField(max_length=21, blank=True, null=True)
    whenchanged = models.CharField(max_length=21, blank=True, null=True)
    lastlogontimestamp = models.CharField(max_length=21, blank=True, null=True)
    lastlogon = models.CharField(max_length=21, blank=True, null=True)
    pwdlastset = models.CharField(max_length=21, blank=True, null=True)
    badpasswordtime = models.CharField(max_length=21, blank=True, null=True)
    msexchwhenmailboxcreated = models.CharField(max_length=21, blank=True, null=True)

    chuidoriginsource = models.CharField(max_length=50, blank=True, null=True)
    evdidmstate = models.CharField(max_length=1, blank=True, null=True)
    evdpmschedulerstatus = models.CharField(max_length=50, blank=True, null=True)
    enatelbegintime = models.CharField(max_length=25, blank=True, null=True)
    enatelendtime = models.CharField(max_length=25, blank=True, null=True)

    rhmatricule = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhprenom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhsexe = models.CharField(max_length=1, blank=True, null=True, default="-")
    rhdnais = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhlangue = models.CharField(max_length=2, blank=True, null=True, default="-")
    rhnumcardid = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnumnational = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhdatedeb = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhdatefin = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhstatutcontrat = models.CharField(max_length=20, blank=True, null=True, default="-")

    rhcodesociete = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhcodeprofil = models.CharField(max_length=10, blank=True, null=True, default="-")
    rhprofil = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhcaqualification = models.CharField(max_length=8, blank=True, null=True, default="-")
    rhcacode = models.CharField(max_length=55, blank=True, null=True, default="-")
    rhcalib = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhinami = models.CharField(max_length=11, blank=True, null=True, default="-")

    rhmetadata = models.CharField(max_length=500, blank=True, null=True, default="-")

    rfidatesync = models.CharField(max_length=21, blank=True, null=True)
    messages = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_provmirror_ad'
        verbose_name = "ProvMirrorAdUser"
        ordering = ["-dateupd"]

    def __str__(self):
        label = f"{self.sn}, {self.givenname}  ({self.samaccountname})"
        return label


# ProvLogAd (Unmanaged Model) ==========


class RefidIopProvLogAd(models.Model):
    id = models.FloatField(primary_key=True)
    samaccountname = models.CharField(max_length=10)

    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    usualsn = models.CharField(max_length=50, blank=True, null=True)
    usualgivenname = models.CharField(max_length=50, blank=True, null=True)

    company = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['HOPITAL'])
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['SITE'])
    department = models.CharField(max_length=50, blank=True, null=True, choices=CHOICES['DEPARTEMENT'])

    businesscategory = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['CATEGORIE'])
    employeetype = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['TYPE'])

    quality = models.CharField(max_length=20, blank=True, null=True, choices=CHOICES['QUALITY'])

    preferredlanguage = models.CharField(max_length=2, blank=True, null=True, choices=CHOICES['LANGUE'])
    gender = models.CharField(max_length=1, blank=True, null=True, choices=CHOICES['GENDER'])
    birthdate = models.CharField(max_length=20, blank=True, null=True)

    cardtype = models.CharField(max_length=15, blank=True, null=True, choices=CHOICES['CARDTYPE'])

    employeenumber = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=30, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=3, blank=True, null=True, choices=CHOICES['MOUVEMENT'])
    extensionattribute11 = models.CharField(max_length=11, blank=True, null=True)

    telephonenumber = models.CharField(max_length=50, blank=True, null=True)
    pager = models.CharField(max_length=20, blank=True, null=True)
    localisation = models.CharField(max_length=20, blank=True, null=True)

    roles = models.CharField(max_length=200, blank=True, null=True, default="NA")
    unites = models.CharField(max_length=200, blank=True, null=True, default="NA")
    specialites = models.CharField(max_length=200, blank=True, null=True, default="NA")

    homedir = models.CharField(max_length=200, blank=True, null=True, )
    homedrive = models.CharField(max_length=5, blank=True, null=True, )

    description = models.CharField(max_length=500, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True, default="IAM-User", choices=CHOICES['SOURCE'])
    extensionattribute15 = models.CharField(max_length=50, blank=False, default="REFID-User", choices=CHOICES['SOURCE'])
    metadata = models.CharField(max_length=50, blank=True, null=True)

    enableaccountexpires = models.CharField(max_length=1, blank=True, null=True, default="0", choices=CHOICES['FLAG'])
    accountexpires = models.CharField(max_length=20, blank=True, null=True)
    changepasswordatlogon = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enabled = models.CharField(max_length=1, blank=False, default="1", choices=CHOICES['FLAG'])
    enablemail = models.CharField(max_length=1, blank=False, default="0", choices=CHOICES['FLAG'])
    mail = models.CharField(max_length=100, blank=True, null=True, default="")

    groups = models.CharField(max_length=4000, blank=True, null=True)
    distributionlist = models.CharField(max_length=4000, blank=True, null=True)

    groupsad = models.CharField(max_length=4000, blank=True, null=True)
    distributionlistad = models.CharField(max_length=4000, blank=True, null=True)

    env = models.CharField(max_length=10, blank=False, default="DEV", choices=CHOICES['ENV'])
    org = models.CharField(max_length=10, blank=False, default="OSIRIS", choices=CHOICES['ORG'])
    src = models.CharField(max_length=10, blank=True, null=True, default="OSIRIS", choices=CHOICES['SRC'])

    usercre = models.CharField(max_length=15, blank=True, null=True, default="-")
    datecre = models.CharField(max_length=20, blank=True, null=True, default="-")
    userupd = models.CharField(max_length=15, blank=True, null=True, default="-")
    dateupd = models.CharField(max_length=20, blank=True, null=True, default="-")

    msgrefid = models.CharField(max_length=500, blank=True, null=True, default="Hello REFID")
    actiontype = models.CharField(max_length=15, blank=False, choices=CHOICES['ACTION'])
    msgdb = models.CharField(max_length=500, blank=True, null=True, default="Hello DB")

    msgad = models.CharField(max_length=500, blank=True, null=True, default="Message from AD")
    datesyncad = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncad = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    msgexchange = models.CharField(max_length=500, blank=True, null=True, default="Message from EXCHANGE")
    datesyncexchange = models.CharField(max_length=20, blank=True, null=True, default="1900-01-01 01:01:01")
    flagsyncexchange = models.CharField(max_length=1, blank=True, null=True, default="9", choices=CHOICES['STATE'])

    password = models.CharField(max_length=50, blank=True, null=True)

    objectsid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")
    objectguid = models.CharField(max_length=50, blank=True, null=True, default="Wait AD return")

    whencreated = models.CharField(max_length=21, blank=True, null=True)
    whenchanged = models.CharField(max_length=21, blank=True, null=True)
    lastlogontimestamp = models.CharField(max_length=21, blank=True, null=True)
    lastlogon = models.CharField(max_length=21, blank=True, null=True)
    pwdlastset = models.CharField(max_length=21, blank=True, null=True)
    badpasswordtime = models.CharField(max_length=21, blank=True, null=True)
    msexchwhenmailboxcreated = models.CharField(max_length=21, blank=True, null=True)

    chuidoriginsource = models.CharField(max_length=50, blank=True, null=True)
    evdidmstate = models.CharField(max_length=1, blank=True, null=True)
    evdpmschedulerstatus = models.CharField(max_length=50, blank=True, null=True)
    enatelbegintime = models.CharField(max_length=25, blank=True, null=True)
    enatelendtime = models.CharField(max_length=25, blank=True, null=True)

    rhmatricule = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhprenom = models.CharField(max_length=50, blank=True, null=True, default="-")
    rhsexe = models.CharField(max_length=1, blank=True, null=True, default="-")
    rhdnais = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhlangue = models.CharField(max_length=2, blank=True, null=True, default="-")
    rhnumcardid = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhnumnational = models.CharField(max_length=30, blank=True, null=True, default="-")
    rhdatedeb = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhdatefin = models.CharField(max_length=20, blank=True, null=True, default="-")
    rhstatutcontrat = models.CharField(max_length=20, blank=True, null=True, default="-")

    rhcodesociete = models.CharField(max_length=15, blank=True, null=True, default="-")
    rhcodeprofil = models.CharField(max_length=10, blank=True, null=True, default="-")
    rhprofil = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhcaqualification = models.CharField(max_length=8, blank=True, null=True, default="-")
    rhcacode = models.CharField(max_length=55, blank=True, null=True, default="-")
    rhcalib = models.CharField(max_length=100, blank=True, null=True, default="-")
    rhinami = models.CharField(max_length=11, blank=True, null=True, default="-")

    rhmetadata = models.CharField(max_length=500, blank=True, null=True, default="-")

    rfidatesync = models.CharField(max_length=21, blank=True, null=True)
    messages = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_provlog_ad'
        verbose_name = "ProvLogAdUser"
        ordering = ["-dateupd"]

    def __str__(self):
        label = f"{self.sn}, {self.givenname}  ({self.samaccountname})"
        return label


# ================================================================================================================
# CACHE Models
# ================================================================================================================


class RefidIopCacheRh(models.Model):
    v100_rh_matricule = models.CharField(primary_key=True, max_length=20)
    v100_rh_nom = models.CharField(max_length=50, blank=True, null=True)
    v100_rh_prenom = models.CharField(max_length=50, blank=True, null=True)
    v100_rh_sexe = models.CharField(max_length=1, blank=True, null=True)
    v100_rh_registre_national = models.CharField(max_length=11, blank=True, null=True)
    v100_rh_date_naissance = models.CharField(max_length=21, blank=True, null=True)
    v100_rh_langue = models.CharField(max_length=2, blank=True, null=True)
    v100_rh_num_carte_id = models.CharField(max_length=21, blank=True, null=True)
    v300_rh_date_debut_contrat = models.CharField(max_length=21, blank=True, null=True)
    v300_rh_date_fin_contrat = models.CharField(max_length=21, blank=True, null=True)
    v100_rh_statut_contrat = models.CharField(max_length=3, blank=True, null=True)

    v200_contrat_code_societe = models.CharField(max_length=15, blank=True, null=True)
    v955_contrat_code_profil = models.CharField(max_length=10, blank=True, null=True)
    v955_contrat_profil_fr = models.CharField(max_length=100, blank=True, null=True)
    v600_ca_ventil_qualification = models.CharField(max_length=8, blank=True, null=True)
    v600_ca_ventil_code = models.CharField(max_length=55, blank=True, null=True)
    v600_ca_ventil_fr = models.CharField(max_length=100, blank=True, null=True)
    v125_rh_inami_11 = models.CharField(max_length=11, blank=True, null=True)

    rfidatesync = models.CharField(max_length=21, blank=True, null=True)
    messages = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_cache_rh'
        verbose_name = "CacheRH"

    def __str__(self):
        label = f"{self.v100_rh_nom}, {self.v100_rh_prenom}  ({self.v100_rh_matricule})"
        return label


class RefidIopCacheEvidian(models.Model):
    cn = models.CharField(primary_key=True, max_length=20)
    stpadlogin = models.CharField(max_length=20, blank=True, null=True)
    employeeid = models.CharField(max_length=20, blank=True, null=True)
    stpniss = models.CharField(max_length=20, blank=True, null=True)
    stpinaminumber = models.CharField(max_length=20, blank=True, null=True)
    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    osirisevidiansex = models.CharField(max_length=1, blank=True, null=True)
    stpbirthdate = models.CharField(max_length=25, blank=True, null=True)
    preferredlanguage = models.CharField(max_length=2, blank=True, null=True)
    businesscategory = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True)
    employeetype = models.CharField(max_length=50, blank=True, null=True)
    osirishrcontractstatus = models.CharField(max_length=5, blank=True, null=True)
    osirishrcontractstartdate = models.CharField(max_length=25, blank=True, null=True)
    osirishrcontractenddate = models.CharField(max_length=25, blank=True, null=True)
    chuidoriginsource = models.CharField(max_length=50, blank=True, null=True)
    distinguishedname = models.CharField(max_length=100, blank=True, null=True)
    evdidmuseridrep = models.CharField(max_length=100, blank=True, null=True)
    evdidmstate = models.CharField(max_length=1, blank=True, null=True)
    evdpmschedulerstatus = models.CharField(max_length=50, blank=True, null=True)
    whencreated = models.CharField(max_length=25, blank=True, null=True)
    whenchanged = models.CharField(max_length=25, blank=True, null=True)
    enatelbegintime = models.CharField(max_length=25, blank=True, null=True)
    enatelendtime = models.CharField(max_length=25, blank=True, null=True)
    rfidatesync = models.CharField(max_length=21, blank=True, null=True)
    messages = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_cache_evidian'
        verbose_name = "CacheEVIDIAN"

    def __str__(self):
        label = f"{self.sn}, {self.givenname}  ({self.cn})"
        return label


class RefidIopCacheAdOsiris(models.Model):
    samaccountname = models.CharField(primary_key=True, max_length=20)
    sn = models.CharField(max_length=50, blank=True, null=True)
    givenname = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    physicaldeliveryofficename = models.CharField(max_length=50, blank=True, null=True)
    businesscategory = models.CharField(max_length=50, blank=True, null=True)
    employeetype = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    preferredlanguage = models.CharField(max_length=5, blank=True, null=True)
    employeenumber = models.CharField(max_length=50, blank=True, null=True)
    extensionattribute1 = models.CharField(max_length=50, blank=True, null=True)
    extensionattribute2 = models.CharField(max_length=50, blank=True, null=True)
    extensionattribute10 = models.CharField(max_length=50, blank=True, null=True)
    extensionattribute11 = models.CharField(max_length=50, blank=True, null=True)
    telephonenumber = models.CharField(max_length=30, blank=True, null=True)
    pager = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    accountexpires = models.CharField(max_length=25, blank=True, null=True)
    enabled = models.CharField(max_length=5, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    cn = models.CharField(max_length=150, blank=True, null=True)
    userprincipalname = models.CharField(max_length=100, blank=True, null=True)
    displayname = models.CharField(max_length=150, blank=True, null=True)
    employeeid = models.CharField(max_length=20, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True)
    extensionattribute3 = models.CharField(max_length=50, blank=True, null=True)
    businessroles = models.CharField(max_length=50, blank=True, null=True)
    homedirectory = models.CharField(max_length=50, blank=True, null=True)
    homedrive = models.CharField(max_length=2, blank=True, null=True)
    distinguishedname = models.CharField(max_length=150, blank=True, null=True)
    networkdomainid = models.CharField(max_length=150, blank=True, null=True)
    objectguid = models.CharField(max_length=150, blank=True, null=True)
    objectsid = models.CharField(max_length=150, blank=True, null=True)
    whencreated = models.CharField(max_length=21, blank=True, null=True)
    whenchanged = models.CharField(max_length=21, blank=True, null=True)
    lastlogontimestamp = models.CharField(max_length=21, blank=True, null=True)
    lastlogon = models.CharField(max_length=21, blank=True, null=True)
    pwdlastset = models.CharField(max_length=21, blank=True, null=True)
    badpasswordtime = models.CharField(max_length=21, blank=True, null=True)
    useraccountcontrol = models.CharField(max_length=50, blank=True, null=True)
    mail = models.CharField(max_length=150, blank=True, null=True)
    msexchwhenmailboxcreated = models.CharField(max_length=21, blank=True, null=True)
    rfidatesync = models.CharField(max_length=21, blank=True, null=True)
    messages = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_cache_ad_osiris'
        verbose_name = "CacheAD"

    def __str__(self):
        label = f"{self.sn}, {self.givenname}  ({self.samaccountname})"
        return label


# ================================================================================================================
# OTHER IOP Models
# ================================================================================================================


class RefidIopRefadgroups(models.Model):
    id = models.FloatField(primary_key=True)
    samaccountname = models.CharField(max_length=100, blank=True, null=True)
    distinguishedname = models.CharField(max_length=200, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    groupcategory = models.CharField(max_length=20, blank=True, null=True)
    whencreated = models.CharField(max_length=21, blank=True, null=True)
    whenchanged = models.CharField(max_length=21, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    info = models.CharField(max_length=50, blank=True, null=True)
    objectguid = models.CharField(max_length=50, blank=True, null=True)
    objectsid = models.CharField(max_length=50, blank=True, null=True)
    env = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_refadgroups'
        verbose_name = "RefAdGroup"
        ordering = ["samaccountname"]


class RefidIopReferences(models.Model):
    id = models.FloatField(primary_key=True)
    reference = models.CharField(max_length=30, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    flag = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_references'
        verbose_name = "Reference"
        ordering = ["id"]

    def __str__(self):
        label = f"{self.id} : {self.reference}[{self.value}]"
        return label


class RefidIopSecurity(models.Model):
    userid = models.CharField(primary_key=True, max_length=10)
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    apps = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refid_iop_security'

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
