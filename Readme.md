## Description
An insta clone python application based on Django framework, 2020

## Author
Habiba Hassan

## Code Beat
[![codebeat badge](https://codebeat.co/badges/759f7338-64d7-4bdf-bab6-c99c34e94a7a)](https://codebeat.co/projects/github-com-habibahassan-instagram-master)

## Specifications
Behaviour		
* Display all photos on database		
* Save uploaded images		
* Update images as  user	 	
* Show image details below image	
* Search by username	 	

Input
* Upload image
* update image at from navbar 'update' option
* search username 'zully'

Output
* Loads all photos
* Saves image
* Updates
* returns images posted by 'bettie' 

## Database-diagram
<img src="/habiba/Instagram-database.png">

## SetUp / Installation Requirements
## Prerequisites
* python3.6
* pip
* postgres database
* virtualenv
* django
* Cloning
In your terminal:

  $ git clone https://github.com/habibahassan/Instagram.git
  $ cd gallery

* Creating the virtual environment

    $ python3.6 -m venv --without-pip virtual
    $ source virtual/bin/env
    $ curl https://bootstrap.pypa.io/get-pip.py | python
* Installing Django and other Modules

    $ python3.6 -m pip install -r requirements.txt
* Run the application:

    $ python3 manage.py runserver 

## Testing the Application
* To run the tests for the class files:

    $ python3.6 manage.py test
* Technologies Used
* Python 3.6
* Django2.2 

## Support and contact details
For any questions, troubleshooting or contributions, find me on:

Email: halimaadan92@gmail.com

## License
licensed under the [MIT License](license)
 copyright(c) 2020 Instagram