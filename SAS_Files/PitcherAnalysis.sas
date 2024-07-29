/* Create analysis for pitchers */
/* Data created is for use in PitcherOutput file */

/* Create library for storing data for Fungo */
x "cd C:\Users\1030c\Desktop\Fungo\Fungo\";
libname Fungo "SAS_Files\Lib";

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
  where swing = 1;
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

data Fungo.swingAndMiss;
  set Fungo.swingAndMiss;
  where ~missing(location);
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

/* Create dataset for swing and miss data by pitch type */
proc means data= Fungo.SpecificPitcher noprint;
  class pitchType;
  var swing miss;
  output out= Fungo.swingsByLocationPType (drop= _TYPE_ _FREQ_)
         n(swing) = totalPitches
         sum(swing) = totalSwings
  ;
run;

data Fungo.onlySwings;
  set Fungo.SpecificPitcher;
  where swing = 1;
run;

proc means data= Fungo.onlySwings noprint;
  class pitchType;
  var miss;
  output out= Fungo.missesByLocationPType (drop= _TYPE_ _FREQ_)
         sum(miss) = totalMisses
  ;
run;

data Fungo.swingAndMissPType;
  merge Fungo.swingsByLocationPType (in= a)
        Fungo.missesByLocationPType (in= b)
  ;
  by pitchType;
  if b = 0 then totalMisses = 0;
  swingingStrRate = totalMisses / totalPitches;
run;

data Fungo.swingAndMissPType;
  set Fungo.swingAndMissPType;
  where ~missing(pitchType);
run;
