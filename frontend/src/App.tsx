import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import HomePage from "./pages/home_page/HomePage.tsx";
import SideBar from "./components/SideBar.tsx";
import AddEvent from "./pages/add_event/AddEvent.tsx";
import UpcomingEvents from "./pages/events_lists/UpcomingEvents.tsx";
import OngoingEvents from "./pages/events_lists/OngoingEvents.tsx";



function App() {


    return (
        <div>
            <Router>
                <SideBar />
                <Routes>
                    <Route path="/" element={<HomePage />}/>
                    <Route path="/add-event" element={ <AddEvent />}/>
                    <Route path="/ongoing-events" element={<OngoingEvents />}/>
                    <Route path="/upcoming-events" element={ <UpcomingEvents /> }/>
                </Routes>
            </Router>
        </div>
    )
}


export default App
