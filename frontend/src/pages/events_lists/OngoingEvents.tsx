import {useEffect, useState} from "react";
import { Event } from '../../interfaces/Event';
import { Link } from 'react-router-dom';



const OngoingEvents = () => {
    const [uEvents, setEvents] = useState<Event[]>([]);
    const [refresh, setRefresh] = useState<boolean>(false);


    async function getData()  {
        const response :Response = await fetch('/event');
        return response.json();
    }

    function refreshData() {
        getData().then(
            (data) => {
                setEvents(data);
                console.log(uEvents);
            }
        )
    }


    async function deleteEvent(eventId:number) {
        try {
            const response = await fetch(`/event/delete/${eventId}`, {
                method: "DELETE",
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            if (response.ok) {
                console.log("Event deleted successfully.");
                setRefresh(true);
            } else {
                console.error("Cannot delete this event.");
            }
        } catch (error) {
            console.error(error);
        }
    }


    useEffect (()=> {
        refreshData();
        setRefresh(false);
    },[refresh])

    if(uEvents.length == 0) {
        return "LOOOOOOAAAADDDIIIING";
    }

    return (
        <div className="content">
            <h1>Ongoing Events</h1>
            <div className="event-list">
                {uEvents.map((event) => (
                    <div className="card" key={event.id}>
                        <div className="card-details">
                            <div className="card-header">
                                {event.name}
                            </div>
                            <div className='card-body'>
                                {event.date}
                            </div>
                        </div>
                        <div className="card-buttons">
                            <button className='card-button' onClick={() => deleteEvent(event.id)} >Delete</button>
                            <Link to={`/event-details/${event.id}`}><button className='card-button'>Show Event</button></Link>
                        </div>
                    </div>
                ))}
            </div>

        </div>
    )
}

export default OngoingEvents;