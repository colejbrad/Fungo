/* Filter Hitter dataset by player */

/* Change definition of this Macro to filter
for specified player. Last name only */
%let hitter = Richardson;

/* Create library for storing data for Fungo */
x 'cd C:\Users\1030c\Desktop\Fungo\Fungo\';
libname Fungo "SAS_Files\Lib";

/* Import data into SAS */
data Fungo.Hitters;
  infile "Raw_Data\HitterData.csv" dsd firstobs= 2 missover;
  attrib date length= $9
         opponent length= $10
         batter length= $10
  ;
  input date $
        opponent $
        batter $
        pitcherHand $
        plateAppearance
        pitchType $
        pitchLocation
        swing
        miss
        result $
        resultType $
        resultLocation
        hitType $
  ;
run;

data Fungo.SpecificHitter;
  set Fungo.Hitters;
  where batter = "&hitter";
run;

data Fungo.SpecificHitterResults;
  set Fungo.SpecificHitter;
  where hitType ne '' or resultType in ('walk', 'hbp');
run;

/* Export data as CSV */
proc export data= Fungo.SpecificHitter
  outfile= "C:\Users\1030c\Desktop\Fungo\Fungo\Output_CSV\&hitter..csv"
  dbms= csv
  replace;
run;

proc export data= Fungo.SpecificHitterResults
  outfile= "C:\Users\1030c\Desktop\Fungo\Fungo\Output_CSV\&hitter.Results.csv"
  dbms= csv
  replace;
run;
