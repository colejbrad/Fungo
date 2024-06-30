# Test various methods across the Fungo files
import os
from FungoImport import FungoImport as fi
from FungoSplits import FungoSplits as fs
from FungoStats import FungoStats as fStat
from FungoVisual import FungoVisual as fv
import matplotlib.pyplot as plt

# Set working directory as parent folder of overall project
os.chdir('C:\\Users\\1030c\\Desktop\\Fungo\\Fungo\\')

# Test FungoImport methods
testHitter = fi.importHitter('Output_CSV\\SnelsonResults.csv')
testHitterAll = fi.importHitter('Output_CSV\\Snelson.csv')
testPitcher = fi.importPitcher('Output_CSV\\Mizener.csv')
testSwingMiss = fi.importSwingAndMiss('SAS_Files\\Lib\\swingandmiss.sas7bdat')

# Test FungoSplits methods
testSplitHitterPAs = fs.getSplitHitterPAs(testHitter)
testSplitPitcherPAs = fs.getSplitPitcherPAs(testPitcher)
testLocationSplits = fs.getLocationSplits(testHitter)

# test FungoStats methods
fStat = fStat()
testAvg = fStat.average(testHitter)
testWhiff = fStat.whiffRate(testHitterAll)
testObp = fStat.onBase(testHitter)
testSlg = fStat.slugging(testHitter)
testIso = fStat.iso(testHitter)
testWalkPct = fStat.walkPct(testHitter)
testKPct = fStat.strikeoutPct(testHitter)
testField = fStat.fieldRatios(testHitter)
testType = fStat.hitTypeRatios(testHitter)
testChase = fStat.chaseRate(testHitterAll)

# test FungoVisual methods
testMatrixHitter = fv.pitchMatrix(testLocationSplits)
testMatrixPitcher = fv.pitchMatrix(testSwingMiss)
testPlotHitter = fv.plotMatrix(testMatrixHitter)
plt.show()
testPlotPitcher = fv.plotMatrix(testMatrixPitcher)
plt.show()
