<h1 align="center">Tournament Organiser</h1>

<p align="center">
    project_description
    <br />
    <a href="https://github.com/sutogabor/tournament-organiser"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    </p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![App Logo][product-screenshot]]


Tournament Organiser is a web application designed to manage and organize sports tournaments and participants.
It provides an intuitive user interface for creating, managing, and monitoring various tournaments. With this application, tournament organizers can easily set up new tournaments, register participants,
and track match outcomes. The application's user-friendly interface and flexible architecture make it suitable
for a wide range of sports and competitive events.

### Built With

#### Backend:
* [![Python][Python.io]][Python-url]
* [![Flask][Flask.io]][Flask-url]
#### Frontend:
* [![Typescript][Typescript.io]][Typescript-url]
* [![React][React.js]][React-url]
#### Database:
* [![PostgreSQL][PostgreSQL.io]][PostgreSQL-url]
#### Styling:
* ![CSS][CSS.io]

<!-- GETTING STARTED -->
## Getting Started

Before you begin, there are a few steps you need to take to get the application up and running.
Make sure to follow the steps outlined below.

### Prerequisites

Make sure you have the following software installed on your system:

- [Python](https://www.python.org/) (v3.7 or higher)
- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/) (Node Package Manager)




## Installation

The following terminal commands will set up the application on your computer:

### Backend Setup

1. Clone the repository to your local machine using Git:
   ```
   git clone https://github.com/sutogabor/tournament-organiser.git
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   ```
3. If you created a virtual environment activate it:
   ```
   source venv/bin/activate
   ```
4. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the Flask development server:
   ```
   python app.py
   ```
The backend API should now be accessible at [http://localhost:5000](http://localhost:5000).

### Frontend setup

1. Navigate to the frontend directory:
   ```
   cd ../frontend
   ```
2. Install frontend dependencies:
   ```
   npm install
   ```

### Running the application

1. In the frontend directory, start the React development server:
   ```
   npm run dev
   ```

2. Open your web browser and navigate to [http://localhost:3000](http://localhost:3000)
   to see the application in action.

## Usage

First you will see the [homepage](http://localhost:3000/homepage) of the application. Here you can find the logo and some
introduction to the application. On the navbar you can find links to the individual pages,
or you can simply click the logo to get to tournaments page.

* You can simply add new tournaments on its respective [page](http://localhost:3000/tournament/add) by giving a title
  and setting a start date and time for the tournament.<br><br>
* The ['Add Players'](http://localhost:3000/player/add) page allows you to register new participants. You can do this
  by filling out the name form and selecting the tournaments from the list in which the player will be involved.<br><br>
* On the [Tournaments](http://localhost:3000/tournaments) page you can see the Ongoing or Upcoming tournaments,
  some basic information about them, or delete them with the delete button. <br>
  Clicking on the Details button takes you to the tournament details page, where you can see the individual
  match-ups between players, as well as the upcoming matches in the tournament in a bracket form.<br><br>
* On this [Tournament Details](http://localhost:3000/tournaments/1) page, you can organize each round of the tournament
  by keeping score and marking match outcomes as the participants progress through the event.<br><br>


## Contact

Sütő Gábor - [@LinkedIn](https://linkedin.com/in/sutogabor) - [@GitHub](https://github.com/sutogabor) - suto.gabor.86@gmail.com

Project Link: [https://github.com/sutogabor/TodoList](https://github.com/sutogabor/TodoList)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[product-screenshot]: assets/images/logo.png
[Python.io]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask.io]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.3.x/
[Typescript.io]: https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white
[Typescript-url]: https://www.typescriptlang.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[PostgreSQL.io]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[PostgreSQL-url]: https://www.postgresql.org/
[CSS.io]: https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white