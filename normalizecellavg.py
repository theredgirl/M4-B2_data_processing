import numpy as np
import pandas as pd

wellData = pd.read_excel("C:\\Users\\cassi\\Desktop\\code\\070124_m4_raw.xlsx",2)
well = np.array(wellData)
time = ((well[:,0])*10)-10
cells = well[:,1:-1]
background = well[:,-1]

#subtract background from cells
zeroCells = cells - background.reshape(-1,1)
#average the first 3 frames together to create a baseline which will be subtracted later
blCells = np.mean(zeroCells[0:3],axis = 0)
#normalize cells
normCells = (zeroCells - blCells)/blCells
#take average of all cells for the well
wellAvg = np.mean(normCells,axis = 1)
wellAvgPrint = pd.DataFrame(wellAvg, time)

wellAvgPrint.to_excel("C:\\Users\\cassi\\Desktop\\code\\averages_proxyfile.xlsx")

