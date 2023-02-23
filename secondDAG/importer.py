def importToTxt(dataArray, txtFileName):
  with open(txtFileName, 'wt', encoding='utf-8') as outputFile:
    for i in dataArray:
      outputFile.write(i)