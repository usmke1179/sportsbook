import django_tables2 as tables
from django.utils.safestring import mark_safe, SafeData
from django_tables2.templatetags.django_tables2 import title


class CustomCheckBoxColumn(tables.CheckBoxColumn):
    def header(self):
        if self.verbose_name:
            if isinstance(self.verbose_name, SafeData):
                return self.verbose_name
            return title(self.verbose_name)

    def render(self, value, record, bound_column):
        default = {
            'type': 'checkbox',
            'name': 'lineid',
            'value': record['gamekey'] + '-' + str(record['rot']) + '-' + bound_column.name
        }
        general = self.attrs.get('input')
        specific = self.attrs.get('td__input')
        attrs = tables.utils.AttributeDict(default, **(specific or general or {}))
        return mark_safe('<input %s/> ' % attrs.as_html() + str(value))


class BaseballLinesTable(tables.Table):
    gamekey = tables.Column()
    gametime = tables.DateTimeColumn(verbose_name="Game Time", orderable=False)
    rot = tables.Column(verbose_name="Rot", orderable=False)
    team = tables.Column(verbose_name="Team", orderable=False)
    pitcher = tables.Column(verbose_name="Pitcher", orderable=False)
    ml = CustomCheckBoxColumn(verbose_name="Moneyline", orderable=False)
    rl = CustomCheckBoxColumn(verbose_name="Runline", orderable=False)
    total = CustomCheckBoxColumn(verbose_name="Total", orderable=False)

    class Meta:
        attrs = {"class": "table table-bordered table-striped table-hover"}
        empty_text = "There are no games available."
        exclude = ("gamekey", )


class BasketballLinesTable(tables.Table):
    gamekey = tables.Column()
    gametime = tables.DateTimeColumn(verbose_name="Game Time", orderable=False)
    rot = tables.Column(verbose_name="Rot", orderable=False)
    team = tables.Column(verbose_name="Team", orderable=False)
    ml = CustomCheckBoxColumn(verbose_name="Moneyline", orderable=False)
    rl = CustomCheckBoxColumn(verbose_name="Spread", orderable=False)
    total = CustomCheckBoxColumn(verbose_name="Total", orderable=False)

    class Meta:
        attrs = {"class": "table table-bordered table-striped table-hover"}
        empty_text = "There are no games available."
        exclude = ("gamekey", )


class FootballLinesTable(tables.Table):
    gamekey = tables.Column()
    gametime = tables.DateTimeColumn(verbose_name="Game Time", orderable=False)
    rot = tables.Column(verbose_name="Rot", orderable=False)
    team = tables.Column(verbose_name="Team", orderable=False)
    ml = CustomCheckBoxColumn(verbose_name="Moneyline", orderable=False)
    rl = CustomCheckBoxColumn(verbose_name="Spread", orderable=False)
    total = CustomCheckBoxColumn(verbose_name="Total", orderable=False)

    class Meta:
        attrs = {"class": "table table-bordered table-striped table-hover"}
        empty_text = "There are no games available."
        exclude = ("gamekey", )


class HockeyLinesTable(tables.Table):
    gamekey = tables.Column()
    gametime = tables.DateTimeColumn(verbose_name="Game Time", orderable=False)
    rot = tables.Column(verbose_name="Rot", orderable=False)
    team = tables.Column(verbose_name="Team", orderable=False)
    ml = CustomCheckBoxColumn(verbose_name="Moneyline", orderable=False)
    rl = CustomCheckBoxColumn(verbose_name="Runline", orderable=False)
    total = CustomCheckBoxColumn(verbose_name="Total", orderable=False)

    class Meta:
        attrs = {"class": "table table-bordered table-striped table-hover"}
        empty_text = "There are no games available."
        exclude = ("gamekey", )
