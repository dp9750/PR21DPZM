import csv
from collections import Counter
from collections import OrderedDict
from matplotlib import pyplot as plt


# Datoteka mora biti v enaki mapi kot Main.py
# Vrne seznam slovarjev - vsaka vrstica je svoj slovar
def read_file(filename):
    try:
        with open(filename) as file:
            reader = csv.DictReader(file, delimiter=";")
            return [row for row in reader]

    except FileNotFoundError:
        print("File {0} not found. ".format(filename))


# Parameter so prebrani podatki
# Izpiše imena atributov
def print_attributes(rows):
    for key in rows[0].keys():
        print(key)


# Parameter rows so prebrani podatki
# Pokaže graf nesreč za vsako uro
def accident_times(rows):
    hours = []
    for row in rows:
        time = row["3. Ura nesreče"]
        hour = time.split(":")[0]
        if hour:
            hours.append(hour)

    count = Counter(hours)
    count = OrderedDict(sorted(count.items(), reverse=True))

    x = [i for i in count.keys()]
    y = [i for i in count.values()]

    plt.barh(x, y)
    plt.title("Nesreče po urah")
    plt.xlabel("Št. nesreč")
    plt.ylabel("Ura")
    plt.show()


# read data
data = read_file("podatki.csv")

# print attribute names
print_attributes(data)

# plot accidents at given hour
accident_times(data)
