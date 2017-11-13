from pyramid.view import (
    view_config,
    view_defaults
    )
from tvshowslib import tvshowslib
from random import randint
from .models import DBSession, Session, Access
from pyramid.response import Response
from datetime import datetime

def format_tvshows(tvshows):
    response = "<ul>"
    for tvshow in tvshows:
        response += "<li> {} </li>".format(tvshow)
    response += "</ul>" 
    return response

@view_defaults()
class ChallengeViews:
    def __init__(self, request):
        self.request = request
        self.sessions_num = 0
        self.now = datetime.now()

    def counter(self):
        session = self.request.session
        session_info = self.request.user_agent.split(") ")[0].replace("(", '')
        if 'counter' in session:
            session['counter'] += 1
        else:
            session['counter'] = 1
            session_instance = Session()
            session_instance.info = session_info
            DBSession.add(session_instance)
            DBSession.flush()
            session['id'] = session_instance.uid
        return session['counter']

    def handle_requests(self, page):
        session = self.request.session
        if 'id' in session:
            query_instance = Access()
            query_instance.session_id = session['id']
            query_instance.page = page
            query_instance.datetime = self.now.strftime("%Y-%m-%d %H:%M")
            DBSession.add(query_instance)

    @view_config(route_name='home', renderer='home.pt')
    def home(self):
        route_name = 'home'
        counter = self.counter()
        self.handle_requests(route_name)
        return {'name': 'Python server made wih "The Pyramid Web Framework" tutorial', 'counter': counter}

    @view_config(route_name='tvshows', renderer='list_view.pt')
    def quotes_request(self):
        route_name = 'tvshows'
        counter = self.counter()
        self.handle_requests(route_name)
        tvshows = tvshowslib.get_tvshows()
        print(tvshows)
        return {'list': tvshows, 'counter': counter}

    @view_config(route_name='tvshow', renderer='home.pt')
    def quote_request(self):
        route_name = 'tvshow'
        counter = self.counter()
        self.handle_requests(route_name)
        quote_num = self.request.matchdict["tvshow_num"]
        tvshow = tvshowslib.get_tvshow(quote_num)
        return {'name': tvshow, 'counter': counter}

    @view_config(route_name='random', renderer='home.pt')
    def random_request(self):
        route_name = 'random'
        counter = self.counter()
        self.handle_requests(route_name)
        tvshows = tvshowslib.get_tvshows()
        random_num = randint(0, len(tvshows))
        tvshow = tvshowslib.get_tvshow(random_num)
        return {'name': "{}. {}".format(random_num, tvshow), 'counter': counter}

    @view_config(route_name='sessions', renderer='sessions_view.pt')
    def sessions(self):
        route_name = 'sessions'
        counter = self.counter()
        self.handle_requests(route_name)
        sessions = DBSession.query(Session).order_by(Session.uid)
        print(sessions)
        return {'list': sessions, 'counter': counter}

    @view_config(route_name='accesses', renderer='accesses_view.pt')
    def accesses(self):
        route_name = 'accesses'
        counter = self.counter()
        self.handle_requests(route_name)
        queries = DBSession.query(Access).order_by(Access.uid)
        return {'list': queries, 'counter': counter}
