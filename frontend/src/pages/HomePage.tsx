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
                            <h3>Welcome to my Tournament Organiser project!</h3>
                            I started this pet project while I was learning programming in CodeCool,
                            in order the help the organisation of school events such as Ping-Pong
                            or video game tournaments. Thank you for trying it's features and feel
                            free to ask me any questions. Enjoy your tournament! May the best win!!
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Homepage;
