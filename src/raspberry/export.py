import csv
import redis

db = redis.Redis()
d = {}
l = list(db.scan_iter("windData:*"))
d = [ {"date" : key.decode("utf-8").split("windData:")[1], "value" : db.get(key).decode("utf-8")} for key in l]
d.sort(key = lambda x:x['date'])
csv_file = "data.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = ["date", "value"])
        writer.writeheader()
        for data in d:
            writer.writerow(data)
except IOError:
    print("I/O error")
