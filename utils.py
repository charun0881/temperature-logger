# module for helper functions
import os
import csv
fileName = "readings.csv"
base_dir = os.path.dirname(os.path.abspath(__file__))
# filePath = os.getcwd()
path = os.path.join(base_dir, fileName)


def init_csv():
    # Checking if the file exists
    if os.path.exists(path):
        print("file exists.")
        print("appending new measurements...")
    else:
        try: 
            with open(path, mode= 'w', newline='') as csvfile:
                wtr = csv.writer(csvfile, delimiter=',', quotechar= '"',quoting= csv.QUOTE_MINIMAL)
                wtr.writerow(["Date", "Time", "Temperature"])
        except Exception as err:
            print(f"Unknown Error : {err}")
        finally: 
            print("File checked or created..")
    return path
        