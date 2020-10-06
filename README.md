# Python-Ciphers-App-MS3

This full-stack website represents the third milestone project I designed at Code Institute Full Stack Development course, specifically the Data Centric Development module.
The main focus of this project was to have a website that allows my registered users to manage a common dataset about the chosen topic, respectively cryptography techniques using Python code. 

## Deployment website

[Click here to view the project live](https://python-ciphers-app.herokuapp.com)

## The Goal of This Website
The idea behind this work is to spark curiosity in learning about the history of cryptography and how we can write simple python code to encrypt messages. 

This website is carved into the following sections:
- Home page. It shows what the website has to offer; an intro to cryptography and cipher pages with correspondent python code snippets, a page where the users can add different ciphers, the Hackathon community page and a form with which a user can send me an email for inquiries and overall collaboration. A cryptography website home page won't be complete without the Matrix rain therefore here it is emerging in front of our very eyes.
- Login/Registration page. Allow users to sign in or sign up. 
- Cipher pages. The users can navigate through different cipher pages where, for the most part, the following pieces of information will be presented: 
    - An introduction about the specific cipher
    - Python code for encryption
    - The outcome of passing a message within the cipher program, basically the encrypted message
    - Python Code for decryption
- Add Your Python Cipher page. The users will have the ability to add/write in a dedicated page their own Python cipher code. Only the author of the cipher can edit or delete the added cipher whereas every cipher information can be freely viewed from any user account.
- Hackathon community. The users will have the ability to join Hackathon community in order to actively contribute and make better our existent ciphers code or simply share cool ideas and suggestions that could lead to improving our code snippets. A user can edit and delete only their own posts whereas every other post can be freely viewed from any user account.

## UX
### User Stories
- As a user, I would like to read interesting material about cryptography in general and python application code examples in particular.
- As a user, I would like to create an account for the website by registering
- As a user, I would like to login to an existent account.
- As a user, I would like to logout of my account.
- As a user, I would like to see on the home page what the website has to offer in terms of topics covered.
- As a user, I would like to have the possibility of adding new python ciphers in order to contribute at overall knowledge extension. 
- As a user, I would like to edit or delete my ciphers.
- As a user, I would like to be part of a community and share ideas or discvover bugs about our existent ciphers or simply speak up about interesting cryptography related news or trends.
- As a user, I would like to edit or delete my community created posts.
- As a user, I would like to contact the creator of the website for questions about the content overall, clarification where needed of code examples, report bugs discovered.

## Easy to navigate
Navigation links must be uniform, easy to recognise, the user  must be able to access any necessary info as quickly as possible.
A user must not be overloaded with information. The interface must remain clean and uncrowded.
The site is quite simple and straight forward.There are two links in the navbar for the two main sections-Home and Hackaton.
The add, edit and delete icons are easy to understand and use.
    
## Security
Whether handling sensitive information, any data stored must be keep secure.
A user must not be overloaded with information. The interface must remain clean and uncrowded.

## Front-End Design
The font-family that I used was Noto Serif providing information in a clean, clear way and Press Start 2P chosen for the main headings.
Each of the fonts used were sourced from Google Fonts.

The color palette was obtained using Coolors https://coolors.co/

[colors-palette](design/python_ciphers_app_colors.pdf)

* ![#072609](https://via.placeholder.com/15/072609/000000?text=+) `#072609`
* ![#7B5E7B](https://via.placeholder.com/15/7B5E7B/000000?text=+) `#7B5E7B`
* ![#938274](https://via.placeholder.com/15/938274/000000?text=+) `#938274`
* ![#E9EB87](https://via.placeholder.com/15/E9EB87/000000?text=+) `#E9EB87`
* ![#B9F18C](https://via.placeholder.com/15/B9F18C/000000?text=+) `#B9F18C`

My goal was to make the website look simple and modern. I added a Matrix Digital Rain Effect with JS on the homepage to integrate with the overall idea of the website. Matrix digital rain contains a green codes rain loop with neon green glowing effect. All the text flows downwards crating a raining effect and keeps glowing. Moreover the text overlapping makes a proper ciphers background theme.

## Wireframes
I used Balsamiq to create wireframes which will provide an overview of how the website will look like on mobile screen size.
(https://balsamiq.com/)

[wireframes](wireframes/python_ciphers_app_wireframes_desktop_mobile.pdf)

## Utilised Technologies
### Languages
- HTML5: used for the content structure of the website
- CSS3: used to style  most of the elements on the page such as fonts, color, spacing, positioning etc.
- JavaScript: to create the Matrix effect on the Home page and send e-mails to the admin 
- Python3: To add functionalities through the back-end

### Frameworks
- Bootstrap: to easily adapt the website to be responsive for all users 
- Flask: python micro framework application engine

### Database
- MongoDB Atlas: To store information into a database

- Database Schema

**users collection**

| Key      	| Value          	| Data Type 	|
|----------	|----------------	|-----------	|
| _id      	| ObjectId("ID") 	| ObjectId  	|
| username 	| "<username>"   	| string    	|
| email    	| "<email>"      	| string    	|
| password 	| "<password>"   	| string    	|

**ciphers collection**

| Key            	| Value                                    	| Data Type 	|
|----------------	|------------------------------------------	|-----------	|
| _id            	| ObjectId("ID")                           	| ObjectId  	|
| username       	| "<username>"                             	| string    	|
| cipher_name    	| name of created cipher                   	| string    	|
| heading        	| automatically generated from cipher_name 	| string    	|
| cipher_content 	| the content of cipher                    	| string    	|

**posts collection**

| Key          	| Value                                                           	| Data Type    	|
|--------------	|-----------------------------------------------------------------	|--------------	|
| _id          	| ObjectId("ID")                                                  	| ObjectId     	|
| author       	| post creator                                                    	| string       	|
| cipher_name  	| name of cipher that the author of the post chosen to contribute 	| string       	|
| post_content 	| author contribution or shared idea                              	| string       	|
| initDate     	| post date                                                       	| Date         	|
| edit_today   	| edit date or Null                                               	| Date or Null 	|

### API
- EmailJS: Allow users to send me an email 

### Tools
- **jQuery**: JavaScript library was employed to streamline Javascript DOM manipulation throughout the project
- **Github**: used to create repository and to host the repository
- **Git**: version control
- **VSCode**: IDE
- **PyMongo**: used as the Python API for MongoDB. This API enabled me to link the data from the back-end database to the front-end app
- **Jinja2**: Python web templating engine
- **Heroku**: as a hosting platform to deploy the live version of the app

#### Additional tools used
- [autoprefixer](https://autoprefixer.github.io/)
- [TinyPNG](https://tinypng.com/):used to compress my image files to try to reduce the loading time for each page
- [Favicon Generator](https://realfavicongenerator.net/): to create favicons
- [Balsamiq](https://balsamiq.com/) for wireframes
- [GoogleFonts](https://fonts.google.com/) I used two complementary fonts from Google for my project: Noto Serif and Press Start 2P
- [FontAwesome](https://fontawesome.com/)

### Validators
- [PEP8 Validator](http://pep8online.com/)
- [JavaScript Validator](https://jshint.com/)
- [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/)
- [HTML Validator](https://validator.w3.org/)

## Features
### Existing Features
- Users can read the website provided introduction to cryptography and cipher code chapters.
- Users can add their own pythoc ciphers.
- Users can see other users created ciphers.
- Users can edit or delete only their created ciphers, these cannot be edited or deleted from any other user account.
- Users can add posts on Hackathon community page.
- Users can edit or delete only their created posts, these cannot be edited or deleted from any other user account.
- All existent ciphers and every cipher that a user adds gets included into the options list on the Hackathon community page to allow a user to contribute to  that cipher.
- EmailJS API for users to send emails to website creator.

### Future Improvements 
- Use generate_password_hash function from werkzeug.security module in order to store my users passwords as a hash and not the clear text password entered at registration.
- Make the python code visualization to appear like in a code editor.

## Testing
- Tested registering a new account
    - MongoDB Atlas reflecting user account information after registration
- Tested registering with a different user but an email already existent and associated with another account in MongoDB
    - Error `'This Email was already used for registration'` raised
- Tested registering with a new email account but a user already existent and associated with another account in MongoDB
    - Error `'This User already exists'` correctly raised
- Tested login functionality. 
    - We grab from DB the the user account data by filtering using email address and if the password introduced in the form matches the DB password then login is succesful
    - If the user email does not match the user password in DB we return error `'Invalid email or password'`. We don't want a user to login with another user valid password but only his/her personal one.
    - If the user tries to login with an email or password that does not exist in DB we intuitively redirect to registration page.
- Testred that once a user is authenticated there's no need to authenticate him again.
- Tested if all the hover effects on the cipher cards work correctly and if each nav-link in the navigation bar links to the right web page
- Tested the JavaScript animation 
- Tested if each link on the home page leads to the correct web page
- Tested if adding ciphers worked and if one was able to delete and edit them only through the user account of the author of that cipher and not through any other account
    - Tests worked correctly, as I was able to add, edit and delete ciphers from only my user account and no other account.
- Tested if adding posts worked and if one was able to delete and edit them only through the user account of the author of that post and not through any other account.
    - Tests worked correctly, as I was able to add, edit and delete posts from only my user account and no other account.
- Tested if other users could see the ciphers added by other users.
- Tested if other accounts could see the Hackathon posts added by other users.
- Tested if ciphers that are added by users would appear in the Hackathon option list to allow all users to contribute and improve the code.
- Tested sending emails to the website author from the section at the bottom of the homepage.
- Tested the responsiveness of the website on different devices using Chrome DevTools.
- Tested on Google Chrome, Internet Explorer & Microsoft Edge to view the website in different browsers.
- Tested by sending the website link to friends and family members in order to receive feedback regarding bugs or visualization issues.

## Deployment
### Local Deployment
For local deployment, you need to have an IDE such as Gitpod or Visual Studio Code or simply Vim if you are courageous.
You will need to install the following packages before creating the virtual environment hosting the application:
- Git, Python3, Pip3
1. At the top of this repository, click the green button **Clone or download**.
2. In the Clone with HTTPs section, copy the clone URL for the repository.
3. Change the current working directory to the location where you want the cloned directory to be made.
4. Type git clone, and then paste the URL you copied in Step 2.
5. Press Enter. Your local clone will be created.
6. To create a virtual environment within project directory enter `python3 -m venv .venv` 
7. Taking Visual Studio Code as example, type: `code .`
8. Edit `~/.bashrc` by adding the following env vars:
`export IP=127.0.0.1`
`export MONGO_URI="mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority"`
`export SECRET=<somethingsecret>`
9. Install all required modules from requirements.txt with the command `python3 -m pip install -r requirements.txt`
10. Now you can run the website with the command `python3 app.py`
11. You can now access the website at http://127.0.0.1:5000

### Heroku Deployment
The website was deployed on [Heroku](https://dashboard.heroku.com/apps) following these steps:
1. Create a **requirements.txt** file using the command `python3 -m pip freeze --local > requirements.txt` in the terminal.
2. Create a **Procfile** using the command `echo web: python app.py > Procfile` in the terminal.
3. Commit and push all the changes to the Github repositoty of this project.
4. Go to Heroku and create a new app. Set a name for this app and select the closest region.
5. Choose Deployment method as GitHub in Heroku Dashboard and link the Github repository to the Heroku app.
6. Go to **Settings** then **Reveal Config Vars** in Heroku Dashboard and set the values as follows:

| config vars   | values                                                                                                                |
| ------------- |-------------                                                                                                          |
| IP            | 0.0.0.0                                                                                                               |
| MONGO_URI     | mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority      | 
| PORT          | 5000                                                                                                                  |
| SECRET        | <your_secret_key>                                                                                                     |

| Key          	| Value                                                           	| Data Type    	|
|--------------	|-----------------------------------------------------------------	|--------------	|
| _id          	| ObjectId("ID")                                                  	| ObjectId     	|
| author       	| post creator                                                    	| string       	|
| cipher_name  	| name of cipher that the author of the post chosen to contribute 	| string       	|
| post_content 	| author contribution or shared idea                              	| string       	|
| initDate     	| post date                                                       	| Date         	|
| edit_today   	| edit date or Null                                               	| Date or Null 	|


## Credits
### Content
- Cipher pages content: [Cracking Codes with Python](https://inventwithpython.com/cracking/)
- The photos used in this site were obtained from the below sites :
* (https://unsplash.com/)
* (https://pixabay.com/)

- The Matrix effect was inspired from:
https://codepen.io/Madchatthew/pen/NWqxbZo

### Resources Used 

- [Code Institute](https://codeinstitute.net/)
- [W3Schools](https://www.w3schools.com/python/)
- [mongoDB Documentation](https://docs.mongodb.com/manual/reference/)
- [PyMongo Documentation](https://api.mongodb.com/python/)
- [Stackoverflow](https://stackoverflow.com/)
- [W3Schools](https://www.w3schools.com/)
- [Slack](https://slack.com/)

## Acknowledgements
- I would like to give a thank you to my mentor Seun Owonikoko for all the help and advice she has given throught the project milestone.

## Disclaimer
This project is for educational purposes only.

