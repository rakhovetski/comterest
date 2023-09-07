# Comtereset - is a site for finding people by common interests and building team

## Launch of the project

In order to run the project you need to run the following commands, for which docker is useful

1) Build docker-compose file

#### docker-compose build --no-cache

2) Apply migrations

#### docker-compose run web-app sh -c "python manage.py migrate"

3) Run project

#### docker-compose up

4) You can also create a super user

#### docker-compose run web-app sh -c "python manage.py createsuperuser"

<hr>

## Technologies

Core technologies:
-Python
- Django
- Django REST
-Docker
- PostgreSQL

Assistive technologies:
- Celery
- Redis
- HTML
- CSS
- Bootstrap

<hr>

## Preview 

### Create your account
![image](https://github.com/rakhovetski/comterest/assets/93330902/38265d56-b231-4ac1-b3af-65d5d5366b0a)

<hr>

### You can login into your account

![image](https://github.com/rakhovetski/comterest/assets/93330902/7097a967-f283-45d3-8aa1-e0eeb7319c63)

<hr>

### In your account, you can add projects you have worked on or create a team to recruit people for a new project

![image](https://github.com/rakhovetski/comterest/assets/93330902/27792648-a124-4662-9fd9-5938756f8d4e)

<hr>

### You can look at other accounts and if they are of interest to you, then subscribe to them

![image](https://github.com/rakhovetski/comterest/assets/93330902/35b20869-b94d-46a5-a9cb-2689cadbd83a)
![image](https://github.com/rakhovetski/comterest/assets/93330902/5286e87d-74fc-4ea8-b8d5-4013f4f6863e)

<hr>

### You can also use search to find users or teams

![image](https://github.com/rakhovetski/comterest/assets/93330902/6db80fc4-01bb-4cc8-83b5-1c2e433690ee)

<hr>


