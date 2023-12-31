import { NavLink, useLocation } from 'react-router-dom';
import './../styles/styles.css';

function Header() {
    const location = useLocation();

    return (
        <header className="header">
            <div className="app-name">
                <h1>Tournament Organiser</h1>
            </div>
            <nav className="nav">
                <ul className="nav-list">
                    <li className="nav-item">
                        <NavLink to="/" className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}>Home</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/tournaments" className={`nav-link ${location.pathname === '/tournaments' ? 'active' : ''}`}>Tournaments</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/add-tournament" className={`nav-link ${location.pathname === '/add-tournament' ? 'active' : ''}`}>New Tournament</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink to="/add-player" className={`nav-link ${location.pathname === '/add-player' ? 'active' : ''}`}>Add Player</NavLink>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
