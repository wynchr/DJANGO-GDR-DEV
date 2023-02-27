"""
=======================================================================================================================
.DESCRIPTION
    Views for REFID Application

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.01	01/01/2023  CWY	Initial Version
    1.02    12/01/2023  CWY Create & Use Custom Functions from Utils Library

.COMMENTS
    .
=======================================================================================================================
"""
import markdown as markdown

from pathlib import Path
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import RefidIopProvAdCreateForm, RefidIopProvAdUpdateForm, \
                    RefidIopProvInitAdCreateForm, RefidIopProvInitAdUpdateForm, \
                    SearchUserForm, SearchRHUserForm, SearchADUserForm, SearchEVIDIANUserForm

from .models import RefidIopProvAd, RefidIopProvInitAd, RefidIopCacheRh,  \
                    RefidIopCacheAdOsiris, RefidIopCacheEvidian

from utils.utils import gen_userid, gen_password, gen_homedir, gen_homedrive, gen_random_password, decodeB64, \
    gen_unique_reference
import ldap
from GenGroupsByRules import GenGroupsByRules

# ================================================================================================================
# INFO containing settings for pages
# ================================================================================================================

INFO = settings.INFO_APPS   # Import Settings

# ================================================================================================================
# INDEX & INFORMATION
# ================================================================================================================


@login_required
def refid_index(request):
    context = {'info': INFO}
    return render(request, "refid/refid-index.html", context)


@login_required
def refid_info_readme(request):
    README_FILE = Path(__file__).resolve().parent.parent.parent / 'readme.md'
    with open(README_FILE, 'r', encoding='utf-8') as f:
        text = f.read()
        contents = markdown.markdown(text)
    context = {'contents': contents, 'info': INFO}
    return render(request, 'refid/refid-info-readme.html', context)


@login_required
def refid_info_todo(request):
    README_FILE = Path(__file__).resolve().parent.parent.parent / 'todo.md'
    with open(README_FILE, 'r', encoding='utf-8') as f:
        text = f.read()
        contents = markdown.markdown(text)
    context = {'contents': contents, 'info': INFO}
    return render(request, 'refid/refid-info-todo.html', context)


@login_required
def refid_info_about(request):
    with open('refid/about.md', 'r', encoding='utf-8') as f:
        text = f.read()
        contents = markdown.markdown(text)
    context = {'contents': contents, 'info': INFO}
    return render(request, 'refid/refid-info-about.html', context)


@login_required
def refid_info_pdf(request, RefidIopProvAd_id):
    user = get_object_or_404(RefidIopProvAd, pk=RefidIopProvAd_id)
    context = {'user': user, 'info': INFO, 'psw': decodeB64(user.password)}

    # print(user.preferredlanguage)

    if user.preferredlanguage == 'fr':
        return render(request, 'refid/refid-info-pdf-FR.html', context)
    elif user.preferredlanguage == 'nl':
        return render(request, 'refid/refid-info-pdf-NL.html', context)
    else:
        return render(request, 'refid/refid-info-pdf-FR.html', context)

# =========================================================================================================
# APPLICATION
# =========================================================================================================

# ProvAd ==========


class RefidProvAdListView(LoginRequiredMixin, FormMixin, ListView):
    title = "Liste des utilisateurs"
    model = RefidIopProvAd
    template_name = "refid/refid-provad-list-view.html"
    form_class = SearchUserForm
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context["title"] = self.title
        context["info"] = INFO
        # print(f"Le titre est '{self.title}'")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        # print(f"form:'{str(form)}'")
        if form.is_valid():
            q_userid = form.cleaned_data['q_userid']
            q_niss = form.cleaned_data['q_niss']
            q_nom = form.cleaned_data['q_nom']
            q_prenom = form.cleaned_data['q_prenom']
            if q_nom == '**':
                queryset = RefidIopProvAd.objects.all()
            elif q_userid:
                queryset = RefidIopProvAd.objects.filter(samaccountname__icontains=q_userid)
            elif q_niss:
                queryset = RefidIopProvAd.objects.filter(employeenumber__icontains=q_niss)
            elif q_nom and q_prenom:
                queryset = RefidIopProvAd.objects.filter(sn__icontains=q_nom).filter(givenname__icontains=q_prenom)
            elif q_nom:
                queryset = RefidIopProvAd.objects.filter(sn__icontains=q_nom)
            # elif q_nom == '':
            #     queryset = RefidIopProvAd.objects.filter(sn__icontains='z')
            elif q_prenom:
                queryset = RefidIopProvAd.objects.filter(givenname__icontains=q_prenom)
            else:
                queryset = RefidIopProvAd.objects.filter(samaccountname="x")  # to retrieve no entries
            # print(f"queryset:'{str(queryset)}'")
        return queryset


