from Bio.PDB import *
import math
import csv
import os
import sys

import itertools

sys.path.append(os.getcwd() + "/Machine_Learning")

from models import *
from contacts import *

'''
cwd = os.getcwd()
parser = PDBParser(PERMISSIVE=True, QUIET=True)
# struct = parser.get_structure(pdbFile, cwd + "/PRODIGY_Dataset/" + pdbFile + ".pdb")
struct = parser.get_structure(
    "1an1", cwd + "\\PPI_Dataset\\pdb" + "1an1" + ".ent")
print(str(list(struct)))
'''


def getProdigyData():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data_2.txt", 'a')
    with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                calculateCA(row[0][0:4], 10, 5, True, "A", "B",
                            cwd + "\\Machine_Learning\\prodigy_data_2.txt")
                f.write(str(row[3]) + "\n")
                f.flush()
            line_count += 1
    f.close()

# print input parameters and experimental affinity to data file from the PPI Affinity dataset for machine learning

# outdated
def getPPIData():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\ppi_data.txt", 'a')
    with open(cwd + "\\PPI_Dataset\\SI-File-4-protein-protein-test-set-2.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0 and os.path.isfile(cwd + "/PPI_Dataset/pdb" + row[0] + ".ent"):
                calculate(row[0], 10, False, "A", "B", cwd +
                          "\\Machine_Learning\\ppi_data.txt")
                f.write(str(row[1]) + "\n")
                f.flush()
            line_count += 1
    f.close()

# print input parameters and experimental affinity to data file from the SKEMPI dataset for machine learning

# outdated
def getSKEMPIData():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\skempi_data.txt", 'a')
    with open(cwd + "\\SKEMPI_Dataset\\skempi.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        pdbs = set()
        for row in csv_reader:
            if line_count != 0 and row[0][0:4] not in pdbs:
                pdbs.add(row[0][0:4])
                calculate(row[0][0:4], 10, True, row[0].split("_")[1], row[0].split(
                    "_")[2], cwd + "\\Machine_Learning\\skempi_data.txt")
                f.write(str(row[8]) + "\n")
                f.flush()
            line_count += 1
    f.close()


def getPDBData():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data_2.txt", 'a')
    with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                calculateCA(row[0][0:4], 10, 5, True, "A", "B",
                            cwd + "\\Machine_Learning\\prodigy_data_2.txt")
                f.write(str(row[3]) + "\n")
                f.flush()
            line_count += 1
    f.close()


def loopProdigy():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data_2.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    for dist in range(1, 30):
        o.write(str(dist) + "\t")
        o.flush()
        with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
            f.truncate(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    calculate(row[0][0:4], 0, dist, True, "A", "B",
                              cwd + "\\Machine_Learning\\prodigy_data_2.txt")
                    f.write(str(row[3]) + "\n")
                    f.flush()
                line_count += 1
            train()
    f.close()
    o.close()


def loopSKEMPI():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\skempi_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    for dist in range(10, 11):
        o.write(str(dist) + "\t")
        o.flush()
        with open(cwd + "\\SKEMPI_Dataset\\skempi.csv") as csv_file:
            f.truncate(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            pdbs = set()
            for row in csv_reader:
                try:
                    if line_count != 0 and row[0][0:4] not in pdbs and float(row[8]) and row[0][0:4] != "1KBH" and len(row[0]) == 8:
                        pdbs.add(row[0][0:4])
                        calculateSKEMPI(row[0][0:4], 0, dist, True, row[0].split("_")[1], row[0].split("_")[2], cwd + "\\Machine_Learning\\skempi_data.txt")
                        # f.write(row[8])
                        f.write(
                            str(math.log(float(row[8]))*298*0.001987204) + "\n")
                        f.flush()
                except ValueError:
                    continue
                line_count += 1

        train(1)
    f.close()
    o.close()


def loopPPI():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\ppi_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    for dist in range(1, 30):
        o.write(str(dist) + "\t")
        o.flush()
        with open(cwd + "\\PPI_Dataset\\set_4.csv") as csv_file:
            f.truncate(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0 and os.path.isfile(cwd + "/PPI_Dataset/pdb" + row[0] + ".ent"):
                    calculate(row[0], 0, dist, False, "A", "B",
                              cwd + "\\Machine_Learning\\ppi_data.txt")
                    f.write(str(row[1]) + "\n")
                    f.flush()
                line_count += 1
        train()
    f.close()
    o.close()


def loopProdigyContacts():
    cwd = os.getcwd()
    with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                calculateHeavy(row[0][0:4], 0, 10, True, "A", "B", cwd +
                               "\\Machine_Learning\\PRODIGY_contacts_by_res\\" + row[0][0:4] + ".txt")
            line_count += 1

def totContactsSKEMPI():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\skempi_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    dist = 5.5
    o.write(str(dist) + "\t")
    with open(cwd + "\\SKEMPI_Dataset\\skempi.csv") as csv_file:
        f.truncate(0)
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        pdbs = set()
        for row in csv_reader:
            try:
                if line_count != 0 and row[0][0:4] not in pdbs and float(row[8]) and row[0][0:4] != "1KBH" and len(row[0]) == 8:
                    pdbs.add(row[0][0:4])
                    calculateSKEMPI(row[0][0:4], 0, dist, True, row[0].split("_")[1], row[0].split("_")[2], cwd + "\\Machine_Learning\\skempi_data.txt")
                        # f.write(row[8])
                    f.write(
                        str(math.log(float(row[8]))*298*0.001987204) + "\n")
                    f.flush()
            except ValueError:
                continue
            line_count += 1

        train(4)
    f.close()
    o.close()


def totContactsProdigy():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    for dist in range(20, 0, -1):
        o.write(str(dist) + "\t")
        o.flush()
        with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
            f.truncate(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    c = open(
                        cwd + "\\Machine_Learning\\PRODIGY_contacts_by_res\\" + row[0][0:4] + ".txt")
                    dists = c.readlines()
                    count = 0
                    for distance in dists:
                        distance = distance.split(' ')
                        if float(distance[0]) <= dist:
                            count += 1
                    f.write(str(count) + " " + str(row[3]) + "\n")
                    f.flush()
                line_count += 1
    f.close()
    o.close()


def heavy_and_ca():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    dist = 5.5
    for i in range(0,1):
        o.write(str(dist) + "\t")
        o.flush()
        with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
            f.truncate(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    c = open(
                        cwd + "\\Machine_Learning\\PRODIGY_contacts_by_any\\" + row[0][0:4] + ".txt")
                    dists = c.readlines()
                    count = 0
                    for distance in dists:
                        distance = distance.split(' ')
                        if float(distance[0]) <= dist:
                            count += 1
                    f.write(str(count) + " ")
                    f.flush()
                    # calculateCA(row[0][0:4], 0, dist, True, "A", "B",cwd + "\\Machine_Learning\\prodigy_data.txt")
                    f.write(str(row[3]) + "\n")
                    f.flush()
                line_count += 1
    f.close()
    o.close()


def heavy():
    nonpolar = ["GLY", "ALA", "PRO", "VAL", "ILE", "MET", "PHE", "LEU", "TRP"]
    polar = ["SER", "THR", "CYS", "ASN", "GLN", "TYR", "HIS"]
    positive = ["LYS", "ARG"]
    negative = ["ASP", "GLU"]

    hydroIndexesKyte = {
        "ALA": 1.80,
        "ARG": -4.50,
        "ASN": -3.50,
        "ASP": -3.50,
        "CYS":	2.50,
        "GLN": -3.50,
        "GLU": -3.50,
        "GLY": -0.40,
        "HIS": -3.20,
        "ILE":	4.50,
        "LEU":	3.80,
        "LYS": -3.90,
        "MET":	1.90,
        "PHE":	2.80,
        "PRO":	1.60,
        "SER": -0.80,
        "THR": -0.70,
        "TRP": -0.90,
        "TYR": -1.30,
        "VAL":	4.20
    }

    polarAtoms = ["O", "N", "S"]
    nonpolarAtoms = ["C"]

    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    for dist in range(5, 6):
        o.write(str(dist) + "\t")
        o.flush()
        with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
            f.truncate(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    HIpositive = 0
                    HInegative = 0
                    c = open(
                        cwd + "\\Machine_Learning\\PRODIGY_contacts_by_any\\" + row[0][0:4] + ".txt")
                    dists = c.readlines()
                    contactTypes = [0, 0, 0, 0, 0, 0, 0]
                    contactTypesAtoms = [0, 0, 0]
                    for distance in dists:
                        distance = distance.split(' ')
                        if float(distance[0]) <= dist and distance[1][0] != "H" and distance[2][0] != "H":
                            '''
                            HIdiff = abs(hydroIndexesKyte[distance[3][:3]]- hydroIndexesKyte[distance[4][:3]])
                            HIscaledDiff = 1-(HIdiff)/(4.5)

                            if HIscaledDiff > 0:
                                HIpositive += 1
                            else:
                                HInegative += 1

                            nonpolarFirst = distance[3][:3] in nonpolar
                            nonpolarSecond = distance[4][:3] in nonpolar
                            polarFirst = distance[3][:3] in polar
                            polarSecond = distance[4][:3] in polar
                            positiveFirst = distance[3][:3] in positive
                            positiveSecond = distance[4][:3] in positive
                            negativeFirst = distance[3][:3] in negative
                            negativeSecond = distance[4][:3] in negative

                            if positiveFirst and positiveSecond or negativeFirst and negativeSecond:
                                contactTypes[0] += 1
                            elif negativeSecond and positiveFirst or positiveFirst and negativeSecond:
                                contactTypes[1] += 1
                            elif (polarFirst or polarSecond) and (positiveFirst or positiveSecond or negativeFirst or negativeSecond):
                                contactTypes[2] += 1
                            elif (nonpolarFirst or nonpolarSecond) and (positiveFirst or positiveSecond or negativeFirst or negativeSecond):
                                contactTypes[3] += 1
                            elif polarFirst and polarSecond:
                                contactTypes[4] += 1
                            elif (polarFirst or polarSecond) and (nonpolarFirst or nonpolarSecond):
                                contactTypes[5] += 1
                            elif nonpolarFirst and nonpolarSecond:
                                contactTypes[6] += 1
                            '''

                            nonpolarFirst = distance[1][0] in nonpolarAtoms
                            nonpolarSecond = distance[2][0] in nonpolarAtoms
                            polarFirst = distance[1][0] in polarAtoms
                            polarSecond = distance[2][0] in polarAtoms

                            if nonpolarFirst and nonpolarSecond:
                                contactTypesAtoms[0] += 1
                            elif nonpolarFirst and polarSecond or polarFirst and nonpolarSecond:
                                contactTypesAtoms[1] += 1
                            elif polarFirst and polarSecond:
                                contactTypesAtoms[2] += 1
                            else:
                                print(str(distance[1]) +
                                      " " + str(distance[2]))

                    # numFavorable = contactTypes[1] + contactTypes[2] + contactTypes[4] + contactTypes[6] + contactTypes[1] + contactTypes[2] + contactTypes[4] + contactTypes[6]
                    # numUnfavorable = contactTypes[0] + contactTypes[3] + contactTypes[5] + contactTypes[0] + contactTypes[3] + contactTypes[5]

                    f.write(str(contactTypesAtoms[0] + contactTypesAtoms[1] +
                            contactTypesAtoms[2]) + " " + str(row[3]) + "\n")
                    f.flush()
                line_count += 1
            train(1)
    f.close()
    o.close()


def ca_res():
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')
    for dist in range(9, 10):
        o.write(str(dist) + "\t")
        o.flush()
        with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
            f.truncate(0)
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    calculateCA(row[0][0:4], 0, dist, True, "A", "B",
                                cwd + "\\Machine_Learning\\prodigy_data.txt")
                    f.write(str(row[3]) + "\n")
                    f.flush()
                line_count += 1
            train(7)
    f.close()
    o.close()

def LR(arr):
    cwd = os.getcwd()
    f = open(cwd + "/Machine_Learning/contactsAA.txt", "r")
    g = open(cwd + "/Machine_Learning/allFeaturesHICombined.txt", "r")
    data = f.readlines()
    data2 = g.readlines()
    o = open(cwd + "/Machine_Learning/data2.txt", 'a')
    o.truncate(0)

    """ with open(cwd + "/Combined_Dataset/Combined141.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        o.truncate(0)
        for row in csv_reader:
            if line_count > 0:
                if row[7] == 'A' or row[7] == 'AB':
                    line = data[line_count-1].split(" ")
                    for num in arr:
                        o.write(line[num] + " ")
                    o.write(line[14])
                    o.flush()
            line_count += 1
    o.close() """


    o.truncate(0)
    lineCount = 1
    for line, line2 in zip(data,data2):
        if lineCount > 0:
            line = line.split("\t")
            line2 = line2.split(" ")
            for num in arr:
                # o.write(line[num] + " ")
                if num >= 20:
                    o.write(line2[num-20] + " ")
                else:
                    o.write(line[num] + " ")
            o.write(line[20])
            o.flush()
        lineCount += 1
    o.close()

cwd = os.getcwd()
ot = open(cwd + "/Machine_Learning/output.txt", 'a')

# all subsets
# ot.truncate(0)

# s = set([1,7,9,15,18,19,20,22,23,24,26,27,28,29,30,31,32,33])
# combos = sum(map(lambda r: list(itertools.combinations(s, r)), range(1, len(s)+1)), [])

# combinations()
""" i = 0
while i < len(combos):
    subset = combos[i]
    if len(subset) < 1:
        continue
    ot.write(str(list(subset)) + "\t")
    ot.flush()
    LR(subset)
    train(len(subset),81,141,0.5)
    i += 1 """


# specific subset

subset = [21,22,23,24,25,26,27,30,33]
# subset = [8]
# ot.write(str(subset) + "\t")
# ot.flush()
LR(subset)
train(9,81,141,1.740)
ot.write("\n")
ot.flush()

# iterate lambda for ridge regression
""" a = 0
while a < 1:
    train(13,81,60,a)
    a += 0.01
"""