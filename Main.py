import csv


# Datoteka mora biti v enaki mapi kot Main.py
# Vrne seznam slovarjev - vsaka vrstica je svoj slovar
def read_file(filename):
    try:
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter=";")
            return [row for row in reader]

    except FileNotFoundError:
        print("File {0} not found. ".format(filename))


data = read_file("podatki.csv")
