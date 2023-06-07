import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import HomePage from "./pages/home_page/HomePage.tsx";
import AddEvent from "./pages/add_event/AddEvent.tsx";

import './App.css'


function App() {


    return (
        <div>
            <Router>
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                    <Route path="/add-event" element={ <AddEvent/>}/>
                </Routes>
            </Router>
        </div>
    )
}

export default App
