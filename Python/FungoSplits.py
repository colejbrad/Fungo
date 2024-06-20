# Subset data from import
import pandas as pd


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
