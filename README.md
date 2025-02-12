## Balance
*** Video Demo:  <https://www.youtube.com/watch?v=nxwYgMWXigs&t=90s> ***
### Description of the functionalities of the project:
*** My project is Balance, as the name says it is supposed to help the user to keep his calorie intake in balance with the number of calories the body of the user needs. It calculates the users BMR and what the daily calorie intake of the user is supposed to be. It helps the user to keep track of the calorie intake and how many calories the user has left for the day after the consumption of different foods, the calculation happens daily. If the user doesn’t know what the calories of certain foods are, he can look the calories for different foods up in a website, the link is implemented on the Balance/Your Calories page. ***
*** If the user will lose/gain weight or the activity level will change, the user can recalculate the needed intake as many times as wished. ***
### Design:
*** I choose soft colors and fonts with a light green background color. It supposed to be calming for the eyes, also green is associated with healthy things. The buttons are in soft shape and have light colors to match the rest of the website. ***
### Code:
**App.py:**
**def home():**
*** Displays the BMR and the total recommended calorie intake of the user on the main page ***
*** Set default values for when the user has not calculated his recommended calorie intake jet. ***
*** It calculates the consumed calories daily and calculates how many calories the user has left for the day. ***
*** Sends the different values to home.html.***
**def login():**
*** Clears the session for a new user to login. ***
*** Allows the user to login, while checking if the values of the username and the password match the values in the database “user” the system has for this user. If the data doesn’t match the data in the database, it shows the user an error message. ***
**def logout():**
*** Logs out the user and clears the session. ***
**def calories():**
*** Gets the values calories and food to add a food the user consumed to the list - calories.html, stores the values of the added food in the database “calories”. If a value is missing or negative it redirects an error message. ***
*** Displays the consumed food to the user with the most actual date first in a table. ***
**def delete():**
*** Allows the user to delete certain foods from the list, for that it calls the id of the food. ***
**def register():**
*** Allows the user to register for the page, allows the user to set a username and a password and stores the values in the database “user”. Makes sure the password is not directly stored in the database by using hash. If the confirmation and the password do not match it displays an error message. At the end it sets the session to the new user id. ***
**def start():**
*** Gets the values the user typed in for the age, height, weight, activity, gender from the start.html. If a value is missing or negative it redirects an error message. ***
*** Calculates with the values and a formula the BMR of the person depending on if it is a female or male. ***
*** Calculates with the BMR of the person with a formula the total recommended calorie intake for the person depending on the activity level. ***
*** Stores the values age, height, weight, activity, gender, user_id, bmr, total_cal in the database “details” if it is a new user by checking if the length of the id in “details” is zero, updates the values otherwise. ***
*** Sends the user back to the home.html where the calculated values are displayed. ***
**def apology()**
*** Sends a picture of an angry cat if the function apology is called together with a text that explains what is wrong. ***
**def login_required(f):**
*** Makes sure the user is logged in if certain functions are called by checking that the session user id it not NULL. ***
**CSS:**
*** Contains the styles for the HTML pages, to make everything look more balanced. ***
**HTML files:**
**Login:**
*** Asks the user for the inputs username and password. Allows the user to submit the values by clicking on the Login button. ***
**Register:**
*** Asks the user for the inputs username, password and confirmation, allows the user to submit the inputs by clicking the button “submit”. ***
**Layout :**
*** Contains the layout of the homepage and the redirects to the different html files in the navigation bar. Includes the links to the different stylesheets used for the html. ***
**Start:**
*** Asks the user for the inputs age, height, weight, activity and gender and allows the user the submit those values by clicking on “Calculate Your Calories”. ***
**Home:**
*** Displays the BRM, the recommended calorie intake of the user, the amount of calories consumed for the day and how many calories the user can still consume for the day by plugging In the values from the function home. ***
**Calories:**
*** Asks the user for the inputs food and calories. Shows a link to a page if the user doesn’t know the calories of the certain food. Allows the user to submit the food to the list by clicking on the button “add food”. ***
*** Displays the list of the consumed foods in a table by calling a for loop. Allows the user to delete a food from the table by clicking on the button delete, function delete, for that it calls the id of the database “calories”. ***
**Apology:**
*** Calls a picture of an angry cat and plugs in the values that will be needed for different error messages. ***
