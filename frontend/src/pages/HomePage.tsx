import React from 'react';
import { Link } from 'react-router-dom';
import logo from './../assets/images/home-page-logo.png';
import './../styles/homepage.css';

const Homepage: React.FC = () => {
    return (
        <div className="homepage-container">
            <header className="homepage-header">
                <h1 className="title">Welcome!</h1>
            </header>
            <div className="content-container">
                <Link to="/tournaments">
                    <img src={logo} alt="Tournaments" className="picture" />
                </Link>
                <div className="information">
                    <div className="information-card">
                        <p>
                            <h3>Welcome to Tournament Organiser!</h3>
                            Tournament Organiser is a learning project designed to manage and organize game tournaments
                            and participants. Tournament organizers can easily set up new tournaments,
                            register participants, and track match outcomes. <br></br>
                            The application's user-friendly interface and flexible architecture make it suitable
                            for a wide range of sports and competitive events. Thank you for trying out this project,
                            may the best win!
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Homepage;
