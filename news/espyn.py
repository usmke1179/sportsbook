# modified from espyn written by chadmasso
import requests
import json


VALID_SPORTS = ['baseball', 'basketball', 'boxing',
                'football', 'golf', 'horse-racing',
                'mma', 'racing', 'soccer', 'tennis']
VALID_LEAGUES = ['mlb', 'nba', 'wnba', 'mens-college-basketball',
                 'womens-college-basketball', 'nfl', 'college-football',
                 'ata', 'wta', 'epl', 'mls', 'pga', 'ntw', 'sgq', 'eur']


class ESPN(object):
    def __init__(self, api_key, version="v1", limit=20):
        self.__api_key = api_key
        self.__version = version
        self.__limit = limit
        self.__url = "http://api.espn.com/%s" % version
        self.__format = "application/json"

    def __valid_sport(self, sport):
        return (sport in VALID_SPORTS)

    def __valid_league(self, league):
        return (league in VALID_LEAGUES)

    def api_call(self, resource, method):
        url = "%s/%s/%s" % (self.__url, resource, method)
        params = {'apikey': self.__api_key, 'limit': self.__limit}
        r = requests.get(url, params=params)
        r.raise_for_status()
        try:
            results = json.loads(r.content)
        except:
            raise("API results could not be parsed")

        if results['status'] == 'success':
            return results
        else:
            raise("%s - %s" % (results['code'], results['message']))

    def headlines(self, **params):
        """Provides an interface for getting data from the headlines api
        Returns Dictionary of results

        :param sport: (optional) Name of sport
        :param league: (optional) Name of league
        :param date: (optional) String date in YYYYMMDD format
        :param athlete: (optional) Id of athlete
        :param team: (optional) Id of team
        """
        # construct resource
        resources = ['sports']
        sport = params.get('sport')
        if sport and self.__valid_sport(sport):
            resources.append(sport)
        league = params.get('league')
        if league and self.__valid_league(league):
            resources.append(league)
        resource = '/'.join(resources)

        #construct method
        methods = ['news/headlines/top']
        date = params.get('date')
        if date:
            methods.append('dates/%s' % date)
        athlete = params.get('athlete')
        team = params.get('team')
        if athlete:
            methods.preprend('athletes/%s' % athlete)
        elif team:
            methods.preprend('teams/%s' % team)
        method = '/'.join(methods)

        return self.api_call(resource, method)
