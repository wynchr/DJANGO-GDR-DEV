"""
=======================================================================================================================
.DESCRIPTION
    Administration configuration for REFID Application

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version

.COMMENTS

=======================================================================================================================
"""
from django.contrib import admin

from .models import RefidIopProvAd,  \
    RefidIopProvInitAd, \
    RefidIopProvMirrorAd, \
    RefidIopProvLogAd, \
    RefidIopCacheRh,  \
    RefidIopCacheEvidian,  \
    RefidIopCacheAdOsiris, \
    RefidIopReferences,  \
    RefidIopRefadgroups

# admin.site.register(RefidIopProvAd)
# admin.site.register(RefidIopProvInitAd)
# admin.site.register(RefidIopProvMirrorAd)
# admin.site.register(RefidIopProvLogAd)
# admin.site.register(RefidIopCacheRh)
# admin.site.register(RefidIopCacheEvidian)
# admin.site.register(RefidIopCacheAdOsiris)
# admin.site.register(RefidIopReferences)
# admin.site.register(RefidIopRefadgroups)


admin.site.site_header = "GDR - RefId"

# ================================================================================================================
# APPLICATION Admin
# ================================================================================================================


@admin.register(RefidIopProvAd)
class RefidProvAdAdmin(admin.ModelAdmin):
    list_display = (
        "samaccountname",
        "sn",
        "givenname",
        # "usualsn",
        # "usualgivenname",
        "company",
        "physicaldeliveryofficename",
        "department",
        "businesscategory",
        "employeetype",
        "preferredlanguage",
        # "quality",
        # "gender",
        # "birthdate",
        "cardtype",
        "employeenumber",
        "extensionattribute1",
        # "extensionattribute2",
        "extensionattribute11",
        "telephonenumber",
        "pager",
        # "localisation",
        # "roles",
        # "unites",
        # "specialites",
        # "homedir",
        # "homedrive",
        # "description",
        "info",
        "extensionattribute15",
        # "metadata",
        "enableaccountexpires",
        "accountexpires",
        "changepasswordatlogon",
        "enabled",
        "enablemail",
        "mail",
        # "groups",
        # "distributionlist",
        "env",
        "org",
        "src",
        # "usercre",
        # "datecre",
        "userupd",
        "dateupd",
        # "msgrefid",
        "actiontype",
        # "msgdb",
        "msgad",
        "datesyncad",
        "flagsyncad",
        "msgexchange",
        "datesyncexchange",
        "flagsyncexchange",
        # "password",
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

        # "rhmatricule",
        # "rhnom",
        # "rhprenom",
        # "rhsexe",
        # "rhdnais",
        # "rhlangue",
        # "rhnumcardid",
        # "rhnumnational",
        "rhdatedeb",
        "rhdatefin",
        "rhstatutcontrat",

        "rhcodesociete",
        # "rhcodeprofil",
        # "rhprofil",
        # "rhcaqualification",
        # "rhcacode",
        # "rhcalib",
        # "rhinami",

        # "rhmetadata",

        "rfidatesync",
        # "messages",
    )

    list_editable = (
        # "flagsyncad",
        # "actiontype",
        # "flagsyncexchange"
    )

    list_filter = (
        "flagsyncad",
        "flagsyncexchange",
        "company",
        "physicaldeliveryofficename",
        "businesscategory",
        "employeetype",
        "department",
    )

    list_per_page = 100

    # list_display_links = ("sn",)

    search_fields = (
        "samaccountname",
        "sn",
        "givenname",
        "company",
    )

    # autocomplete_fields = (
    #     "actiontype",
    # )

    # empty_value_display = "Inconnu"

    fieldsets = (
                    ('KEY', {'fields': (
                        "samaccountname",
                    )}),
                    ('IDENTITY', {'fields': (
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
                    )}),
                    ('AD', {'fields': (
                        "homedir",
                        "homedrive",
                        "description",
                        "info",
                        "extensionattribute15",
                        "enableaccountexpires",
                        "accountexpires",
                        "changepasswordatlogon",
                        "enabled",
                    )}),
                    ('EXCHANGE', {'fields': (
                        "enablemail",
                        "mail",
                    )}),
                    ('SECURITY-GROUPS', {'fields': (
                        "groups",
                    )}),
                    ('DISTRIBUTION-LIST', {'fields': (
                        "distributionlist",
                    )}),
                    ('SYSTEM', {'fields': (
                        "env",
                        "org",
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
                        "objectsid",
                        "objectguid",
                    )}),
                    ('AD-OSIRIS', {'fields': (
                    "whencreated",
                    "whenchanged",
                    "lastlogontimestamp",
                    "lastlogon",
                    "pwdlastset",
                    "badpasswordtime",
                    "msexchwhenmailboxcreated",
                    )}),
                    ('HR-ARNO', {'fields': (
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
                    )}),
                    ('IAM-EVIDIAN', {'fields': (
                    "chuidoriginsource",
                    "evdidmstate",
                    "evdpmschedulerstatus",
                    "enatelbegintime",
                    "enatelendtime",
                    )}),
                )


