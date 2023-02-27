"""
=======================================================================================================================
.DESCRIPTION
    Forms for REFID Application

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS

=======================================================================================================================
"""
from django import forms
from django.shortcuts import render
from django.views.generic import FormView

from django.utils.safestring import mark_safe
import markdown


# from GDR import settings
from .models import RefidIopProvAd, RefidIopProvInitAd

from utils import utils
from utils import ldap
from utils.utils import check_niss


# =========================================================================================================
# APPLICATION Forms
# =========================================================================================================

# ProvAd ==========

# samaccountname
#
# sn
# givenname
# usualsn
# usualgivenname
#
# company
# physicaldeliveryofficename
# department
#
# businesscategory
# employeetype
#
# quality
#
# preferredlanguage
# gender
# birthdate
#
# cardtype
# employeenumber
# extensionattribute1
# extensionattribute2
# extensionattribute11
#
# telephonenumber
# pager
# localisation
#
# roles
# unites
# specialites
#
# homedir
# homedrive
#
# description
# info
# extensionattribute15
# metadata
#
# enableaccountexpires
# accountexpires
# changepasswordatlogon
# enabled
# enablemail
# mail
#
# groups
# distributionlist

# groupsad
# distributionlistad
#
# env
# org
# src
#
# usercre
# datecre
# userupd
# dateupd
#
# msgrefid
# actiontype
# msgdb
#
# msgad
# datesyncad
# flagsyncad
#
# msgexchange
# datesyncexchange
# flagsyncexchange
#
# password
#
# objectsid
# objectguid

# whencreated
# whenchanged
# lastlogontimestamp
# lastlogon
# pwdlastset
# badpasswordtime
# msexchwhenmailboxcreated
#
# chuidoriginsource
# evdidmstate
# evdpmschedulerstatus
# enatelbegintime
# enatelendtime

# rhmatricule
# rhnom
# rhprenom
# rhsexe
# rhdnais
# rhlangue
# rhnumcardid
# rhnumnational
# rhdatedeb
# rhdatefin
# rhstatutcontrat

# rhcodesociete
# rhcodeprofil
# rhprofil
# rhcaqualification
# rhcacode
# rhcalib
# rhinami

# rhmetadata

# rfidatesync
# messages


