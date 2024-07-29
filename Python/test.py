# Test various methods across the Fungo files
import os
from pathlib import Path
from FungoImport import FungoImport as fi
from FungoSplits import FungoSplits as fs
from FungoStats import FungoStats as fStat
from FungoVisual import FungoVisual as fv
from FungoPlayer import FungoPlayer as fp
import matplotlib.pyplot as plt
import pandas as pd

# Set working directory as parent folder of overall project
os.chdir("C:\\Users\\1030c\\Desktop\\Fungo\\Fungo\\")

# Test FungoImport methods
testHitter = fi.importHitter("Output_CSV\\SnelsonResults.csv")
testHitterAll = fi.importHitter("Output_CSV\\Snelson.csv")
testPitcher = fi.importPitcher("Output_CSV\\Mizener.csv")
testSwingMiss = fi.importSwingAndMiss("SAS_Files\\Lib\\swingandmiss.sas7bdat")

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
testRollingAvg = fv.rollingAvg(testHitter)
fig, ax = plt.subplots()
ax.plot(range(1, len(testHitter) + 1), testRollingAvg)
plt.show()

# Jonalan Richardson
richardson = fi.importHitter("Output_CSV\\RichardsonResults.csv")
richardsonAll = fi.importHitter("Output_CSV\\Richardson.csv")
richardsonLocations = fs.getLocationSplits(richardson)
fStat = fStat()
richardsonAvg = fStat.average(richardson)
richardsonWhiff = fStat.whiffRate(richardsonAll)
richardsonObp = fStat.onBase(richardson)
richardsonSlg = fStat.slugging(richardson)
richardsonIso = fStat.iso(richardson)
richardsonWalkPct = fStat.walkPct(richardson)
richardsonKPct = fStat.strikeoutPct(richardson)
richardsonField = fStat.fieldRatios(richardson)
richardsonType = fStat.hitTypeRatios(richardson)
richardsonChase = fStat.chaseRate(richardsonAll)
richardsonMatrix = fv.pitchMatrix(richardsonLocations)
richardsonPlot = fv.plotMatrix(richardsonMatrix)
plt.show()
richardsonRolling = fv.rollingAvg(richardson)
fig, ax = plt.subplots()
ax.plot(range(1, len(richardson) + 1), richardsonRolling)
plt.show()
fig.savefig("C:\\Users\\1030c\\Desktop\\test.png")

RichardsonDict = fp.createPlayer("Richardson")
Path.cwd()

player = {1: "a", 2: "b", 3: "c"}
