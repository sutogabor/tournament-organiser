import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import HomePage from "./pages/home_page/HomePage.tsx";

import './App.css'


function App() {


    return (
        <div>
            <Router>
                <Routes>
                    <Route path="/" element={<HomePage/>}/>
                </Routes>
            </Router>
        </div>
    )
}

export default App
