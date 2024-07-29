# Create strikezone based plots for hitters and pitchers
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from FungoStats import FungoStats as fStat


class FungoVisual:
    # Change filepath to location on user's disk
    filepath: str = "C:\\Users\\1030c\\Desktop\\Fungo\\Fungo\\Images\\"

    def pitchMatrix(playerData: pd.DataFrame | list[float]) -> np.array:
        """
        Transform a DataFrame or list of pitch location data formatted to fit
        the correct locations in a strikezone in an array

        Parameters
        ----------
        playerData : DataFrame, list
            DataFrame or list containing pitch location data

        Returns
        -------
        pitchMatrix : array
            formatted array of the input DataFrame

        """
        pitchMatrix = np.empty((5, 5))

        if isinstance(playerData, pd.DataFrame):
            for index, row in playerData.iterrows():
                location = row["location"]
                rate = row["swingingStrRate"]

                if pd.notna(location) and isinstance(location, int):
                    location = int(location)

                match location:
                    case 1:
                        pitchMatrix[1, 1] = rate
                    case 2:
                        pitchMatrix[1, 2] = rate
                    case 3:
                        pitchMatrix[1, 3] = rate
                    case 4:
                        pitchMatrix[2, 1] = rate
                    case 5:
                        pitchMatrix[2, 2] = rate
                    case 6:
                        pitchMatrix[2, 3] = rate
                    case 7:
                        pitchMatrix[3, 1] = rate
                    case 8:
                        pitchMatrix[3, 2] = rate
                    case 9:
                        pitchMatrix[3, 3] = rate
                    case 10:
                        pitchMatrix[0, 0] = rate
                        pitchMatrix[0, 1] = rate
                        pitchMatrix[1, 0] = rate
                        pitchMatrix[2, 0] = rate
                    case 11:
                        pitchMatrix[0, 2] = rate
                        pitchMatrix[0, 3] = rate
                        pitchMatrix[0, 4] = rate
                        pitchMatrix[1, 4] = rate
                    case 12:
                        pitchMatrix[3, 0] = rate
                        pitchMatrix[4, 0] = rate
                        pitchMatrix[4, 1] = rate
                        pitchMatrix[4, 2] = rate
                    case 13:
                        pitchMatrix[4, 3] = rate
                        pitchMatrix[4, 4] = rate
                        pitchMatrix[3, 4] = rate
                        pitchMatrix[2, 4] = rate
                    case _:
                        continue
        elif isinstance(playerData, list):
            for i, v in enumerate(playerData):
                match i:
                    case 0:
                        pitchMatrix[1, 1] = v
                    case 1:
                        pitchMatrix[1, 2] = v
                    case 2:
                        pitchMatrix[1, 3] = v
                    case 3:
                        pitchMatrix[2, 1] = v
                    case 4:
                        pitchMatrix[2, 2] = v
                    case 5:
                        pitchMatrix[2, 3] = v
                    case 6:
                        pitchMatrix[3, 1] = v
                    case 7:
                        pitchMatrix[3, 2] = v
                    case 8:
                        pitchMatrix[3, 3] = v
                    case 9:
                        pitchMatrix[0, 0] = v
                        pitchMatrix[0, 1] = v
                        pitchMatrix[1, 0] = v
                        pitchMatrix[2, 0] = v
                    case 10:
                        pitchMatrix[0, 2] = v
                        pitchMatrix[0, 3] = v
                        pitchMatrix[0, 4] = v
                        pitchMatrix[1, 4] = v
                    case 11:
                        pitchMatrix[3, 0] = v
                        pitchMatrix[4, 0] = v
                        pitchMatrix[4, 1] = v
                        pitchMatrix[4, 2] = v
                    case 12:
                        pitchMatrix[4, 3] = v
                        pitchMatrix[4, 4] = v
                        pitchMatrix[3, 4] = v
                        pitchMatrix[2, 4] = v
                    case _:
                        continue

        return pitchMatrix

    def plotMatrix(playerName: str, plotType: str, pitchMatrix: np.array) -> None:
        """
        Plots the formatted pitch location data and saves it as PNG

        Parameters
        ----------
        playerName : str
            The last name of the player, title case
        plotType : str
            The type of plot requested: BA for batting average, Whiff for whiff %
        pitchMatrix : np.array
            Formatted array of pitch information based on pitch location

        Returns
        -------
        None

        """
        plot = sns.heatmap(
            pitchMatrix,
            linecolor="white",
            cmap="inferno",
            annot=True,
            fmt=".3f",
            linewidths=0.5,
        )

        fileLocation = FungoVisual.filepath + f"{playerName}{plotType}Zone.png"
        plotFig = plot.get_figure()
        if plotType == "BA":
            plotFig.set_title("Batting Average by zone", fontsize=20)
        elif plotType == "Whiff":
            plotFig.set_title("Whiff Percentage by zone", fontsize=20)

        plotFig.savefig(fileLocation)

    def rollingAvg(playerData: pd.DataFrame) -> list[float]:
        """
        Creates list of the rolling average of a player after each plate
        appearance for use in plotting

        Parameters
        ----------
        playerData : DataFrame
            DataFrame containing plate appearance results for a specified batter

        Returns
        -------
        avgList : list
            List of rolling averages at each plate appearance for a batter

        """
        avgList = [
            fStat.average(playerData.iloc[: (i + 1)]) for i, r in playerData.iterrows()
        ]

        return avgList

    def plotRollingAvg(playerName: str, playerData: list[float]) -> None:
        """
        Creates a series plot showing a player's rolling batting average througout the
        season

        Parameters
        ----------
        playerName : str
            The last name of the player, title case
        playerData : list[float]
            A list of the player's rolling batting average, measured for each
            plate appearance

        Returns
        -------
        None

        """
        fig, ax = plt.subplots()
        ax.plot(range(1, len(playerData) + 1), FungoVisual.rollingAvg(playerData))

        ax.set_title("Rolling Batting Average", fontsize=20)
        ax.set_xlabel("Plate Appearance", fontsize=14)
        ax.set_ylabel("Batting Average", fontsize=14)

        fileLocation = FungoVisual.filepath + f"{playerName}RollingBA.png"
        fig.savefig(fileLocation)

    def plotPitchTypeBAs(playerName: str, playerData: tuple) -> None:
        """
        Creates plot with 4 series plots, one for each pitch type a player saw and saves
        the plot as a PNG

        Parameters
        ----------
        playerName : str
            The last name of the plauer, title case
        playerData : tuple
            DataFrames containing plate appearance information subsetted by pitch type

        Returns
        -------
        None

        """
        fig, ax = plt.subplots()
        ax.plot(
            range(1, len(playerData) + 1),
            FungoVisual.rollingAvg(playerData[0]),
            label="FB",
            color="blue",
        )
        ax.plot(
            range(1, len(playerData) + 1),
            FungoVisual.rollingAvg(playerData[1]),
            label="CH",
            color="red",
        )
        ax.plot(
            range(1, len(playerData) + 1),
            FungoVisual.rollingAvg(playerData[2]),
            label="CB",
            color="green",
        )
        ax.plot(
            range(1, len(playerData) + 1),
            FungoVisual.rollingAvg(playerData[3]),
            label="SL",
            color="orange",
        )

        ax.set_title("Rolling Batting Average", fontsize=20)
        ax.set_xlabel("Plate Appearance", fontsize=14)
        ax.set_ylabel("Batting Average", fontsize=14)

        fileLocation = FungoVisual.filepath + f"{playerName}PitchTypeBA.png"
        fig.savefig(fileLocation)
