#Clears full call log, should be schedualed to run yearly
import csv
FULL_CALL_LOG = "/home/pi/callerid/full_call_log.csv"
with open(FULL_CALL_LOG, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["number", "timestamp", "name"])