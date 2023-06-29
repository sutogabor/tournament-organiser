import {useEffect, useState} from "react";
import {Event} from "../interfaces/Event.ts";
import {apiGet} from "../utils/apiCalls.ts";


const AddPlayer = () => {
    const [events, setEvents] = useState<Event[]>([]);

    const getEvents = async () :void => {
        const response :Promise<Event[]> = await apiGet('/event');
        setEvents(response);
    }

    useEffect(()=> {
        getEvents();
    },[])

    return (
        <div>
            {events.map((event:Event)=> (
                <p>{event.name}</p>
            ))}
        </div>
    )

}

export default AddPlayer;