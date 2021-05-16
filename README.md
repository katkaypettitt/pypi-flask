# PyPI Flask Website 

> A fake website modelled after [PyPI.org](https://pypi.org/) made using Python, HTML, and CSS with the help of [TalkPython](https://talkpython.fm/).

![PyPI Flask Website by Katrina Alaimo](https://video.wixstatic.com/video/d051dc_3991c67351ad4c2ba584f7aeda0f07fd/1080p/mp4/file.mp4)

## General info

This website is modelled after the Python Package Index website using the Flask web framework and includes functional registration and login forms and a SQLite database with Python package information imported from JSON files. Jinja2 was used as the dynamic html language and Bootstrap significantly modernized the layout. Data queries are done through SQLAlchemy and Alembic, which automatically remaps database schema with migrations to sync the database. 

The layout creation was streamlined by creating a shared page template for all package pages. A view model design pattern was utilized to make testing more efficient as well as the action and view methods simpler to implement. The view models are tightly tied to the HTML form to exchange and validate data. This ensures that duplicate accounts cannot be created, passwords adhere to specific guidelines, and email addresses are properly inserted. 

Tests debug the site and ensure it is without major errors. Specifically, the following types of testing were used: view model testing, view method testing, and integration (fake HTTP request) testing. 

This Flask website can be improved by filling in additional pages (e.g. Donate page, child pages within each package page, etc.) and by making it completely interactive (i.e. the search bar).

<u>Run `app.py` to start the web application.</u> Note that Alembic will need to be initialised (`alembic init alembic`), updated (`alembic revision --autogenerate -m`) and upgraded (`alembic upgrade head`) if it is the first time using it on the machine. 

## Technologies

- Python 3 (Flask, SQLAlchemy, Alembic, pytest)
- Jinja2
- HTML
- CSS & Bootstrap

## Contact

Created by [@katrinaalaimo](https://www.katrinaalaimo.com/) — feel free to contact me!