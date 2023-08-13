import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import HomePage from "./pages/HomePage.tsx";
import SideBar from "./components/SideBar.tsx";
import AddEvent from "./pages/AddEvent.tsx";
import UpcomingEvents from "./pages/event_lists/UpcomingEvents.tsx";
import OngoingEvents from "./pages/event_lists/OngoingEvents.tsx";

import EventDetails from "./pages/EventDetails.tsx";
import AddPlayer from "./pages/AddPlayer.tsx";


function App() {


    return (
        <div>
            <Router>
                <SideBar />
                <Routes>
                    <Route path="/" element={<HomePage />}/>
                    <Route path="/event-details/:id" element={ <EventDetails />}/>
                    <Route path="/add-event" element={ <AddEvent />}/>
                    <Route path="/ongoing-events" element={<OngoingEvents />}/>
                    <Route path="/upcoming-events" element={ <UpcomingEvents /> }/>
                    <Route path="/add-player" element={ <AddPlayer /> }/>
                </Routes>
            </Router>
        </div>
    )
}


export default App
