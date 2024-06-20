# Import individual player data and fix resulting dataframes
import csv
import pandas as pd


class FungoImport:

    def importHitter(playerData):
        try:
            with open(playerData, newline='') as playerFile:
                reader = csv.reader(playerFile)
                playerData = list(reader)
        except FileNotFoundError:
            print(f"Error: The file '{playerData}' was not found.")
            return pd.DataFrame()
        except csv.Error as e:
            print(f"Error reading the CSV file: {e}")
            return pd.DataFrame()

        if len(playerData) < 2:
            print("Error: The CSV file does not contain enough data.")
            return pd.DataFrame()

        try:
            playerDF = pd.DataFrame(playerData[1:], columns=playerData[0])

            numericColumns = ['plateAppearance', 'pitchLocation',
                              'swing', 'miss']
            playerDF[numericColumns] = playerDF[numericColumns].apply(
                pd.to_numeric, errors='coerce')
            playerDF[numericColumns] = playerDF[numericColumns].fillna(
                0).astype(int)

        except ValueError as e:
            print(f"Error converting columns to int: {e}")
            return pd.DataFrame()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame()

        return playerDF

    def importPitcher(playerData):
        try:
            with open(playerData, newline='') as playerFile:
                reader = csv.reader(playerFile)
                playerData = list(reader)
        except FileNotFoundError:
            print(f"Error: The file '{playerData}' was not found.")
            return pd.DataFrame()
        except csv.Error as e:
            print(f"Error reading the CSV file: {e}")
            return pd.DataFrame()

        if len(playerData) < 2:
            print("Error: The CSV file does not contain enough data.")
            return pd.DataFrame()

        try:
            playerDF = pd.DF(playerData[1:], columns=playerData[0])

            numericColumns = ['battersFaced', 'velocity', 'location',
                              'swing', 'miss']
            playerDF[numericColumns] = playerDF[numericColumns].apply(
                pd.to_numeric, errors='coerce')
            playerDF[numericColumns] = playerDF[numericColumns].fillna(
                0).astype(int)

        except ValueError as e:
            print(f"Error converting columns to int: {e}")
            return pd.DataFrame()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return pd.DataFrame()

        return playerDF


hitter = FungoImport.importHitter('Output_CSV\\SnelsonResults.csv')
pitcher = FungoImport.importPitcher('Output_CSV\\Mizener.csv')
