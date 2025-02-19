# Balance  
This is a calorie-tracking application designed to help users maintain a balance between their daily calorie intake and their body's energy requirements. The app calculates **Basal Metabolic Rate (BMR)** and the **recommended daily calorie intake**, enabling users to track their food consumption effectively.  

## Technology Stack 🛠️  
- **Python (Flask)** : Backend framework to handle API requests and manage data.  
- **SQLite** : Lightweight relational database to store user and food consumption data.  
- **HTML, CSS, JavaScript** : Frontend technologies for rendering the user interface.  
- **Bootstrap** : Responsive design framework for styling UI elements.  
- **Jinja2** : Templating engine for rendering dynamic content in HTML files.  

## Getting started 😎  

### Clone the repository  

```
git clone https://github.com/your-username/balance.git
```

### Change the directory  

```
cd balance
```

### Install the dependencies 

```
pip install -r requirements.txt
```

### Run the application  

```
flask run
```

## User stories 💃 🕺  
- As a user, I want to **calculate my daily calorie intake** based on my age, height, weight, and activity level.  
- As a user, I want to **log in and register** so that my data is saved securely.  
- As a user, I want to **add the food I consume**, so that I can track my daily calories.  
- As a user, I want to **delete items from my food log**, in case I make an error or change my diet.  
- As a user, I want to **recalculate my recommended intake** if my weight or activity level changes.  
- As a user, I want to **search for food calorie values**, so that I can accurately log my consumption.  

## Features ✅  
- **User Authentication** : Secure login and registration with hashed passwords.  
- **Calorie Calculation** : Computes BMR and daily calorie intake based on user input.  
- **Food Tracking** : Allows users to add, view, and delete food entries.  
- **Daily Update** : Resets calorie tracking at midnight to start a new day.  
- **Calorie Lookup** : Provides an external link to check food calorie values.  
- **Error Handling** : Displays error messages (with an angry cat image) for invalid inputs.  
- **Responsive Design** : Light green UI for a calming experience, with soft buttons and typography.  
