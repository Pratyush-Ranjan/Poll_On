# django_App
Django project (Followed Net Ninja tutorial & django official website tutorial)

## Technology Stack

- Django (version = 3.0.4)
- MySQL
- HTML, CSS

## Getting Started

To test, contribute or just see what we did follow few easy steps:
- Clone the repository
- Install python3 and python3-pip on your machine
- Then create a new virtual environment(env) to work with the current project
- Run the virtual enviroment by source env\Scripts\activate
- Install django, mysqlclient and all the required dependencies as mentioned in requirements.txt file
- Then we need to setup MySQL workbench and create a new database and a new user to handle that database
- Change the database settings in settings.py file
- Create a new superuser that will act as admin - 
  python3 manage.py createsuperuser
- Migrate all the changes to the database by the command-
  python3 manage.py makemigrations
  python3 manage.py migrate
- Now, your local development enviroment is set. To run the server , type python3 manage.py runserver. By default, the server
  will start on port 8000.


## Contributing
1. Fork it (<https://github.com/Pratyush-Ranjan/Poll_On/>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
