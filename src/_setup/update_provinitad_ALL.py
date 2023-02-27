"""
====================================================================================================
.DESCRIPTION
    Run ALL scripts to fill PROVINIT_AD

.FUNCTIONALITY
    Version	Date		Who	Comment
    -------	----		---	-------
    1.0		09/02/2023  CWY Initial Version

.COMMENTS
    update_provinitad_with_cacherh.py
    update_provinitad_with_cacheevidian.py
    update_provinitad_quality.py
    update_provinitad_cardtype.py
====================================================================================================
"""
# =========================================
# Import modules
import os
import sys
import datetime
import logging

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

logging.info(f'==> script[{os.path.basename(__file__)}]')
print(f'==> script[{os.path.basename(__file__)}]')


# =========================================
# Main

# Start Script

now_start = datetime.datetime.now()
logging.info(f"Start at : {now_start.strftime('%Y-%m-%d %H:%M:%S')}")

# Update PROVINIT to adjust some fields

os.system("python update_provinitad_with_cacherh.py")

os.system("python update_provinitad_with_cacheevidian.py")

os.system("python update_provinitad_quality.py")

os.system("python update_provinitad_cardtype.py")

# Stop Script

now_stop = datetime.datetime.now()
logging.info(f"Stop at : {now_stop.strftime('%Y-%m-%d %H:%M:%S')} ")

delta = now_stop - now_start
logging.info(f"Delta time : {delta}")


# =========================================
# End of Script

logging.info(f"<***** End of Script *****>")