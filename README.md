# python_pyramid
Python server using the pyramid web framework - contains database integration and sessions recording.

- Pyramid web framework v1.9.1
- RESTful API
- SQLAlchemy database integration
- Python 2.7 as programming language
- Sessions

Before running the program:
- pip install -e 

To run the program:
- pserve development.ini --reload

Observations:
- Server runs on localhost:8080
- Webpages shows how many times the server was accessed in a session

Available endpoints/pages:
- localhost:8080/ - home
- localhost:8080/tvshows - tvshows names from a local library
- localhost:8080/tvshows/{tvshownumber} - get one tvshow name according to the number (1 to 10)
- localhost:8080/sessions - shows all sessions used to access the server pages
- localhost:8080/queries - shows all pages requests that were done
 
Tutorial used:
- https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html by The Pyramid Web Framework v1.9.1 

Author:
Laura Vieira