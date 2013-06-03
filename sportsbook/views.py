import datetime
from django_tables2 import SingleTableView
from book import parsepinnyxml, tables, models


class Home(SingleTableView):
    # def get(self, request, *args, **kwargs):
    #     parsepinnyxml.parsemlb()
    #     parsepinnyxml.parsenba()
    #     self.object_list = self.get_queryset()
    #     context = self.get_context_data(object_list=self.object_list)
    #     return self.render_to_response(context)

    template_name = "book/index.html"
    model = models.BaseballLine
    display = []
    for line in model.objects.filter(periodnum=0):#, eventtime__gt=datetime.datetime.now()):
        display.append({
            "gamekey": line.gamekey,
            "gametime": line.eventtime,
            "rot": line.vrot,
            "team": line.vteam,
            "pitcher": line.vpitcher,
            "ml": line.vml,
            "rl": str(line.vspread) + " " + str(line.vodds),
            "total": "o" + str(line.total) + " " + str(line.overodds),
        })
        display.append({
            "gamekey": line.gamekey,
            "rot": line.hrot,
            "team": line.hteam,
            "pitcher": line.hpitcher,
            "ml": line.hml,
            "rl": str(line.hspread) + " " + str(line.hodds),
            "total": "u" + str(line.total) + " " + str(line.underodds),
        })
    table_data = display
    table_class = tables.BaseballLinesTable
