# Fungo
Author: Cole Bradley


Code used for analysis during internship at Wake Forest Fungo

## Python Files
### Fungo Import
- Used for importing data for a specific hitter or pitcher into Python for use in other methods and programs
- importHitter() is used for importing a hitter
- importPitcher() is used for importing a pitcher

### Fungo Splits
- Used for splitting imported data by the dominant hand of the opponent
- getSplitHitterPAs() is used for subsetting a hitter's full data set by the pitcher they faced in a plate appearance's pitching hand
- getSplitPitcherPAs() is used for subsetting a pitcher's full data set by the batter they faced in a plate appearance's batting stance

### Fungo Stats
- Creates basic stats for a player such as avergae, obp, slg, etc. All methods can accept a full player's dataset as well as each of their subsetted data
- average() calculates a player's batting average
- onBasePct() calculates a player's on base percentage
- slugging() calculates a player's slugging percentage
- whiffRate() calculates a player's swing and miss rate

## SAS Files
- HitterCleaning is used to create datasets for a specific hitter from the raw hitter dataset. It also creates a dataset for just the result of each of their
plate appearances instead of every pitch they saw. These datasets are then exported as CSVs. Change the value of the hitter macro to change which batter's data
is subsetted
- PitcherCleaning is used to create datasets for a specific pitcher from the raw pitcher dataset. This dataset is then exported as CSVs. Change the value of the 
pitcher macro to change which pitcher's data is subsetted
- PitcherAnalysis is used to create reports based on a pitcher's dataset, and exports as a PDF. What is included depends on what the pitcher wants to know. Could be
by-pitch velocities, effectiveness of a specific training regiment, etc.

## Output_CSV
- Output destination for HitterCleaning and PitcherCleaning

## Output_Files
- Output destination for PitcherAnalysis

## Raw_Data
- Contains the raw datasets for all pitchers and hitters. These datasets are stored as CSVs.

The structure of the datasets are as follows, types in parentheses based on which language they will be used in (Python, SAS):

Hitter Data:
    date (str, char), opponent (str, char), batter (str, char), pitcherHand (str, char), plateAppearance (int, num), pitchType (str, char),
    pitchLocation (int, num), swing (int, num), miss (int, num), result (str, char), resultType (str, char),
    resultLocation (int, num), hitType (str, char)

Pitcher Data:
    date (str, char), opponent (str, char), pitcher (str, char), batterHand (str, char), battersFaced (int, num), velocity (int, num),
    pitchType (str, char), location (int, num), swing (int, num), miss (int, num)