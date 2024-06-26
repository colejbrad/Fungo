/* Filter Pitcher dataset by player */

/* Change definition of this Macro to filter
for specified player. Last name only */
%let pitcher = Mizener;

/* Create library for storing data for Fungo */
x 'cd C:\Users\1030c\Desktop\Fungo\Fungo\';
libname Fungo "SAS_Files\Lib";

/* Import data into SAS */
data Fungo.Pitchers;
  infile "Raw_Data\PitcherData.csv" dsd firstobs= 2 missover;
  attrib date length= $9
         opponent length= $10
         pitcher length= $10
  ;
  input date $
        opponent $
        pitcher $
        batterHand $
        battersFaced
        velocity
        pitchType $
        location
        swing
        miss
  ;
run;

data Fungo.SpecificPitcher;
  set Fungo.Hitters;
  where pitcher = "&pitcher";
run;

/* Export Data as CSV */
proc export data= Fungo.SpecificPitcher
  outfile= "C:\Users\1030c\Desktop\Fungo\Fungo\Output_CSV\&pitcher..csv"
  dbms= csv
  replace;
run;
