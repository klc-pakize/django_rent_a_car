# Description

<p>Is an online single page web application that enables you to manage orders and inventory with ability to get, add, edit, or delete products, firms, brands, sales, and purchases.</p>

# Models

- Car
- Reservation
- User

![Model]()

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

- <a href="https://pakize.pythonanywhere.com/">Live of the project</a>
- <a href="https://pakize.pythonanywhere.com/swagger/">For the swagger of the project</a>
