from os import listdir
from os.path import isfile, join

filedir = "/run/media/icebrah/buh/SteamLibrary/steamapps/common/Risk of Rain 2/Risk of Rain 2_Data/StreamingAssets/Audio/GeneratedSoundBanks/Windows/"
outputdir = "/run/media/icebrah/buh/SteamLibrary/steamapps/common/Risk of Rain 2/Risk of Rain 2_Data/StreamingAssets/Audio/GeneratedSoundBanks/test/"
onlyfiles = [f for f in listdir(filedir) if isfile(join(filedir, f))]

txtfiles = []
for f in onlyfiles:
    if f.endswith(".txt"):
        txtfiles.append(f)

with open(outputdir + "output.html", "w") as text_file:
    text_file.write("<!DOCTYPE html>\n<html>\n<head>\n<link rel=\"stylesheet\" href=\"style.css\">\n<script src=\"https://kit.fontawesome.com/bfcdb4196e.js\"></script>\n\n</head>\n\n\n\n\n\n\n\n<h1>\nRisk Of Rain 2 Wwise Events\n</h1>\n<p> A list of every Wwise event located in risk of rain 2. You can play them using RoR2.Util.PlaySound(Event, gameObject)</p>\n\n\n\n\n")
    text_file.write("<table id=\"default\">\n")
    text_file.write("   <tr>\n")
    text_file.write("       <th id=\"header\">ID</th>\n")
    text_file.write("       <th id=\"header\">Name</th>\n")
    text_file.write("       <th id=\"header\">Wwise Object Path</th>\n")
    text_file.write("   </tr>\n")

print(len(txtfiles))
for f in txtfiles:
    addLines = False
    txt = open(filedir + f, "r")
    for line in txt:
        if addLines:
            splitline = line.split("	")
            notEmpty = False
            for split in splitline:
                if split != "" and split != "\n":
                    notEmpty = True
                    break
            if notEmpty:
                notInList = False
                with open(outputdir + "output.html", "r") as text_file:
                    if splitline[2].replace("\n", "") not in text_file.read() and splitline[1].replace("\n", "") not in text_file.read():
                        notInList = True
                if notInList:
                    with open(outputdir + "output.html", "a") as text_file:
                        text_file.write("   <tr>\n")
                        #text_file.write("        {")
                        #text_file.write("\"" + splitline[2].replace("\n", "") + "\", ")
                        #text_file.write("" + splitline[1].replace("\n", "") + "")
                        #text_file.write("},\n")
                        for split in splitline:
                            if split != "" and split != "\n":
                                text_file.write("       <td>%s</td>\n" % split.replace("\n", ""))
                        text_file.write("   </tr>\n")

        if line.__contains__("Event	ID	Name			Wwise Object Path	Notes"):
            addLines = True
        elif line == "\n" or line == "":
            addLines = False

with open(outputdir + "output.html", "a") as text_file:
    text_file.write("</table>")
