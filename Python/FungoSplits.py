# Subset data from import
import pandas as pd


class FungoSplits:

    def getSplitHitterPAs(playerData):
        rightyData = []
        leftyData = []
        for index, row in playerData.iterrows():
            if row['pitcherHand'] == 'R':
                rightyData.append(row)
            else:
                leftyData.append(row)

        rightyDataFrame = pd.DataFrame(rightyData, columns=playerData.columns)
        leftyDataFrame = pd.DataFrame(leftyData, columns=playerData.columns)

        return (rightyDataFrame, leftyDataFrame)

    def getSplitPitcherPAs(playerData):
        rightyData = []
        leftyData = []
        for index, row in playerData.iterrows():
            if row['batterHand'] == 'R':
                rightyData.append(row)
            else:
                leftyData.append(row)

        rightyDataFrame = pd.DataFrame(rightyData, columns=playerData.columns)
        leftyDataFrame = pd.DataFrame(leftyData, columns=playerData.columns)

        return (rightyDataFrame, leftyDataFrame)
