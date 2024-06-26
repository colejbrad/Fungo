# Create strikezone based plots for hitters and pitchers
import FungoImport as fi
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


class FungoVisual:

    def importSwingAndMiss(playerData):
        '''
        Reads in the Swing and Miss dataset from PitcherAnalysis.sas file
        and outputs the dataset in a dataframe

        Parameters
        ----------
        playerData : str
            Filepath of the .sas7bdat file containing the desired dataset

        Returns
        -------
        playerDF : DataFrame
            DataFrame representation of the SAS dataset

        '''
        playerDF = pd.read_sas(playerData)

        return playerDF

    def pitchMatrix(playerData):
        '''
        Transform a DataFrame of pitch location data formatted to fit the
        correct locations in a strikezone in an array

        Parameters
        ----------
        playerData : DataFrame
            DataFrame containing pitch location data

        Returns
        -------
        pitchMatrix : array
            formatted array of the input DataFrame

        '''
        pitchMatrix = np.empty((5, 5))

        for index, row in playerData.iterrows():
            location = row['location']
            rate = row['swingingStrRate']

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

        return pitchMatrix

    def plotMatrix(pitchMatrix):
        '''
        Plots the formatted pitch location data

        Parameters
        ----------
        pitchMatrix : array
            Formatted array of pitch information based on pitch location

        Returns
        -------
        plot : plot
            Plotted array

        '''
        plot = sns.heatmap(pitchMatrix, linecolor='white',
                           annot=True, fmt='.3f', linewidths=0.5)

        return plot


swingData = FungoVisual.importSwingAndMiss('SAS_Files\\swingandmiss.sas7bdat')
swingMatrix = FungoVisual.pitchMatrix(swingData)
swingPlot = FungoVisual.plotMatrix(swingMatrix)
plt.show()
