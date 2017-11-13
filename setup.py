from setuptools import setup

requires = [
    'pyramid',
    'waitress',
    'pyramid_chameleon',
    'deform',
    'sqlalchemy',
    'pyramid_tm',
    'zope.sqlalchemy'
]

setup(name='challenge',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = challenge:main
      [console_scripts]
      initialize_challenge_db = challenge.initialize_db:main
      """,
)