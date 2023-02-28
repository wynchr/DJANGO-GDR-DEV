"""
====================================================================================================
.DESCRIPTION
    Run ALL scripts to create CACHEs and PROV Tables
    REPRISE

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		09/02/2023  CWY Initial Version

.COMMENTS
    # ========================================================================
    # CACHE
    # ========================================================================

    # Reload CACHE RH
    os.system("python create_REFID_IOP_CACHE_RH.py %s" % filename)
    os.system("python sync_REFID_IOP_CACHE_RH.py %s" % filename)

    # Reload CACHE AD
    os.system("python create_REFID_IOP_CACHE_AD_OSIRIS.py %s" % filename)
    os.system("python sync_REFID_IOP_CACHE_AD.py %s" % filename)

    # Reload CACHE EVIDIAN
    os.system("python create_REFID_IOP_CACHE_EVIDIAN.py %s" % filename)
    os.system("python sync_REFID_IOP_CACHE_EVIDIAN.py %s" % filename)

    # ========================================================================
    # PROV INIT
    # ========================================================================

    # Reload PROVINIT AD (no more in PRODUCTION)
    os.system("python create_REFID_IOP_PROVINIT_AD.py %s" % filename)
    os.system("python sync_REFID_IOP_PROVINIT_AD.py %s" % filename)

    # ========================================================================
    # PROV LIVE
    # ========================================================================

    # Reload PROV AD (One time & no more in PRODUCTION)
    os.system("python create_REFID_IOP_PROV_AD.py %s" % filename)

    # Reload PROVLOG AD (no more in PRODUCTION)
    os.system("python create_REFID_IOP_PROVLOG_AD.py %s" % filename)

    # Reload PROVMIRROR AD (no more in PRODUCTION)
    os.system("python create_REFID_IOP_PROVMIRROR_AD.py %s" % filename)
    os.system("python sync_REFID_IOP_PROVMIRROR_AD.py %s" % filename)

    # ========================================================================
    # PROV AddOns
    # ========================================================================

    # Update PROVINIT to adjust some fields (no more in PRODUCTION)
    os.system("python update_provinitad_with_cacherh.py %s" % filename)
    os.system("python update_provinitad_with_cacheevidian.py %s" % filename)
    os.system("python update_provinitad_quality.py %s" % filename)
    os.system("python update_provinitad_cardtype.py %s" % filename)

    # ========================================================================
    # REFERENCES
    # ========================================================================

    # Create REFADGROUPS/REFERENCE/SECURITY/SETTINGS  (no more in PRODUCTION)
    # os.system("python create_REFID_IOP_REFADGROUPS_CWY.py %s" % filename)
    # os.system("python sync_REFID_IOP_REFADGROUPS_CWY.py %s" % filename)
    # os.system("python create_REFID_IOP_REFADGROUPS.py %s" % filename)
    # os.system("python sync_REFID_IOP_REFADGROUPS.py %s" % filename)

    # Create REFERENCE/SECURITY/SETTINGS  (no more in PRODUCTION)
    # os.system("python create_REFID_IOP_REFERENCES.py %s" % filename)
    # os.system("python create_REFID_IOP_SECURITY.py %s" % filename)
    # os.system("python create_REFID_IOP_SETTINGS.py %s" % filename)
====================================================================================================
"""
# =========================================
# Import modules
import os
import sys
import datetime
import logging

from config.config import Config
from sendmail import sendmailhtmlwithattach

CUR_DIR = os.path.dirname(__file__)
config_start = Config()

# =========================================
# Init Logging

# check if argument is passed
if len(sys.argv) > 1:
    # the first argument is the script name, so we start from the second argument
    filename = sys.argv[1]
    # print("filename:", filename)
else:
    # print("No arguments passed - Create a new filename")
    folder_path = f"../_log/{datetime.datetime.now().strftime('%Y-%m-%d')}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filename = f"{folder_path}/refid_sync_{datetime.datetime.now().strftime('%H%M%S')}.log"

logging.basicConfig(level=logging.DEBUG,
                    format='%(process)d:%(name)s ; %(asctime)s ; %(levelname)s ; %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename=filename,
                    filemode='a'
                    )

# =========================================
# Init Global Variables

