/* Filter Hitter dataset by player */

/* Change definition of this Macro to filter
for specified player. Last name only */
%let hitter = Richardson;

/* Create library for storing data for Fungo */
x "cd C:\Users\1030c\Desktop\Fungo\Fungo\";
libname Fungo "SAS_Files\Lib";

/* Import data into SAS */
data Fungo.Hitters;
  infile "Raw_Data\HitterData.csv" dsd firstobs= 2 missover;
  attrib date format= ddmmyy9.
         opponent length= $10
         batter length= $10
  ;
  input date : date9.
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

/* Create datasets for swing and miss data & merge them */
proc means data= Fungo.SpecificHitter noprint;
  class location;
  var swing miss;
  output out= Fungo.swingsByLocationHitter (drop= _TYPE_ _FREQ_)
         n(swing) = totalPitches
         sum(swing) = totalSwings
  ;
run;

data Fungo.onlySwingsHitter;
  set Fungo.SpecificHitter;
  if swing = 1;
run;

proc means data= Fungo.onlySwingsHitter noprint;
  class location;
  var miss;
  output out= Fungo.missesByLocationHitter (drop= _TYPE_ _FREQ_)
         sum(miss) = totalMisses
  ;
run;

data Fungo.&hitter.SwingAndMiss;
  merge Fungo.swingsByLocationHitter (in= a)
        Fungo.missesByLocationHitter (in= b)
  ;
  by location;
  if b = 0 then totalMisses = 0;
  swingingStrRate = totalMisses / totalPitches;
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
