# module for saving data to csv
from datetime import datetime
import csv
from tabulate import tabulate

def log(temp, path):   
    try:
        with open(path, mode = 'a', newline="") as csvfile:

            # Writing into the file
            wtr = csv.writer(csvfile, delimiter=',', quotechar= '"',quoting= csv.QUOTE_MINIMAL)
            
            now = datetime.now()
            date_str = now.date().isoformat()
            time_str = now.time().isoformat(timespec="seconds")

            wtr.writerow([date_str,time_str,temp])
                
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as err:
        print(f"Unknown error : {err}")



# read the log
def show_log(path):
    with open(path, mode = 'r', newline='') as readings: 
        csv_reader = csv.reader(readings, delimiter=',')
        table = list(csv_reader)
        print(tabulate(table, headers="firstrow", tablefmt="grid"))
