from django.core.cache import cache
from django_tables2 import SingleTableView
from . import pinnaclesports
from . import tables
from . import models


class BaseballView(SingleTableView):
    template_name = "book/lines.html"
    table_pagination = False
    table_class = tables.BaseballLinesTable

    def get_queryset(self):
        if cache.get("mlbLines") is not None:
            return cache.get("mlbLines")
        else:
            pinnacle_object = pinnaclesports.Pinnacle()
            mlb_lines = pinnacle_object.parse_xml(sporttype="baseball", sportsubtype="mlb")
            lines_by_date = sorted(mlb_lines, key=lambda k: k["eventtime"])
            display = []
            for line in lines_by_date:
                if "periodnum" in line:
                    if line["periodnum"] == 0:
                        row1 = {}
                        if "gamenumber" in line:
                            row1["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                        if "eventtime" in line:
                            row1["gametime"] = line["eventtime"]
                        if "vrot" in line:
                            row1["rot"] = line["vrot"]
                        if "vteam" in line:
                            row1["team"] = line["vteam"]
                        if "vpitcher" in line:
                            row1["pitcher"] = line["vpitcher"]
                        if "vml" in line:
                            row1["ml"] = line["vml"]
                        if "vspread" in line:
                            row1["rl"] = str(line["vspread"]) + " " + str(line["vodds"])
                        if "total" in line:
                            row1["total"] = "o" + str(line["total"]) + " " + str(line["overodds"])
                        display.append(row1)
                        row2 = {}
                        if "gamenumber" in line:
                            row2["gamekey"] = line["gamenumber"]+str(line["periodnum"])
                        if "hrot" in line:
                            row2["rot"] = line["hrot"]
                        if "hteam" in line:
                            row2["team"] = line["hteam"]
                        if "hpitcher" in line:
                            row2["pitcher"] = line["hpitcher"]
                        if "hml" in line:
                            row2["ml"] = line["hml"]
                        if "hspread" in line:
                            row2["rl"] = str(line["hspread"]) + " " + str(line["hodds"])
                        if "total" in line:
                            row2["total"] = "u" + str(line["total"]) + " " + str(line["underodds"])
                        display.append(row2)
            cache.set("mlbLines", display)
            return display


class BasketballView(SingleTableView):
    template_name = "book/lines.html"
    table_pagination = False
    table_class = tables.BasketballLinesTable

    def get_queryset(self):
        if cache.get("nbaLines") is not None:
            return cache.get("nbaLines")
        else:
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
                            rowdict["rl"] = str(line["vspread"]) + " " + str(line["vodds"])
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
                            rowdict["rl"] = str(line["hspread"]) + " " + str(line["hodds"])
                        if "total" in line:
                            rowdict["total"] = "u" + str(line["total"]) + " " + str(line["underodds"])
                        display.append(rowdict)
            cache.set("nbaLines", display)
            return display


class FootballView(SingleTableView):
    template_name = "book/lines.html"
    table_pagination = False
    table_class = tables.FootballLinesTable

    def get_queryset(self):
        if cache.get("nflLines") is not None:
            return cache.get("nflLines")
        else:
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
                            rowdict["rl"] = str(line["vspread"]) + " " + str(line["vodds"])
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
                            rowdict["rl"] = str(line["hspread"]) + " " + str(line["hodds"])
                        if "total" in line:
                            rowdict["total"] = "u" + str(line["total"]) + " " + str(line["underodds"])
                        display.append(rowdict)
            cache.set("nflLines", display)
            return display