@admin.register(RefidIopProvInitAd)
class RefidProvInitAdmin(admin.ModelAdmin):
    list_display = (
        "samaccountname",
        "sn",
        "givenname",
        # "usualsn",
        # "usualgivenname",
        "company",
        "physicaldeliveryofficename",
        "department",
        "businesscategory",
        "employeetype",
        "preferredlanguage",
        # "quality",
        # "gender",
        # "birthdate",
        "cardtype",
        "employeenumber",
        "extensionattribute1",
        # "extensionattribute2",
        "extensionattribute11",
        "telephonenumber",
        "pager",
        # "localisation",
        # "roles",
        # "unites",
        # "specialites",
        # "homedir",
        # "homedrive",
        # "description",
        "info",
        "extensionattribute15",
        # "metadata",
        "enableaccountexpires",
        "accountexpires",
        "changepasswordatlogon",
        "enabled",
        "enablemail",
        "mail",
        # "groups",
        # "distributionlist",
        "env",
        "org",
        "src",
        # "usercre",
        # "datecre",
        "userupd",
        "dateupd",
        # "msgrefid",
        "actiontype",
        # "msgdb",
        "msgad",
        "datesyncad",
        "flagsyncad",
        "msgexchange",
        "datesyncexchange",
        "flagsyncexchange",
        # "password",
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

        # "rhmatricule",
        # "rhnom",
        # "rhprenom",
        # "rhsexe",
        # "rhdnais",
        # "rhlangue",
        # "rhnumcardid",
        # "rhnumnational",
        "rhdatedeb",
        "rhdatefin",
        "rhstatutcontrat",

        "rhcodesociete",
        # "rhcodeprofil",
        # "rhprofil",
        # "rhcaqualification",
        # "rhcacode",
        # "rhcalib",
        # "rhinami",

        # "rhmetadata",

        "rfidatesync",
        # "messages",
    )

    list_editable = (
        # "flagsyncad",
        # "actiontype",
        # "flagsyncexchange"
    )

    list_filter = (
        "flagsyncad",
        "flagsyncexchange",
        "company",
        "physicaldeliveryofficename",
        "businesscategory",
        "employeetype",
        "department",
    )

    list_per_page = 100

    # list_display_links = ("sn",)

    search_fields = (
        "samaccountname",
        "sn",
        "givenname",
        "company",
    )

    # autocomplete_fields = (
    #     "actiontype",
    # )

    # empty_value_display = "Inconnu"

    fieldsets = (
                    ('KEY', {'fields': (
                        "samaccountname",
                    )}),
                    ('IDENTITY', {'fields': (
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
                    )}),
                    ('AD', {'fields': (
                        "homedir",
                        "homedrive",
                        "description",
                        "info",
                        "extensionattribute15",
                        "enableaccountexpires",
                        "accountexpires",
                        "changepasswordatlogon",
                        "enabled",
                    )}),
                    ('EXCHANGE', {'fields': (
                        "enablemail",
                        "mail",
                    )}),
                    ('SECURITY-GROUPS', {'fields': (
                        "groups",
                    )}),
                    ('DISTRIBUTION-LIST', {'fields': (
                        "distributionlist",
                    )}),
                    ('SYSTEM', {'fields': (
                        "env",
                        "org",
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
                        "objectsid",
                        "objectguid",
                    )}),
                    ('AD-OSIRIS', {'fields': (
                    "whencreated",
                    "whenchanged",
                    "lastlogontimestamp",
                    "lastlogon",
                    "pwdlastset",
                    "badpasswordtime",
                    "msexchwhenmailboxcreated",
                    )}),
                    ('HR-ARNO', {'fields': (
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
                    )}),
                    ('IAM-EVIDIAN', {'fields': (
                    "chuidoriginsource",
                    "evdidmstate",
                    "evdpmschedulerstatus",
                    "enatelbegintime",
                    "enatelendtime",
                    )}),
                )

