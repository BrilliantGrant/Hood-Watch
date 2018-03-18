# Neighborhood Watch

This application was built by Django version 1.11 a python framework.

A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

#### 16nd March 2018

#### By Brilliant Kaimba briegrant416@gmail.com

### Description

A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.


## User Stories

As a user I would like to:

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.


## Setup/Installation Requirements

* Install python version 3.6.3
* Install Heroku that helps to deploy your application.
* Clone https://github.com/BrilliantGrant/Hood-Watch.git
* Atleast have a computer or a laptop
* Have an internet connection
* Visit 

* install Django

   ```$ pip install django==1.11```

* Create a virtual environment

   `$ sudo apt-get install python3.6-venv`

   ```$ python3.6 -m venv virtual```

   ```$ source virtual/bin/activate```

* Install gunicorn: (virtual)

   ```$ python3.6 -m pip install gunicorn```


## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
|Display of in form | N/A | Displays sign in form when a user visits the site | 
|Logout current user | click the logout link in the drop down in the navbar | Displays the login form |
|Display of current user | N/A | Displays name of current user in a Navbar when user signs in |
|Display Businesses in Neighborhood | Click Business link in navbar | Displays all businesses in new template |
|Create New Business | Click the plus sign in the businesses page | Redirects to pages where users can create a business |

