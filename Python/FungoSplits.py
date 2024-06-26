# Subset data from import
import pandas as pd
import FungoStats as fStat


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
            match row['location']:
                case 1:
                    dataDict['tl'] = dataDict['tl'].append(row)
                case 2:
                    dataDict['tm'] = dataDict['tm'].append(row)
                case 3:
                    dataDict['tr'] = dataDict['tr'].append(row)
                case 4:
                    dataDict['ml'] = dataDict['ml'].append(row)
                case 5:
                    dataDict['mm'] = dataDict['mm'].append(row)
                case 6:
                    dataDict['mr'] = dataDict['mr'].append(row)
                case 7:
                    dataDict['bl'] = dataDict['bl'].append(row)
                case 8:
                    dataDict['bm'] = dataDict['bm'].append(row)
                case 9:
                    dataDict['br'] = dataDict['br'].append(row)
                case 10:
                    dataDict['ui'] = dataDict['ui'].append(row)
                case 11:
                    dataDict['uo'] = dataDict['uo'].append(row)
                case 12:
                    dataDict['li'] = dataDict['li'].append(row)
                case 13:
                    dataDict['lo'] = dataDict['lo'].append(row)
                case _:
                    continue

        dataList = []
        for key in dataDict:
            dataDict[key] = fStat.average(dataDict[key])
            dataList.append(dataDict[key])

        return dataList
