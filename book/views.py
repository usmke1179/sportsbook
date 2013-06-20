import datetime
from django_tables2 import SingleTableView
import pinnaclesports
import tables
import models


class BaseballView(SingleTableView):
    template_name = "book/lines.html"
    model = models.BaseballLine
    table_pagination = False
    table_class = tables.BaseballLinesTable

    def get_queryset(self):
        pinnacle_object = pinnaclesports.Pinnacle()
        mlb_lines = pinnacle_object.parse_xml(sporttype="baseball", sportsubtype="mlb")
        display = []
        for line in mlb_lines:
            if "periodnum" in line:
                if line["periodnum"] == 0:
                    rowdict = {}
                    if "gamenumber" in line:
                        rowdict["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                    if "eventtime" in line:
                        rowdict["gametime"] = line["eventtime"]
                    if "vrot" in line:
                        rowdict["rot"] = line["vrot"]
                    if "vteam" in line:
                        rowdict["team"] = line["vteam"]
                    if "vpitcher" in line:
                        rowdict["pitcher"] = line["vpitcher"]
                    if "vml" in line:
                        rowdict["ml"] = line["vml"]
                    if "vspread" in line:
                        rowdict["rl"] = str(line["vspread"]) + str(line["vodds"])
                    if "total" in line:
                        rowdict["total"] = "o" + str(line["total"]) + " " + str(line["overodds"])
                    display.append(rowdict)
                    rowdict = {}
                    if "gamenumber" in line:
                        rowdict["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                    if "hrot" in line:
                        rowdict["rot"] = line["hrot"]
                    if "hteam" in line:
                        rowdict["team"] = line["hteam"]
                    if "hpitcher" in line:
                        rowdict["pitcher"] = line["hpitcher"]
                    if "hml" in line:
                        rowdict["ml"] = line["hml"]
                    if "hspread" in line:
                        rowdict["rl"] = str(line["hspread"]) + str(line["hodds"])
                    if "total" in line:
                        rowdict["total"] = "u" + str(line["total"]) + " " + str(line["underodds"])
                    display.append(rowdict)
        return display


class BasketballView(SingleTableView):
    template_name = "book/lines.html"
    model = models.BasketballLine
    table_pagination = False
    table_class = tables.BasketballLinesTable

    def get_queryset(self):
        pinnacle_object = pinnaclesports.Pinnacle()
        nba_lines = pinnacle_object.parse_xml(sporttype="basketball", sportsubtype="nba")
        display = []
        for line in nba_lines:
            if "periodnum" in line:
                if line["periodnum"] == 0:
                    rowdict = {}
                    if "gamenumber" in line:
                        rowdict["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                    if "eventtime" in line:
                        rowdict["gametime"] = line["eventtime"]
                    if "vrot" in line:
                        rowdict["rot"] = line["vrot"]
                    if "vteam" in line:
                        rowdict["team"] = line["vteam"]
                    if "vml" in line:
                        rowdict["ml"] = line["vml"]
                    if "vspread" in line:
                        rowdict["rl"] = str(line["vspread"]) + str(line["vodds"])
                    if "total" in line:
                        rowdict["total"] = "o" + str(line["total"]) + " " + str(line["overodds"])
                    display.append(rowdict)
                    rowdict = {}
                    if "gamenumber" in line:
                        rowdict["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                    if "hrot" in line:
                        rowdict["rot"] = line["hrot"]
                    if "hteam" in line:
                        rowdict["team"] = line["hteam"]
                    if "hml" in line:
                        rowdict["ml"] = line["hml"]
                    if "hspread" in line:
                        rowdict["rl"] = str(line["hspread"]) + str(line["hodds"])
                    if "total" in line:
                        rowdict["total"] = "u" + str(line["total"]) + " " + str(line["underodds"])
                    display.append(rowdict)
        return display


class FootballView(SingleTableView):
    template_name = "book/lines.html"
    model = models.FootballLine
    table_pagination = False
    table_class = tables.FootballLinesTable

    def get_queryset(self):
        pinnacle_object = pinnaclesports.Pinnacle()
        nfl_lines = pinnacle_object.parse_xml(sporttype="football", sportsubtype="nfl")
        display = []
        for line in nfl_lines:
            if "periodnum" in line:
                if line["periodnum"] == 0:
                    rowdict = {}
                    if "gamenumber" in line:
                        rowdict["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                    if "eventtime" in line:
                        rowdict["gametime"] = line["eventtime"]
                    if "vrot" in line:
                        rowdict["rot"] = line["vrot"]
                    if "vteam" in line:
                        rowdict["team"] = line["vteam"]
                    if "vml" in line:
                        rowdict["ml"] = line["vml"]
                    if "vspread" in line:
                        rowdict["rl"] = str(line["vspread"]) + str(line["vodds"])
                    if "total" in line:
                        rowdict["total"] = "o" + str(line["total"]) + " " + str(line["overodds"])
                    display.append(rowdict)
                    rowdict = {}
                    if "gamenumber" in line:
                        rowdict["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                    if "hrot" in line:
                        rowdict["rot"] = line["hrot"]
                    if "hteam" in line:
                        rowdict["team"] = line["hteam"]
                    if "hml" in line:
                        rowdict["ml"] = line["hml"]
                    if "hspread" in line:
                        rowdict["rl"] = str(line["hspread"]) + str(line["hodds"])
                    if "total" in line:
                        rowdict["total"] = "u" + str(line["total"]) + " " + str(line["underodds"])
                    display.append(rowdict)
        return display
