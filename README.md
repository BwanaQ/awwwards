# AWWWARDS

A web application built on Django as a mockup for the site (awwwards), a search function and sorts images by categories

## Getting Started

- clone this repo

```
$ git clone https://github.com/BwanaQ/awwwards.git
```

### Prerequisites

- Python 3 latest version
- Pip3 installer
- virtualenv command

### Installing

1. cd into the awwwards folder

```
$ cd awwwards
```

2. Add a python 3 environment

```
$ virtualenv env
```

3. Enter the virtual environment

```
$ source env/bin/activate
```

4. Install dependancies from requirements.txt

```
(env)$ pip install -r requirements.txt
```

5. rename .env copy to .env then run this command

```
(env) $ source .env
```

6. Run server

```
(env) $ python manage.py runserver
```

## Deployment

to deploy to heroku simply create a project and attach your git hub repository

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Bootstrap](https://getbootstrap.com/) - Frontend for the monolithic app

## Authors

- **Tom Hunja**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Thanks to [Toptal](https://www.toptal.com/developers/gitignore/api/django) for a beautiful .gitignore file
- Thanks to [Firchow](http://circle.firchow.net/) for the pure css percentage circle
- Inspiration - My Technical Mentor Kelvin Onkundi and The Olympians Team MC38
