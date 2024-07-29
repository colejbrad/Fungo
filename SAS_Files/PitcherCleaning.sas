/* Filter Pitcher dataset by player */

/* Change definition of this Macro to filter
   for specified player. Last name only. If pitcher
   is also in hitter dataset, add 'Pitcher' after macro
   call in proc export.*/
%let pitcher = Snelson;

/* Create library for storing data for Fungo */
x "cd C:\Users\1030c\Desktop\Fungo\Fungo\";
libname Fungo "SAS_Files\Lib";

/* Import data into SAS */
data Fungo.Pitchers;
  infile "Raw_Data\PitcherData.csv" dsd firstobs= 2 missover;
  attrib date format= ddmmyy9.
         opponent length= $10
         pitcher length= $10
  ;
  input date : date9.
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
  set Fungo.Pitchers;
  where pitcher = "&pitcher";
run;

/* Export Data as CSV */
proc export data= Fungo.SpecificPitcher
  outfile= "C:\Users\1030c\Desktop\Fungo\Fungo\Output_CSV\&pitcher.Pitching.csv"
  dbms= csv
  replace;
run;
