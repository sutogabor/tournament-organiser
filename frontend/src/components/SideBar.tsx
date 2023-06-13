import MyButton from "./MyButton.tsx";
import {Link} from "react-router-dom";


const SideBar = () => {


    //const button_texts:string[] = ["New Event", "Ongoing Event"]

    return(
        <div className="navBar">
            <Link to="/ongoing-events"><MyButton className="navButton" text="ONGOING EVENTS"/></Link>
            <Link to="/upcoming-events"><MyButton className="navButton" text="UPCOMING EVENTS"/></Link>
            <Link to="/add-event"><MyButton className="navButton" text="NEW EVENT"/></Link>
        </div>

    )
}

export default SideBar