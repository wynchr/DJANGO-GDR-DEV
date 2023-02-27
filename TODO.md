## <u>__Projet REFID__ </u> 
###### __Provisionnement AD/EXCHANGE__

---------------------------------------------------------------------- 
### <u> VERSION </u> 
    1.1.87  27/02/2023  CWY SQLEX='select instance from V$THREAD' for PROD
----------------------------------------------------------------------
### <u> TODO 26/02/2023 </u> 

#### _IN PROGRESS_
    - ========================================================================
    - Intégration des remarques utilisateurs & résolution des bugs fixes
        - 15/02/2023 Réunion RH que BRU
        * 10/02/2023 Réunion RH
        * 08/02/2023 Suite à la réunion IT
        * 25/01/2023 Suite à la présentation RH
        * 16/01/2023 DILEK
    - ========================================================================

    - ScriptPath = login.bat

    - Rules SWE

    - Extract csv & reload csv users

    - Change Secutiy and LD
    - Reset PSW update DB

    - Add DATEIN & DATEOUT

    - load_provad_with_new_rh (code=8)  (SQL REFID_load_new_rh_in_prov.sql)
    - load_provad_with_date_rh (code=7)
    - load_provad_with_matricule_rh (code=6)

    - Worklist NEW RH
    - Worklist NEW DATE

    - Création des accès users pour différents tests
    - Test User Access & Password

    - APScheduler as Windows Service

#### _BUG/FIX_

#### _PRIORITY CRITICAL_

#### _PRIORITY HIGH_

#### _PRIORITY NORMAL_

###### CODE
    - Comment lancer un script python à partir de django et recevoir les print dans une page
    - Please DRY this F* Code
    - Use Popups
    - Test why crispy ?
    - Call RestApi from Class View & pass JSON in context form
    - Test JSON/CRUD (DataTables Mastery)
    - Trigger Scripts from Django
    - Schema Django Logic

###### APPLICATION
    - Create Action Button on DATATABLE for DISABLE, RESETPWD ...
    - Add Button to show/hide Search in DataTable (Problem with title when exporting) 
    - Manage Page Error 500 404
    - Load REFERENCE from DB
    - Add Worklist for users (ex. Transactions in ERROR ...)
    - Document MPA explication sur les champs
    - Scheduler Enable USER with DATEIN
    - Scheduler Disable USER with DATEOUT
    - Obligation de mettre une date de fin pour certain type d'employé ???

###### DATA

###### ALGO

###### PDF

###### API
    - Use API HuMann (JPI) => DELETE interdit via l'API -> Suppression logique
    - Use API USER to sync ANNUAIRE (SWE)
    - Use API RH Information (SWE)

###### SERVICE PS

###### MONITOR
    - Add form on MONITOR page
    - Extend MONITOR finctionality

###### UTILITY
    - Add Dashboard / Stat Page
    - Execute Reprise Jobs from Admin
    - Migrate PS scripts in PYTHON (Reprises,...)

