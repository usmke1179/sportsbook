import urllib
import datetime
# import models
from xml.etree import ElementTree as ET
# from django.db import models
import bettingformulas as bf


timezoneadj = datetime.timedelta(hours=4)

VALID_SPORTS = ["baseball", "basketball", "boxing",
                "football", "golf", "horse-racing",
                "mma", "racing", "soccer", "tennis"]
VALID_LEAGUES = ["mlb", "nba", "wnba", "mens-college-basketball",
                 "womens-college-basketball", "nfl", "college-football",
                 "ata", "wta", "epl", "mls", "pga", "ntw", "sgq", "eur"]


class Pinnacle(object):
    def __init__(self):
        self.__url = "http://xml.pinnaclesports.com/pinnaclefeed.aspx"
        self.__format = "application/xml"

    def __valid_sport(self, sport):
        return (sport in VALID_SPORTS)

    def __valid_league(self, league):
        return (league in VALID_LEAGUES)

    def parse_xml(self, **params):
        """Provides an interface for getting data from the pinnaclesports api
        Returns list of results

        :param sporttype: (optional) Name of sport
        :param sportsubtype: (optional) Name of league
        """
        # construct resource
        attributes = []
        sporttype = params.get("sporttype")
        if sporttype and self.__valid_sport(sporttype):
            attributes.append("sporttype=" + sporttype)
        sportsubtype = params.get("sportsubtype")
        if sportsubtype and self.__valid_league(sportsubtype):
            attributes.append("sportsubtype=" + sportsubtype)
        attributes = "&".join(attributes)

        url = "%s?%s" % (self.__url, attributes)
        feed = urllib.urlopen(url)

        tree = ET.parse(feed)
        feed_time = datetime.datetime.now()
        pinnacle_feed_time = tree.find("PinnacleFeedTime").text
        lines = []
        for events in tree.iter("event"):
            event = {}
            event["feed_time"] = feed_time
            event["pinnaclefeedtime"] = pinnacle_feed_time
            event["gamenumber"] = events.find("gamenumber").text if events.find("gamenumber") is not None else None
            event["eventtime"] = datetime.datetime.strptime(events.find("event_datetimeGMT").text, "%Y-%m-%d %H:%M") - timezoneadj if events.find("event_datetimeGMT") is not None else None
            for participants in events.iter("participant"):
                if participants.find("visiting_home_draw").text == "Visiting":
                    event["vteam"] = participants.find("participant_name").text if participants.find("participant_name") is not None else None
                    if sporttype == "baseball":
                        event["vpitcher"] = participants.find("pitcher").text if participants.find("pitcher") is not None else None
                    event["vrot"] = int(participants.find("rotnum").text) if participants.find("rotnum") is not None else None
                if participants.find("visiting_home_draw").text == "Home":
                    event["hteam"] = participants.find("participant_name").text if participants.find("participant_name") is not None else None
                    if sporttype == "baseball":
                        event["hpitcher"] = participants.find("pitcher").text if participants.find("pitcher") is not None else None
                    event["hrot"] = int(participants.find("rotnum").text) if participants.find("rotnum") is not None else None
            for periods in events.iter("period"):
                if int(periods.find("period_number").text) == 0:
                    event["periodnum"] = int(periods.find("period_number").text) if periods.find("period_number") is not None else None
                    event["perioddesc"] = periods.find("period_description").text if periods.find("period_description") is not None else None
                    for moneylines in periods.iter("moneyline"):
                        event["vml"] = int(moneylines.find("moneyline_visiting").text) if moneylines.find("moneyline_visiting") is not None else None
                        event["hml"] = int(moneylines.find("moneyline_home").text) if moneylines.find("moneyline_home") is not None else None
                    for spreads in periods.iter("spread"):
                        event["vspread"] = float(spreads.find("spread_visiting").text) if spreads.find("spread_visiting") is not None else None
                        event["vodds"] = int(spreads.find("spread_adjust_visiting").text) if spreads.find("spread_adjust_visiting") is not None else None
                        event["hspread"] = float(spreads.find("spread_home").text) if spreads.find("spread_home") is not None else None
                        event["hodds"] = int(spreads.find("spread_adjust_home").text) if spreads.find("spread_adjust_home") is not None else None
                    for totals in periods.iter("total"):
                        event["total"] = float(totals.find("total_points").text) if totals.find("total_points") is not None else None
                        event["overodds"] = int(totals.find("over_adjust").text) if totals.find("over_adjust") is not None else None
                        event["underodds"] = int(totals.find("under_adjust").text) if totals.find("under_adjust") is not None else None
                    event["vml"] = int(bf.adjustedvig(event.get("vml"), event.get("hml"))) if event.get("vml") is not None else None
                    event["hml"] = int(bf.adjustedvig(event.get("hml"), event.get("vml"))) if event.get("hml") is not None else None
                    event["vodds"] = int(bf.adjustedvig(event.get("vodds"), event.get("hodds"))) if event.get("vodds") is not None else None
                    event["hodds"] = int(bf.adjustedvig(event.get("hodds"), event.get("vodds"))) if event.get("hodds") is not None else None
                    event["overodds"] = int(bf.adjustedvig(event.get("overodds"), event.get("underodds"))) if event.get("overodds") is not None else None
                    event["underodds"] = int(bf.adjustedvig(event.get("underodds"), event.get("overodds"))) if event.get("underodds") is not None else None
            lines.append(event)
        return lines

    def save_lines(self, lines):
        for line in lines:
            l = models.BaseballLine(
                gamekey=line["gamenumber"]+str(line["periodnum"]),
                eventtime=line["eventtime"],
                vteam=line["vteam"],
                vpitcher=line["vpitcher"],
                vrot=line["vrot"],
                hteam=line["hteam"],
                hpitcher=line["hpitcher"],
                hrot=line["hrot"],
                periodnum=line["periodnum"],
                perioddesc=line["perioddesc"],
                vml=line["vml"],
                hml=line["hml"],
                vspread=line["vspread"],
                vodds=line["vodds"],
                hspread=line["hspread"],
                hodds=line["hodds"],
                total=line["total"],
                overodds=line["overodds"],
                underodds=line["underodds"])
            l.save()
