import {useState, useEffect} from 'react';

interface Event {
    id: number
    name: string
    date: string
}

function UpcomingEvents() {

    const [events, setEvents] = useState<Event[]>([]);
    const [refresh, setRefresh] = useState<boolean>(false);


    async function getData() {
        const response: Response = await fetch('/event');
        return response.json();
    }

    function refreshData() {
        getData().then(
            (data) => {
                setEvents(data);
                console.log(events);
            }
        )
    }


    async function deleteEvent(eventId: number) {
        try {
            const response = await fetch(`/event/delete/${eventId}`, {
                method: "POST",
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


    useEffect(() => {
        refreshData();
        setRefresh(false);
    }, [refresh])

    if (events.length == 0) {
        return "LOOOOOOAAAADDDIIIING";
    }

    return (
        <div className="content">
            <h1>Upcoming Events</h1>
            <div className="event-list">
                {events.map((event) => (
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
                            <div className="delete-button">
                                <input type='button' onClick={() => deleteEvent(event.id)} value="Delete"/>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

        </div>
    )
}

export default UpcomingEvents;