@admin.register(RefidIopProvMirrorAd)
class RefidIopProvMirrorAdAdmin(admin.ModelAdmin):
    list_display = (
        "samaccountname",
        "sn",
        "givenname",
        # "usualsn",
        # "usualgivenname",
        "company",
        "physicaldeliveryofficename",
        "department",
        "businesscategory",
        "employeetype",
        "preferredlanguage",
        # "quality",
        # "gender",
        # "birthdate",
        "cardtype",
        "employeenumber",
        "extensionattribute1",
        # "extensionattribute2",
        "extensionattribute11",
        "telephonenumber",
        "pager",
        # "localisation",
        # "roles",
        # "unites",
        # "specialites",
        # "homedir",
        # "homedrive",
        # "description",
        "info",
        "extensionattribute15",
        # "metadata",
        "enableaccountexpires",
        "accountexpires",
        "changepasswordatlogon",
        "enabled",
        "enablemail",
        "mail",
        # "groups",
        # "distributionlist",
        "env",
        "org",
        "src",
        # "usercre",
        # "datecre",
        "userupd",
        "dateupd",
        # "msgrefid",
        "actiontype",
        # "msgdb",
        "msgad",
        "datesyncad",
        "flagsyncad",
        "msgexchange",
        "datesyncexchange",
        "flagsyncexchange",
        # "password",
        "objectsid",
        "objectguid",
        # "rhmatricule",
        # "rhnom",
        # "rhprenom",
        # "rhsexe",
        # "rhdnais",
        # "rhlangue",
        # "rhnumcardid",
        # "rhnumnational",
        # "rhdatedeb",
        # "rhdatefin",
        # "rhstatutcontrat",
        # "rhmetadata",
    )

    list_filter = (
        "flagsyncad",
        "flagsyncexchange",
        "company",
        "physicaldeliveryofficename",
        "businesscategory",
        "employeetype",
        "department",
    )

    list_per_page = 100


    search_fields = (
        "samaccountname",
        "sn",
        "givenname",
        "company",
    )


    fieldsets = (
                    ('KEY', {'fields': (
                        "samaccountname",
                    )}),
                    ('IDENTITY', {'fields': (
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
                    )}),
                    ('HR-ARNO', {'fields': (
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
                    )}),
                    ('AD', {'fields': (
                        "homedir",
                        "homedrive",
                        "description",
                        "info",
                        "extensionattribute15",
                        "enableaccountexpires",
                        "accountexpires",
                        "changepasswordatlogon",
                        "enabled",
                    )}),
                    ('EXCHANGE', {'fields': (
                        "enablemail",
                        "mail",
                    )}),
                    ('SECURITY-GROUPS', {'fields': (
                        "groups",
                    )}),
                    ('DISTRIBUTION-LIST', {'fields': (
                        "distributionlist",
                    )}),
                    ('SYSTEM', {'fields': (
                        "env",
                        "org",
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
                        "objectsid",
                        "objectguid",
                    )}),
                )


@admin.register(RefidIopProvLogAd)
class RefidIopProvLogAdAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "samaccountname",
        "sn",
        "givenname",
        # "usualsn",
        # "usualgivenname",
        "company",
        "physicaldeliveryofficename",
        "department",
        "businesscategory",
        "employeetype",
        "preferredlanguage",
        # "quality",
        # "gender",
        # "birthdate",
        "cardtype",
        "employeenumber",
        "extensionattribute1",
        # "extensionattribute2",
        "extensionattribute11",
        "telephonenumber",
        "pager",
        # "localisation",
        # "roles",
        # "unites",
        # "specialites",
        # "homedir",
        # "homedrive",
        # "description",
        "info",
        "extensionattribute15",
        # "metadata",
        "enableaccountexpires",
        "accountexpires",
        "changepasswordatlogon",
        "enabled",
        "enablemail",
        "mail",
        # "groups",
        # "distributionlist",
        "env",
        "org",
        "src",
        # "usercre",
        # "datecre",
        "userupd",
        "dateupd",
        # "msgrefid",
        "actiontype",
        # "msgdb",
        "msgad",
        "datesyncad",
        "flagsyncad",
        "msgexchange",
        "datesyncexchange",
        "flagsyncexchange",
        # "password",
        # "objectsid",
        # "objectguid",
        # "rhmatricule",
        # "rhnom",
        # "rhprenom",
        # "rhsexe",
        # "rhdnais",
        # "rhlangue",
        # "rhnumcardid",
        # "rhnumnational",
        # "rhdatedeb",
        # "rhdatefin",
        # "rhstatutcontrat",
        # "rhmetadata",
    )

    list_filter = (
        "samaccountname",
        "sn",
        "givenname",
    )

    list_per_page = 100

    search_fields = (
        "samaccountname",
        "sn",
        "givenname",
        "company",
    )

