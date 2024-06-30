# Subset data from import
import pandas as pd
from FungoStats import FungoStats as fStat


class FungoSplits:

    def getSplitHitterPAs(playerData):
        '''
        Creates separate dataframes based on the pitcherHand column
        for hitter data.

        Parameters
        ----------
        playerData : DataFrame
            A dataframe of a specified hitter's data

        Returns
        -------
        rightyDataFrame : DataFrame
            DataFrame of all rows from the input DataFrame where
            pitcherHand == "R"
        leftyDataFrame : DataFrame
            DataFrame of all rows from the input DataFrame where
            pitcherHand == "L"

        '''
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
        '''
        Creates separate dataframes based on the batterHand column
        for pitcher data.

        Parameters
        ----------
        playerData : DataFrame
            A dataframe of a specified pitcher's data

        Returns
        -------
        rightyDataFrame : DataFrame
            DataFrame of all rows from the input DataFrame where
            batterHand == "R"
        leftyDataFrame : DataFrame
            DataFrame of all rows from the input DataFrame where
            batterHand == "L"

        '''
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

    def getLocationSplits(playerData):
        '''
        Calculates a player's batting average based on the location of the pitch
        for the ultimate pitch in an at bat

        Parameters
        ----------
        playerData : DataFrame
            DataFrame containing information about the final pitch of each
            at bat a player has

        Returns
        -------
        dataList : list
            A list containing the batting average for each of the zones defined
            in the strikezone. The list is ordered to match the numerical
            definition of these zones (1 is top left of strikezone going across
            down to 9 in bottom right of the zone with zones 10-13 being
            quadrants outside the zone)

        '''
        dataDict = {
            'tl': pd.DataFrame(),
            'tm': pd.DataFrame(),
            'tr': pd.DataFrame(),
            'ml': pd.DataFrame(),
            'mm': pd.DataFrame(),
            'mr': pd.DataFrame(),
            'bl': pd.DataFrame(),
            'bm': pd.DataFrame(),
            'br': pd.DataFrame(),
            'ui': pd.DataFrame(),
            'uo': pd.DataFrame(),
            'li': pd.DataFrame(),
            'lo': pd.DataFrame()
        }

        for index, row in playerData.iterrows():
            match row['pitchLocation']:
                case 1:
                    dataDict['tl'] = pd.concat(
                        [dataDict['tl'], row.to_frame().T])
                case 2:
                    dataDict['tm'] = pd.concat(
                        [dataDict['tm'], row.to_frame().T])
                case 3:
                    dataDict['tr'] = pd.concat(
                        [dataDict['tr'], row.to_frame().T])
                case 4:
                    dataDict['ml'] = pd.concat(
                        [dataDict['ml'], row.to_frame().T])
                case 5:
                    dataDict['mm'] = pd.concat(
                        [dataDict['mm'], row.to_frame().T])
                case 6:
                    dataDict['mr'] = pd.concat(
                        [dataDict['mr'], row.to_frame().T])
                case 7:
                    dataDict['bl'] = pd.concat(
                        [dataDict['bl'], row.to_frame().T])
                case 8:
                    dataDict['bm'] = pd.concat(
                        [dataDict['bm'], row.to_frame().T])
                case 9:
                    dataDict['br'] = pd.concat(
                        [dataDict['br'], row.to_frame().T])
                case 10:
                    dataDict['ui'] = pd.concat(
                        [dataDict['ui'], row.to_frame().T])
                case 11:
                    dataDict['uo'] = pd.concat(
                        [dataDict['uo'], row.to_frame().T])
                case 12:
                    dataDict['li'] = pd.concat(
                        [dataDict['li'], row.to_frame().T])
                case 13:
                    dataDict['lo'] = pd.concat(
                        [dataDict['lo'], row.to_frame().T])
                case _:
                    continue

        dataList = []
        stats = fStat()
        for key in dataDict:
            if len(dataDict[key]) == 0:
                dataList.append(0)
            else:
                dataDict[key] = stats.average(dataDict[key])
                dataList.append(dataDict[key])

        return dataList