logging.info(f'*****> script[{os.path.basename(__file__)}]')
print(f'*****> script[{os.path.basename(__file__)}]')


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

# ========================================================================
# CACHE
# ========================================================================

# Reload CACHE RH
os.system("python create_REFID_IOP_CACHE_RH.py %s" % filename)
os.system("python sync_REFID_IOP_CACHE_RH.py %s" % filename)

# Reload CACHE AD
os.system("python create_REFID_IOP_CACHE_AD_OSIRIS.py %s" % filename)
os.system("python sync_REFID_IOP_CACHE_AD.py %s" % filename)

# Reload CACHE EVIDIAN
os.system("python create_REFID_IOP_CACHE_EVIDIAN.py %s" % filename)
os.system("python sync_REFID_IOP_CACHE_EVIDIAN.py %s" % filename)

# ========================================================================
# PROV INIT
# ========================================================================

# Reload PROVINIT AD (no more in PRODUCTION)
# os.system("python create_REFID_IOP_PROVINIT_AD.py %s" % filename)
# os.system("python sync_REFID_IOP_PROVINIT_AD.py %s" % filename)

# ========================================================================
# PROV LIVE
# ========================================================================

# Reload PROV AD (One time & no more in PRODUCTION)
os.system("python create_REFID_IOP_PROV_AD.py %s" % filename)
if config_start.get_env() == 'PROD':
    os.system("python sync_REFID_IOP_PROV_AD.py %s" % filename)     # Only at ACTIVATION IN PROD

# Reload PROVLOG AD (no more in PRODUCTION)
os.system("python create_REFID_IOP_PROVLOG_AD.py %s" % filename)

# Reload PROVMIRROR AD (no more in PRODUCTION)
os.system("python create_REFID_IOP_PROVMIRROR_AD.py %s" % filename)
# os.system("python sync_REFID_IOP_PROVMIRROR_AD.py %s" % filename)

# ========================================================================
# PROV AddOns
# ========================================================================

# Update PROV to adjust some fields (no more in PRODUCTION)
# os.system("python update_provad_with_cacherh.py %s" % filename)
# os.system("python update_provad_with_cacheevidian.py %s" % filename)
# os.system("python update_provad_quality.py %s" % filename)
# os.system("python update_provad_cardtype.py %s" % filename)

# Update PROVINIT to adjust some fields (no more in PRODUCTION)
# os.system("python update_provinitad_with_cacherh.py %s" % filename)
# os.system("python update_provinitad_with_cacheevidian.py %s" % filename)
# os.system("python update_provinitad_quality.py %s" % filename)
# os.system("python update_provinitad_cardtype.py %s" % filename)

# ========================================================================
# REFERENCES
# ========================================================================

# Create REFADGROUPS/REFERENCE/SECURITY/SETTINGS  (no more in PRODUCTION)
# os.system("python create_REFID_IOP_REFAD_GROUPS_RULES.py %s" % filename)
# os.system("python create_REFID_IOP_REFADGROUPS.py %s" % filename)
# os.system("python sync_REFID_IOP_REFADGROUPS.py %s" % filename)
# os.system("python create_REFID_IOP_REFADGROUPS_CWY.py %s" % filename)
# os.system("python sync_REFID_IOP_REFADGROUPS_CWY.py %s" % filename)


# Create REFERENCE/SECURITY/SETTINGS  (no more in PRODUCTION)
# os.system("python create_REFID_IOP_REFERENCES.py %s" % filename)
# os.system("python create_REFID_IOP_SECURITY.py %s" % filename)
# os.system("python create_REFID_IOP_SETTINGS.py %s" % filename)


# Stop Script

now_stop = datetime.datetime.now()
logging.info(f"Stop at : {now_stop.strftime('%Y-%m-%d %H:%M:%S')} ")

delta = now_stop - now_start
logging.info(f"Delta time : {delta}")

# Send Mail for Stop

sender = 'refid.planb@chu-brugmann.be'
recipient = 'christian.wyns@chu-brugmann.be'
subject = 'REFID Start run_all_scripts'

html = '<html><body><h1>Stop run_all_scripts</h1></body></html>'
# filename = filename
sendmailhtmlwithattach(sender, recipient, subject, html, filename)

# =========================================
# End of Script

logging.info(f"<***** End of Script *****>")
print(f"<***** End of Script *****>")
