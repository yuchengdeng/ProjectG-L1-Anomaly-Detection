import os
import pandas as pd
from time import time

SaveFile_Name = r"C:\Users\YcDen\Documents\projectG\data\CICIDS2017.csv"
dir = r"C:\Users\YcDen\Documents\projectG\data"
suffix = ".csv"


def getFiles(dir, suffix):
    res = []
    for root, directory, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    return res

labelDict = {}
nameList = getFiles(dir, suffix)
print (nameList)
for LoadFile_Name in nameList:
    df = pd.read_csv(LoadFile_Name, header=0, low_memory=False)
    for ele in df[" Label"]:
        if labelDict.__contains__(ele):
            labelDict[ele] = labelDict[ele] + 1
        else:
            labelDict[ele] = 0
print(labelDict)

'''{
'BENIGN': 2273096, 
'DDoS': 128026, 
'PortScan': 158929, 
'Bot': 1965, 
'Infiltration': 35, 
'Web Attack � Brute Force': 1506, 
'Web Attack � XSS': 651, 
'Web Attack � Sql Injection': 20, 
'FTP-Patator': 7937, 
'SSH-Patator': 5896, 
'DoS slowloris': 5795, 
'DoS Slowhttptest': 5498, 
'DoS Hulk': 231072, 
'DoS GoldenEye': 10292, 
'Heartbleed': 10
}'''