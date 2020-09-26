# Python-Ciphers-App-MS3

This full-stack website represents the third milestone project I designed at Code Institute Full Stack Development course, specifically the Data Centric Development module.
The main focus of this project was to have a website that allows my registered users to manage a common dataset about the chosen topic, respectively cryptography techniques using Python code. 

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

## Credits
### Content
- Cipher pages content: [Cracking Codes with Python](https://inventwithpython.com/cracking/)
- The photos used in this site were obtained from the below sites :
* (https://unsplash.com/)
* (https://pixabay.com/)

- The Matrix effect was inspired from:
(https://codepen.io/Madchatthew/pen/NWqxbZo)
