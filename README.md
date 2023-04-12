# Description

<p>Is an online single page web application that enables you to manage orders and inventory with ability to get, add, edit, or delete products, firms, brands, sales, and purchases.🚘</p>

# Models

- Car
- Reservation
- User

![Model](https://github.com/klc-pakize/django_rent_a_car/blob/master/RentACarAppERD.png)

# Customers

    - Can select start and end date and see the list of available cars on selected dates.
    - Can choose a car on the list and reserve that car, but can not reserve more than one car on a selected time period,
    - Can see the list of their reservations including past ones.
    - Can update reservations, but;
        - Can not extend end dates if the car is reserved by other customers on selected time.
    - Can delete their reservations.

# Admins

    - Can make CRUD operations on Car table,
    - Can make CRUD operations on Customers table,
    - Can make CRUD operations on Reservations table,

# Live Project

- <a href="http://klc.pythonanywhere.com/">Live of the project</a>
- <a href="https://klc.pythonanywhere.com/swagger/">For the swagger of the project</a>

# Docker:

<p>1- docker pull pakizekilic/rentacar:v1</p>
<p>2- docker run -d -p 8000:8000 kullanici_adi/rentacar:v1</p>
<p>3- docker images</p>
<p>4- docker exec -it <imaj_id> bash</p>
<p>5- python manage.py createsuperuser</p>
<p>6- http://localhost:8000</p>
