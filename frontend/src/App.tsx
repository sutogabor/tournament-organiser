import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import HomePage from "./pages/home_page/HomePage.tsx";
import AddEvent from "./pages/add_event/AddEvent.tsx";
import EventsList from "./pages/events_list/EventsList.tsx";

import './App.css'
import EventDetails from "./pages/event_details/EventDetails.tsx";


function App() {


    return (
        <div>
            <Router>
                <Routes>
                    {/* TODO */}
                    <Route path="/event-details/:id" element={ <EventDetails />}/>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/add-event" element={ <AddEvent/>}/>
                    <Route path="/events" element={ <EventsList /> }/>
                </Routes>
            </Router>
        </div>
    )
}

export default App
