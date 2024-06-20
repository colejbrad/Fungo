/* Create analysis for pitchers */

*Establish macro variables;
%let IdStamp= footnote &FootOpts "Output Created by Cole Bradley";

%let TitleOpts= height= 14 pt bold;

%let SubTitleOpts= height= 10 pt bold;

%let FootOpts= j= l height= 8pt italic;

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
&IdStamp;
proc means data= Fungo.SpecificPitcher n min mean max;
  where ~missing(velocity);
  class pitchType;
  var velocity;
run;

/* Create bar plot from information above */
title &TitleOpts "Velocity Breakdown by Pitch Type";
title2 &SubTitleOpts "visual of above table";
title3 &SubTitleOpts "*Data available for home games only*";
&IdStamp;
proc sgplot data= Fungo.SpecificPitcher;
  where ~missing(velocity);
  hbox velocity / category= pitchType;
  styleattrs datacolors= (cx8da0cb cxe78ac3 cxa6d854);
  xaxis label= "Velocity" grid values= (55 to 95 by 5);
  yaxis label= "Pitch Type";
  keylegend / location= inside position= topright 
              opaque title= "Pitch Type"
  ;
run;

ods pdf close;
quit;
