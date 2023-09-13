import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Header from "./components/Header.tsx";
import HomePage from "./pages/HomePage.tsx";
import AddTournament from "./pages/AddTournament.tsx";
import Tournaments from "./pages/Tournaments.tsx";
import TournamentDetails from "./pages/TournamentDetails.tsx";
import AddPlayer from "./pages/AddPlayer.tsx";
import Footer from "./components/Footer.tsx";


function App() {


    return (
        <div>
            <Router>
                <Header />
                <Routes>
                    <Route path="/" element={<HomePage />}/>
                    <Route path="/event-details/:id" element={ <TournamentDetails />}/>
                    <Route path="/add-tournament" element={ <AddTournament />}/>
                    <Route path="/tournaments" element={ <Tournaments /> }/>
                    <Route path="/add-player" element={ <AddPlayer /> }/>
                </Routes>
                <Footer/>
            </Router>
        </div>
    )
}


export default App
