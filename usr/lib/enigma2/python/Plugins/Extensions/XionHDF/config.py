import os
import re
from Components.config import config, ConfigSelection, ConfigSubsection, ConfigSelectionNumber, ConfigText
from Tools.Directories import fileExists
from boxbranding import getBoxType, getImageArch

################# ColorList #########################################

ColorList = [
	("00F0A30A", _("Amber")),
	("00B27708", _("Amber dark")),
	("001B1775", _("Blue")),
	("000E0C3F", _("Blue dark")),
	("007D5929", _("Brown")),
	("003F2D15", _("Brown dark")),
	("000050EF", _("Cobalt")),
	("00001F59", _("Cobalt dark")),
	("001BA1E2", _("Cyan")),
	("000F5B7F", _("Cyan dark")),
	("00FFEA04", _("Yellow")),
	("00999999", _("Grey")),
	("003F3F3F", _("Grey dark")),
	("0070AD11", _("Green")),
	("00213305", _("Green dark")),
	("001DFF00", _("Neon green")),
	("00FFFF00", _("Neon yellow")),
	("006D8764", _("Olive")),
	("00313D2D", _("Olive dark")),
	("00C3461B", _("Orange")),
	("00892E13", _("Orange dark")),
	("00F472D0", _("Pink")),
	("00723562", _("Pink dark")),
	("00E51400", _("Red")),
	("00330400", _("Red dark")),
	("00000000", _("Black")),
	("00647687", _("Steel")),
	("00262C33", _("Steel dark")),
	("006C0AAB", _("Violet")),
	("001F0333", _("Violet dark")),
	("00ffffff", _("White"))
	]

################# SelectionBorderList ################################

SelectionBorderList = [("none", _("Off"))]
SelectionBorderList = ColorList + SelectionBorderList

################# bmeminfo ###########################################

if fileExists('/proc/bmeminfo'):
	entrie = os.popen('cat /proc/bmeminfo').read()
	mem = entrie.split(':', 1)[1].split('k')[0]
	bmem = int(mem) / 1024
else:
	mem_info = []
	entrie = os.popen('cat /proc/cmdline').read()

	if getBoxType() in ('vusolo4k', 'zgemmah7', 'zgemmah9t', 'zgemmah9s', 'zgemmah82h', 'e4hdultra', 'sfx6008', 'sfx6018'):
		mem = re.findall('_cma=(.*?)M', entrie)
	else:
		mem = re.findall('bmem=(.*?)M', entrie)

	for info in mem:
		mem_info.append((info))

	if len(mem_info) > 1:
		bmem = int(mem_info[0]) + int(mem_info[1])
	else:
		if getImageArch() == 'cortexa15hf-neon-vfpv4' or getBoxType() in ('zgemmah9s', 'zgemmah82h', 'e4hdultra', 'sfx6008', 'sfx6018'):
			bmem = 250
		else:
			bmem = int(mem_info[0])

SkinModeList = [("hd", _("HD Skin 1280 x 720"))]
if bmem > 180:
	SkinModeList.append(("fullhd", _("FullHD Skin 1920 x 1080")))

################################################################

config.plugins.XionHDF = ConfigSubsection()
config.plugins.XionHDF.refreshInterval = ConfigSelectionNumber(min=10, max=240, stepwidth=5, default=60, wraparound=True)
config.plugins.XionHDF.weather_cityname = ConfigText(default="", visible_width=250, fixed_size=False)
config.plugins.XionHDF.weather_foundcity = ConfigText(default="")
config.plugins.XionHDF.weather_latitude = ConfigText(default="")
config.plugins.XionHDF.weather_longitude = ConfigText(default="")

config.plugins.XionHDF.BackgroundColorTrans = ConfigSelection(default="1c", choices=[
				("00", _("Off")),
				("1c", _("Lower")),
				("2d", _("Low")),
				("4a", _("Middle")),
				("6c", _("Medium")),
				("8c", _("High"))
				])

