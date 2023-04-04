import csv, sys

try:
    if len(sys.argv) <3:
        print("Too few command-line arguments")
    if len(sys.argv) >3:
        print("Too many command-line arguments")
    else:
        with open(sys.argv[1], "r"  ) as before:
             reader = csv.DictReader(before)
             
             with open(sys.argv[2], "w", newline="") as after:
                field_names=["first", "lastname", "house"]
                writer = csv.DictWriter(after, fieldnames=field_names)
                writer.writeheader()
                for row in reader:
                    dict= {}
                    first, lastname = row["name"].split(",")
                    house = row["house"]
                    dict["first"] = first
                    dict["lastname"] = lastname
                    dict["house"] = house
                    writer.writerow(dict)
except FileNotFoundError:
    print("Could not read ")                           