class RefidIopProvAdCreateForm(forms.ModelForm):
    mode = 'create'

    class Meta:
        model = RefidIopProvAd

        fields = [
            "samaccountname",
            "sn",
            "givenname",
            "usualsn",
            "usualgivenname",
            "company",
            "physicaldeliveryofficename",
            "department",
            "businesscategory",
            "employeetype",
            "preferredlanguage",
            "quality",
            "gender",
            "birthdate",
            "cardtype",
            "employeenumber",
            "extensionattribute1",
            "extensionattribute2",
            "extensionattribute11",
            "telephonenumber",
            "pager",
            "localisation",
            "roles",
            "unites",
            "specialites",
            "homedir",
            "homedrive",
            "description",
            "info",
            "extensionattribute15",
            "metadata",
            "enableaccountexpires",
            "accountexpires",
            "changepasswordatlogon",
            "enabled",
            "enablemail",
            "mail",
            "groups",
            "distributionlist",
            "groupsad",
            "distributionlistad",
            "env",
            "org",
            "src",
            "usercre",
            "datecre",
            "userupd",
            "dateupd",
            "msgrefid",
            "actiontype",
            "msgdb",
            "msgad",
            "datesyncad",
            "flagsyncad",
            "msgexchange",
            "datesyncexchange",
            "flagsyncexchange",
            "password",
            "objectsid",
            "objectguid",
            "whencreated",
            "whenchanged",
            "lastlogontimestamp",
            "lastlogon",
            "pwdlastset",
            "badpasswordtime",
            "msexchwhenmailboxcreated",
            "chuidoriginsource",
            "evdidmstate",
            "evdpmschedulerstatus",
            "enatelbegintime",
            "enatelendtime",
            "rhmatricule",
            "rhnom",
            "rhprenom",
            "rhsexe",
            "rhdnais",
            "rhlangue",
            "rhnumcardid",
            "rhnumnational",
            "rhdatedeb",
            "rhdatefin",
            "rhstatutcontrat",
            "rhcodesociete",
            "rhcodeprofil",
            "rhprofil",
            "rhcaqualification",
            "rhcacode",
            "rhcalib",
            "rhinami",
            "rhmetadata",
            "rfidatesync",
            "messages",
        ]

        exclude = ["roles", "unites", "specialites"]

        labels = {
            "samaccountname": "USERID",
            "sn": "NOM OFFICIEL *",
            "givenname": "PRENOM OFFICIEL *",
            "usualsn": "NOM USUEL *",
            "usualgivenname": "PRENOM USUEL *",
            "company": "HOPITAL *",
            "physicaldeliveryofficename": "SITE *",
            "department": "DEPARTEMENT",
            "businesscategory": "CATEGORIE *",
            "employeetype": "TYPE *",
            "quality": "QUALITE *",
            "preferredlanguage": "LANGUE *",
            "gender": "GENRE *",
            "birthdate": "DATE DE NAISSANCE",
            "cardtype": "TYPE DE DOCUMENT *",
            "employeenumber": "N°DOCUMENT *",
            "extensionattribute1": "N°MATRICULE/REFERENCE",
            "extensionattribute2": "MOUVEMENT",
            "extensionattribute11": "N°INAMI",
            "telephonenumber": "TELEPHONE",
            "pager": "PORTABLE",
            "localisation": "LOCALISATION",
            "roles": "ROLES",
            "unites": "UNITES",
            "specialites": "SPECIALITES",
            "homedir": "HOME DIRECTORY *",
            "homedrive": "HOME DRIVE *",
            "description": "DESCRIPTION",
            "info": "INFO IAM *",
            "extensionattribute15": "INFO REFID *",
            "metadata": "METADATA",
            "enableaccountexpires": "DATE D'EXPIRATION ACTIVE",
            "accountexpires": "DATE D'EXPIRATION",
            "changepasswordatlogon": "CHANGE PSW @LOGON",
            "enabled": "COMPTE ACTIF",
            "enablemail": "MAIL ACTIF *",
            "mail": "MAIL *",
            "groups": "GROUPES DE SECURITE",
            "distributionlist": "LISTES DE DISTRIBUTION",
            "groupsad": "GROUPES DE SECURITE AD",
            "distributionlistad": "LISTES DE DISTRIBUTION AD",
            "env": "ENVIRONNEMENT *",
            "org": "ORGANISATION *",
            "src": "SOURCE *",
            "usercre": "USER CREATE",
            "datecre": "DATE CREATE",
            "userupd": "USER UPDATE",
            "dateupd": "DATE UPDATE",
            "msgrefid": "MSG REFID",
            "actiontype": "ACTION TYPE *",
            "msgdb": "MSG DB",
            "msgad": "RETURN CODE AD",
            "datesyncad": "DATE SYNC AD",
            "flagsyncad": "STATE AD *",
            "msgexchange": "RETURN CODE EXCHANGE",
            "datesyncexchange": "DATE SYNC EXCHANGE",
            "flagsyncexchange": "STATE EXCHANGE *",
            "password": "PASSWORD *",
            "objectsid": "AD OBJECT SID",
            "objectguid": "AD OBJECT GUID",
            "whencreated": "AD WHEN CREATED",
            "whenchanged": "AD AD WHEN CHANGED",
            "lastlogontimestamp": "AD LAST LOGON TIMESTAMP",
            "lastlogon": "AD LAST LOGON",
            "pwdlastset": "AD PWD LAST SET",
            "badpasswordtime": "AD BAD PASSWORD TIME",
            "msexchwhenmailboxcreated": "AD EXCHANGE MAIL CREATED",
            "chuidoriginsource": "EVIDIAN SOURCE",
            "evdidmstate": "EVIDIAN STATE",
            "evdpmschedulerstatus": "EVIDIAN SCHEDULER STATUS",
            "enatelbegintime": "EVIDIAN BEGIN TIME",
            "enatelendtime": "EVIDIAN END TIME",
            "rhmatricule": "MATRICULE (RH)",
            "rhnom": "NOM (RH)",
            "rhprenom": "PRENOM (RH)",
            "rhsexe": "SEXE (RH)",
            "rhdnais": "DATE DE NAISSANCE (RH)",
            "rhlangue": "LANGUE (RH)",
            "rhnumcardid": "N°CARTE ID (RH)",
            "rhnumnational": "N°NATIONAL (RH)",
            "rhdatedeb": "DATE DE DEBUT (RH)",
            "rhdatefin": "DATE DE FIN (RH)",
            "rhstatutcontrat": "STATUT CONTRAT (RH)",
            "rhcodesociete": "HOPITAL (RH)",
            "rhcodeprofil": "PROFIL CODE(RH)",
            "rhprofil": "PROFIL (RH)",
            "rhcaqualification": "CA QUALIFICATION (RH)",
            "rhcacode": "CA CODE (RH)",
            "rhcalib": "CA LIB (RH)",
            "rhinami": "INAMI (RH)",
            "rhmetadata": "METADATA (RH)",
            "rfidatesync": "DATE SYNC REFID",
            "messages": "MESSAGE REFID",
        }

        widgets = {
            "samaccountname": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),

            "sn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "givenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualsn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualgivenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "company": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "physicaldeliveryofficename": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "department": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "businesscategory": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeetype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "quality": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "preferredlanguage": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "gender": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "birthdate": forms.DateInput(attrs={
                'type': 'date',
                'data-provide': 'datepicker',
                'min': '1900-01-01',
                'max': '2031-12-31'},),

            "cardtype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'readonly': 'readonly'}),

            "extensionattribute2": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute11": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "telephonenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "pager": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "localisation": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "description": forms.Textarea(attrs={'class': 'form-text', 'cols': 50, 'rows': 2}),

            "enableaccountexpires": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            'accountexpires': forms.DateInput(attrs={
                    'type': 'date',
                    'onkeydown': 'return false',
                    'min': '2020-01-01',
                    'max': '2031-12-31'}),

            # comment in create ?
            "changepasswordatlogon": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "enabled": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "enablemail": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),
            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groups": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlist": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groupsad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlistad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "homedir": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "homedrive": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "info": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute15": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "metadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "env": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "org": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "src": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "usercre": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "datecre": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "userupd": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "dateupd": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "msgrefid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msgdb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "actiontype": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncad": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncexchange": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "objectsid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "objectguid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "whencreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "whenchanged": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogontimestamp": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogon": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "pwdlastset": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "badpasswordtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msexchwhenmailboxcreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "chuidoriginsource": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdidmstate": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdpmschedulerstatus": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelbegintime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelendtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmatricule": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprenom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhsexe": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdnais": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhlangue": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumcardid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumnational": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatedeb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatefin": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhstatutcontrat": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhcodesociete": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcodeprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcaqualification": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcacode": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcalib": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhinami": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmetadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rfidatesync": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "messages": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            # READ-ONLY for CREATE
            "password": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),
        }

    # validation au niveau du serveur

    def clean_samaccountname(self):
        samaccountname = self.cleaned_data.get('samaccountname')
        return samaccountname

    def clean_sn(self):
        sn = self.cleaned_data.get("sn")
        if sn == "":
            raise forms.ValidationError("le nom est obligatoire.")
        if utils.check_regex('letters', sn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if sn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom doit commencer par ZZ.")
        if len(sn) < 3:
            raise forms.ValidationError("Le nom doit avoir au moins 3 lettres.")
        return sn

    def clean_givenname(self):
        givenname = self.cleaned_data.get("givenname")
        if givenname == "":
            raise forms.ValidationError("le prénom est obligatoire.")
        if utils.check_regex('letters', givenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(givenname) < 1:
            raise forms.ValidationError(
                "Le prénom doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return givenname

    def clean_usualsn(self):
        usualsn = self.cleaned_data.get("usualsn")
        if usualsn == "":
            raise forms.ValidationError("le nom usuel est obligatoire.")
        if utils.check_regex('letters', usualsn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if usualsn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom usuel doit commencer par ZZ.")
        if len(usualsn) < 3:
            raise forms.ValidationError("Le nom usuel doit avoir au moins 3 lettres.")
        return usualsn

    def clean_usualgivenname(self):
        usualgivenname = self.cleaned_data.get("usualgivenname")
        if usualgivenname == "":
            raise forms.ValidationError("le prénom usuel est obligatoire.")
        if utils.check_regex('letters', usualgivenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(usualgivenname) < 1:
            raise forms.ValidationError(
                "Le prénom usuel doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return usualgivenname

    def clean_quality(self):
        quality = self.cleaned_data.get("quality")
        if quality is None:
            raise forms.ValidationError("la qualité est obligatoire.")
        return quality

    def clean_preferredlanguage(self):
        preferredlanguage = self.cleaned_data.get("preferredlanguage")
        if preferredlanguage is None:
            raise forms.ValidationError("la langue est obligatoire.")
        return preferredlanguage

    def clean_gender(self):
        gender = self.cleaned_data.get("gender")
        if gender is None:
            raise forms.ValidationError("le genre est obligatoire.")
        return gender

    def clean_company(self):
        company = self.cleaned_data.get("company")
        if company is None:
            raise forms.ValidationError("l'hôpital est obligatoire.")
        return company

    def clean_physicaldeliveryofficename(self):
        physicaldeliveryofficename = self.cleaned_data.get("physicaldeliveryofficename")
        company = self.cleaned_data.get("company")
        if physicaldeliveryofficename is None and company != 'Huderf':
            raise forms.ValidationError("le site est obligatoire.")
        return physicaldeliveryofficename

    def clean_businesscategory(self):
        businesscategory = self.cleaned_data.get("businesscategory")
        if businesscategory is None:
            raise forms.ValidationError("la catégorie est obligatoire.")
        return businesscategory

    def clean_employeetype(self):
        employeetype = self.cleaned_data.get("employeetype")
        if employeetype is None:
            raise forms.ValidationError("la type de personnel est obligatoire.")
        return employeetype

    def clean_cardtype(self):
        cardtype = self.cleaned_data.get("cardtype")
        if cardtype is None:
            raise forms.ValidationError("le type de document est obligatoire.")
        return cardtype

    def clean_employeenumber(self):
        # La structure du NISS est la suivante : AAMMJJ-sss-NC
        #
        # AA = année de naissance
        # MM = mois de naissance (augmenté de 20 ou 40 pour les numéros bis)
        # JJ = jour de naissance
        # sss = numéro de suite renseignant en dernière position le sexe (impair pour les hommes, pair pour les femmes)
        # NC = nombre de contrôle

        employeenumber = self.cleaned_data.get("employeenumber")
        cardtype = self.cleaned_data.get("cardtype")
        samaccountname = self.cleaned_data.get("samaccountname")

        if employeenumber == "":
            raise forms.ValidationError("le N°DOCUMENT est obligatoire.")

        # if employeenumber[0:3] != '000':
        #     raise forms.ValidationError("En Phase de Test le N°de document doit commencer par '000'.")

        if cardtype == 'NISS':
            # if utils.check_regex('numbers', employeenumber) is False:
            #     raise forms.ValidationError("Seul les chiffres sont permis.")
            # if len(employeenumber) != 11:
            #     raise forms.ValidationError("le N°NISS doit avoir 11 caractères.")
            if not check_niss(employeenumber):
                raise forms.ValidationError("le N°NISS n'est pas correct.")

        if employeenumber and self.mode == 'create':
            qs = RefidIopProvAd.objects.filter(employeenumber=employeenumber).values()
            if qs.exists():
                print(f"\nUser {employeenumber.upper()} exists")
                raise forms.ValidationError("Le N°NISS existe déjà")

        if employeenumber:
            employeenumber_userid = ldap.search_ldap_exists_employeenumberfor('OSIRIS-ALL', employeenumber)
            print(f"\nUser {employeenumber.upper()} exists : {employeenumber_userid}")
            if (employeenumber_userid != "") and (employeenumber_userid != samaccountname):
                raise forms.ValidationError(
                    f"Le N°NISS existe déjà dans l'AD OSIRIS pour le userid : {employeenumber_userid}")

        return employeenumber

    # def clean_extensionattribute1(self):
    #     extensionattribute1 = self.cleaned_data.get("extensionattribute1")
    #
    #     if extensionattribute1 == "":
    #         raise forms.ValidationError("le N°MATRICULE est obligatoire.")
    #     if utils.check_regex('numbers', extensionattribute1) is False:
    #         raise forms.ValidationError("Seul les chiffres sont permis.")
    #     if len(extensionattribute1) > 9:
    #         raise forms.ValidationError("le N°MATRICULE doit avoir maximum 9 caractères.")
    #
    #     if extensionattribute1 and self.mode == 'create':
    #         # print('go into extensionattribute1')
    #         qs = RefidIopProvAd.objects.filter(extensionattribute1=extensionattribute1).values()
    #         # print(f"extensionattribute1:'{extensionattribute1}'")
    #         # print(f"qs:'{qs}'")
    #         # print(f"qs.exists():'{qs.exists()}'")
    #         if qs.exists():
    #             raise forms.ValidationError("Le N°MATRICULE existe déjà")
    #
    #     return extensionattribute1

    def clean_extensionattribute11(self):
        extensionattribute11 = self.cleaned_data.get("extensionattribute11")
        employeetype = self.cleaned_data.get("employeetype")

        # if employeetype != "Medical" and extensionattribute11 != "":
        #     raise forms.ValidationError("le n°INAMI ne doit être présent que pour le médical.")
        if employeetype == "Medical":
            if extensionattribute11 == "":
                raise forms.ValidationError("le personnel MEDICAL doit avoir un n°INAMI.")
            if utils.check_regex('numbersonly', extensionattribute11) is False:
                raise forms.ValidationError("Seul les chiffres sont permis.")
            if (len(extensionattribute11) != 11) and (len(extensionattribute11) != 0):
                raise forms.ValidationError("le N°INAMI doit avoir 11 caractères.")
            if extensionattribute11 and extensionattribute11[0] != "1":
                raise forms.ValidationError("le N°INAMI doit commencer par 1.")

        if extensionattribute11 and self.mode == 'create':
            # print('go into extensionattribute11')
            qs = RefidIopProvAd.objects.filter(extensionattribute11=extensionattribute11).values()
            # print(f"extensionattribute11:'{extensionattribute11}'")
            # print(f"qs:'{qs}'")
            # print(f"qs.exists():'{qs.exists()}'")
            if qs.exists() and extensionattribute11:
                raise forms.ValidationError("Le N°INAMI existe déjà")

        return extensionattribute11

    def clean_telephonenumber(self):
        telephonenumber = self.cleaned_data.get("telephonenumber")
        if utils.check_regex('numbers', telephonenumber) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(telephonenumber) > 50:
            raise forms.ValidationError("le Téléphone doit avoir maximum 50 caractères.")
        return telephonenumber

    def clean_pager(self):
        pager = self.cleaned_data.get("pager")
        if utils.check_regex('numbers', pager) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(pager) > 20:
            raise forms.ValidationError("le Téléphone portable doit avoir maximum 20 caractères.")
        return pager

    def clean_accountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")
        if enableaccountexpires == "1" and accountexpires is None:
            raise forms.ValidationError("la date d'expiration doit être encodée.")
        return accountexpires

    def clean_enableaccountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")

        if enableaccountexpires == "0" and accountexpires is not None:
            raise forms.ValidationError("Si vous encodé une date d'expiration le flag doit être positionné.")
        return enableaccountexpires


class RefidIopProvAdUpdateForm(forms.ModelForm):
    mode = 'update'

    class Meta:
        model = RefidIopProvAd

        fields = [
            "samaccountname",
            "sn",
            "givenname",
            "usualsn",
            "usualgivenname",
            "company",
            "physicaldeliveryofficename",
            "department",
            "businesscategory",
            "employeetype",
            "preferredlanguage",
            "quality",
            "gender",
            "birthdate",
            "cardtype",
            "employeenumber",
            "extensionattribute1",
            "extensionattribute2",
            "extensionattribute11",
            "telephonenumber",
            "pager",
            "localisation",
            "roles",
            "unites",
            "specialites",
            "homedir",
            "homedrive",
            "description",
            "info",
            "extensionattribute15",
            "metadata",
            "enableaccountexpires",
            "accountexpires",
            "changepasswordatlogon",
            "enabled",
            "enablemail",
            "mail",
            "groups",
            "distributionlist",
            "groupsad",
            "distributionlistad",
            "env",
            "org",
            "src",
            "usercre",
            "datecre",
            "userupd",
            "dateupd",
            "msgrefid",
            "actiontype",
            "msgdb",
            "msgad",
            "datesyncad",
            "flagsyncad",
            "msgexchange",
            "datesyncexchange",
            "flagsyncexchange",
            "password",
            "objectsid",
            "objectguid",
            "whencreated",
            "whenchanged",
            "lastlogontimestamp",
            "lastlogon",
            "pwdlastset",
            "badpasswordtime",
            "msexchwhenmailboxcreated",
            "chuidoriginsource",
            "evdidmstate",
            "evdpmschedulerstatus",
            "enatelbegintime",
            "enatelendtime",
            "rhmatricule",
            "rhnom",
            "rhprenom",
            "rhsexe",
            "rhdnais",
            "rhlangue",
            "rhnumcardid",
            "rhnumnational",
            "rhdatedeb",
            "rhdatefin",
            "rhstatutcontrat",
            "rhcodesociete",
            "rhcodeprofil",
            "rhprofil",
            "rhcaqualification",
            "rhcacode",
            "rhcalib",
            "rhinami",
            "rhmetadata",
            "rfidatesync",
            "messages",
        ]

        exclude = ["roles", "unites", "specialites", "password", ]  # password important else cleaning

        labels = {
            "samaccountname": "USERID",
            "sn": "NOM OFFICIEL *",
            "givenname": "PRENOM OFFICIEL *",
            "usualsn": "NOM USUEL *",
            "usualgivenname": "PRENOM USUEL *",
            "company": "HOPITAL *",
            "physicaldeliveryofficename": "SITE *",
            "department": "DEPARTEMENT",
            "businesscategory": "CATEGORIE *",
            "employeetype": "TYPE *",
            "quality": "QUALITE *",
            "preferredlanguage": "LANGUE *",
            "gender": "GENRE *",
            "birthdate": "DATE DE NAISSANCE",
            "cardtype": "TYPE DE DOCUMENT *",
            "employeenumber": "N°DOCUMENT *",
            "extensionattribute1": "N°MATRICULE/REFERENCE",
            "extensionattribute2": "MOUVEMENT",
            "extensionattribute11": "N°INAMI",
            "telephonenumber": "TELEPHONE",
            "pager": "PORTABLE",
            "localisation": "LOCALISATION",
            "roles": "ROLES",
            "unites": "UNITES",
            "specialites": "SPECIALITES",
            "homedir": "HOME DIRECTORY *",
            "homedrive": "HOME DRIVE *",
            "description": "DESCRIPTION",
            "info": "INFO IAM *",
            "extensionattribute15": "INFO REFID *",
            "metadata": "METADATA",
            "enableaccountexpires": "DATE D'EXPIRATION ACTIVE",
            "accountexpires": "DATE D'EXPIRATION",
            "changepasswordatlogon": "CHANGE PSW @LOGON",
            "enabled": "COMPTE ACTIF",
            "enablemail": "MAIL ACTIF *",
            "mail": "MAIL *",
            "groups": "GROUPES DE SECURITE",
            "distributionlist": "LISTES DE DISTRIBUTION",
            "groupsad": "GROUPES DE SECURITE AD",
            "distributionlistad": "LISTES DE DISTRIBUTION AD",
            "env": "ENVIRONNEMENT *",
            "org": "ORGANISATION *",
            "src": "SOURCE *",
            "usercre": "USER CREATE",
            "datecre": "DATE CREATE",
            "userupd": "USER UPDATE",
            "dateupd": "DATE UPDATE",
            "msgrefid": "MSG REFID",
            "actiontype": "ACTION TYPE *",
            "msgdb": "MSG DB",
            "msgad": "RETURN CODE AD",
            "datesyncad": "DATE SYNC AD",
            "flagsyncad": "STATE AD *",
            "msgexchange": "RETURN CODE EXCHANGE",
            "datesyncexchange": "DATE SYNC EXCHANGE",
            "flagsyncexchange": "STATE EXCHANGE *",
            "password": "PASSWORD *",
            "objectsid": "AD OBJECT SID",
            "objectguid": "AD OBJECT GUID",
            "whencreated": "AD WHEN CREATED",
            "whenchanged": "AD AD WHEN CHANGED",
            "lastlogontimestamp": "AD LAST LOGON TIMESTAMP",
            "lastlogon": "AD LAST LOGON",
            "pwdlastset": "AD PWD LAST SET",
            "badpasswordtime": "AD BAD PASSWORD TIME",
            "msexchwhenmailboxcreated": "AD EXCHANGE MAIL CREATED",
            "chuidoriginsource": "EVIDIAN SOURCE",
            "evdidmstate": "EVIDIAN STATE",
            "evdpmschedulerstatus": "EVIDIAN SCHEDULER STATUS",
            "enatelbegintime": "EVIDIAN BEGIN TIME",
            "enatelendtime": "EVIDIAN END TIME",
            "rhmatricule": "MATRICULE (RH)",
            "rhnom": "NOM (RH)",
            "rhprenom": "PRENOM (RH)",
            "rhsexe": "SEXE (RH)",
            "rhdnais": "DATE DE NAISSANCE (RH)",
            "rhlangue": "LANGUE (RH)",
            "rhnumcardid": "N°CARTE ID (RH)",
            "rhnumnational": "N°NATIONAL (RH)",
            "rhdatedeb": "DATE DE DEBUT (RH)",
            "rhdatefin": "DATE DE FIN (RH)",
            "rhstatutcontrat": "STATUT CONTRAT (RH)",
            "rhcodesociete": "HOPITAL (RH)",
            "rhcodeprofil": "PROFIL CODE(RH)",
            "rhprofil": "PROFIL (RH)",
            "rhcaqualification": "CA QUALIFICATION (RH)",
            "rhcacode": "CA CODE (RH)",
            "rhcalib": "CA LIB (RH)",
            "rhinami": "INAMI (RH)",
            "rhmetadata": "METADATA (RH)",
            "rfidatesync": "DATE SYNC REFID",
            "messages": "MESSAGE REFID",
        }

        widgets = {
            "samaccountname": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),

            "sn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "givenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualsn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualgivenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "company": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "physicaldeliveryofficename": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "department": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "businesscategory": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeetype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "quality": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "preferredlanguage": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "gender": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "birthdate": forms.DateInput(attrs={
                'type': 'date',
                'data-provide': 'datepicker',
                'min': '1900-01-01',
                'max': '2031-12-31'},),

            "cardtype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'readonly': 'readonly'}),

            "extensionattribute2": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute11": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "telephonenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "pager": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "localisation": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "description": forms.Textarea(attrs={'class': 'form-text', 'cols': 50, 'rows': 2}),

            "enableaccountexpires": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            'accountexpires': forms.DateInput(attrs={
                    'type': 'date',
                    'onkeydown': 'return false',
                    'min': '2020-01-01',
                    'max': '2031-12-31'}),

            # comment in create ?
            "changepasswordatlogon": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "enabled": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "enablemail": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),
            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groups": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlist": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groupsad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlistad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "homedir": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "homedrive": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "info": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute15": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "metadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "env": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "org": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "src": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "usercre": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "datecre": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "userupd": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "dateupd": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "msgrefid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msgdb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "actiontype": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncad": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncexchange": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "objectsid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "objectguid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "whencreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "whenchanged": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogontimestamp": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogon": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "pwdlastset": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "badpasswordtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msexchwhenmailboxcreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "chuidoriginsource": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdidmstate": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdpmschedulerstatus": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelbegintime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelendtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmatricule": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprenom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhsexe": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdnais": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhlangue": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumcardid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumnational": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatedeb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatefin": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhstatutcontrat": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhcodesociete": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcodeprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcaqualification": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcacode": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcalib": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhinami": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmetadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rfidatesync": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "messages": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            # HIDDEN for UPDATE
            "password": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'hidden': 'hidden'}),
        }

    # validation au niveau du serveur

    def clean_samaccountname(self):
        samaccountname = self.cleaned_data.get('samaccountname')
        return samaccountname

    def clean_sn(self):
        sn = self.cleaned_data.get("sn")
        if sn == "":
            raise forms.ValidationError("le nom est obligatoire.")
        if utils.check_regex('letters', sn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if sn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom doit commencer par ZZ.")
        if len(sn) < 3:
            raise forms.ValidationError("Le nom doit avoir au moins 3 lettres.")
        return sn

    def clean_givenname(self):
        givenname = self.cleaned_data.get("givenname")
        if givenname == "":
            raise forms.ValidationError("le prénom est obligatoire.")
        if utils.check_regex('letters', givenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(givenname) < 1:
            raise forms.ValidationError(
                "Le prénom doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return givenname

    def clean_usualsn(self):
        usualsn = self.cleaned_data.get("usualsn")
        if usualsn == "":
            raise forms.ValidationError("le nom usuel est obligatoire.")
        if utils.check_regex('letters', usualsn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if usualsn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom usuel doit commencer par ZZ.")
        if len(usualsn) < 3:
            raise forms.ValidationError("Le nom usuel doit avoir au moins 3 lettres.")
        return usualsn

    def clean_usualgivenname(self):
        usualgivenname = self.cleaned_data.get("usualgivenname")
        if usualgivenname == "":
            raise forms.ValidationError("le prénom usuel est obligatoire.")
        if utils.check_regex('letters', usualgivenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(usualgivenname) < 1:
            raise forms.ValidationError(
                "Le prénom usuel doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return usualgivenname

    def clean_quality(self):
        quality = self.cleaned_data.get("quality")
        if quality is None:
            raise forms.ValidationError("la qualité est obligatoire.")
        return quality

    def clean_preferredlanguage(self):
        preferredlanguage = self.cleaned_data.get("preferredlanguage")
        if preferredlanguage is None:
            raise forms.ValidationError("la langue est obligatoire.")
        return preferredlanguage

    def clean_gender(self):
        gender = self.cleaned_data.get("gender")
        if gender is None:
            raise forms.ValidationError("le genre est obligatoire.")
        return gender

    def clean_company(self):
        company = self.cleaned_data.get("company")
        if company is None:
            raise forms.ValidationError("l'hôpital est obligatoire.")
        return company

    def clean_physicaldeliveryofficename(self):
        physicaldeliveryofficename = self.cleaned_data.get("physicaldeliveryofficename")
        company = self.cleaned_data.get("company")
        if physicaldeliveryofficename is None and company != 'Huderf':
            raise forms.ValidationError("le site est obligatoire.")
        return physicaldeliveryofficename

    def clean_businesscategory(self):
        businesscategory = self.cleaned_data.get("businesscategory")
        if businesscategory is None:
            raise forms.ValidationError("la catégorie est obligatoire.")
        return businesscategory

    def clean_employeetype(self):
        employeetype = self.cleaned_data.get("employeetype")
        if employeetype is None:
            raise forms.ValidationError("la type de personnel est obligatoire.")
        return employeetype

    def clean_cardtype(self):
        cardtype = self.cleaned_data.get("cardtype")
        if cardtype is None:
            raise forms.ValidationError("le type de document est obligatoire.")
        return cardtype

    def clean_employeenumber(self):
        # La structure du NISS est la suivante : AAMMJJ-sss-NC
        #
        # AA = année de naissance
        # MM = mois de naissance (augmenté de 20 ou 40 pour les numéros bis)
        # JJ = jour de naissance
        # sss = numéro de suite renseignant en dernière position le sexe (impair pour les hommes, pair pour les femmes)
        # NC = nombre de contrôle

        employeenumber = self.cleaned_data.get("employeenumber")
        cardtype = self.cleaned_data.get("cardtype")
        samaccountname = self.cleaned_data.get("samaccountname")

        if employeenumber == "":
            raise forms.ValidationError("le N°DOCUMENT est obligatoire.")

        # if employeenumber[0:3] != '000':
        #     raise forms.ValidationError("En Phase de Test le N°de document doit commencer par '000'.")

        if cardtype == 'NISS':
            # if utils.check_regex('numbers', employeenumber) is False:
            #     raise forms.ValidationError("Seul les chiffres sont permis.")
            # if len(employeenumber) != 11:
            #     raise forms.ValidationError("le N°NISS doit avoir 11 caractères.")
            if not check_niss(employeenumber):
                raise forms.ValidationError("le N°NISS n'est pas correct.")


        if employeenumber and self.mode == 'create':
            qs = RefidIopProvAd.objects.filter(employeenumber=employeenumber).values()
            if qs.exists():
                print(f"\nUser {employeenumber.upper()} exists")
                raise forms.ValidationError("Le N°NISS existe déjà")

        if employeenumber:
            employeenumber_userid = ldap.search_ldap_exists_employeenumberfor('OSIRIS-ALL', employeenumber)
            print(f"\nUser {employeenumber.upper()} exists : {employeenumber_userid}")
            if (employeenumber_userid != "") and (employeenumber_userid != samaccountname):
                raise forms.ValidationError(f"Le N°NISS existe déjà dans l'AD OSIRIS pour le userid : {employeenumber_userid}")

        return employeenumber

    # def clean_extensionattribute1(self):
    #     extensionattribute1 = self.cleaned_data.get("extensionattribute1")
    #
    #     if extensionattribute1 == "":
    #         raise forms.ValidationError("le N°MATRICULE est obligatoire.")
    #     if utils.check_regex('numbers', extensionattribute1) is False:
    #         raise forms.ValidationError("Seul les chiffres sont permis.")
    #     if len(extensionattribute1) > 9:
    #         raise forms.ValidationError("le N°MATRICULE doit avoir maximum 9 caractères.")
    #
    #     if extensionattribute1 and self.mode == 'create':
    #         # print('go into extensionattribute1')
    #         qs = RefidIopProvAd.objects.filter(extensionattribute1=extensionattribute1).values()
    #         # print(f"extensionattribute1:'{extensionattribute1}'")
    #         # print(f"qs:'{qs}'")
    #         # print(f"qs.exists():'{qs.exists()}'")
    #         if qs.exists():
    #             raise forms.ValidationError("Le N°MATRICULE existe déjà")
    #
    #     return extensionattribute1

    def clean_extensionattribute11(self):
        extensionattribute11 = self.cleaned_data.get("extensionattribute11")
        employeetype = self.cleaned_data.get("employeetype")

        # if employeetype != "Medical" and extensionattribute11 != "":
        #     raise forms.ValidationError("le n°INAMI ne doit être présent que pour le médical.")
        if employeetype == "Medical":
            if extensionattribute11 == "":
                raise forms.ValidationError("le personnel MEDICAL doit avoir un n°INAMI.")
            if utils.check_regex('numbersonly', extensionattribute11) is False:
                raise forms.ValidationError("Seul les chiffres sont permis.")
            if (len(extensionattribute11) != 11) and (len(extensionattribute11) != 0):
                raise forms.ValidationError("le N°INAMI doit avoir 11 caractères.")
            if extensionattribute11 and extensionattribute11[0] != "1":
                raise forms.ValidationError("le N°INAMI doit commencer par 1.")

        if extensionattribute11 and self.mode == 'create':
            # print('go into extensionattribute11')
            qs = RefidIopProvAd.objects.filter(extensionattribute11=extensionattribute11).values()
            # print(f"extensionattribute11:'{extensionattribute11}'")
            # print(f"qs:'{qs}'")
            # print(f"qs.exists():'{qs.exists()}'")
            if qs.exists() and extensionattribute11:
                raise forms.ValidationError("Le N°INAMI existe déjà")

        return extensionattribute11

    def clean_telephonenumber(self):
        telephonenumber = self.cleaned_data.get("telephonenumber")
        if utils.check_regex('numbers', telephonenumber) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(telephonenumber) > 50:
            raise forms.ValidationError("le Téléphone doit avoir maximum 50 caractères.")
        return telephonenumber

    def clean_pager(self):
        pager = self.cleaned_data.get("pager")
        if utils.check_regex('numbers', pager) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(pager) > 20:
            raise forms.ValidationError("le Téléphone portable doit avoir maximum 20 caractères.")
        return pager

    def clean_accountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")
        if enableaccountexpires == "1" and accountexpires is None:
            raise forms.ValidationError("la date d'expiration doit être encodée.")
        return accountexpires

    def clean_enableaccountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")

        if enableaccountexpires == "0" and accountexpires is not None:
            raise forms.ValidationError("Si vous encodé une date d'expiration le flag doit être positionné.")
        return enableaccountexpires


# ProvInitAd ==========


class RefidIopProvInitAdCreateForm(forms.ModelForm):
    mode = 'create'

    class Meta:
        model = RefidIopProvInitAd

        fields = [
            "samaccountname",
            "sn",
            "givenname",
            "usualsn",
            "usualgivenname",
            "company",
            "physicaldeliveryofficename",
            "department",
            "businesscategory",
            "employeetype",
            "preferredlanguage",
            "quality",
            "gender",
            "birthdate",
            "cardtype",
            "employeenumber",
            "extensionattribute1",
            "extensionattribute2",
            "extensionattribute11",
            "telephonenumber",
            "pager",
            "localisation",
            "roles",
            "unites",
            "specialites",
            "homedir",
            "homedrive",
            "description",
            "info",
            "extensionattribute15",
            "metadata",
            "enableaccountexpires",
            "accountexpires",
            "changepasswordatlogon",
            "enabled",
            "enablemail",
            "mail",
            "groups",
            "distributionlist",
            "groupsad",
            "distributionlistad",
            "env",
            "org",
            "src",
            "usercre",
            "datecre",
            "userupd",
            "dateupd",
            "msgrefid",
            "actiontype",
            "msgdb",
            "msgad",
            "datesyncad",
            "flagsyncad",
            "msgexchange",
            "datesyncexchange",
            "flagsyncexchange",
            "password",
            "objectsid",
            "objectguid",
            "whencreated",
            "whenchanged",
            "lastlogontimestamp",
            "lastlogon",
            "pwdlastset",
            "badpasswordtime",
            "msexchwhenmailboxcreated",
            "chuidoriginsource",
            "evdidmstate",
            "evdpmschedulerstatus",
            "enatelbegintime",
            "enatelendtime",
            "rhmatricule",
            "rhnom",
            "rhprenom",
            "rhsexe",
            "rhdnais",
            "rhlangue",
            "rhnumcardid",
            "rhnumnational",
            "rhdatedeb",
            "rhdatefin",
            "rhstatutcontrat",
            "rhcodesociete",
            "rhcodeprofil",
            "rhprofil",
            "rhcaqualification",
            "rhcacode",
            "rhcalib",
            "rhinami",
            "rhmetadata",
            "rfidatesync",
            "messages",
        ]

        exclude = ["roles", "unites", "specialites"]

        labels = {
            "samaccountname": "USERID",
            "sn": "NOM OFFICIEL *",
            "givenname": "PRENOM OFFICIEL *",
            "usualsn": "NOM USUEL *",
            "usualgivenname": "PRENOM USUEL *",
            "company": "HOPITAL *",
            "physicaldeliveryofficename": "SITE *",
            "department": "DEPARTEMENT",
            "businesscategory": "CATEGORIE *",
            "employeetype": "TYPE *",
            "quality": "QUALITE *",
            "preferredlanguage": "LANGUE *",
            "gender": "GENRE *",
            "birthdate": "DATE DE NAISSANCE",
            "cardtype": "TYPE DE DOCUMENT *",
            "employeenumber": "N°DOCUMENT *",
            "extensionattribute1": "N°MATRICULE/REFERENCE",
            "extensionattribute2": "MOUVEMENT",
            "extensionattribute11": "N°INAMI",
            "telephonenumber": "TELEPHONE",
            "pager": "PORTABLE",
            "localisation": "LOCALISATION",
            "roles": "ROLES",
            "unites": "UNITES",
            "specialites": "SPECIALITES",
            "homedir": "HOME DIRECTORY *",
            "homedrive": "HOME DRIVE *",
            "description": "DESCRIPTION",
            "info": "INFO IAM *",
            "extensionattribute15": "INFO REFID *",
            "metadata": "METADATA",
            "enableaccountexpires": "DATE D'EXPIRATION ACTIVE",
            "accountexpires": "DATE D'EXPIRATION",
            "changepasswordatlogon": "CHANGE PSW @LOGON",
            "enabled": "COMPTE ACTIF",
            "enablemail": "MAIL ACTIF *",
            "mail": "MAIL *",
            "groups": "GROUPES DE SECURITE",
            "distributionlist": "LISTES DE DISTRIBUTION",
            "groupsad": "GROUPES DE SECURITE AD",
            "distributionlistad": "LISTES DE DISTRIBUTION AD",
            "env": "ENVIRONNEMENT *",
            "org": "ORGANISATION *",
            "src": "SOURCE *",
            "usercre": "USER CREATE",
            "datecre": "DATE CREATE",
            "userupd": "USER UPDATE",
            "dateupd": "DATE UPDATE",
            "msgrefid": "MSG REFID",
            "actiontype": "ACTION TYPE *",
            "msgdb": "MSG DB",
            "msgad": "RETURN CODE AD",
            "datesyncad": "DATE SYNC AD",
            "flagsyncad": "STATE AD *",
            "msgexchange": "RETURN CODE EXCHANGE",
            "datesyncexchange": "DATE SYNC EXCHANGE",
            "flagsyncexchange": "STATE EXCHANGE *",
            "password": "PASSWORD *",
            "objectsid": "AD OBJECT SID",
            "objectguid": "AD OBJECT GUID",
            "whencreated": "AD WHEN CREATED",
            "whenchanged": "AD AD WHEN CHANGED",
            "lastlogontimestamp": "AD LAST LOGON TIMESTAMP",
            "lastlogon": "AD LAST LOGON",
            "pwdlastset": "AD PWD LAST SET",
            "badpasswordtime": "AD BAD PASSWORD TIME",
            "msexchwhenmailboxcreated": "AD EXCHANGE MAIL CREATED",
            "chuidoriginsource": "EVIDIAN SOURCE",
            "evdidmstate": "EVIDIAN STATE",
            "evdpmschedulerstatus": "EVIDIAN SCHEDULER STATUS",
            "enatelbegintime": "EVIDIAN BEGIN TIME",
            "enatelendtime": "EVIDIAN END TIME",
            "rhmatricule": "MATRICULE (RH)",
            "rhnom": "NOM (RH)",
            "rhprenom": "PRENOM (RH)",
            "rhsexe": "SEXE (RH)",
            "rhdnais": "DATE DE NAISSANCE (RH)",
            "rhlangue": "LANGUE (RH)",
            "rhnumcardid": "N°CARTE ID (RH)",
            "rhnumnational": "N°NATIONAL (RH)",
            "rhdatedeb": "DATE DE DEBUT (RH)",
            "rhdatefin": "DATE DE FIN (RH)",
            "rhstatutcontrat": "STATUT CONTRAT (RH)",
            "rhcodesociete": "HOPITAL (RH)",
            "rhcodeprofil": "PROFIL CODE(RH)",
            "rhprofil": "PROFIL (RH)",
            "rhcaqualification": "CA QUALIFICATION (RH)",
            "rhcacode": "CA CODE (RH)",
            "rhcalib": "CA LIB (RH)",
            "rhinami": "INAMI (RH)",
            "rhmetadata": "METADATA (RH)",
            "rfidatesync": "DATE SYNC REFID",
            "messages": "MESSAGE REFID",
        }

        widgets = {
            "samaccountname": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),

            "sn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "givenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualsn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualgivenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "company": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "physicaldeliveryofficename": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "department": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "businesscategory": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeetype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "quality": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "preferredlanguage": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "gender": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "birthdate": forms.DateInput(attrs={
                'type': 'date',
                'data-provide': 'datepicker',
                'min': '1900-01-01',
                'max': '2031-12-31'},),

            "cardtype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'readonly': 'readonly'}),

            "extensionattribute2": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute11": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "telephonenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "pager": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "localisation": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "description": forms.Textarea(attrs={'class': 'form-text', 'cols': 50, 'rows': 2}),

            "enableaccountexpires": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            'accountexpires': forms.DateInput(attrs={
                    'type': 'date',
                    'onkeydown': 'return false',
                    'min': '2020-01-01',
                    'max': '2031-12-31'}),

            # comment in create ?
            "changepasswordatlogon": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "enabled": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "enablemail": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),
            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groups": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlist": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groupsad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlistad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "homedir": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "homedrive": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "info": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute15": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "metadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "env": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "org": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "src": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "usercre": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "datecre": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "userupd": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "dateupd": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "msgrefid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msgdb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "actiontype": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncad": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncexchange": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "objectsid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "objectguid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "whencreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "whenchanged": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogontimestamp": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogon": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "pwdlastset": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "badpasswordtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msexchwhenmailboxcreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "chuidoriginsource": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdidmstate": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdpmschedulerstatus": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelbegintime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelendtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmatricule": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprenom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhsexe": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdnais": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhlangue": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumcardid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumnational": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatedeb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatefin": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhstatutcontrat": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhcodesociete": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcodeprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcaqualification": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcacode": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcalib": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhinami": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmetadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rfidatesync": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "messages": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            # READ-ONLY for CREATE
            "password": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),
        }

    # validation au niveau du serveur

    def clean_samaccountname(self):
        samaccountname = self.cleaned_data.get('samaccountname')
        return samaccountname

    def clean_sn(self):
        sn = self.cleaned_data.get("sn")
        if sn == "":
            raise forms.ValidationError("le nom est obligatoire.")
        if utils.check_regex('letters', sn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if sn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom doit commencer par ZZ.")
        if len(sn) < 3:
            raise forms.ValidationError("Le nom doit avoir au moins 3 lettres.")
        return sn

    def clean_givenname(self):
        givenname = self.cleaned_data.get("givenname")
        if givenname == "":
            raise forms.ValidationError("le prénom est obligatoire.")
        if utils.check_regex('letters', givenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(givenname) < 1:
            raise forms.ValidationError(
                "Le prénom doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return givenname

    def clean_usualsn(self):
        usualsn = self.cleaned_data.get("usualsn")
        if usualsn == "":
            raise forms.ValidationError("le nom usuel est obligatoire.")
        if utils.check_regex('letters', usualsn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if usualsn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom usuel doit commencer par ZZ.")
        if len(usualsn) < 3:
            raise forms.ValidationError("Le nom usuel doit avoir au moins 3 lettres.")
        return usualsn

    def clean_usualgivenname(self):
        usualgivenname = self.cleaned_data.get("usualgivenname")
        if usualgivenname == "":
            raise forms.ValidationError("le prénom usuel est obligatoire.")
        if utils.check_regex('letters', usualgivenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(usualgivenname) < 1:
            raise forms.ValidationError(
                "Le prénom usuel doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return usualgivenname

    def clean_quality(self):
        quality = self.cleaned_data.get("quality")
        if quality is None:
            raise forms.ValidationError("la qualité est obligatoire.")
        return quality

    def clean_preferredlanguage(self):
        preferredlanguage = self.cleaned_data.get("preferredlanguage")
        if preferredlanguage is None:
            raise forms.ValidationError("la langue est obligatoire.")
        return preferredlanguage

    def clean_gender(self):
        gender = self.cleaned_data.get("gender")
        if gender is None:
            raise forms.ValidationError("le genre est obligatoire.")
        return gender

    def clean_company(self):
        company = self.cleaned_data.get("company")
        if company is None:
            raise forms.ValidationError("l'hôpital est obligatoire.")
        return company

    def clean_physicaldeliveryofficename(self):
        physicaldeliveryofficename = self.cleaned_data.get("physicaldeliveryofficename")
        company = self.cleaned_data.get("company")
        if physicaldeliveryofficename is None and company != 'Huderf':
            raise forms.ValidationError("le site est obligatoire.")
        return physicaldeliveryofficename

    def clean_businesscategory(self):
        businesscategory = self.cleaned_data.get("businesscategory")
        if businesscategory is None:
            raise forms.ValidationError("la catégorie est obligatoire.")
        return businesscategory

    def clean_employeetype(self):
        employeetype = self.cleaned_data.get("employeetype")
        if employeetype is None:
            raise forms.ValidationError("la type de personnel est obligatoire.")
        return employeetype

    def clean_cardtype(self):
        cardtype = self.cleaned_data.get("cardtype")
        if cardtype is None:
            raise forms.ValidationError("le type de document est obligatoire.")
        return cardtype

    def clean_employeenumber(self):
        # La structure du NISS est la suivante : AAMMJJ-sss-NC
        #
        # AA = année de naissance
        # MM = mois de naissance (augmenté de 20 ou 40 pour les numéros bis)
        # JJ = jour de naissance
        # sss = numéro de suite renseignant en dernière position le sexe (impair pour les hommes, pair pour les femmes)
        # NC = nombre de contrôle

        employeenumber = self.cleaned_data.get("employeenumber")
        cardtype = self.cleaned_data.get("cardtype")
        samaccountname = self.cleaned_data.get("samaccountname")

        if employeenumber == "":
            raise forms.ValidationError("le N°DOCUMENT est obligatoire.")

        # if employeenumber[0:3] != '000':
        #     raise forms.ValidationError("En Phase de Test le N°de document doit commencer par '000'.")

        if cardtype == 'NISS':
            # if utils.check_regex('numbers', employeenumber) is False:
            #     raise forms.ValidationError("Seul les chiffres sont permis.")
            # if len(employeenumber) != 11:
            #     raise forms.ValidationError("le N°NISS doit avoir 11 caractères.")
            if not check_niss(employeenumber):
                raise forms.ValidationError("le N°NISS n'est pas correct.")

        if employeenumber and self.mode == 'create':
            qs = RefidIopProvAd.objects.filter(employeenumber=employeenumber).values()
            if qs.exists():
                print(f"\nUser {employeenumber.upper()} exists")
                raise forms.ValidationError("Le N°NISS existe déjà")

        if employeenumber:
            employeenumber_userid = ldap.search_ldap_exists_employeenumberfor('OSIRIS-ALL', employeenumber)
            print(f"\nUser {employeenumber.upper()} exists : {employeenumber_userid}")
            if (employeenumber_userid != "") and (employeenumber_userid != samaccountname):
                raise forms.ValidationError(
                    f"Le N°NISS existe déjà dans l'AD OSIRIS pour le userid : {employeenumber_userid}")

        return employeenumber

    # def clean_extensionattribute1(self):
    #     extensionattribute1 = self.cleaned_data.get("extensionattribute1")
    #
    #     if extensionattribute1 == "":
    #         raise forms.ValidationError("le N°MATRICULE est obligatoire.")
    #     if utils.check_regex('numbers', extensionattribute1) is False:
    #         raise forms.ValidationError("Seul les chiffres sont permis.")
    #     if len(extensionattribute1) > 9:
    #         raise forms.ValidationError("le N°MATRICULE doit avoir maximum 9 caractères.")
    #
    #     if extensionattribute1 and self.mode == 'create':
    #         # print('go into extensionattribute1')
    #         qs = RefidIopProvAd.objects.filter(extensionattribute1=extensionattribute1).values()
    #         # print(f"extensionattribute1:'{extensionattribute1}'")
    #         # print(f"qs:'{qs}'")
    #         # print(f"qs.exists():'{qs.exists()}'")
    #         if qs.exists():
    #             raise forms.ValidationError("Le N°MATRICULE existe déjà")
    #
    #     return extensionattribute1

    def clean_extensionattribute11(self):
        extensionattribute11 = self.cleaned_data.get("extensionattribute11")
        employeetype = self.cleaned_data.get("employeetype")

        # if employeetype != "Medical" and extensionattribute11 != "":
        #     raise forms.ValidationError("le n°INAMI ne doit être présent que pour le médical.")
        if employeetype == "Medical":
            if extensionattribute11 == "":
                raise forms.ValidationError("le personnel MEDICAL doit avoir un n°INAMI.")
            if utils.check_regex('numbersonly', extensionattribute11) is False:
                raise forms.ValidationError("Seul les chiffres sont permis.")
            if (len(extensionattribute11) != 11) and (len(extensionattribute11) != 0):
                raise forms.ValidationError("le N°INAMI doit avoir 11 caractères.")
            if extensionattribute11 and extensionattribute11[0] != "1":
                raise forms.ValidationError("le N°INAMI doit commencer par 1.")

        if extensionattribute11 and self.mode == 'create':
            # print('go into extensionattribute11')
            qs = RefidIopProvAd.objects.filter(extensionattribute11=extensionattribute11).values()
            # print(f"extensionattribute11:'{extensionattribute11}'")
            # print(f"qs:'{qs}'")
            # print(f"qs.exists():'{qs.exists()}'")
            if qs.exists() and extensionattribute11:
                raise forms.ValidationError("Le N°INAMI existe déjà")

        return extensionattribute11


    def clean_telephonenumber(self):
        telephonenumber = self.cleaned_data.get("telephonenumber")
        if utils.check_regex('numbers', telephonenumber) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(telephonenumber) > 50:
            raise forms.ValidationError("le Téléphone doit avoir maximum 50 caractères.")
        return telephonenumber

    def clean_pager(self):
        pager = self.cleaned_data.get("pager")
        if utils.check_regex('numbers', pager) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(pager) > 20:
            raise forms.ValidationError("le Téléphone portable doit avoir maximum 20 caractères.")
        return pager

    def clean_accountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")
        if enableaccountexpires == "1" and accountexpires is None:
            raise forms.ValidationError("la date d'expiration doit être encodée.")
        return accountexpires

    def clean_enableaccountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")

        if enableaccountexpires == "0" and accountexpires is not None:
            raise forms.ValidationError("Si vous encodé une date d'expiration le flag doit être positionné.")
        return enableaccountexpires


class RefidIopProvInitAdUpdateForm(forms.ModelForm):
    mode = 'update'

    class Meta:
        model = RefidIopProvInitAd

        fields = [
            "samaccountname",
            "sn",
            "givenname",
            "usualsn",
            "usualgivenname",
            "company",
            "physicaldeliveryofficename",
            "department",
            "businesscategory",
            "employeetype",
            "preferredlanguage",
            "quality",
            "gender",
            "birthdate",
            "cardtype",
            "employeenumber",
            "extensionattribute1",
            "extensionattribute2",
            "extensionattribute11",
            "telephonenumber",
            "pager",
            "localisation",
            "roles",
            "unites",
            "specialites",
            "homedir",
            "homedrive",
            "description",
            "info",
            "extensionattribute15",
            "metadata",
            "enableaccountexpires",
            "accountexpires",
            "changepasswordatlogon",
            "enabled",
            "enablemail",
            "mail",
            "groups",
            "distributionlist",
            "groupsad",
            "distributionlistad",
            "env",
            "org",
            "src",
            "usercre",
            "datecre",
            "userupd",
            "dateupd",
            "msgrefid",
            "actiontype",
            "msgdb",
            "msgad",
            "datesyncad",
            "flagsyncad",
            "msgexchange",
            "datesyncexchange",
            "flagsyncexchange",
            "password",
            "objectsid",
            "objectguid",
            "whencreated",
            "whenchanged",
            "lastlogontimestamp",
            "lastlogon",
            "pwdlastset",
            "badpasswordtime",
            "msexchwhenmailboxcreated",
            "chuidoriginsource",
            "evdidmstate",
            "evdpmschedulerstatus",
            "enatelbegintime",
            "enatelendtime",
            "rhmatricule",
            "rhnom",
            "rhprenom",
            "rhsexe",
            "rhdnais",
            "rhlangue",
            "rhnumcardid",
            "rhnumnational",
            "rhdatedeb",
            "rhdatefin",
            "rhstatutcontrat",
            "rhcodesociete",
            "rhcodeprofil",
            "rhprofil",
            "rhcaqualification",
            "rhcacode",
            "rhcalib",
            "rhinami",
            "rhmetadata",
            "rfidatesync",
            "messages",
        ]

        exclude = ["roles", "unites", "specialites", "password", ]  # password important else cleaning

        labels = {
            "samaccountname": "USERID",
            "sn": "NOM OFFICIEL *",
            "givenname": "PRENOM OFFICIEL *",
            "usualsn": "NOM USUEL *",
            "usualgivenname": "PRENOM USUEL *",
            "company": "HOPITAL *",
            "physicaldeliveryofficename": "SITE *",
            "department": "DEPARTEMENT",
            "businesscategory": "CATEGORIE *",
            "employeetype": "TYPE *",
            "quality": "QUALITE *",
            "preferredlanguage": "LANGUE *",
            "gender": "GENRE *",
            "birthdate": "DATE DE NAISSANCE",
            "cardtype": "TYPE DE DOCUMENT *",
            "employeenumber": "N°DOCUMENT *",
            "extensionattribute1": "N°MATRICULE/REFERENCE",
            "extensionattribute2": "MOUVEMENT",
            "extensionattribute11": "N°INAMI",
            "telephonenumber": "TELEPHONE",
            "pager": "PORTABLE",
            "localisation": "LOCALISATION",
            "roles": "ROLES",
            "unites": "UNITES",
            "specialites": "SPECIALITES",
            "homedir": "HOME DIRECTORY *",
            "homedrive": "HOME DRIVE *",
            "description": "DESCRIPTION",
            "info": "INFO IAM *",
            "extensionattribute15": "INFO REFID *",
            "metadata": "METADATA",
            "enableaccountexpires": "DATE D'EXPIRATION ACTIVE",
            "accountexpires": "DATE D'EXPIRATION",
            "changepasswordatlogon": "CHANGE PSW @LOGON",
            "enabled": "COMPTE ACTIF",
            "enablemail": "MAIL ACTIF *",
            "mail": "MAIL *",
            "groups": "GROUPES DE SECURITE",
            "distributionlist": "LISTES DE DISTRIBUTION",
            "groupsad": "GROUPES DE SECURITE AD",
            "distributionlistad": "LISTES DE DISTRIBUTION AD",
            "env": "ENVIRONNEMENT *",
            "org": "ORGANISATION *",
            "src": "SOURCE *",
            "usercre": "USER CREATE",
            "datecre": "DATE CREATE",
            "userupd": "USER UPDATE",
            "dateupd": "DATE UPDATE",
            "msgrefid": "MSG REFID",
            "actiontype": "ACTION TYPE *",
            "msgdb": "MSG DB",
            "msgad": "RETURN CODE AD",
            "datesyncad": "DATE SYNC AD",
            "flagsyncad": "STATE AD *",
            "msgexchange": "RETURN CODE EXCHANGE",
            "datesyncexchange": "DATE SYNC EXCHANGE",
            "flagsyncexchange": "STATE EXCHANGE *",
            "password": "PASSWORD *",
            "objectsid": "AD OBJECT SID",
            "objectguid": "AD OBJECT GUID",
            "whencreated": "AD WHEN CREATED",
            "whenchanged": "AD AD WHEN CHANGED",
            "lastlogontimestamp": "AD LAST LOGON TIMESTAMP",
            "lastlogon": "AD LAST LOGON",
            "pwdlastset": "AD PWD LAST SET",
            "badpasswordtime": "AD BAD PASSWORD TIME",
            "msexchwhenmailboxcreated": "AD EXCHANGE MAIL CREATED",
            "chuidoriginsource": "EVIDIAN SOURCE",
            "evdidmstate": "EVIDIAN STATE",
            "evdpmschedulerstatus": "EVIDIAN SCHEDULER STATUS",
            "enatelbegintime": "EVIDIAN BEGIN TIME",
            "enatelendtime": "EVIDIAN END TIME",
            "rhmatricule": "MATRICULE (RH)",
            "rhnom": "NOM (RH)",
            "rhprenom": "PRENOM (RH)",
            "rhsexe": "SEXE (RH)",
            "rhdnais": "DATE DE NAISSANCE (RH)",
            "rhlangue": "LANGUE (RH)",
            "rhnumcardid": "N°CARTE ID (RH)",
            "rhnumnational": "N°NATIONAL (RH)",
            "rhdatedeb": "DATE DE DEBUT (RH)",
            "rhdatefin": "DATE DE FIN (RH)",
            "rhstatutcontrat": "STATUT CONTRAT (RH)",
            "rhcodesociete": "HOPITAL (RH)",
            "rhcodeprofil": "PROFIL CODE(RH)",
            "rhprofil": "PROFIL (RH)",
            "rhcaqualification": "CA QUALIFICATION (RH)",
            "rhcacode": "CA CODE (RH)",
            "rhcalib": "CA LIB (RH)",
            "rhinami": "INAMI (RH)",
            "rhmetadata": "METADATA (RH)",
            "rfidatesync": "DATE SYNC REFID",
            "messages": "MESSAGE REFID",
        }

        widgets = {
            "samaccountname": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),

            "sn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "givenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualsn": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "usualgivenname": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "company": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "physicaldeliveryofficename": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "department": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "businesscategory": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeetype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "quality": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "preferredlanguage": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "gender": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "birthdate": forms.DateInput(attrs={
                'type': 'date',
                'data-provide': 'datepicker',
                'min': '1900-01-01',
                'max': '2031-12-31'},),

            "cardtype": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "employeenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            # "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "extensionattribute1": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'readonly': 'readonly'}),

            "extensionattribute2": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute11": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "telephonenumber": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "pager": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "localisation": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "description": forms.Textarea(attrs={'class': 'form-text', 'cols': 50, 'rows': 2}),

            "enableaccountexpires": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            'accountexpires': forms.DateInput(attrs={
                    'type': 'date',
                    'onkeydown': 'return false',
                    'min': '2020-01-01',
                    'max': '2031-12-31'}),

            # comment in create ?
            "changepasswordatlogon": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "enabled": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "enablemail": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),
            "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'readonly': 'readonly'}),
            # "mail": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groups": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlist": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "groupsad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "distributionlistad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "homedir": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "homedrive": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "info": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "extensionattribute15": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "metadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50}),

            "env": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "org": forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "src": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "usercre": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "datecre": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "userupd": forms.TextInput(attrs={'class': 'form-text', 'size': 10, 'disabled': 'disabled'}),
            "dateupd": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "msgrefid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msgdb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "actiontype": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncad": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncad": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "msgexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "datesyncexchange": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "flagsyncexchange": forms.Select(attrs={'class': 'form-select form-select-sm'}),

            "objectsid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "objectguid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "whencreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "whenchanged": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogontimestamp": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "lastlogon": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "pwdlastset": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "badpasswordtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "msexchwhenmailboxcreated": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "chuidoriginsource": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdidmstate": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "evdpmschedulerstatus": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelbegintime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "enatelendtime": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmatricule": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprenom": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhsexe": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdnais": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhlangue": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumcardid": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhnumnational": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatedeb": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhdatefin": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhstatutcontrat": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhcodesociete": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcodeprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhprofil": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcaqualification": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcacode": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhcalib": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "rhinami": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rhmetadata": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            "rfidatesync": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),
            "messages": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'disabled': 'disabled'}),

            # HIDDEN for UPDATE
            "password": forms.TextInput(attrs={'class': 'form-text', 'size': 50, 'hidden': 'hidden'}),
        }

    # validation au niveau du serveur

    def clean_samaccountname(self):
        samaccountname = self.cleaned_data.get('samaccountname')
        return samaccountname

    def clean_sn(self):
        sn = self.cleaned_data.get("sn")
        if sn == "":
            raise forms.ValidationError("le nom est obligatoire.")
        if utils.check_regex('letters', sn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if sn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom doit commencer par ZZ.")
        if len(sn) < 3:
            raise forms.ValidationError("Le nom doit avoir au moins 3 lettres.")
        return sn

    def clean_givenname(self):
        givenname = self.cleaned_data.get("givenname")
        if givenname == "":
            raise forms.ValidationError("le prénom est obligatoire.")
        if utils.check_regex('letters', givenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(givenname) < 1:
            raise forms.ValidationError(
                "Le prénom doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return givenname

    def clean_usualsn(self):
        usualsn = self.cleaned_data.get("usualsn")
        if usualsn == "":
            raise forms.ValidationError("le nom usuel est obligatoire.")
        if utils.check_regex('letters', usualsn) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if usualsn[0:2].upper() != "ZZ":
            raise forms.ValidationError("En Test le nom usuel doit commencer par ZZ.")
        if len(usualsn) < 3:
            raise forms.ValidationError("Le nom usuel doit avoir au moins 3 lettres.")
        return usualsn

    def clean_usualgivenname(self):
        usualgivenname = self.cleaned_data.get("usualgivenname")
        if usualgivenname == "":
            raise forms.ValidationError("le prénom usuel est obligatoire.")
        if utils.check_regex('letters', usualgivenname) is False:
            raise forms.ValidationError("Seul les lettres sont permises")
        if len(usualgivenname) < 1:
            raise forms.ValidationError(
                "Le prénom usuel doit avoir au moins 1 lettre. Veullez introduire X si pas de prénom.")
        return usualgivenname

    def clean_quality(self):
        quality = self.cleaned_data.get("quality")
        if quality is None:
            raise forms.ValidationError("la qualité est obligatoire.")
        return quality

    def clean_preferredlanguage(self):
        preferredlanguage = self.cleaned_data.get("preferredlanguage")
        if preferredlanguage is None:
            raise forms.ValidationError("la langue est obligatoire.")
        return preferredlanguage

    def clean_gender(self):
        gender = self.cleaned_data.get("gender")
        if gender is None:
            raise forms.ValidationError("le genre est obligatoire.")
        return gender

    def clean_company(self):
        company = self.cleaned_data.get("company")
        if company is None:
            raise forms.ValidationError("l'hôpital est obligatoire.")
        return company

    def clean_physicaldeliveryofficename(self):
        physicaldeliveryofficename = self.cleaned_data.get("physicaldeliveryofficename")
        company = self.cleaned_data.get("company")
        if physicaldeliveryofficename is None and company != 'Huderf':
            raise forms.ValidationError("le site est obligatoire.")
        return physicaldeliveryofficename

    def clean_businesscategory(self):
        businesscategory = self.cleaned_data.get("businesscategory")
        if businesscategory is None:
            raise forms.ValidationError("la catégorie est obligatoire.")
        return businesscategory

    def clean_employeetype(self):
        employeetype = self.cleaned_data.get("employeetype")
        if employeetype is None:
            raise forms.ValidationError("la type de personnel est obligatoire.")
        return employeetype

    def clean_cardtype(self):
        cardtype = self.cleaned_data.get("cardtype")
        if cardtype is None:
            raise forms.ValidationError("le type de document est obligatoire.")
        return cardtype

    def clean_employeenumber(self):
        # La structure du NISS est la suivante : AAMMJJ-sss-NC
        #
        # AA = année de naissance
        # MM = mois de naissance (augmenté de 20 ou 40 pour les numéros bis)
        # JJ = jour de naissance
        # sss = numéro de suite renseignant en dernière position le sexe (impair pour les hommes, pair pour les femmes)
        # NC = nombre de contrôle

        employeenumber = self.cleaned_data.get("employeenumber")
        cardtype = self.cleaned_data.get("cardtype")
        samaccountname = self.cleaned_data.get("samaccountname")

        if employeenumber == "":
            raise forms.ValidationError("le N°DOCUMENT est obligatoire.")

        # if employeenumber[0:3] != '000':
        #     raise forms.ValidationError("En Phase de Test le N°de document doit commencer par '000'.")

        if cardtype == 'NISS':
            # if utils.check_regex('numbers', employeenumber) is False:
            #     raise forms.ValidationError("Seul les chiffres sont permis.")
            # if len(employeenumber) != 11:
            #     raise forms.ValidationError("le N°NISS doit avoir 11 caractères.")
            if not check_niss(employeenumber):
                raise forms.ValidationError("le N°NISS n'est pas correct.")


        if employeenumber and self.mode == 'create':
            qs = RefidIopProvAd.objects.filter(employeenumber=employeenumber).values()
            if qs.exists():
                print(f"\nUser {employeenumber.upper()} exists")
                raise forms.ValidationError("Le N°NISS existe déjà")

        if employeenumber:
            employeenumber_userid = ldap.search_ldap_exists_employeenumberfor('OSIRIS-ALL', employeenumber)
            print(f"\nUser {employeenumber.upper()} exists : {employeenumber_userid}")
            if (employeenumber_userid != "") and (employeenumber_userid != samaccountname):
                raise forms.ValidationError(
                    f"Le N°NISS existe déjà dans l'AD OSIRIS pour le userid : {employeenumber_userid}")

        return employeenumber

    # def clean_extensionattribute1(self):
    #     extensionattribute1 = self.cleaned_data.get("extensionattribute1")
    #
    #     if extensionattribute1 == "":
    #         raise forms.ValidationError("le N°MATRICULE est obligatoire.")
    #     if utils.check_regex('numbers', extensionattribute1) is False:
    #         raise forms.ValidationError("Seul les chiffres sont permis.")
    #     if len(extensionattribute1) > 9:
    #         raise forms.ValidationError("le N°MATRICULE doit avoir maximum 9 caractères.")
    #
    #     if extensionattribute1 and self.mode == 'create':
    #         # print('go into extensionattribute1')
    #         qs = RefidIopProvAd.objects.filter(extensionattribute1=extensionattribute1).values()
    #         # print(f"extensionattribute1:'{extensionattribute1}'")
    #         # print(f"qs:'{qs}'")
    #         # print(f"qs.exists():'{qs.exists()}'")
    #         if qs.exists():
    #             raise forms.ValidationError("Le N°MATRICULE existe déjà")
    #
    #     return extensionattribute1

    def clean_extensionattribute11(self):
        extensionattribute11 = self.cleaned_data.get("extensionattribute11")
        employeetype = self.cleaned_data.get("employeetype")

        # if employeetype != "Medical" and extensionattribute11 != "":
        #     raise forms.ValidationError("le n°INAMI ne doit être présent que pour le médical.")
        if employeetype == "Medical":
            if extensionattribute11 == "":
                raise forms.ValidationError("le personnel MEDICAL doit avoir un n°INAMI.")
            if utils.check_regex('numbersonly', extensionattribute11) is False:
                raise forms.ValidationError("Seul les chiffres sont permis.")
            if (len(extensionattribute11) != 11) and (len(extensionattribute11) != 0):
                raise forms.ValidationError("le N°INAMI doit avoir 11 caractères.")
            if extensionattribute11 and extensionattribute11[0] != "1":
                raise forms.ValidationError("le N°INAMI doit commencer par 1.")

        if extensionattribute11 and self.mode == 'create':
            # print('go into extensionattribute11')
            qs = RefidIopProvAd.objects.filter(extensionattribute11=extensionattribute11).values()
            # print(f"extensionattribute11:'{extensionattribute11}'")
            # print(f"qs:'{qs}'")
            # print(f"qs.exists():'{qs.exists()}'")
            if qs.exists() and extensionattribute11:
                raise forms.ValidationError("Le N°INAMI existe déjà")

        return extensionattribute11

    def clean_telephonenumber(self):
        telephonenumber = self.cleaned_data.get("telephonenumber")
        if utils.check_regex('numbers', telephonenumber) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(telephonenumber) > 50:
            raise forms.ValidationError("le Téléphone doit avoir maximum 50 caractères.")
        return telephonenumber

    def clean_pager(self):
        pager = self.cleaned_data.get("pager")
        if utils.check_regex('numbers', pager) is False:
            raise forms.ValidationError("Seul les chiffres sont permis.")
        if len(pager) > 20:
            raise forms.ValidationError("le Téléphone portable doit avoir maximum 20 caractères.")
        return pager

    def clean_accountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")
        if enableaccountexpires == "1" and accountexpires is None:
            raise forms.ValidationError("la date d'expiration doit être encodée.")
        return accountexpires

    def clean_enableaccountexpires(self):
        accountexpires = self.cleaned_data.get("accountexpires")
        enableaccountexpires = self.cleaned_data.get("enableaccountexpires")

        if enableaccountexpires == "0" and accountexpires is not None:
            raise forms.ValidationError("Si vous encodé une date d'expiration le flag doit être positionné.")
        return enableaccountexpires


# =========================================================================================================
# SEARCH Forms
# =========================================================================================================


class SearchUserForm(forms.Form):
    q_userid = forms.CharField(label='USERID', max_length=20, required=False)
    q_niss = forms.CharField(label='NISS', max_length=20, required=False)
    q_nom = forms.CharField(label='NOM', max_length=30, required=False)
    q_prenom = forms.CharField(label='PRENOM', max_length=30, required=False)


class SearchRHUserForm(forms.Form):
    q_matricule = forms.CharField(label='MATRICULE', max_length=20, required=False)
    q_niss = forms.CharField(label='NISS', max_length=20, required=False)
    q_nom = forms.CharField(label='NOM', max_length=30, required=False)
    q_prenom = forms.CharField(label='PRENOM', max_length=30, required=False)


class SearchADUserForm(forms.Form):
    q_userid = forms.CharField(label='USERID', max_length=20, required=False)
    q_niss = forms.CharField(label='NISS', max_length=20, required=False)
    q_nom = forms.CharField(label='NOM', max_length=30, required=False)
    q_prenom = forms.CharField(label='PRENOM', max_length=30, required=False)


class SearchEVIDIANUserForm(forms.Form):
    q_userid = forms.CharField(label='USERID', max_length=20, required=False)
    q_niss = forms.CharField(label='NISS', max_length=20, required=False)
    q_nom = forms.CharField(label='NOM', max_length=30, required=False)
    q_prenom = forms.CharField(label='PRENOM', max_length=30, required=False)

# =========================================================================================================
# UTILS Classes
# =========================================================================================================


class Lowercase(forms.CharField):
    """Convert values in a field to lowercase."""

    def to_python(self, value):
        return value.lower()


class Uppercase(forms.CharField):
    """Convert values in a field to uppercase."""

    def to_python(self, value):
        return value.upper()


class MarkdownForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].label = "Enter your Markdown content"

    def clean_content(self):
        content = self.cleaned_data['content']
        return mark_safe(markdown.markdown(content))


# ================================================================================================================
# TESTS
# ================================================================================================================


class SearchForm(forms.Form):
    query = forms.CharField(label='SearchUser', max_length=100)


class SearchView(FormView):
    template_name = 'refid/refid-search-cbv.html'
    form_class = SearchForm
    success_url = '/refid-search-view/'

    def form_valid(self, form):
        query = form.cleaned_data['query']
        results = RefidIopProvAd.objects.filter(company__contains=query)
        return render(self.request, 'refid/refid-search-cbv.html', {'results': results})

# EOF ---------------------------------------------------------------
