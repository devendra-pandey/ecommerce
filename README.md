# ecommerce
This is the ecommerce project completely build on python with the help of Django framework.
plss install the Rabbit Mq and start in your system if its not installed and running.
At the very first Basic step pls check to install in your system.

--sudo apt install python3-distutils.

After this plss do the following as follows-

1. Create the Virtual env 
2. Install all the requirements with command
 -- pip install -r requirements.txt
3. python3 manage.py makemigrations
4. python3 manage.py migrate
5. create the superuser for the admin side 
    python3 manage.py createsuperuser
6. python3 manage.py runserver
7. Run celery system Parallel By using the following command-
    celery -A ecommerce_with_vendor worker -l info


8. For testing Purpose for the Payments You can use following Cards Informations.
    card Number - 4111 1111 1111 1111
    Cvv - 123
    expiry Date - 12/24
