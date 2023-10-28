# Family Expense Tracker

This project is meant to show how a family can keep track of all its daily expenses. Every family member can register and faithfully and honestly update how much money they spent on something.

### Table Of Contents

- [Technologies Used](#technologies-used)
- [Demo](#demo)
- [Testing The Application Locally](#testing-the-application-locally)


## Technologies Used

- Flask microframework
- Python for programming
- HTML for data presentation on a browser
- Bootstrap for styling and responosiveness


## Demo

- Website design: 
- See the live app: [Live app]()

## Additional information

| Prototype | Database Design | Live App Link |
| --------- | --------------- | ------------- |
| [Figma](https://www.figma.com/proto/3DddSA3j3n39Ugr9PgMQuX/Register?type=design&node-id=6-142&t=IWGkbfR2mrOxylHe-1&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=6%3A142&show-proto-sidebar=1&mode=design) |  [DrawSQL](https://drawsql.app/teams/expense-trackers/diagrams/family-expense-tracker)    |  [Render]()   |


## Roles

**Ayanda**
- Design the templates
    - Landing page
    - Login page
- Design the routes:
    - Landing page
    - Login
- Design the database
    - User
    - Income


**Harry**
- Design the database
    - Expense
- Design the templates
    - Register page
    - Home page etc
- Design the routes:
    - Register etc
    - Home page
- Error handling
    - If page not found
    - If there is an issue with the database


## Testing The Application Locally

- Clone this repository:

    ```python
    $ git clone git@github.com:GitauHarrison/expense-tracker.git
    ```

- Change directory to the cloned folder:

    ```python
    $ cd expense-tracker
    ```

- Activate your virtual environment:

    ```python
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

- Install project dependancies:

    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Start the flask server:

    ```python
    (venv)$ flask run
    ```

- See the application on our browser:
    - Paste http://127.0.0.1:5000 on your favourite browser

