from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .models import DBSession, Base
from pyramid.session import SignedCookieSessionFactory

def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    my_session_factory = SignedCookieSessionFactory(
        'mysessions')
    config = Configurator(settings=settings,
                          root_factory='challenge.models.Root', 
                          session_factory=my_session_factory)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.add_route('random', '/tvshows/random')
    config.add_route('tvshow', '/tvshows/{tvshow_num}')
    config.add_route('tvshows', '/tvshows')
    config.add_route('sessions', '/sessions')
    config.add_route('accesses', '/accesses')
    config.add_static_view('deform_static', 'deform:static/')
    config.scan('.views')
    return config.make_wsgi_app()