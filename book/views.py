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
            display.append({
                "gamekey": line["gamenumber"]+str(line["periodnum"]),
                "gametime": line["eventtime"],
                "rot": line["vrot"],
                "team": line["vteam"],
                "pitcher": line["vpitcher"],
                "ml": line["vml"],
                "rl": str(line["vspread"]) + " " + str(line["vodds"]),
                "total": "o" + str(line["total"]) + " " + str(line["overodds"]),
            })
            display.append({
                "gamekey": line["gamenumber"]+str(line["periodnum"]),
                "rot": line["hrot"],
                "team": line["hteam"],
                "pitcher": line["hpitcher"],
                "ml": line["hml"],
                "rl": str(line["hspread"]) + " " + str(line["hodds"]),
                "total": "u" + str(line["total"]) + " " + str(line["underodds"]),
            })
    table_data = display
    table_class = tables.BaseballLinesTable
