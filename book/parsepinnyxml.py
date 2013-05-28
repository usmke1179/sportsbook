import urllib, datetime, models
from xml.etree import ElementTree as ET
# from django.db import models
import bettingformulas as bf
from django.views.generic import TemplateView


timezoneadj = datetime.timedelta(hours=4)

def parsemlb():
    feed = urllib.urlopen("http://xml.pinnaclesports.com/pinnaclefeed.aspx?sporttype=Baseball&sportsubtype=MLB")
    tree = ET.parse(feed)
    for events in tree.iter('event'):
        gamenumber = None
        eventtime = None
        vteam = None
        vpitcher = None
        vrot = None
        hteam = None
        hpitcher = None
        hrot = None
        periodnum = None
        perioddesc = None
        vml = None
        hml = None
        vspread = None
        vodds = None
        hspread = None
        hodds = None
        total = None
        overodds = None
        underodds = None
        gamenumber = events.find('gamenumber').text if events.find('gamenumber') is not None else None
        eventtime = datetime.datetime.strptime(events.find('event_datetimeGMT').text,'%Y-%m-%d %H:%M') - timezoneadj if events.find('event_datetimeGMT') is not None else None
        for participants in events.iter('participant'):
            if participants.find('visiting_home_draw').text == 'Visiting':
                vteam = participants.find('participant_name').text if participants.find('participant_name') is not None else None
                vpitcher = participants.find('pitcher').text if participants.find('pitcher') is not None else None
                vrot = int(participants.find('rotnum').text) if participants.find('rotnum') is not None else None
            if participants.find('visiting_home_draw').text == 'Home':
                hteam = participants.find('participant_name').text if participants.find('participant_name') is not None else None
                hpitcher = participants.find('pitcher').text if participants.find('pitcher') is not None else None
                hrot = int(participants.find('rotnum').text) if participants.find('rotnum') is not None else None
        for periods in events.iter('period'):
            periodnum = int(periods.find('period_number').text) if periods.find('period_number') is not None else None
            perioddesc = periods.find('period_description').text if periods.find('period_description') is not None else None
            for moneylines in periods.iter('moneyline'):
                vml = int(moneylines.find('moneyline_visiting').text) if moneylines.find('moneyline_visiting') is not None else None
                hml = int(moneylines.find('moneyline_home').text) if moneylines.find('moneyline_home') is not None else None
            for spreads in periods.iter('spread'):
                vspread = float(spreads.find('spread_visiting').text) if spreads.find('spread_visiting') is not None else None
                vodds = int(spreads.find('spread_adjust_visiting').text) if spreads.find('spread_adjust_visiting') is not None else None
                hspread = float(spreads.find('spread_home').text) if spreads.find('spread_home') is not None else None
                hodds = int(spreads.find('spread_adjust_home').text) if spreads.find('spread_adjust_home') is not None else None
            for totals in periods.iter('total'):
                total = float(totals.find('total_points').text) if totals.find('total_points') is not None else None
                overodds = int(totals.find('over_adjust').text) if totals.find('over_adjust') is not None else None
                underodds = int(totals.find('under_adjust').text) if totals.find('under_adjust') is not None else None
            vml = int(bf.adjustedvig(vml, hml)) if vml is not None else None
            hml = int(bf.adjustedvig(hml, vml)) if hml is not None else None
            vodds = int(bf.adjustedvig(vodds, hodds)) if vodds is not None else None
            hodds = int(bf.adjustedvig(hodds, vodds)) if hodds is not None else None
            overodds = int(bf.adjustedvig(overodds, underodds)) if overodds is not None else None
            underodds = int(bf.adjustedvig(underodds, overodds)) if underodds is not None else None
            line = models.BaseballLine(gamekey = gamenumber+str(periodnum),
                                        eventtime = eventtime,
                                        vteam = vteam,
                                        vpitcher = vpitcher,
                                        vrot = vrot,
                                        hteam = hteam,
                                        hpitcher = hpitcher,
                                        hrot = hrot,
                                        periodnum = periodnum,
                                        perioddesc = perioddesc,
                                        vml = vml,
                                        hml = hml,
                                        vspread = vspread,
                                        vodds = vodds,
                                        hspread = hspread,
                                        hodds = hodds,
                                        total = total,
                                        overodds = overodds,
                                        underodds = underodds)
            line.save()
    #old = db.Query(mydatabases.MLBlines).filter("eventtime <", datetime.datetime.now() - datetime.timedelta(days=7)
    #old.delete()

