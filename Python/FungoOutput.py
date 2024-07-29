# Create output PDF with stats and plots
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from FungoImport import FungoImport as fi
from FungoSplits import FungoSplits as fs
from FungoPlayer import FungoPlayer as fp
from FungoVisual import FungoVisual as fv

# Get the name of the player requested and generate stats
player = input("Who would you like to generate a report for? (last name only) ")
playerDict = fp.createPlayer(player)

# Create DataFrames for use in plots
csvLocation = "C:\\Users\\1030c\\Desktop\\Fungo\\Fungo\\Output_CSV\\"
playerAll = fi.importHitter(csvLocation + f"{player}.csv")
playerPAs = fi.importHitter(csvLocation + f"{player}Results.csv")
playerSplitPAs = fs.getLocationSplits(playerPAs)
playerPitchTypePAs = fs.getPitchTypeSplits(playerPAs)
playerBALocations = fs.getLocationSplits(playerPAs)
playerWhiffLocations = fi.importSwingAndMiss(
    f"SAS_Files\\Lib\\{player.lower()}swingandmiss.sas7bdat"
)

# Generate images of graphs
rollingBA = fv.rollingAvg(playerPAs)
fv.plotRollingAvg(player, rollingBA)

avgMatrix = fv.pitchMatrix(playerBALocations)
fv.plotMatrix(player, "BA", avgMatrix)

whiffMatrix = fv.pitchMatrix(playerWhiffLocations)
fv.plotMatrix(player, "Whiff", whiffMatrix)

fv.plotPitchTypeBAs(player, playerPitchTypePAs)

# Set document settings
filename = f"C:\\Users\\1030c\\Desktop\\Fungo\\Fungo\\Output_Files\\{player}Report.pdf"
documentTitle = f"{player} Report"
title = player
subTitle1 = "Overall statistics"
subTitle2 = "R/L split statistics"

# List containing basic statistics for overall plate appearances
textLines1 = [
    f"AVG: {round(playerDict['avg'][0], 3)}   OBP: {round(playerDict['obp'][0], 3)}    SLG: {round(playerDict['slg'][0], 3)}",
    f"ISO: {round(playerDict['iso'][0], 3)}   BB%: {round(playerDict['walkPct'][0], 3)}   K%: {round(playerDict['kPct'][0], 3)}",
    f"Whiff Rate: {round(playerDict['whiffPct'], 3)}   Chase Rate: {round(playerDict['chasePct'], 3)}",
    f"Ground ball%: {round(playerDict['hitTypes'][0], 3)}   Line drive%: {round(playerDict['hitTypes'][1], 3)}     Fly ball%: {round(playerDict['hitTypes'][2], 3)}",
    f"Left field%: {round(playerDict['fieldPcts'][0], 3)}    Center field%: {round(playerDict['fieldPcts'][1], 3)}   Right field%: {round(playerDict['fieldPcts'][2], 3)}",
]

textLines2 = [
    f"AVG: {round(playerDict['avg'][1], 3)}/{round(playerDict['avg'][2], 3)}   OBP: {round(playerDict['obp'][1], 3)}/{round(playerDict['obp'][2], 3)}",
    f"SLG: {round(playerDict['slg'][1], 3)}/{round(playerDict['slg'][2], 3)}     ISO: {round(playerDict['iso'][1], 3)}/{round(playerDict['iso'][2], 3)}",
    f"BB%: {round(playerDict['walkPct'][1], 3)}/{round(playerDict['walkPct'][2], 3)}   K%: {round(playerDict['kPct'][1], 3)}/{round(playerDict['kPct'][2], 3)}",
]

# Reference file locations for plots
fileLocation = "C:\\Users\\1030c\\Desktop\\Fungo\\Fungo\\Images\\"
image1 = fileLocation + f"{player}BAZone.png"
image2 = fileLocation + f"{player}WhiffZone.png"
image3 = fileLocation + f"{player}RollingBA.png"
image4 = fileLocation + f"{player}PitchTypeBA.png"

# Create the pdf
pdf = canvas.Canvas(filename)

pdf.setTitle(documentTitle)

pdf.setFont("Courier", 30)
pdf.drawCentredString(300, 770, title)

pdf.setFont("Courier", 16)
pdf.drawCentredString(100, 720, subTitle1)

# Write overall statistics to PDF
text1 = pdf.beginText(100, 680)
text1.setFont("Courier", 12)
for line in textLines1:
    text1.textLine(line)
pdf.drawText(text1)

pdf.setFont("Courier", 16)
pdf.drawCentredString(120, 580, subTitle2)

# Write R/L splits to PDF
text2 = pdf.beginText(120, 540)
text2.setFont("Courier", 12)
for line in textLines2:
    text2.textLine(line)
pdf.drawText(text2)

# Write graphs to PDF'
pdf.drawImage(image1, 10, 250, width=10 * cm, height=7 * cm)
pdf.drawImage(image2, 300, 250, width=10 * cm, height=7 * cm)
pdf.drawImage(image3, 10, 10, width=10 * cm, height=7 * cm)
pdf.drawImage(image4, 300, 10, width=10 * cm, height=7 * cm)

pdf.save()

print(f"The PDF was saved to: Output_Files\\{player}Report.pdf")
