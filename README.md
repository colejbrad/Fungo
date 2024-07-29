# Fungo
Author: Cole Bradley


Code used for analysis and communication during internship at Wake Forest Fungo

## Python Files
### Fungo Import
- Used for importing data for a specific hitter or pitcher into Python for use in other methods and programs
- importHitter() is used for importing a hitter, takes in the filepath of the desired hitter's dataset as a string and outputs a pandas DataFrame of that information
- importPitcher() is used for importing a pitcher, takes in the filepath of the desired hitter's dataset as a string and outputs a pandas DataFrame of that information
- importSwingAndMiss() is used to import swing and miss datasets, takes in the filepath of the desired hitter's swing and miss data as a string and outputs a pandas DataFrame with this information

### Fungo Splits
- Used for splitting imported data by the various variables in the DataFrames
- getSplitHitterPAs() is used for subsetting a hitter's full dataset by the pitcher they faced in a plate appearance's pitching hand (R, L)
- getSplitPitcherPAs() is used for subsetting a pitcher's full dataset by the batter they faced in a plate appearance's batting stance (R, L)
- getPitchTypeSplits() is used for subsetting a hitter's full dataset by the type of pitch they faced (FB, CH, CB, SL)
- getlocationSplits() is used for subsetting a hitter's full dataset by the location of the pitch they faced (1 - 13) and applies the FungoStats average method to each of the locations

### Fungo Stats
- Creates basic stats for a player such as average, obp, slg, etc. All methods can accept a full player's dataset as well as each of their subsetted data
- average() calculates a player's batting average
- onBasePct() calculates a player's on base percentage
- slugging() calculates a player's slugging percentage
- whiffRate() calculates a player's swing and miss rate
- iso() calculates a player's isolated power (slugging - batting average)
- walkPct() calculates the percentage of a player's plate appearances result in a walk
- strikeoutPct() calculates the percentage of a player's plate appearances result in a strikeout
- chaseRate() calculates the percentage of pitches a player swings and misses at
- fieldRatios() calculates the percentage of a player's hits end up in each 1/3 of the field (left, center, right)
- hitTypeRatios() calculates the percentage of a player's hits that are of each type (grounder, liner, fly ball)

### Fungo Visual
- Creates datasets that are suitable for use in graphing as well as creating said graphs
- pitchMatrix() creates a numpy array for by-location statistic plotting, and has a setting for either a list or a pandas DataFrame as the input
- plotMatrix() saves the plot from the pitchMatrix() function to the Images folder
- rollingAvg() creates a plot showing a player's rolling batting average, calculated after each plate appearance
- plotRollingAvg() saves the plot from the rollingAvg() function to the Images folder
- plotPitchTypeBAs() creates a plot that subsets a player's full dataset by the type of pitch they saw (FB, CH, CB, SL), calculates the rolling batting average for each subset, and saves the plot to the Images folder

### Fungo Output
- Used to create the final PDF containing statistics and graphs for a specified player and saves it to the Output_Files folder

## SAS Files
- HitterCleaning is used to create datasets for a specific hitter from the raw hitter dataset. It also creates a dataset for just the result of each of their
plate appearances instead of every pitch they saw. These datasets are then exported as CSVs. Change the value of the hitter macro to change which batter's data is subsetted
- PitcherCleaning is used to create datasets for a specific pitcher from the raw pitcher dataset. This dataset is then exported as CSVs. Change the value of the pitcher macro to change which pitcher's data is subsetted
- PitcherAnalysis is used to create datasets for use in analysis and reporting in the PitcherOutputs.sas file
- PitcherOutputs is used to create reports based on a pitcher's dataset, and exports as a PDF. What is included depends on what the pitcher wants to know. Could be by-pitch velocities, effectiveness of a specific training regiment, etc.
- Lib folder is used as the path for the library used across each of the sas files and stores the datasets within it

## Output_CSV
- Output destination for HitterCleaning.sas and PitcherCleaning.sas

## Output_Files
- Output destination for PitcherOutputs.sas and FungoOutput.py

## Images
- Output destination for created graphs from FungoVisual.py

## Raw_Data
- Contains the raw datasets for all pitchers and hitters. These datasets are stored as CSVs.

The structure of the datasets are as follows, types in parentheses based on which language they will be used in (Python, SAS):

Hitter Data:
    date (str, datetime)
    opponent (str, char)
    batter (str, char)
    pitcherHand (str, char)
    plateAppearance (int, num)
    pitchType (str, char)
    pitchLocation (int, num)
    swing (int, num)
    miss (int, num)
    result (str, char)
    resultType (str, char)
    resultLocation (int, num)
    hitType (str, char)

Pitcher Data:
    date (str, datetime)
    opponent (str, char)
    pitcher (str, char)
    batterHand (str, char)
    battersFaced (int, num)
    velocity (int, num)
    pitchType (str, char)
    location (int, num)
    wing (int, num)
    miss (int, num)
    