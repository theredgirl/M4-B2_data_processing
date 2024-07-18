import numpy as np
import pandas as pd
import os


xlsWriter = pd.ExcelWriter(os.path.join(os.getcwd(), "averages_proxyfile.xlsx"))
allData = pd.read_excel(os.path.join(os.getcwd(), "070124_m4_raw.xlsx"), sheet_name=None)
firstData = allData["well 1"]
firstWell = np.array(firstData)
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
        timeFrame.to_excel(xlsWriter, index=False)

#     #instead of to_excel, make a variable for the writer and use to_excel and make the first argument the writer
#     #missing something in the sheet_name= key part to make it cycle through each key (possibly need to make each its own loop?)
#     #use os path library for file paths (os.path.join) (os.getcwd) use import os