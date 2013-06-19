import datetime
from django_tables2 import SingleTableView
import pinnaclesports
import tables
# import models


class BaseballView(SingleTableView):
    pinnacle_object = pinnaclesports.Pinnacle()
    mlb_lines = pinnacle_object.parse_xml(sporttype="baseball", sportsubtype="mlb")
    template_name = "book/index.html"
    # model = models.BaseballLine
    queryset = 0
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

    table_data = display
    table_pagination = False
    table_class = tables.BaseballLinesTable

