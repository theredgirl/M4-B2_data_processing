import numpy as np
import pandas as pd
import os

fileName = input("What is the name of the file to read?") + ".xlsx"
xlsWriter = pd.ExcelWriter(os.path.join(os.getcwd(), "averages_proxyfile.xlsx"))
allData = pd.read_excel(os.path.join(os.getcwd(), fileName), sheet_name=None)
firstData = list(allData.values())
firstWell = np.array(firstData[0])

time = ((firstWell[:,0])*10)-10
timeFrame = pd.DataFrame(columns=["time"])
timeFrame.time = time

for key in allData:
    wellData = allData[key]
    well = np.array(wellData)
    cells = well[:,1:-1]
    background = well[:,-1]

    #subtract background from cells
    zeroCells = cells - background.reshape(-1,1)
    #average the first 3 frames together to create a baseline which will be subtracted later
    blCells = np.mean(zeroCells[0:3],axis = 0)
    #normalize cells
    normCells = (zeroCells - blCells)/blCells
    #take average of all cells for the well
    wellAvg = np.mean(normCells, axis = 1)
    wellAvgPrint = pd.DataFrame({key:[x for x in wellAvg]})
    timeFrame = timeFrame.join(wellAvgPrint, lsuffix='_caller', rsuffix='_other')

with xlsWriter as writer:
        timeFrame.to_excel(xlsWriter, sheet_name="well averages", index=False)