config.plugins.XionHDF.skin_mode = ConfigSelection(default="hd", choices=SkinModeList)
config.plugins.XionHDF.SelectionBackground = ConfigSelection(default="00C3461B", choices=ColorList)
config.plugins.XionHDF.Font1 = ConfigSelection(default="00ffffff", choices=ColorList)
config.plugins.XionHDF.Font2 = ConfigSelection(default="00ffffff", choices=ColorList)
config.plugins.XionHDF.SelectionFont = ConfigSelection(default="00ffffff", choices=ColorList)
config.plugins.XionHDF.NotAvailableFont = ConfigSelection(default="00999999", choices=ColorList)
config.plugins.XionHDF.ButtonText = ConfigSelection(default="00ffffff", choices=ColorList)
config.plugins.XionHDF.Progress = ConfigSelection(default="00C3461B", choices=ColorList)
config.plugins.XionHDF.Line = ConfigSelection(default="00ffffff", choices=ColorList)
config.plugins.XionHDF.SelectionBorder = ConfigSelection(default="none", choices=SelectionBorderList)

config.plugins.XionHDF.EMCStyle = ConfigSelection(default="emc-nocover", choices=[
				("emc-nocover", _("No cover")),
				("emc-smallcover", _("Small cover")),
				("emc-bigcover", _("Big cover")),
				("emc-verybigcover", _("Very big cover")),
				("emc-listbigcover", _("List big cover")),
				("emc-minitv", _("MiniTV"))
				])

config.plugins.XionHDF.MovieStyle = ConfigSelection(default="movieselectionnocover", choices=[
				("movieselectionnocover", _("No cover")),
				("movieselectionsmallcover", _("Small cover")),
				("movieselectionbigcover", _("Big cover")),
				("movieselectionlistbigcover", _("List big cover")),
				("movieselectionminitv", _("MiniTV"))
				])

config.plugins.XionHDF.InfobarStyle = ConfigSelection(default="infobar-style-xpicon", choices=[
				("infobar-style-xpicon", _("X-Picon"))
				])

config.plugins.XionHDF.SIB = ConfigSelection(default="infobar-style-xpicon_end1", choices=[
				("infobar-style-xpicon_end1", _("Only current program")),
				("infobar-style-xpicon_end2", _("Top/Bottom")),
				("infobar-style-xpicon_end3", _("Left/Right"))
				])

config.plugins.XionHDF.ChannelSelectionStyle = ConfigSelection(default="channelselection-twocolumns", choices=[
				("channelselection-twocolumns", _("Two columns")),
				("channelselection-threecolumns", _("Three columns")),
				("channelselection-xpicon", _("X-Picon")),
				("channelselection-minitv", _("MiniTV"))
				])

config.plugins.XionHDF.InfobarChannelname = ConfigSelection(default="infobar-style-xpicon_middle1", choices=[
				("infobar-style-xpicon_middle1", _("Small")),
				("infobar-style-xpicon_middle2", _("Big")),
				("infobar-style-xpicon_middleP", _("Poster")),
				("infobar-style-xpicon_middle3", _("Off"))
				])

config.plugins.XionHDF.RunningText = ConfigSelection(default="movetype=running", choices=[
				("movetype=running", _("On")),
				("movetype=none", _("Off"))
				])

IconsList = [("none", _("off"))]
IconDir = "/usr/share/enigma2/WeatherIconSets"
if os.path.exists(IconDir):
	folders = os.listdir(IconDir)
	for folder in folders:
		folderpath = os.path.join(IconDir, folder)
		if os.path.isdir(folderpath):
			IconsList.append((folder, folder))
config.plugins.XionHDF.CustomWeatherFolder = ConfigSelection(default="none", choices=IconsList)

config.plugins.XionHDF.WeatherStyle = ConfigSelection(default="weather-off", choices=[
				("weather-off", _("Off")),
				("weather-info", _("Infos in place of weather")),
				("weather-big", _("Big")),
				("weather-slim", _("Slim")),
				("weather-small", _("Small"))
				])

config.plugins.XionHDF.ScrollBar = ConfigSelection(default="showNever", choices=[
				("showOnDemand", _("On")),
				("showNever", _("Off"))
				])

config.plugins.XionHDF.FontStyleHeight_1 = ConfigSelectionNumber(default=95, stepwidth=1, min=0, max=120, wraparound=True)
config.plugins.XionHDF.FontStyleHeight_2 = ConfigSelectionNumber(default=95, stepwidth=1, min=0, max=120, wraparound=True)
