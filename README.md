# exitpro
Program to track and manage user relieval 

## APIs for the program to track and manage user relieval
### Installation
##### Below documentation is for ubuntu 20.04 distro

1. Git clone - https://github.com/tutoo-ev/exitpro.git
Prerequisites - Python and Virtualenv
  1. check for python in the machine using ```python3 -V```
  2. If not found, please install using ```sudo apt-get install python3```
    Note: Python version 3.8.10 is used for this project. Please try to use the same version in order to avoid conflicts.
  3. Re-run step 1 to confirm the installation.
Install PIP
  1. install 'pip' using ```sudo apt-get install -y python3-pip```
  2. confirm installation using ```pip3 -V```
Create a virtual environment to run the project.
  If virtual env is not installed, please follow the below steps:
  1. Open terminal and run  ```pip install virtualenv```
  2. check installation ```virtualenv --version```
  3. Once the installation is finished, create a virtualenv - ```virtualenv env```
  4. Activate 'env' by ```source env/bin/activate```

Now we open our project
  1. ```cd exitpro```
  2. Run ```pip install -r requirements.txt```. This will install all the dependencies.
  3. Once completed you are good to go
  4. In the terminal run ```python3 manage.py runserver```
  5. Open http://127.0.0.1:8000/ to get all the apis.
  
  
  
Note: The APIs are having permissions based on the work they have to perform. So please read the comments/ documentation before proceeding

Admin Panel
http://127.0.0.1:8000/admin - will give you access to admin panel
superuser details:
admin@gmail.com
mobile_number = 9655205631
password = password

Other test users:
{
  "name": "HR User",
  "email": "hr@example.com",
  "mobile_number": "12341234",
  "password": "password"
}

{
  "name": "Admin User",
  "email": "admin@example.com",
  "mobile_number": "23451234",
  "password": "password"
}

{
  "name": "Partner User",
  "email": "partner@example.com",
  "mobile_number": "123123123",
  "password": "password",
}

Please use this accordingly..!!
