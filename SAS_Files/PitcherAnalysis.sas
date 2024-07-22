/* Create analysis for pitchers */
/* Data created is for use in PitcherOutput file */

/* Create library for storing data for Fungo */
x 'cd C:\';
libname Fungo "Users\1030c\Desktop\Fungo\Fungo\SAS_Files\Lib";

/* Establish macro variables */
%let pitcher = Snelson;

/* Create datasets for swing and miss data & merge them */
proc means data= Fungo.SpecificPitcher noprint;
  class location;
  var swing miss;
  output out= Fungo.swingsByLocation (drop= _TYPE_ _FREQ_)
         n(swing) = totalPitches
         sum(swing) = totalSwings
  ;
run;

data Fungo.onlySwings;
  set Fungo.SpecificPitcher;
  if swing = 1;
run;

proc means data= Fungo.onlySwings noprint;
  class location;
  var miss;
  output out= Fungo.missesByLocation (drop= _TYPE_ _FREQ_)
         sum(miss) = totalMisses
  ;
run;

data Fungo.swingAndMiss;
  merge Fungo.swingsByLocation (in= a)
        Fungo.missesByLocation (in= b)
  ;
  by location;
  if b = 0 then totalMisses = 0;
  swingingStrRate = totalMisses / totalPitches;
run;


/* Create dataset for average velocity by game */
proc means data= Fungo.SpecificPitcher noprint;
  where ~missing(velocity);
  class pitchType date;
  var velocity;
  output out= Fungo.avgVeloByGame (drop= _TYPE_ _FREQ_)
         mean(velocity) = veloAvg
  ;
run;

/* Remove entries with missing pitchType and date
   from the avgVeloByGame dataset */
data Fungo.avgVeloByGame;
  set Fungo.avgVeloByGame;
  if ~missing(pitchType) and ~missing(date);
run;
