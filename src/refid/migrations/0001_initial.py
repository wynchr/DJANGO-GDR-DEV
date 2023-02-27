# Generated by Django 4.1.4 on 2023-01-04 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RefidIopProvAd',
            fields=[
                ('samaccountname', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sn', models.CharField(blank=True, max_length=50, null=True)),
                ('givenname', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, choices=[('CHU-BRUGMANN', 'CHU-BRUGMANN'), ('HUDERF', 'HUDERF')], max_length=50, null=True)),
                ('physicaldeliveryofficename', models.CharField(blank=True, choices=[('Astrid', 'Astrid'), ('Brien', 'Brien'), ('Horta', 'Horta')], max_length=50, null=True)),
                ('businesscategory', models.CharField(blank=True, choices=[('INDIVIDUAL', 'INDIVIDUAL'), ('Named', 'Named'), ('PG', 'PG'), ('at60', 'at60'), ('external', 'external'), ('interim', 'interim'), ('internal', 'internal'), ('pg', 'pg'), ('students', 'students'), ('volunteers', 'volunteers')], max_length=20, null=True)),
                ('employeetype', models.CharField(blank=True, choices=[('Administratif', 'Administratif'), ('Medical', 'Medical'), ('Nursing', 'Nursing'), ('Other', 'Other'), ('Ouvrier', 'Ouvrier'), ('Paramedical', 'Paramedical'), ('Technique', 'Technique'), ('Unknown', 'Unknown')], max_length=20, null=True)),
                ('department', models.CharField(blank=True, choices=[('Achats', 'Achats'), ('Anesthésie', 'Anesthésie'), ('Cardiologie', 'Cardiologie'), ('Centrale électrique', 'Centrale électrique'), ('Chirurgie', 'Chirurgie'), ('Chirurgie Vasculaire', 'Chirurgie Vasculaire'), ('Comptabilité', 'Comptabilité'), ('Consultations', 'Consultations'), ('Dialyse', 'Dialyse'), ('Direction Secrétariat', 'Direction Secrétariat'), ('Direction département infirmier et paramédical', 'Direction département infirmier et paramédical'), ('Direction financière', 'Direction financière'), ('Diététique', 'Diététique'), ('Facturation', 'Facturation'), ('Gastro', 'Gastro'), ('HUDE', 'HUDE'), ('Informatique', 'Informatique'), ('Labo Sommeil', 'Labo Sommeil'), ('Laboratoire', 'Laboratoire'), ('Maintenance', 'Maintenance'), ('Nourissons', 'Nourissons'), ('Nursing', 'Nursing'), ('Néo-Natal', 'Néo-Natal'), ('Néphrologie', 'Néphrologie'), ('O.R.L.', 'O.R.L.'), ('Oncologie', 'Oncologie'), ('Pharmacie', 'Pharmacie'), ('Pneumologie', 'Pneumologie'), ('Polyclinique', 'Polyclinique'), ('Psychiatrie', 'Psychiatrie'), ('Radiologie', 'Radiologie'), ('Revalidation Neurologique', 'Revalidation Neurologique'), ('Rhumatologie', 'Rhumatologie'), ('Secrétariat Polyclinique', 'Secrétariat Polyclinique'), ('Secrétariat médical', 'Secrétariat médical'), ('Service GRH', 'Service GRH'), ('Stomatologie', 'Stomatologie'), ('Tarification', 'Tarification'), ('Trésorerie', 'Trésorerie'), ('Urgences', 'Urgences')], max_length=50, null=True)),
                ('preferredlanguage', models.CharField(blank=True, choices=[('fr', 'fr'), ('nl', 'nl'), ('en', 'en'), ('de', 'de')], max_length=2, null=True)),
                ('employeenumber', models.CharField(blank=True, max_length=30, null=True)),
                ('extensionattribute1', models.CharField(blank=True, max_length=30, null=True)),
                ('extensionattribute2', models.CharField(blank=True, choices=[('IN', 'IN'), ('OUT', 'OUT'), ('EXT', 'EXT'), ('NEW', 'NEW'), ('UKN', 'UKN')], max_length=3, null=True)),
                ('extensionattribute11', models.CharField(blank=True, max_length=11, null=True)),
                ('telephonenumber', models.CharField(blank=True, max_length=50, null=True)),
                ('pager', models.CharField(blank=True, max_length=20, null=True)),
                ('roles', models.CharField(blank=True, default='NA', max_length=200, null=True)),
                ('unites', models.CharField(blank=True, default='NA', max_length=200, null=True)),
                ('specialites', models.CharField(blank=True, default='NA', max_length=200, null=True)),
                ('homedir', models.CharField(blank=True, max_length=200, null=True)),
                ('homedrive', models.CharField(blank=True, max_length=5, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('info', models.CharField(blank=True, max_length=50, null=True)),
                ('extensionattribute15', models.CharField(blank=True, default='REFID-User', max_length=50, null=True)),
                ('enableaccountexpires', models.CharField(blank=True, choices=[('0', 'FALSE'), ('1', 'TRUE')], default='1', max_length=1, null=True)),
                ('accountexpires', models.CharField(blank=True, max_length=20, null=True)),
                ('changepasswordatlogon', models.CharField(blank=True, choices=[('0', 'FALSE'), ('1', 'TRUE')], default='1', max_length=1, null=True)),
                ('enabled', models.CharField(blank=True, choices=[('0', 'FALSE'), ('1', 'TRUE')], default='1', max_length=1, null=True)),
                ('enablemail', models.CharField(blank=True, choices=[('0', 'FALSE'), ('1', 'TRUE')], default='0', max_length=1, null=True)),
                ('mail', models.CharField(blank=True, default='xxx@chu-brugmann.be', max_length=100, null=True)),
                ('groups', models.CharField(blank=True, choices=[('CN=REFID_Administratif,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be', 'REFID_Administratif'), ('CN=REFID_Medecin,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be', 'REFID_Medecin'), ('CN=REFID_Nursing,OU=REFID,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be', 'REFID_Nursing')], max_length=4000, null=True)),
                ('distributionlist', models.CharField(blank=True, choices=[('CN=REFID - Distribution List for IT,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be', 'REFID - Distribution List for IT'), ('CN=REFIDT - Test DL,OU=Distribution Group,OU=Exchange,OU=Applications,OU=Groups,OU=TESTOSIRIS,DC=chu-brugmann,DC=be', 'REFIDT - Test DL')], max_length=4000, null=True)),
                ('env', models.CharField(blank=True, default='DEV', max_length=10, null=True)),
                ('org', models.CharField(blank=True, default='OSIRIS', max_length=10, null=True)),
                ('usercre', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('datecre', models.CharField(blank=True, default='-', max_length=20, null=True)),
                ('userupd', models.CharField(blank=True, default='-', max_length=10, null=True)),
                ('dateupd', models.CharField(blank=True, default='-', max_length=20, null=True)),
                ('msgrefid', models.CharField(blank=True, default='Hello REFID', max_length=500, null=True)),
                ('actiontype', models.CharField(blank=True, choices=[('CREATE', 'CREATE'), ('UPDATE', 'UPDATE'), ('ENABLE', 'ENABLE'), ('DISABLE', 'DISABLE'), ('SETEXPIRATION', 'SETEXPIRATION'), ('CLEAREXPIRATION', 'CLEAREXPIRATION'), ('RESETPASSWORD', 'RESETPASSWORD')], max_length=15, null=True)),
                ('msgdb', models.CharField(blank=True, default='Hello DB', max_length=500, null=True)),
                ('msgad', models.CharField(blank=True, default='Message from AD', max_length=500, null=True)),
                ('datesyncad', models.CharField(blank=True, default='1900-01-01 01:01:01', max_length=20, null=True)),
                ('flagsyncad', models.CharField(blank=True, choices=[('0', 'PENDING'), ('1', 'INTEGRATED'), ('2', 'ERROR'), ('9', 'UNCOMPLETED')], default='9', max_length=1, null=True)),
                ('msgexchange', models.CharField(blank=True, default='Message from EXCHANGE', max_length=500, null=True)),
                ('datesyncexchange', models.CharField(blank=True, default='1900-01-01 01:01:01', max_length=20, null=True)),
                ('flagsyncexchange', models.CharField(blank=True, choices=[('0', 'PENDING'), ('1', 'INTEGRATED'), ('2', 'ERROR'), ('9', 'UNCOMPLETED')], default='9', max_length=1, null=True)),
                ('objectsid', models.CharField(blank=True, default='Wait AD return', max_length=50, null=True)),
                ('objectguid', models.CharField(blank=True, default='Wait AD return', max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'ProvAdUser',
                'db_table': 'refid_iop_prov_ad',
                'ordering': ['flagsyncad', 'samaccountname'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField(verbose_name='date created')),
            ],
            options={
                'db_table': 'z_temp_user',
            },
        ),
    ]