# ================================================================================================================
# CACHE Admin
# ================================================================================================================


@admin.register(RefidIopCacheRh)
class RefidCacheRHAdmin(admin.ModelAdmin):
    list_display = (
    "v100_rh_matricule",
    "v100_rh_nom",
    "v100_rh_prenom",
    "v100_rh_sexe",
    "v100_rh_registre_national",
    "v100_rh_date_naissance",
    "v100_rh_langue",
    "v100_rh_num_carte_id",
    "v300_rh_date_debut_contrat",
    "v300_rh_date_fin_contrat",
    "v100_rh_statut_contrat",
    "v200_contrat_code_societe",
    "v955_contrat_code_profil",
    "v955_contrat_profil_fr",
    "v600_ca_ventil_qualification",
    "v600_ca_ventil_code",
    "v600_ca_ventil_fr",
    "v125_rh_inami_11",
    "rfidatesync",
    # "messages",
    )
    list_per_page = 100
    list_filter = (
        "v100_rh_statut_contrat",
        "v200_contrat_code_societe",
        "v600_ca_ventil_code",
        "v600_ca_ventil_fr",
    )


@admin.register(RefidIopCacheEvidian)
class RefidCacheEVIDIANAdmin(admin.ModelAdmin):
    list_display = (
        "cn",
        "stpadlogin",
        "employeeid",
        "stpniss",
        "stpinaminumber",
        "sn",
        "givenname",
        "osirisevidiansex",
        "stpbirthdate",
        "preferredlanguage",
        "businesscategory",
        "company",
        "physicaldeliveryofficename",
        "employeetype",
        "osirishrcontractstatus",
        "osirishrcontractstartdate",
        "osirishrcontractenddate",
        "chuidoriginsource",
        # "distinguishedname",
        # "evdidmuseridrep",
        "evdidmstate",
        "evdpmschedulerstatus",
        "whencreated",
        "whenchanged",
        "enatelbegintime",
        "enatelendtime",
        "rfidatesync",
        # "messages",
    )
    list_per_page = 100
    list_filter = (
        "company",
        "physicaldeliveryofficename",
        "employeetype",
        "osirishrcontractstatus",
        "evdidmstate",
        "evdpmschedulerstatus",
    )


@admin.register(RefidIopCacheAdOsiris)
class RefidCacheADAdmin(admin.ModelAdmin):
    list_display = (
        "samaccountname",
        "sn",
        "givenname",
        "company",
        "physicaldeliveryofficename",
        "businesscategory",
        "employeetype",
        "department",
        "preferredlanguage",
        "employeenumber",
        "extensionattribute1",
        "extensionattribute2",
        "extensionattribute10",
        "extensionattribute11",
        "telephonenumber",
        "pager",
        # "description",
        "enabled",
        # "name",
        # "cn",
        "userprincipalname",
        # "displayname",
        # "employeeid",
        "info",
        # "extensionattribute3",
        # "businessroles",
        # "homedirectory",
        # "homedrive",
        # "distinguishedname",
        # "networkdomainid",
        "objectguid",
        "objectsid",
        "whencreated",
        "whenchanged",
        # "lastlogontimestamp",
        # "lastlogon",
        # "pwdlastset",
        # "badpasswordtime",
        # "useraccountcontrol",
        "mail",
        "msexchwhenmailboxcreated",
        "rfidatesync",
        # "messages",
    )
    list_per_page = 100
    list_filter = (
        "company",
        "physicaldeliveryofficename",
        "businesscategory",
        "employeetype",
    )

# ================================================================================================================
# REFERENCE Admin
# ================================================================================================================


@admin.register(RefidIopReferences)
class RefidIopReferencesADAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "reference",
        "value",
        "flag",
        "description",
    )
    list_per_page = 100
    list_filter = (
        "reference",
    )


@admin.register(RefidIopRefadgroups)
class RefidIopRefadgroupsADAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "samaccountname",
        "distinguishedname",
        "mail",
        "groupcategory",
        "whencreated",
        "whenchanged",
        "description",
        "info",
        # "objectguid",
        # "objectsid",
        "env",
    )
    list_per_page = 100
    list_filter = (
        "samaccountname",
        "groupcategory",
    )