class RefidProvAdCreateView(LoginRequiredMixin, CreateView):
    title = "Création d'un compte"
    model = RefidIopProvAd
    template_name = "refid/refid-provad-update-view.html"
    form_class = RefidIopProvAdCreateForm
    context_object_name = "user"
    success_url = reverse_lazy("refid-provad-list-view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        context["mode"] = "create"
        context["submit_text"] = "Créer"
        return context

    def get_initial(self):
        nom = ""
        prenom = ""

        initial = super().get_initial()
        initial['sn'] = nom
        initial['givenname'] = prenom

        initial['samaccountname'] = "*--------*"
        initial['extensionAttribute1'] = "*--------*"

        initial['enablemail'] = "0"

        initial['src'] = "REFID"
        initial['actiontype'] = "CREATE"

        initial['datesyncad'] = "-"
        initial['flagsyncad'] = ""
        initial['msgad'] = "-"

        initial['datesyncexchange'] = "-"
        initial['flagsyncexchange'] = ""
        initial['msgexchange'] = "-"
        return initial

    def form_valid(self, form):
        # print(form.cleaned_data)
        if self.request.user.is_authenticated:
            form.instance.samaccountname = gen_userid(form.instance.sn, form.instance.givenname)

            samaccountname = form.instance.samaccountname
            if len(samaccountname) != 6 and len(samaccountname) != 7:
                # print(f"samaccountname généré n'a pas 6 ou 7 lettres.:'{samaccountname}'")
                return super().form_invalid(form)

            if samaccountname:
                qs = RefidIopProvAd.objects.filter(samaccountname=samaccountname).values()
                # print(f"samaccountname:'{samaccountname}'")
                # print(f"qs:'{qs}'")
                # print(f"qs.exists():'{qs.exists()}'")
                if qs.exists():
                    # raise forms.ValidationError("samaccountname is taken")
                    # print(f"Le userId existe déjà:'{samaccountname}'")
                    return super().form_invalid(form)

            form.instance.password = gen_password(gen_random_password(12))

            form.instance.extensionattribute1 = gen_unique_reference()

            form.instance.homedir = gen_homedir(form.instance.samaccountname)
            form.instance.homedrive = gen_homedrive()

            form.instance.src = "REFID"
            form.instance.actiontype = "CREATE"

            form.instance.usercre = str(self.request.user)
            form.instance.userupd = str(self.request.user)
            form.instance.datecre = str(datetime.today())[:19]
            form.instance.dateupd = str(datetime.today())[:19]

            form.instance.flagsyncad = "0"

            if form.instance.enablemail == "1":
                form.instance.flagsyncexchange = "0"
            else:
                form.instance.flagsyncexchange = "9"

            # Fill GROUPS & DISTRIBUTIONLIST
            company = form.instance.company

            if form.instance.physicaldeliveryofficename is None:
                physicaldeliveryofficename = ''
            else:
                physicaldeliveryofficename = form.instance.physicaldeliveryofficename

            if form.instance.company.upper() == 'HUDERF':
                physicaldeliveryofficename = ''

            if form.instance.employeetype[0:7] == 'Medical':
                employeetype = 'Medical'
            else:
                employeetype = form.instance.employeetype

            print(f"\nuserid : {form.instance.samaccountname}")
            print(f"company : {company}")
            print(f"physicaldeliveryofficename : {physicaldeliveryofficename}")
            print(f"employeetype : {employeetype}\n")

            ALLDISTRIBUTIONLIST = ""
            ALLGROUPS = ""

            groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
            for group in groups:
                print(group)
                if "OU=Distribution" in group:
                    ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
                elif "OU=Applications" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                elif "OU=Security" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                else:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'

            # For Brugmann run for ALL site

            if form.instance.company.upper() == 'CHU-BRUGMANN':
                physicaldeliveryofficename = ''

            groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
            for group in groups:
                print(group)
                if "OU=Distribution" in group:
                    ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
                elif "OU=Applications" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                elif "OU=Security" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                else:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'

            print(f"\nALLGROUPS : {ALLGROUPS}")
            print(f"ALLDISTRIBUTIONLIST : {ALLDISTRIBUTIONLIST}")

            form.instance.groups = ALLGROUPS
            form.instance.distributionlist = ALLDISTRIBUTIONLIST

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("refid-provad-list-view")


class RefidProvAdUpdateView(LoginRequiredMixin, UpdateView):
    title = "Edition d'un compte"
    model = RefidIopProvAd
    template_name = "refid/refid-provad-update-view.html"
    form_class = RefidIopProvAdUpdateForm
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        context["mode"] = "update"
        context["submit_text"] = "Modifier"
        return context

    def get_success_url(self):
        return reverse("refid-provad-list-view")

    def form_valid(self, form):
        # if form.instance.enablemail == "1":
        # form.instance.mail = utils.gen_mail(form.instance.usualsn, form.instance.usualgivenname, form.instance.company)

        form.instance.homedir = gen_homedir(form.instance.samaccountname)
        form.instance.homedrive = gen_homedrive()

        form.instance.src = "REFID"
        # form.instance.actiontype = "UPDATE"

        form.instance.userupd = str(self.request.user)
        form.instance.dateupd = str(datetime.today())[:19]

        form.instance.flagsyncad = "0"

        if form.instance.enablemail == "1":
            form.instance.flagsyncexchange = "0"
        else:
            form.instance.flagsyncexchange = "9"

        # Fill GROUPS & DISTRIBUTIONLIST
        company = form.instance.company

        if form.instance.physicaldeliveryofficename is None:
            physicaldeliveryofficename = ''
        else:
            physicaldeliveryofficename = form.instance.physicaldeliveryofficename

        if form.instance.company.upper() == 'HUDERF':
            physicaldeliveryofficename = ''

        if form.instance.employeetype[0:7] == 'Medical':
            employeetype = 'Medical'
        else:
            employeetype = form.instance.employeetype

        print(f"\nuserid : {form.instance.samaccountname}")
        print(f"company : {company}")
        print(f"physicaldeliveryofficename : {physicaldeliveryofficename}")
        print(f"employeetype : {employeetype}\n")

        ALLDISTRIBUTIONLIST = ""
        ALLGROUPS = ""

        groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
        for group in groups:
            print(group)
            if "OU=Distribution" in group:
                ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
            elif "OU=Applications" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            elif "OU=Security" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            else:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'

        # For Brugmann run for ALL site

        if form.instance.company.upper() == 'CHU-BRUGMANN':
            physicaldeliveryofficename = ''

        groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
        for group in groups:
            print(group)
            if "OU=Distribution" in group:
                ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
            elif "OU=Applications" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            elif "OU=Security" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            else:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'

        print(f"\nALLGROUPS : {ALLGROUPS}")
        print(f"ALLDISTRIBUTIONLIST : {ALLDISTRIBUTIONLIST}")

        form.instance.groups = ALLGROUPS
        form.instance.distributionlist = ALLDISTRIBUTIONLIST

        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        initial['actiontype'] = "UPDATE"
        return initial

# ProvInitAd ==========


class RefidProvInitAdListView(LoginRequiredMixin, FormMixin, ListView):
    title = "Liste des utilisateurs (Reprise-Initialisation)"
    model = RefidIopProvInitAd
    template_name = "refid/refid-provinitad-list-view.html"
    form_class = SearchUserForm
    context_object_name = "users"
    # paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context["title"] = self.title
        context["info"] = INFO
        # print(f"Le titre est '{self.title}'")
        # print(f"context['form']:'{str(context['form'])}'")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        # print(f"form:'{str(form)}'")
        if form.is_valid():
            q_userid = form.cleaned_data['q_userid']
            q_niss = form.cleaned_data['q_niss']
            q_nom = form.cleaned_data['q_nom']
            q_prenom = form.cleaned_data['q_prenom']
            if q_nom == '**':
                queryset = RefidIopProvInitAd.objects.all()
            elif q_userid:
                queryset = RefidIopProvInitAd.objects.filter(samaccountname__icontains=q_userid)
            elif q_niss:
                queryset = RefidIopProvInitAd.objects.filter(employeenumber__icontains=q_niss)
            elif q_nom and q_prenom:
                queryset = RefidIopProvInitAd.objects.filter(sn__icontains=q_nom).filter(givenname__icontains=q_prenom)
            elif q_nom:
                queryset = RefidIopProvInitAd.objects.filter(sn__icontains=q_nom)
            # elif q_nom == '':
            #     queryset = RefidIopProvAd.objects.filter(sn__icontains='z')
            elif q_prenom:
                queryset = RefidIopProvInitAd.objects.filter(givenname__icontains=q_prenom)
            else:
                queryset = RefidIopProvInitAd.objects.filter(samaccountname="x")  # to retrieve no entries
            # print(f"queryset:'{str(queryset)}'")
        return queryset


class RefidProvInitAdCreateView(LoginRequiredMixin, CreateView):
    title = "Création d'un compte"
    model = RefidIopProvInitAd
    template_name = "refid/refid-provinitad-update-view.html"
    form_class = RefidIopProvInitAdCreateForm
    context_object_name = "user"
    # success_url = reverse_lazy("refid-home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        context["mode"] = "create"
        context["submit_text"] = "Créer"
        return context

    def get_initial(self):
        nom = ""
        prenom = ""

        initial = super().get_initial()
        initial['sn'] = nom
        initial['givenname'] = prenom

        initial['samaccountname'] = "*--------*"
        initial['extensionAttribute1'] = "*--------*"

        initial['enablemail'] = "0"

        initial['src'] = "REFID"
        initial['actiontype'] = "CREATE"

        initial['datesyncad'] = "-"
        initial['flagsyncad'] = ""
        initial['msgad'] = "-"

        initial['datesyncexchange'] = "-"
        initial['flagsyncexchange'] = ""
        initial['msgexchange'] = "-"
        return initial

    def form_valid(self, form):
        # print(form.cleaned_data)
        if self.request.user.is_authenticated:
            form.instance.samaccountname = gen_userid(form.instance.sn, form.instance.givenname)

            samaccountname = form.instance.samaccountname
            if len(samaccountname) != 6 and len(samaccountname) != 7:
                # print(f"samaccountname généré n'a pas 6 ou 7 lettres.:'{samaccountname}'")
                return super().form_invalid(form)

            if samaccountname:
                qs = RefidIopProvAd.objects.filter(samaccountname=samaccountname).values()
                # print(f"samaccountname:'{samaccountname}'")
                # print(f"qs:'{qs}'")
                # print(f"qs.exists():'{qs.exists()}'")
                if qs.exists():
                    # raise forms.ValidationError("samaccountname is taken")
                    # print(f"Le userId existe déjà:'{samaccountname}'")
                    return super().form_invalid(form)

            form.instance.password = gen_password(gen_random_password(12))

            form.instance.extensionattribute1 = gen_unique_reference()

            form.instance.homedir = gen_homedir(form.instance.samaccountname)
            form.instance.homedrive = gen_homedrive()

            form.instance.src = "REFID"
            form.instance.actiontype = "CREATE"

            form.instance.usercre = str(self.request.user)
            form.instance.userupd = str(self.request.user)
            form.instance.datecre = str(datetime.today())[:19]
            form.instance.dateupd = str(datetime.today())[:19]

            form.instance.flagsyncad = "0"

            if form.instance.enablemail == "1":
                form.instance.flagsyncexchange = "0"
            else:
                form.instance.flagsyncexchange = "9"

            # Fill GROUPS & DISTRIBUTIONLIST
            company = form.instance.company

            if form.instance.physicaldeliveryofficename is None:
                physicaldeliveryofficename = ''
            else:
                physicaldeliveryofficename = form.instance.physicaldeliveryofficename

            if form.instance.company.upper() == 'HUDERF':
                physicaldeliveryofficename = ''

            if form.instance.employeetype[0:7] == 'Medical':
                employeetype = 'Medical'
            else:
                employeetype = form.instance.employeetype

            print(f"\nuserid : {form.instance.samaccountname}")
            print(f"company : {company}")
            print(f"physicaldeliveryofficename : {physicaldeliveryofficename}")
            print(f"employeetype : {employeetype}\n")

            ALLDISTRIBUTIONLIST = ""
            ALLGROUPS = ""

            groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
            for group in groups:
                print(group)
                if "OU=Distribution" in group:
                    ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
                elif "OU=Applications" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                elif "OU=Security" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                else:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'

            # For Brugmann run for ALL site

            if form.instance.company.upper() == 'CHU-BRUGMANN':
                physicaldeliveryofficename = ''

            groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
            for group in groups:
                print(group)
                if "OU=Distribution" in group:
                    ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
                elif "OU=Applications" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                elif "OU=Security" in group:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'
                else:
                    ALLGROUPS += ldap.extract_samaccountname(group) + ';'

            print(f"\nALLGROUPS : {ALLGROUPS}")
            print(f"ALLDISTRIBUTIONLIST : {ALLDISTRIBUTIONLIST}")

            form.instance.groups = ALLGROUPS
            form.instance.distributionlist = ALLDISTRIBUTIONLIST

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("refid-provinitad-list-view")


class RefidProvInitAdUpdateView(LoginRequiredMixin, UpdateView):
    title = "Edition d'un compte"
    model = RefidIopProvInitAd
    template_name = "refid/refid-provinitad-update-view.html"
    form_class = RefidIopProvInitAdUpdateForm
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        context["mode"] = "update"
        context["submit_text"] = "Modifier"
        return context

    def get_initial(self):
        initial = super().get_initial()
        initial['actiontype'] = "UPDATE"
        return initial

    def form_valid(self, form):
        # if form.instance.enablemail == "1":
        # form.instance.mail = gen_mail(form.instance.usualsn, form.instance.usualgivenname, form.instance.company)

        form.instance.homedir = gen_homedir(form.instance.samaccountname)
        form.instance.homedrive = gen_homedrive()

        form.instance.src = "REFID"
        # form.instance.actiontype = "UPDATE"

        form.instance.userupd = str(self.request.user)
        form.instance.dateupd = str(datetime.today())[:19]

        form.instance.flagsyncad = "0"

        if form.instance.enablemail == "1":
            form.instance.flagsyncexchange = "0"
        else:
            form.instance.flagsyncexchange = "9"

        # Fill GROUPS & DISTRIBUTIONLIST
        company = form.instance.company

        if form.instance.physicaldeliveryofficename is None:
            physicaldeliveryofficename = ''
        else:
            physicaldeliveryofficename = form.instance.physicaldeliveryofficename

        if form.instance.company.upper() == 'HUDERF':
            physicaldeliveryofficename = ''

        if form.instance.employeetype[0:7] == 'Medical':
            employeetype = 'Medical'
        else:
            employeetype = form.instance.employeetype

        print(f"\nuserid : {form.instance.samaccountname}")
        print(f"company : {company}")
        print(f"physicaldeliveryofficename : {physicaldeliveryofficename}")
        print(f"employeetype : {employeetype}\n")

        ALLDISTRIBUTIONLIST = ""
        ALLGROUPS = ""

        groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
        for group in groups:
            print(group)
            if "OU=Distribution" in group:
                ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
            elif "OU=Applications" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            elif "OU=Security" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            else:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'

        # For Brugmann run for ALL site

        if form.instance.company.upper() == 'CHU-BRUGMANN':
            physicaldeliveryofficename = ''

        groups = GenGroupsByRules.find_rule_by_key(company, physicaldeliveryofficename, employeetype)
        for group in groups:
            print(group)
            if "OU=Distribution" in group:
                ALLDISTRIBUTIONLIST += ldap.extract_samaccountname(group) + ';'
            elif "OU=Applications" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            elif "OU=Security" in group:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'
            else:
                ALLGROUPS += ldap.extract_samaccountname(group) + ';'

        print(f"\nALLGROUPS : {ALLGROUPS}")
        print(f"ALLDISTRIBUTIONLIST : {ALLDISTRIBUTIONLIST}")

        form.instance.groups = ALLGROUPS
        form.instance.distributionlist = ALLDISTRIBUTIONLIST

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("refid-provinitad-list-view")


# ================================================================================================================
# MONITORING
# ================================================================================================================


class RefidMonitorListView(LoginRequiredMixin, ListView):
    title = "Monitor"
    model = RefidIopProvAd
    template_name = "refid/refid-monitor-list-view.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        # print(f"Le titre est '{self.title}'")
        return context


class RefidMonitorDetailView(LoginRequiredMixin, DetailView):
    title = "Monitor Detail"
    model = RefidIopProvAd
    template_name = "refid/refid-monitor-detail-view.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        # print(f"Le titre est '{self.title}'")
        return context


@login_required
def refid_monitor_compare(request):
    context = {'info': INFO}
    return render(request, 'refid/refid-monitor-compare.html', context)


@login_required
def refid_monitor_log(request):
    file = r"\\brdev01\d$\DEV\PS\PROJETS\REFID\LOG\DEV\OSIRIS\REFID_PROV_AD_Service_DEV_OSIRIS_2023-01-25.log"
    text = ""
    with open(file, 'tr') as f:
        for line in f:
            text += line
    f.close()
    context = {'contents': text, 'info': INFO}
    return render(request, 'refid/refid-monitor-log.html', context)


# =========================================================================================================
# CACHE
# =========================================================================================================

# Cache RH ==========

class RefidCacheRHListView(LoginRequiredMixin, FormMixin, ListView):
    title = "Cache RH"
    model = RefidIopCacheRh
    template_name = "refid/refid-cacherh-list-view.html"
    context_object_name = "users"
    form_class = SearchRHUserForm

    @staticmethod
    def show_message(request, message):
        messages.add_message(request, messages.SUCCESS, message)

    # def form_valid(self, form):
    #     print("form_valid")
    #     self.show_message(self, 'This request can take a little time.')
    #     return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context["title"] = self.title
        context["info"] = INFO
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        # print(f"form:'{str(form)}'")
        if form.is_valid():
            q_matricule = form.cleaned_data['q_matricule']
            q_niss = form.cleaned_data['q_niss']
            q_nom = form.cleaned_data['q_nom']
            q_prenom = form.cleaned_data['q_prenom']
            if q_nom == '**':
                queryset = RefidIopCacheRh.objects.all()
            elif q_matricule:
                queryset = RefidIopCacheRh.objects.filter(v100_rh_matricule__icontains=q_matricule)
            elif q_niss:
                queryset = RefidIopCacheRh.objects.filter(v100_rh_registre_national__icontains=q_niss)
            elif q_nom and q_prenom:
                queryset = RefidIopCacheRh.objects.filter(v100_rh_nom__icontains=q_nom).filter(v100_rh_prenom__icontains=q_prenom)
            elif q_nom:
                queryset = RefidIopCacheRh.objects.filter(v100_rh_nom__icontains=q_nom)
            elif q_prenom:
                queryset = RefidIopCacheRh.objects.filter(v100_rh_prenom__icontains=q_prenom)
            else:
                queryset = RefidIopCacheRh.objects.filter(v100_rh_matricule="*")  # to retrieve no entries
            # print(f"queryset:'{str(queryset)}'")
        return queryset


class RefidCacheRHDetailView(LoginRequiredMixin, DetailView):
    title = "Cache RH Detail"
    model = RefidIopCacheRh
    template_name = "refid/refid-cacherh-detail-view.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        # print(f"Le titre est '{self.title}'")
        return context

# Cache AD ==========


class RefidCacheADListView(LoginRequiredMixin, FormMixin, ListView):
    title = "Cache AD"
    model = RefidIopCacheAdOsiris
    template_name = "refid/refid-cachead-list-view.html"
    context_object_name = "users"
    form_class = SearchADUserForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context["title"] = self.title
        context["info"] = INFO
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        # print(f"form:'{str(form)}'")
        if form.is_valid():
            q_userid = form.cleaned_data['q_userid']
            q_niss = form.cleaned_data['q_niss']
            q_nom = form.cleaned_data['q_nom']
            q_prenom = form.cleaned_data['q_prenom']
            if q_nom == '**':
                queryset = RefidIopCacheAdOsiris.objects.all()
            elif q_userid:
                queryset = RefidIopCacheAdOsiris.objects.filter(samaccountname__icontains=q_userid)
            elif q_niss:
                queryset = RefidIopCacheAdOsiris.objects.filter(employeenumber__icontains=q_niss)
            elif q_nom and q_prenom:
                queryset = RefidIopCacheAdOsiris.objects.filter(sn__icontains=q_nom).filter(givenname__icontains=q_prenom)
            elif q_nom:
                queryset = RefidIopCacheAdOsiris.objects.filter(sn__icontains=q_nom)
            elif q_prenom:
                queryset = RefidIopCacheAdOsiris.objects.filter(givenname__icontains=q_prenom)
            else:
                queryset = RefidIopCacheAdOsiris.objects.filter(samaccountname__icontains="*")  # to retrieve no entries
            # print(f"queryset:'{str(queryset)}'")
        return queryset


class RefidCacheADDetailView(LoginRequiredMixin, DetailView):
    title = "Cache AD Detail"
    model = RefidIopCacheAdOsiris
    template_name = "refid/refid-cachead-detail-view.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        # print(f"Le titre est '{self.title}'")
        return context

# Cache EVIDIAN ==========


class RefidCacheEVIDIANListView(LoginRequiredMixin, FormMixin, ListView):
    title = "Cache EVIDIAN"
    model = RefidIopCacheEvidian
    template_name = "refid/refid-cacheevidian-list-view.html"
    context_object_name = "users"
    form_class = SearchEVIDIANUserForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context["title"] = self.title
        context["info"] = INFO
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.form_class(self.request.GET)
        # print(f"form:'{str(form)}'")
        if form.is_valid():
            q_userid = form.cleaned_data['q_userid']
            q_niss = form.cleaned_data['q_niss']
            q_nom = form.cleaned_data['q_nom']
            q_prenom = form.cleaned_data['q_prenom']
            if q_nom == '**':
                queryset = RefidIopCacheEvidian.objects.all()
            elif q_userid:
                queryset = RefidIopCacheEvidian.objects.filter(stpadlogin__icontains=q_userid)
            elif q_niss:
                queryset = RefidIopCacheEvidian.objects.filter(stpniss__icontains=q_niss)
            elif q_nom and q_prenom:
                queryset = RefidIopCacheEvidian.objects.filter(sn__icontains=q_nom).filter(givenname__icontains=q_prenom)
            elif q_nom:
                queryset = RefidIopCacheEvidian.objects.filter(sn__icontains=q_nom)
            elif q_prenom:
                queryset = RefidIopCacheEvidian.objects.filter(givenname__icontains=q_prenom)
            else:
                queryset = RefidIopCacheEvidian.objects.filter(stpadlogin="*")  # to retrieve no entries
            # print(f"queryset:'{str(queryset)}'")
        return queryset


class RefidCacheEVIDIANDetailView(LoginRequiredMixin, DetailView):
    title = "Cache EVIDIAN Detail"
    model = RefidIopCacheEvidian
    template_name = "refid/refid-cacheevidian-detail-view.html"
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context["info"] = INFO
        # print(f"Le titre est '{self.title}'")
        return context


# ================================================================================================================
# Function Handle Errors pages
# ================================================================================================================


def error_500(request):
    return render(request, '500.html')


def error_404(request, exception):
    print(exception)
    return render(request, '404.html')

# ================================================================================================================
# TESTS
# ================================================================================================================





# ================================================================================================================
# Function NO MORE USED (Staying for examples)
# ================================================================================================================


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# @login_required
# def refid_provad_create(request):
#     if request.method == "POST":
#         form = RefidIopProvAdForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             if request.user.is_authenticated:
#                 RefidIopProvAd = form.save(commit=False)
#                 RefidIopProvAd.extensionattribute2 = "IN"
#                 RefidIopProvAd.homedir = str(request.user)
#                 RefidIopProvAd.homedrive = "\\chu-brugmann\share\home\"{}".format(RefidIopProvAd.samaccountname)
#                 RefidIopProvAd.usercre = str(request.user)
#                 RefidIopProvAd.userupd = str(request.user)
#                 RefidIopProvAd.datecre = str(datetime.today())[:19]
#                 RefidIopProvAd.dateupd = str(datetime.today())[:19]
#                 RefidIopProvAd.flagsyncad = "0"
#                 RefidIopProvAd.flagsyncexchange = "0"
#                 RefidIopProvAd.save()
#
#                 # print(type(RefidIopProvAd))
#                 print(RefidIopProvAd)
#
#             # return HttpResponse("Merci de vous être inscrit au site.")
#             return HttpResponseRedirect(request.path)
#     else:
#         if request.user.is_authenticated:
#             init_values = {}
#             init_values["samaccountname"] = "ZZCHRIS"
#             init_values["sn"] = "ZZWyns"
#             init_values["givenname"] = "Chris"
#             init_values["password"] = "UABhAHMAcwB3AEAAcgBkADAAMQAoACkA"
#             init_values["enablemail"] = "1"
#             init_values["mail"] = "zzchris@chu-brugmann.be"
#             init_values["groups"] = "CN=REFID_Administratif,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be"
#             init_values["distributionlist"] = "CN=REFID - Distribution List for IT,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be"
#             init_values["homedir"] = r"\\chu-brugmann\share\home\ZZCHRIS"
#             init_values["homedrive"] = "H:"
#             init_values["usercre"] = request.user
#             init_values["userupd"] = request.user
#             init_values["datecre"] = str(datetime.today())[:19]
#             init_values["dateupd"] = str(datetime.today())[:19]
#             form = RefidIopProvAdForm(initial=init_values)
#             return render(request, "refid/refid-provad-create.html", {"form": form, 'info': INFO})


# def refid_monitor_list(request):
#     monitor_list = RefidIopProvAd.objects.all()
#     context = {'monitor_list': monitor_list, 'info': INFO}
#     return render(request, 'refid/refid-monitor-list.html', context)


# def refid_monitor_detail(request, RefidIopProvAd_id):
#     user = get_object_or_404(RefidIopProvAd, pk=RefidIopProvAd_id)
#     context = {'user': user, 'info': INFO}
#     return render(request, 'refid/refid-monitor-detail.html', context)


# def refid_test_form(request):
#     context = {'info': INFO, 'user': user}
#     return render(request, "refid/refid-test-form.html", context)

# class TestView(LoginRequiredMixin, View):
#     title = "Default Title"
#
#     def get(self, request):
#         print(f"Le titre est '{self.title}'")
#         context = {'info': INFO}
#         return render(request, 'refid/refid-home.html', context)
#
#     def post(self, request):
#         pass
#
#
# class TestTemplateView(LoginRequiredMixin, TemplateView):
#     template_name = 'refid/refid-home.html'
#     title = "Default"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["info"] = INFO
#         context["title"] = self.title
#         return context
#

#
# def refid_search(request):
#     form = SearchForm(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['query']
#         results = RefidIopProvAd.objects.filter(company__contains=query)
#         return render(request, 'refid/refid-search.html', {'results': results})
#     else:
#         return render(request, 'refid/refid-search.html', {'form': form})
#
#
# class SearchView(FormView):
#     template_name = 'refid/refid-search-cbv.html'
#     form_class = SearchForm
#     success_url = '/search-results/'
#
#     def form_valid(self, form):
#         query = form.cleaned_data['query']
#         results = RefidIopProvAd.objects.filter(company__contains=query)
#         return render(self.request, 'refid/refid-search-cbv.html', {'results': results})
#
#
# def test_markdown_view(request):
#     form = MarkdownForm(request.POST or None)
#     if form.is_valid():
#         content = form.cleaned_data['content']
#         return render(request, 'refid/test-markdown-template.html', {'content': content})
#     return render(request, 'refid/test-markdown-template.html', {'form': form})
# EOF ---------------------------------------------------------------
