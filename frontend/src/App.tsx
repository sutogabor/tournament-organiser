import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header.tsx';
import HomePage from './pages/HomePage.tsx';
import Tournaments from './pages/Tournaments.tsx';
import EventDetails from './pages/EventDetails.tsx';
import AddPlayer from './pages/AddPlayer.tsx';
import Footer from './components/Footer.tsx';
import AddTournament from "./pages/AddTournament.tsx";

const Layout = ({ children }: { children: React.ReactNode }) => (
    <div>
        <Header />
        {children}
        <Footer />
    </div>
);

function App() {
    return (
        <div>
            <Router>
                <Header />
                <Routes>
                    <Route path="/" element={<HomePage />}/>
                    <Route path="/tournament/:id" element={ <TournamentDetails />}/>
                    <Route path="/add-tournament" element={ <AddTournament />}/>
                    <Route path="/tournaments" element={ <Tournaments /> }/>
                    <Route path="/add-player" element={ <AddPlayer /> }/>
                </Routes>
                <Footer/>
            </Router>
        </div>
    )
}

export default App;
