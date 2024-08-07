# Subset data from import
import pandas as pd
from FungoStats import FungoStats as fStat


class FungoSplits:
    def getSplitHitterPAs(playerData: pd.DataFrame) -> tuple[pd.DataFrame]:
        """
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

        """
        rightyData = playerData[playerData.pitcherHand == "R"]
        leftyData = playerData[playerData.pitcherHand == "L"]

        return (rightyData, leftyData)

    def getSplitPitcherPAs(playerData: pd.DataFrame) -> tuple[pd.DataFrame]:
        """
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

        """
        rightyData = playerData[playerData.batterHand == "R"]
        leftyData = playerData[playerData.batterHand == "L"]

        return (leftyData, rightyData)

    def getPitchTypeSplits(playerData: pd.DataFrame) -> tuple[pd.DataFrame]:
        """
        Creates a tuple containing DataFrames for each pitch type a player saw from a
        dataset containing plate appearance information

        Parameters
        ----------
        playerData : pd.DataFrame
            DataFrame containing information about a player's plate appearances

        Returns
        -------
        A tuple containg DataFrames for each pitch type a player saw in their plate
        appearance results

        """
        fastball = playerData[playerData.pitchType == "FB"]
        changeup = playerData[playerData.pitchType == "CH"]
        curveball = playerData[playerData.pitchType == "CB"]
        slider = playerData[playerData.pitchType == "SL"]

        return (fastball, changeup, curveball, slider)

    def getLocationSplits(playerData: pd.DataFrame) -> list[float]:
        """
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
        """

        dataDict = {
            "tl": [],
            "tm": [],
            "tr": [],
            "ml": [],
            "mm": [],
            "mr": [],
            "bl": [],
            "bm": [],
            "br": [],
            "ui": [],
            "uo": [],
            "li": [],
            "lo": [],
        }

        locationMap = {
            1: "tl",
            2: "tm",
            3: "tr",
            4: "ml",
            5: "mm",
            6: "mr",
            7: "bl",
            8: "bm",
            9: "br",
            10: "ui",
            11: "uo",
            12: "li",
            13: "lo",
        }

        for _, row in playerData.iterrows():
            key = locationMap.get(row["pitchLocation"])
            if key:
                dataDict[key].append(row)

        for key in dataDict:
            dataDict[key] = pd.DataFrame(dataDict[key])

        dataList = [
            0 if dataDict[key].empty else fStat.average(dataDict[key]) for key in dataDict
        ]

        return dataList
