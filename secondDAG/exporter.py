import csv
import re

def export_raw(filePathExport):
  regExp = r'(\,)'
  regExpComp = re.compile(regExp)
  dataArray = []
  with open(filePathExport, newline="", encoding="utf-8") as csvFile:
    for i in csvFile:
      dataArray.append(re.sub(regExp, ' ', i))
  return dataArray