def parsenba():
    feed = urllib.urlopen("http://xml.pinnaclesports.com/pinnaclefeed.aspx?sporttype=Basketball&sportsubtype=NBA")
    tree = ET.parse(feed)
    for events in tree.iter('event'):
        gamenumber = None
        eventtime = None
        vteam = None
        vrot = None
        hteam = None
        hpitcher = None
        hrot = None
        periodnum = None
        perioddesc = None
        vml = None
        hml = None
        vspread = None
        vodds = None
        hspread = None
        hodds = None
        total = None
        overodds = None
        underodds = None
        gamenumber = events.find('gamenumber').text if events.find('gamenumber') is not None else None
        eventtime = datetime.datetime.strptime(events.find('event_datetimeGMT').text,'%Y-%m-%d %H:%M') - timezoneadj if events.find('event_datetimeGMT') is not None else None
        for participants in events.iter('participant'):
            if participants.find('visiting_home_draw').text == 'Visiting':
                vteam = participants.find('participant_name').text if participants.find('participant_name') is not None else None
                vrot = int(participants.find('rotnum').text) if participants.find('rotnum') is not None else None
            if participants.find('visiting_home_draw').text == 'Home':
                hteam = participants.find('participant_name').text if participants.find('participant_name') is not None else None
                hrot = int(participants.find('rotnum').text) if participants.find('rotnum') is not None else None
        for periods in events.iter('period'):
            periodnum = int(periods.find('period_number').text) if periods.find('period_number') is not None else None
            perioddesc = periods.find('period_description').text if periods.find('period_description') is not None else None
            for moneylines in periods.iter('moneyline'):
                vml = int(moneylines.find('moneyline_visiting').text) if moneylines.find('moneyline_visiting') is not None else None
                hml = int(moneylines.find('moneyline_home').text) if moneylines.find('moneyline_home') is not None else None
            for spreads in periods.iter('spread'):
                vspread = float(spreads.find('spread_visiting').text) if spreads.find('spread_visiting') is not None else None
                vodds = int(spreads.find('spread_adjust_visiting').text) if spreads.find('spread_adjust_visiting') is not None else None
                hspread = float(spreads.find('spread_home').text) if spreads.find('spread_home') is not None else None
                hodds = int(spreads.find('spread_adjust_home').text) if spreads.find('spread_adjust_home') is not None else None
            for totals in periods.iter('total'):
                total = float(totals.find('total_points').text) if totals.find('total_points') is not None else None
                overodds = int(totals.find('over_adjust').text) if totals.find('over_adjust') is not None else None
                underodds = int(totals.find('under_adjust').text) if totals.find('under_adjust') is not None else None
            vml = int(bf.adjustedvig(vml, hml)) if vml is not None else None
            hml = int(bf.adjustedvig(hml, vml)) if hml is not None else None
            vodds = int(bf.adjustedvig(vodds, hodds)) if vodds is not None else None
            hodds = int(bf.adjustedvig(hodds, vodds)) if hodds is not None else None
            overodds = int(bf.adjustedvig(overodds, underodds)) if overodds is not None else None
            underodds = int(bf.adjustedvig(underodds, overodds)) if underodds is not None else None
            line = models.BasketballLine(gamekey = gamenumber+str(periodnum),
                                        eventtime = eventtime,
                                        vteam = vteam,
                                        vrot = vrot,
                                        hteam = hteam,
                                        hrot = hrot,
                                        periodnum = periodnum,
                                        perioddesc = perioddesc,
                                        vml = vml,
                                        hml = hml,
                                        vspread = vspread,
                                        vodds = vodds,
                                        hspread = hspread,
                                        hodds = hodds,
                                        total = total,
                                        overodds = overodds,
                                        underodds = underodds)
            line.save()

class ParseXML(TemplateView):
    parsemlb()
    parsenba()
    template_name = "book/parse.html"