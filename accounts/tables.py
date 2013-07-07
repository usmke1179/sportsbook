import django_tables2 as tables


class BaseballLinesTable(tables.Table):
    eventtime = tables.DateTimeColumn(verbose_name="Game Time")
    bet_desc = tables.Column(verbose_name="Description")
    risk = tables.Column(verbose_name="Risk")
    to_win = tables.Column(verbose_name="To Win")
    result = tables.Column(verbose_name="Result")

    class Meta:
        attrs = {"class": "table table-bordered table-striped table-hover"}
        empty_text = "There are no games available."
        exclude = ("gamekey", )
