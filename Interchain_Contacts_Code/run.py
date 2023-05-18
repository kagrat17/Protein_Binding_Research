from Bio.PDB import *
import math
import csv
import os
import sys

sys.path.append(os.getcwd() + "\\Machine_Learning")

# from models import *
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


# making the list of subsets of features

def decimalToBinary(n):   # converting decimal to binary
    b = 0
    i = 1
    while (n != 0):
        r = n % 2
        b += r * i
        n //= 2
        i = i * 10
    return b


def makeList(k):       # list of the binary element produced
    a = []
    if (k == 0):
        a.append(0)
    while (k > 0):
        a.append(k % 10)
        k //= 10
    a.reverse()
    return a


def checkBinary(bin, l):
    temp = []
    for i in range(len(bin)):
        if (bin[i] == 1):
            temp.append(l[i])
    return temp
l = [8, 9, 10, 11,12,13,14,15,16]
binlist = []
subsets = []
n = len(l)
for i in range(2**n):
    s = decimalToBinary(i)
    arr = makeList(s)

    binlist.append(arr)

    for i in binlist:

        k = 0

        while (len(i) != n):
            i.insert(k, 0)
            k = k + 1
for i in binlist:
    subsets.append(checkBinary(i, l))



# maxDiff = 9
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

def prodigy_LR(arr, dist):
    cwd = os.getcwd()
    f = open(cwd + "\\Machine_Learning\\prodigy_data.txt", 'a')
    o = open(cwd + "\\Machine_Learning\\output.txt", 'a')

    nonpolar = ["GLY", "ALA", "PRO", "VAL", "ILE", "MET", "PHE", "LEU", "TRP"]
    polar = ["SER", "THR", "CYS", "ASN", "GLN", "TYR"]
    positive = ["LYS", "ARG", "HIS"]
    negative = ["ASP", "GLU"]
    all = {
        "GLY": 0,
        "ALA": 1,
        "PRO": 2,
        "VAL": 3, 
        "ILE": 4, 
        "MET": 5, 
        "PHE": 6, 
        "LEU": 7, 
        "TRP": 8,
        "SER": 9,
        "THR": 10, 
        "CYS": 11, 
        "ASN": 12, 
        "GLN": 13, 
        "TYR": 14,
        "LYS": 15, 
        "ARG": 16, 
        "HIS": 17,
        "ASP": 18, 
        "GLU": 19
    }

    with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
        f.truncate(0)
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                grid = []
                for i in range(0, 20):
                    grid.append([])
                    for j in range(0,20):
                        grid[i].append(0)

                
                for num in arr:
                    f.write(row[num] + " ")
                f.write(row[3])
                f.write("\n")
                
                '''
                r = open(cwd + "\\Machine_Learning\\PRODIGY_contacts_by_res\\" + row[0][0:4] + ".txt")
                lines = r.readlines()
                hi = [0,0]
                contactTypes = [0, 0, 0, 0, 0, 0, 0]
                for line in lines:
                    line = line.split()
                    if float(line[0]) < dist:

                        # o.write(line[3] + " " + line[4] + " " + line[0] + "\n")

                        nonpolarFirst = line[3][:3] in nonpolar
                        nonpolarSecond = line[4][:3] in nonpolar
                        polarFirst = line[3][:3] in polar
                        polarSecond = line[4][:3] in polar
                        positiveFirst = line[3][:3] in positive
                        positiveSecond = line[4][:3] in positive
                        negativeFirst = line[3][:3] in negative
                        negativeSecond = line[4][:3] in negative

                        if positiveFirst and positiveSecond or negativeFirst and negativeSecond:
                            contactTypes[0] += 1
                        elif negativeFirst and positiveSecond or positiveFirst and negativeSecond:
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
                        else:
                            print(line[3] + " " + line[4] + " ERROR" + "\n")

                        HIdiff = abs(hydroIndexesKyte[line[3][:3]]- hydroIndexesKyte[line[4][:3]])
                        HIscaledDiff = 1-(HIdiff)/(4.5)
                        if HIscaledDiff >= 0:
                            hi[0] += 1
                        else:
                            hi[1] += 1
                        
                        grid[all[line[3][:3]]][all[line[4][:3]]] += 1

                '''
                # f.write(str(hi[0]) + " ")
                # f.write(str(hi[1]) + " ")

                '''
                for i in range(20):
                    for j in range(i,20):
                        if i != j:
                            f.write(str(grid[i][j]+grid[j][i]) + " ")
                        else:
                            f.write(str(grid[i][j]) + " ")
                '''

                
                '''
                f.write(str(contactTypes[0] + contactTypes[1]) + " ")
                f.write(str(contactTypes[4]) + " ")
                f.write(str(contactTypes[3]) + " ")
                f.write(str(contactTypes[5]) + " ")
                
                f.write(row[3] + " ")
                f.write("\n")
                '''
                
                '''
                f.write(row[8] + " ")
                f.write(row[9] + " ")
                f.write(row[10] + " ")
                f.write(row[11] + " ")
                f.write(row[12] + " ")
                f.write(row[13] + " ")
                '''
                '''
                f.write(row[14] + " ")
                f.write(row[15] + " ")
                f.write(row[16] + " ")
                f.write(row[3] + "\n")
                '''
                
            line_count += 1
            f.flush()
        f.close()
        # train(len(arr) + 2)
        # o.write(str(arr) + "\n")

heavy_and_ca()


'''

cwd = os.getcwd()
count = 0
listSkempi = os.listdir(cwd + "\\SKEMPI_Dataset")
listProdigy = os.listdir(cwd + "\\PRODIGY_Dataset")

f = open(cwd + "\\Machine_Learning\\test1.txt", 'a')

with open(cwd + "\\SKEMPI_Dataset\\skempi.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    pdbs = set()
    for row in csv_reader:
        try:
            if line_count != 0 and row[0][0:4] not in pdbs and float(row[8]) and row[0][0:4] != "1KBH":
                pdbs.add(row[0][0:4])
                if str(row[0][0:4]) + ".pdb" in listProdigy:
                    calculate(row[0][0:4],0,8,True,row[0].split("_")[1],row[0].split("_")[2],cwd + "\\Machine_Learning\\test1.txt")
                    f.write(" " + str(math.log(float(row[8]))*8.314*274/4184))
                    f.write("\n")
                    f.flush()
        except ValueError:
            continue
        line_count += 1
f.close()

cwd = os.getcwd()
listSkempi = os.listdir(cwd + "\\SKEMPI_Dataset")
listSkempi = [file[0:4] for file in listSkempi]
listProdigy = os.listdir(cwd + "\\PRODIGY_Dataset")
listProdigy = [file[0:4] for file in listProdigy]



f = open(cwd + "\\Machine_Learning\\test2.txt", 'a')
with open(cwd + "\\PRODIGY_Dataset\\PRODIGY_dataset.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0 and row[0][0:4] not in listSkempi:
            calculate(row[0][0:4],0,8,True,"A","B",cwd + "\\Machine_Learning\\test2.txt")
            f.write(str(row[3]) + "\n")
            f.flush()
        line_count += 1
f.close()

'''
