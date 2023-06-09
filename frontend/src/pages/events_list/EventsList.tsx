import { useState, useEffect } from 'react';



function EventsList() {

    const [events, setEvents] = useState([]);


    async function getData()  {
        const response = await fetch('http://localhost:5000/event');
        
        return response.json();
    }
    
    function deleteEvent(eventId:number) {
        return "ok"
    }

    useEffect (()=> {
        getData().then(
            (data) => {
                setEvents(data);
                console.log(events);
            }
            )

    },[])
    

    return (
            <div>
                <div className="pokemon-list">
                    {events.map((event) => (
                        <div className="card" key={event.id}> 
                            <div className="card-header">
                                {event.name}
                            </div>
                            <div className='card-body'>
                                {event.date}
                            </div>
                            
                            <div className="card-footer">
                            <button>Delete</button>
                            </div>
                        </div>
                    ))}
            </div>
                
            </div>
    )
}

export default EventsList;
