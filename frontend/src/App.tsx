import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header.tsx';
import HomePage from './pages/HomePage.tsx';
import Tournaments from './pages/Tournaments.tsx';
import EventDetails from './pages/EventDetails.tsx';
import AddPlayer from './pages/AddPlayer.tsx';
import Footer from './components/Footer.tsx';
import AddTournament from "./pages/AddTournament.tsx";

// Define a layout component that includes the header and footer
const Layout = ({ children }: { children: React.ReactNode }) => (
    <div>
        <Header />
        {children}
        <Footer />
    </div>
);

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Layout><HomePage /></Layout>} />
                <Route path="/event-details/:id" element={<Layout><EventDetails /></Layout>} />
                <Route path="/add-tournament" element={<Layout><AddTournament /></Layout>} />
                <Route path="/tournaments" element={<Layout><Tournaments /></Layout>} />
                <Route path="/add-player" element={<Layout><AddPlayer /></Layout>} />
            </Routes>
        </Router>
    );
}

export default App;
