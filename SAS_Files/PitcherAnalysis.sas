/* Create analysis for pitchers */

/* Create library for storing data for Fungo */
x 'cd C:\';
libname Fungo "Users\1030c\Desktop\Fungo\Fungo\SAS_Files\Lib";

*Establish macro variables;
%let TitleOpts= height= 14 pt bold;

%let SubTitleOpts= height= 10 pt bold;

%let pitcher = Mizener;

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

/* Set options for the output files */
ods _all_ close;
ods pdf file= "C:\Users\1030c\Desktop\Fungo\Fungo\Output_Files\&pitcher Pitch Information.pdf"
        style= sapphire dpi= 300
        ;
options nodate;
ods noproctitle;
ods graphics / reset width= 6in;

/* Create basic breakdown of velocities by pitch type */
title &TitleOpts "Velocity Breakdown by Pitch Type";
title2 &SubTitleOpts "*Data available for home games only*";
proc means data= Fungo.SpecificPitcher n min mean max maxdec= 1;
  where ~missing(velocity);
  class pitchType;
  var velocity;
run;

/* Create bar plot from information above */
title &TitleOpts "Velocity Breakdown by Pitch Type";
title2 &SubTitleOpts "visual of above table";
title3 &SubTitleOpts "*Data available for home games only*";
proc sgplot data= Fungo.SpecificPitcher;
  where ~missing(velocity);
  hbox velocity / category= pitchType;
  styleattrs datacolors= (cx3066be cxee4266 cx64f58d cxf17300);
  xaxis label= "Velocity" grid values= (55 to 95 by 5);
  yaxis label= "Pitch Type";
  keylegend / location= inside position= topright 
              opaque title= "Pitch Type"
  ;
run;
title;

/* Create a report that shows the number of swings, the number of misses,
   and the swinging strike rate by location of the pitch*/
title &TitleOpts "Swinging Strike Rate by Zone";
title2 &SubTitleOpts "Zones 1-9 are inside strikezone, 10-13 are outside of zone";
proc report data= Fungo.swingAndMiss;
  column location totalPitches totalSwings totalMisses swingingStrRate;
  define location / group 'Pitch Location';
  define totalPitches / analysis 'Total Pitches';
  define totalSwings / analysis 'Total Swings';
  define totalMisses / analysis 'Total Misses';
  define swingingStrRate / analysis format= percent8.2
                                    'Swinging Strike Rate';
run;
title;

ods pdf close;
quit;
