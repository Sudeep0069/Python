import csv
data = [
    {"Name": "Alice", "Age": 20, "Grade": "A"},
    {"Name": "Bob", "Age": 21, "Grade": "B"},
    {"Name": "Charlie", "Age": 19, "Grade": "A+"}
]
with open("students.csv", "w", newline="") as f:
    fields = ["Name", "Age", "Grade"]
    
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

with open("students.csv",'r') as f2:
  rd=csv.DictReader(f2)
  for i in rd:
    if int(i["Age"])>19:
       print(i["Name"],":",i["Age"])