###### LDAP
    - Test script TestLdapSearch (ldap3)
    - Django LDAP login setup (https://chat.openai.com/chat#)
    - Create Ldap connection
    - Add Security Ldap (LDAP_AUTH)

###### DATABASE
    - Unique key on table
    - Install Oracle Client 19 on BRDEV01 (Get Install Procedure) => Ask ONA
    - PATCH (Waiting for Oracle Client 19)
    - Change fields for date boolean
    - Test DB Connection with custom message if DB Down !!

###### REPRISE
    - Make Checklist for REPRISE

###### CACHE Utilities

###### SECURITY
    - Use ROLE for Application

###### DEPLOYMENT
    - CheckList Deploy in PROD
    - Active PROD for Users Tests ?
    - Load on GitMann
    - Test Application on JPI server
	- Test Deploy on IIS
    - Test Deploy in Docker/Gunicorn/NGINX (Docker file) - Oracle ???

###### MANDATORY TO GO LIVE_
    - CheckList Deploy in PROD 

#### _PRIORITY LOW_
    - Create Model project Django
-----------------------------------------------------------------------
### <u> DONE </u> 
    1.1.87  27/02/2023  CWY SQLEX='select instance from V$THREAD' for PROD
    1.1.86  26/02/2023  CWY Set all script to run in DEV or PROD
    1.1.86  26/02/2023  CWY Prepare scripts for PROV_AD (copy from PROV_INIT)
    1.1.85  24/02/2023  CWY Test User Access & Password (UTF-8)
    1.1.84  23/02/2023  CWY MATRICULE not mandatory (coming from RH, INTERNEO via fetch on NISS) - Gen N°REFERENCE (ex. MATRICULE for RH, EXT- for EVIDIAN, RFI- for REFID)
    1.1.83  23/02/2023  CWY reset password with menu (service : Password reset with Passw@rdReset01()`nuser need to change password at logon) => no print
    1.1.82  23/02/2023  CWY disable, enable with menu
    1.1.81  23/02/2023  CWY Review Groups Process in Service
    1.1.81  23/02/2023  CWY test brintratest.chu-brugmann.be/Intranet/refidv1/scripts/generation_rule.php on REFGROUP_CWY
    1.1.81  23/02/2023  CWY Create a hardcoded Gestion
    1.1.80  22/02/2023  CWY Set Attribute15 to groups for ou in rules (prenvention) => ldap utils
    1.1.79  22/02/2023  CWY Display GS & DL in tabs
    1.1.78  22/02/2023  CWY GenGroupsByRules to GROUPS & DISTRIBUTIONLIST
    1.1.77  22/02/2023  CWY Add GROUPSAD & DISTRIBUTIONLISTAD
    1.1.77  21/02/2023  CWY Rename Log file   
    1.1.76  21/02/2023  CWY Get Groups and decide Insert or Append into groups
    1.1.75  21/02/2023  CWY sync REFID IOP REFADGROUPS CWY
    1.1.74  21/02/2023  CWY Reorg displat panels
    1.1.73  21/02/2023  CWY Optimize Load GS & DL in PROVINIT (Put in Dict)
    1.1.72  21/02/2023  CWY sync REFID IOP CACHE EVIDIAN
    1.1.71  19/02/2023  CWY Add GS & DL in PROVINIT
    1.1.70  18/02/2023  CWY sync REFID IOP PROVMIRROR
    1.1.69  18/02/2023  CWY Add function for NISS Validation
    1.1.69  18/02/2023  CWY Add function for NISS Validation
    1.1.68  18/02/2023  CWY in utils genuserid & check AD exists (same as NISS)
    1.1.67  18/02/2023  CWY Send mail in Django
    1.1.66  18/02/2023  CWY Add APScheduler
    1.1.65  15/02/2023  CWY Add icon to print PDF or Reset PWD
    1.1.64  15/02/2023  CWY Add mail to PDF
    1.1.63  14/02/2023  CWY Inverse  sn: usual nom   givenname: usual prenom  usualsn  : official nom : for mail,upn,displayName  usualgivenname  : officiel prenom
    1.1.62  13/02/2023  CWY Gen PDF
    1.1.61  13/02/2023  CWY Remove DEPARTEMENT Field
    1.1.60  12/02/2023  CWY Saisie automatique du nom et prénom vers le nom et prénom usuel
    1.1.59  11/02/2023  CWY Check AD when create user (on NISS)
    1.1.58  11/02/2023  CWY Arrange Scripts in specific dirs
    1.1.57  10/02/2023  CWY En Phase de Test le N°de document doit commencer par '000'
    1.1.56  09/02/2023  CWY Create LOGGING for scripts
    1.1.55  08/02/2023  CWY Gen Password  - Les caractères à exclure lors de la génération de mdp sont :  iloO10LI§£><\°|€^ 
    1.1.54  08/02/2023  CWY Add new Fields in APP & Forms EVIDIAN Tabs 
    1.1.53  06/02/2023  CWY Create RH Users
    1.1.53  06/02/2023  CWY Add EVIDIAN & AD Fields in PROVINIT
    1.1.52  04/02/2023  CWY Create & Sync all Cache & Prov in Python
    1.1.51  01/02/2023  CWY retirer ‘Chu Brugmann/Huderf’ dans le champ ‘Hopital’
    1.1.50  25/01/2023  CWY Update ToDo & ReadMe
    1.1.49  25/01/2023  CWY Add Test ClassGestionRegle
    1.1.48  23/01/2023  CWY update_provinit_ALL to Load additional data into PROVINIT_AD
    1.1.47  23/01/2023  CWY RH Hopital & CA
    1.1.46  22/01/2023  CWY Update ToDo
    1.1.45  22/01/2023  CWY Create Scripts to Correct PROVINIT_AD
    1.1.44  22/01/2023  CWY if len N°Doc = 11 CartType = NISS
    1.1.44  22/01/2023  CWY Add Generic Script & Utilities
    1.1.44  22/01/2023  CWY Correct Import DNAIS format in EVIDIAN Cache
    1.1.43  22/01/2023  CWY Script to load GENDER, BIRTHDATE in ProvAd table from EVIDIAN Cache
    1.1.43  22/01/2023  CWY Script to load RH in ProvAd table from RH Cache
    1.1.42  20/01/2023  CWY Change Cache List Layout
    1.1.41  19/01/2023  CWY Add Scripts Functions
    1.1.40  19/01/2023  CWY Add EVIDIAN Detail view
    1.1.39  19/01/2023  CWY Create page for EVIDIAN Cache 
    1.1.39  19/01/2023  CWY Create page for AD Cache 
    1.1.38  19/01/2023  CWY Create page for RH Cache
    1.1.37  19/01/2023  CWY Add all models to ADMIN
    1.1.36  19/01/2023  CWY Put CHOICES in Forms instead Models ? Quid Administration
    1.1.35  18/01/2023  CWY Add EVIDIAN Cache in ADMIN
    1.1.35  18/01/2023  CWY Add RH Cache in ADMIN
    1.1.35  18/01/2023  CWY Add AD Cache in ADMIN
    1.1.34  18/01/2023  CWY CARDTYPE = N°NISS -> Validation (len & numbersonly)
    1.1.34  18/01/2023  CWY CARDTYPE = N°xxx -> Validation (???)
    1.1.34  18/01/2023  CWY Gen USERID logic (retrieve class in HuMann API)
    1.1.33  18/01/2023  CWY SOURCE not required
    1.1.33  18/01/2023  CWY REFIF Change Table REFID_PROV_AD QUALITY, USUELSN, CARDTYPE, RH*
    1.1.33  18/01/2023  CWY Add existing GS/DL in tabs
    1.1.32  18/01/2023  CWY Add New Fields in forms
    1.1.31  18/01/2023  CWY INAMI startwith 1
    1.1.30  17/01/2023  CWY Add New Fields to model ex.RH, ...
    1.1.30  17/01/2023  CWY Create New Fields in PROVAD (inverse psw & name)
    1.1.30  17/01/2023  CWY birthday => birthdate
    1.1.29  17/01/2023  CWY Arrange INFO-IAM INFO-REFID
    1.1.28  16/01/2023  CWY Put Check/Regex fields in clean_*
    1.1.28  16/01/2023  CWY RECHERCHE par nom, prénom, NISS et numéro de document
    1.1.28  16/01/2023  CWY Sexe => genre, Widget Date Entry
    1.1.27  16/01/2023  CWY Problem with Date Widget Format on some computer => Regional Settings
    1.1.26  15/01/2023  CWY Refactor info html & todo
    1.1.25  15/01/2023  CWY Create Tab Securite & Distribution, Add Utility Page, Add Cache View menu
    1.1.24  15/01/2023  CWY Add Utility Page
    1.1.24  15/01/2023  CWY Create Tab Securite & Distribution
    1.1.24  15/01/2023  CWY ChatOpenAi - Django listview searchmixin with form sample
    1.1.23  15/01/2023  CWY Add Tab IDENTITE, SECURITE, DISTRIBUTION
    1.1.22  14/01/2023  CWY Create Search on home page
    1.1.21  14/01/2023  CWY Arrange url & views
    1.1.21  14/01/2023  CWY Change title in pages
    1.1.21  14/01/2023  CWY Change buttons in forms
    1.1.20  14/01/2023  CWY Secure TESTS App
    1.1.19  13/01/2023  CWY Menu Monitoring with Dropdown
    1.1.19  13/01/2023  CWY Valid Name 'Only letters are allowed.'
    1.1.19  13/01/2023  CWY Login Info next Logout Button  
    1.1.18  13/01/2023  CWY Update genuserid 5+2
    1.1.18  13/01/2023  CWY Add RepriseInit Model, Form, Pages
    1.1.17  13/01/2023  CWY Change Login Page
    1.1.16  13/01/2023  CWY Adjust label on crispy form CSS
    1.1.16  13/01/2023  CWY Filter Access on SuperUser or Staff
    1.1.15  12/01/2023  CWY Change Service HTML Mail Layout
    1.1.14  12/01/2023  CWY Creation Problem
    1.1.14  12/01/2023  CWY Logout Automatic settimeout at 15'
    1.1.14  12/01/2023  CWY Install App on BRDEV01 for testing
    1.1.13  12/01/2023  CWY Create Utils Library
    1.1.12  11/01/2023  CWY Validation fields, Password processing @ creation
    1.1.11  11/01/2023  CWY Problem in Services with Date Expiration - Flag OK & no date
    1.1.10  11/01/2023  CWY Add comments via models 
    1.1.09  11/01/2023  CWY New Datatable (YT)
    1.1.09  11/01/2023  CWY Create Login form
    1.1.08  08/01/2023  CWY Reload Page
    1.1.08  08/01/2023  CWY Test Crispy (YT)
    1.1.07  07/01/2023  CWY Add Tabs
    1.1.07  07/01/2023  CWY Use custom forms
    1.1.07  07/01/2023  CWY Create Templates/Forms (Wireframe definition)
    1.1.06  05/01/2023  CWY Rendering fields manually
    1.1.06  04/01/2023  CWY Arrange settings
    1.1.06  04/01/2023  CWY Use .env for settings
    1.1.06  04/01/2023  CWY Delete _ in Class name
    1.1.05  28/12/2022  CWY Redefine ADMIN views
    1.1.05  28/12/2022  CWY python3 manage.py runserver 0.0.0.0:8000
    1.1.04  26/12/2022  CWY Sync Version with Git
    1.1.04  26/12/2022  CWY Copy Forms & View into _SAVE folder
    1.1.04  26/12/2022  CWY Rename Forms & Views
    1.1.03  24/12/2022  CWY Add CBV & CRUD
    1.1.02  15/04/2022  CWY HTML5 datatable 
    1.1.02  15/04/2022  CWY datatables tests
    1.1.01  05/04/2022  CWY Create Header & Footer
    1.1.01  05/04/2022  CWY Create BootStrap 5 design
    1.1.01  05/04/2022  CWY Create Project Structure
    1.1.01  05/04/2022  CWY Create environment base/dev/prod
    1.1.01  05/04/2022  CWY Create security files in json (credentials)
    1.1.01  05/04/2022  CWY Create GitHub repository
    1.1.01  05/04/2022  CWY Create Oracle connection
----------------------------------------------------------------------
#### _USERS TESTS_
##### Intégration des remarques utilisateurs
    - Document MPA explication sur les champs
    - Dilek centralise les demandes utilisateurs


###### 15/02/2023 Réunion RH que BRU

    -	Création des accès users pour différents tests:

        o	Front Office
            Roijer Caherine (roicat)
            Xhrouet Manon (xhrouem)
        
        o	Cellule médecin
            Goffart Arnaud (goffaar)
            Niyodushima Marc (niyodum)
            Couvreur Joelle (cojoell)
            Ndeye Severine (ndeysev)
        
        o	Cellule non médical
            Alaime Nathalie (alanat)
            Vyncke Genevieve (vyngen)
            Ramdoo Melissa (rammel)
            Michiels Pascal (micpas)
            El Moustakim Leyla (elmlay)

    *	Lors de la génération du pdf :
        o	Ajouter l’adresse mail avec les données usuelles
        o	Corriger le document en ndls : faute de frappe au mot ‘round’ à modifier en ‘rond’

    -	Dans le champ ‘ Type’, il faudra vérifier ton check car certains users ont des inamis autres que médical => peut générer des problèmes lors de la reprises Arno.
    Cela peut être infirmier, paramédical, … 

    *	Eclaircir le champ Hôpital ‘Brustp’, est-ce qu’il faut maintenir ou supprimer.
        Cela est-il nécessaire ? À voir avec Marc P.

    *	Je dois mettre à jour la procédure avec la partie ‘génération du pdf’ + traduction ndls 


###### 10/02/2023 Réunion RH

    * Une nouvelle catégorie « médecin sans inami » afin que l’inami ne soit pas obligatoire à l’encodage
    * Retirer la zone departement (obsolète)
    * Il faudra prévoir la synchronisation des dates de sortie, 
        et des prolongations pour le moment il y a des tâches qui tourne sur evidian (idsynch ou autre ??)
    * Pour voir aller récupérer les données d’arno et les injecter dans le formulaire. 
            Au fait certaines personnes qui ne trouver pas dans la recherche la personne , 
            passer par la cache « arno » est pensé qu’il y avait un bouton pour pouvoir importer les données dans le formulaire.
            Est-il possible d’ajouter dans le formulaire d’encodage au-dessus une zone recherche matricule , ou la personne peut rechercher le matricule. On appelle une requête arno et on récupère un json des données que l’on met dans le formulaire
            On peut faire un appel javascript Ou alors dès la première page, pouvoir inclure la recherche arno , je le fais par exemple dans le dsi
            Je recherche dans le dsi même et avec un union je recherche dans wish,  
            et si le dossier n’est pas présent , je fais importer les données  de wish dans le dsi. 
            Je ne suis pas encore familière avec django, mais c’est possible ou non ?

    * Dans la table de prov sur la dev, les lignes sont en double lors de la création,
        hier on a tester avec un zz et un vrai niss(le mien) et on est passé sans problème,
        la création dans la base de donnée et dans l’ad .
        Tu as désactivé les contrôles ? 
        Il faudrait rajouter des contraintes d’intégrité dans la db, comme ça on aura déjà moins de souci
        •	Samaccountname primary key
        •	Inami unique key
        •	Matricule unique key
        •	Niss unique key



###### 08/02/2023 Réunion IT 

    * Le n° de matricule.  
        Celui-ci est généré automatiquement par Arno.  
        Christian l’a donc mis comme champs obligatoire dans le Plan B mais est-ce réellement obligatoire étant donné que ce n° n’a aucune interaction avec les applis IT
        Décision est prise de maintenir ce champs obligatoire car cela aura peut-être, plus tard, une incidence avec Interneo.  Dans le futur, ce champs sera une source externe
    
    * Faut-il maintenir le champs « Département » étant donné qu’il n’est pas obligatoire ?  
        Marc vT propose de ne pas trop perturber les RH et de maintenir ce qui existe aujourd’hui avec Evidian et donc laisser ce champs même si celui-ci n’est pas obligatoire.  Marc P précise qu’il faudra y ajouter « HUB ».  Christian rappelle que ce champs ne représente pas la localisation physique de l’utilisateur 
    
    * Le champs « Genre » doit-il être modifié étant donné que Christian n’a précisé que « Féminin » / « Masculin ». 
        Marc vT décide de laisser cela tel quel sachant que la carte d’identité ne reprend également que ces 2 possibilités
    
    * Dans le champs « Type », si on opte pour « Médical », le n° Inami doit alors être obligatoirement complété.  
        Marc P fera parvenir à Christian la liste des autres métiers qui nécessitent un n° Inami (Sage-femme, kiné, logopède, …) afin de l’ajouter dans le Plan B
    
    * Génération des login & mot de passe : on garde le même principe qu’Evidian.  
        Marc vT décide que ce soit Sara qui finalise le pdf qui générera automatiquement le login & mot de passe.  
        Cela devrait prendre ½ jour, 1 jour max.  
        Lors de l’envoi du lien pour la phase test, Sabrina précisera aux « testeurs » que les tests de cette semaine n’auront pas encore ce pdf mais lors de la phase test de la semaine prochaine, ce sera en ordre.  Ce pdf sera envoyé sur la boîte mail partagée déjà existante
    
    * L’encodage d’une date de fin : 
        les RH demandent s’il est nécessaire d’encore le préciser.
        Christian relève que sur 9082 utilisateurs, seules 20 personnes ont une date de fin.  
        Ce champs est donc maintenu mais sans obligation de le compléter
    
    * Les RH ont également demandé que la date de fin = date de fin avec J+1 => 
        Christian fera la même chose dans le Plan B

    * Document MPA explication sur les champs

###### 25/01/2023 Réunion RH - Suite à la présentation

    *	A retirer ‘Chu Brugmann/Huderf’ dans le champ ‘Hopital’
    *	N° matricule : se basé s/ n° RH
        o	Ext + n° incrémentale
        o	Cfr Extended attribut 1
    *	Ajouter un Flag ‘Création Mailbox’
    *	Suppression de la visibilité du mdp dans la DB + encryptions
        o	Monitoring\Monitor => suppression de la visibilité du mdp
    *	Dans le champ Mail, accès ne doit pas être éditable 
        o	Le mail doit être identique à ‘prénom usuel’ et ‘nom usuel’
        o	Le mail doit être créé en caractère minuscule
    *	Arno : Vérifier le type => à faire par Sarah
    *	Localisation => laisser accessible
    *	Création d’1 icône qui permettra de copier les donnée d’arno vers Compte User



###### 16/01/2023 DILEK
        * RECHERCHE par nom, prénom, NISS et numéro de document
            . La recherche par Niss ne fonctionne pas ( pas de champ 'numéro de document') 

        * DATA Qualité, Nom officiel, Prénom officiel, Nom usuel, Nom et Prénom usuel validé, Prénom usuel,
                Sexe, Langue, Type de document, N° Document, Catégorie professionnelle
            . Qualité(Mme,Mr,Dr,...),'nom officiel', 'prénom officiel',… pas encore développés dans cette version

        * NOM (Minimum 1 caractère) 
            . Impossible de tester uniquement avec 1 caractère car dans la version de test une protection d'encodage
                qui doit commencer par ZZ

        * PRENOM (Minimum 1 caractère) 
            . Demande d'introduire minimum 3 caractères

        * GENRE 
            . Doit-on garder 'Autre'

        * DNAIS 
            . Autoriser l'encodage via le pavé numérique et pas uniquement via l'icône calendrier. 
                Pas de check d'âge limite.

        * HOPITAL 
            . Lorsqu'on choisit Huderf, le champs site doit être inaccessible

        * CATEGORIE 
            . A revoir le contenu. Mettre par ordre alphabétique. Utiliser la même 'CASE'

        * N°MATRICULE 
            . On se base sur quelle info pour le matricule? 

        * N°NISS (EID ou n°DOCUMENT) N°Niss devrait avoir un choix entre Eid ou n°de document. 
            Selon le choix, faire un check sur le nombre de caractères pour le EID
            . Si Eid, les lettres ne doivent pas être acceptées

        * N°INAMI 
            . Les tirets ne sont pas acceptés. Check sur 11 chiffres :OK

        * TELEPHONE (Acceptation uniquement des chiffres et le '/') 
            . Accepte les lettres. 

        * PORTABLE (Acceptation uniquement des chiffres et le '/') 
            . Accepte les lettres. A introduire quel numéro de téléphone, Privé, perso?
----------------------------------------------------------------------
### _PATCH (Waiting for Oracle Client 19)_

#####  D:\DEV\DJANGO-GDR\.env\Lib\site-packages\django\db\backends\base\base.py

    def check_database_version_supported(self):
        """
        Raise an error if the database version isn't supported by this
        version of Django.
        """
        if (
            self.features.minimum_database_version is not None
            and self.get_database_version() < self.features.minimum_database_version
        ):
            db_version = ".".join(map(str, self.get_database_version()))
            min_db_version = ".".join(map(str, self.features.minimum_database_version))
            # raise NotSupportedError(
            #     f"{self.display_name} {min_db_version} or later is required "
            #     f"(found {db_version}).

----------------------------------------------------------------------
