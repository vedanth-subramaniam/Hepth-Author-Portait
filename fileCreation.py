import json
import os
import pandas as pd


def extract():
    par_dir = "hepth"
    dataset = pd.DataFrame(columns=["Paper Id", "Authors", "Year"])
    for folderYear in os.listdir(par_dir):
        year = folderYear
        for fileName in os.listdir(par_dir + "/" + folderYear):
            with open(par_dir + "/" + folderYear + "/" + fileName) as fh:
                file_dict = {}
                count = 0
                for line in fh:
                    if count == 2:
                        break
                    elif line == "//\n":
                        count += 1
                    elif count == 1:
                        key, value = line.strip().split(None, 1)
                        file_dict[key] = value.strip()
            break
        break