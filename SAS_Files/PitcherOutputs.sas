/* Create visual output for pitcher stats
   created in the PitcherAnalysis file */

/* Create library for storing data for Fungo */
x "cd C:\Users\1030c\Desktop\Fungo\Fungo\";
libname Fungo "SAS_Files\Lib";

*Establish macro variables;
%let TitleOpts= height= 14 pt bold;

%let SubTitleOpts= height= 10 pt bold;

%let Pitcher= Snelson;

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
  xaxis label= "Velocity" grid values= (55 to 95 by 5);
  yaxis label= "Pitch Type";
run;
title;

/* Create series plot from avgVelo dataset */
title &TitleOpts "Average Velocity by Game";
title2 &SubTitleOpts "Grouped by pitch type";
title3 &SubTitleOpts "*Data available for home games only*";
proc sgplot data= Fungo.avgVeloByGame;
  series x= date y= veloAvg / group= pitchType datalabel;
  xaxis label= "Game Date";
  yaxis label= "Average Velocity" grid values= (55 to 95 by 5);
run;
title;

/* Perform ANOVA for BIB with pitchType as the block, location as
   the treatment, and swinging strike rate as the response */
ods exclude ClassLevels NObs;
title &TitleOpts "Analysis of Swinging Strike Rate by Pitch Type and Location";
proc glm data= Fungo.swingAndMissBIB plots= diagnostics;
  class location pitchType;
  model swingingStrRate = location pitchType / ss3;
  lsmeans pitchType / cl adjust= tukey;
run;
title;

/* Create a report that shows the number of swings, the number of misses,
   and the swinging strike rate by location of the pitch*/
title &TitleOpts "Swinging Strike Rate by Zone";
title2 &SubTitleOpts "Zones 1-9 are inside strikezone, 10-13 are outside of zone";
proc report data= Fungo.swingAndMiss;
  column location totalPitches totalSwings totalMisses swingingStrRate;
  define location / group "Pitch Location";
  define totalPitches / analysis "Total Pitches";
  define totalSwings / analysis "Total Swings";
  define totalMisses / analysis "Total Misses";
  define swingingStrRate / analysis format= percent8.2
                                    "Swinging Strike Rate";
run;
title;

/* Create a report that shows the number of swings, the number of misses,
   and the swinging strike rate by the type of pitch*/
title &TitleOpts "Swing and Miss Data by Location and Pitch Type";
proc report data= Fungo.swingAndMissPType;
  column pitchType totalPitches totalSwings totalMisses swingingStrRate;
  define pitchType / group "Pitch Type";
  define totalPitches / analysis "Total Pitches";
  define totalSwings / analysis "Total Swings";
  define totalMisses / analysis "Total Misses";
  define swingingStrRate / analysis format= percent8.2
                                    "Swinging Strike Rate";
run;
title;

proc sort data= Fungo.SpecificPitcher;
  by pitchType date;
run;

ods exclude ClassLevels NObs;
title &TitleOpts "Regression Analysis of Velocity by Pitch Type";
title2 &SubTitleOpts "*Data available for home games only*";
proc glm data= Fungo.SpecificPitcher;
  class date;
  model velocity = date;
  by pitchType;
run;

ods pdf close;
quit;
