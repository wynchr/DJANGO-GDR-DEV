## <u>__Projet REFID__ </u> 
###### __Provisionnement AD/EXCHANGE__

----------------------------------------------------------------------
### _LINKS TO APPLICATION_ 

_Home_ [Link](http://127.0.0.1:8000/)

_Application_ [Link](http://127.0.0.1:8000/refid/application)

_Monitoring_ [Link](http://127.0.0.1:8000/refid/monitor-list-view)

_Administration_ [Link](http://127.0.0.1:8000/gdr-admin)


----------------------------------------------------------------------
### _RULES TO ATTRIBUTE SECURITY GROUPS AND DISTIBUTION LIST_ 
|GROUPCATEGORY|INSTITUTION|SITE|EMPLOYEETYPE|SAMACCOUNTNAME|DISTINGUISHEDNAME|
|-------------|-----------|----|------------|--------------|-----------------|
|Distribution|CHU-BRUGMANN|ASTRID|ADMINISTRATIF|Tout le PATO de Reine Astrid|CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Distribution|CHU-BRUGMANN|ASTRID|OTHER|Tout le PATO de Reine Astrid|CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Distribution|CHU-BRUGMANN|ASTRID|PARAMEDICAL|Tout le PATO de Reine Astrid|CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Distribution|CHU-BRUGMANN|ASTRID|TECHNIQUE|Tout le PATO de Reine Astrid|CN=Tout le PATO de Reine Astrid,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Distribution|CHU-BRUGMANN|BRIEN|ADMINISTRATIF|Tout le PATO de Brien|CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Distribution|CHU-BRUGMANN|BRIEN|OTHER|Tout le PATO de Brien|CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Distribution|CHU-BRUGMANN|BRIEN|PARAMEDICAL|Tout le PATO de Brien|CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Distribution|CHU-BRUGMANN|BRIEN|TECHNIQUE|Tout le PATO de Brien|CN=Tout le PATO de Brien,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|-|MEDICAL|OSIRIS - MVSL - Medical|CN=OSIRIS - MVSL - Medical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|-|MEDICAL|Tous les medecins de Brugmann|CN=Tous les medecins de Brugmann,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|-|MEDICAL|Wireless Users|CN=Wireless Users,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|-|NURSING|OSIRIS - MVSL - Nursing|CN=OSIRIS - MVSL - Nursing,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|-|PARAMEDICAL|OSIRIS - MVSL - Paramedical|CN=OSIRIS - MVSL - Paramedical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|ASTRID|MEDICAL|Tous les medecins de Brugmann|CN=Tous les medecins de Brugmann,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|ASTRID|MEDICAL|Tout le nursing de Reine Astrid|CN=Tout le nursing de Reine Astrid,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|ASTRID|NURSING|Tout le nursing de Reine Astrid|CN=Tout le nursing de Reine Astrid,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|BRIEN|MEDICAL|Tous les medecins de Brien|CN=Tous les medecins de Brien,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|BRIEN|NURSING|Tout le nursing de Brien|CN=Tout le nursing de Brien,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|HORTA|ADMINISTRATIF|Tout le PATO de Horta|CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|HORTA|MEDICAL|Tous les medecins de Horta|CN=Tous les medecins de Horta,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|HORTA|NURSING|Tout le nursing de Horta|CN=Tout le nursing de Horta,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|HORTA|OTHER|Tout le PATO de Horta|CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|HORTA|PARAMEDICAL|Tout le PATO de Horta|CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|CHU-BRUGMANN|HORTA|TECHNIQUE|Tout le PATO de Horta|CN=Tout le PATO de Horta,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|ADMINISTRATIF|Tout le PATO de l Huderf|CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|MEDICAL|OSIRIS - MVSL - Medical|CN=OSIRIS - MVSL - Medical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|MEDICAL|Tous les medecins de l Huderf|CN=Tous les medecins de l Huderf,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|MEDICAL|Wireless Users|CN=Wireless Users,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|NURSING|OSIRIS - MVSL - Nursing|CN=OSIRIS - MVSL - Nursing,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|NURSING|Tout le nursing de l Huderf|CN=Tout le nursing de l Huderf,OU=Security,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|OTHER|Tout le PATO de l Huderf|CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|PARAMEDICAL|OSIRIS - MVSL - Paramedical|CN=OSIRIS - MVSL - Paramedical,OU=MedicalViewerSilverLight,OU=Applications,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|PARAMEDICAL|Tout le PATO de l Huderf|CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|
|Security|HUDERF|-|TECHNIQUE|Tout le PATO de l Huderf|CN=Tout le PATO de l Huderf,OU=Distribution,OU=Groups,OU=OSIRIS,DC=chu-brugmann,DC=be|

----------------------------------------------------------------------
### _MODEL - RefidIopProvAd_

    samaccountname

    sn
    givenname
    +usualsn
    +usualgivenname


    company
    physicaldeliveryofficename 
    department

    businesscategory 
    employeetype

    +quality

    preferredlanguage 
    gender 
    birthdate 

    +cardtype
    employeenumber
    extensionattribute1
    ----extensionattribute2
    extensionattribute11 

    telephonenumber 
    pager
    +localisation

    roles 
    unites 
    specialites 

    homedir
    homedrive 

    description
    info 
    extensionattribute15 
    metadata 

    enableaccountexpires
    accountexpires 
    changepasswordatlogon
    enabled
    enablemail
    mail 

    groups 
    distributionlist 

    env
    org
    +src

    usercre
    datecre
    userupd
    dateupd 

    msgrefid
    actiontype
    msgdb 

    msgad
    datesyncad
    flagsyncad

    msgexchange 
    datesyncexchange 
    flagsyncexchange 

    password 

    objectsid
    objectguid

    +rhmatricule 
    +rhnom 
    +rhprenom 

    +rhsexe 
    +rhdnais
    +rhlangue 

    +rhnumcardid 
    +rhnumnational

    +rhdatedeb 
    +rhdatefin

    +rhstatutcontrat 

    +rhcodesociete
    +rhcodeprofil
    +rhprofil
    +rhcaqualification 
    +rhcacode 
    +rhcalib
    +rhinami

    +rhmetadata 

----------------------------------------------------------------------
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

    QUALITY_CHOICES = (
        ("Mr.", "Monsieur"),
        ("Mme.", "Madame"),
        ("Dr.", "Docteur"),
        ("Prf.", "Professeur"),
        ("Ir.", "Ingénieur"),
    )

    GENDER_CHOICES = (
        ("M", "Masculin"),
        ("F", "Féminin"),
    )

    CARDTYPE_CHOICES = (
        ("EID", "Carte d'indentité"),
        ("EIDbis", "Carte d'indentité Bis"),
        ("PASSPORT", "Passport"),
        ("AUTRES", "Autres"),
    )

    SRC_CHOICES = (
        ("RH", "RH"),
        ("INTERNEO", "INTERNEO"),
        ("REFID", "REFID"),
        ("AUTRES", "Autres"),
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
----------------------------------------------------------------------
### _ENVIRONMENT DEFINITION MODEL (.env)_

    ENV='DEV'
    
    SECRET_KEY='django-insecure-***'
    DEBUG=True
    ALLOWED_HOSTS='127.0.0.1'
    
    DB_ENGINE='django.db.backends.oracle'
    DB_NAME='INTRDV'
    DB_HOST='polonium.chu-brugmann.be'
    DB_PORT='1521'
    DB_SERVICE_NAME='INTRDV.chu-brugmann.be'
    DB_ENCODING='UTF-8'
    DB_USER='***'
    DB_PASSWORD='***'

    LDAP_HOST='helium.chu-brugmann.be'
    LDAP_USER='AdminLDAP'
    LDAP_PWD='***'
    LDAP_SEARCHBASE='OU=REFID,OU=Users,OU=TESTOSIRIS,DC=chu-brugmann,DC=be'
    LDAP_ATTRIBUTES=['objectGUID',
                        'objectSID',
                        'distinguishedName',
                        'sAMAccountName',
                        'sn',
                        'givenName',
                        'cn',
                        'name',
                        'displayName',
                        'userPrincipalName',
                        'extensionAttribute1',
                        'extensionAttribute2',
                        'extensionAttribute10',
                        'extensionAttribute11',
                        'employeeID',
                        'employeeNumber',
                        'preferredLanguage',
                        'company',
                        'physicalDeliveryOfficeName',
                        'employeeType',
                        'BusinessCategory',
                        'department',
                        'telephoneNumber',
                        'pager',
                        'info',
                        'mail',
                        'homeDirectory',
                        'homeDrive',
                        'msExchWhenMailboxCreated',
                        'whenCreated',
                        'whenchanged',
                        'LastLogon',
                        'LastLogonTimeStamp',
                        'pwdLastSet',
                        'accountExpires',
                        'description',
                        'enabled',
                        'MemberOf']

----------------------------------------------------------------------
---
ENVIRONMENT:
  TYPE: "TEST"
  DEBUG: true
  DATABASE-IT:
    DBMS: Oracle
    VERSION: Unknown
    HOST: ""
    SERVICE: ""
    PORT: "1521"
    CLIENT:
      PATH: "\\instantclient_21_6"
    CREDENTIAL:
      USERNAME: ""
      PASSWORD: ""
  DATABASE-RH:
    DBMS: Oracle
    VERSION: Unknown
    HOST: ""
    SERVICE: ""
    PORT: 1521
    CLIENT:
      PATH: "C:/HOME/ORACLE/instantclient_21_7"
    CREDENTIAL:
      USERNAME: ""
      PASSWORD: ""
    LDAP:
      SOFTWARE: Microsoft Active Directoy
      SERVER_ADDRESS: ''
      HOST: ''
      DOMAIN: ''
      BASEDN: ''
      USER: ''
      PWD: ''
----------------------------------------------------------------------