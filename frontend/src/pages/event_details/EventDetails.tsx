import React, { useEffect, useState } from 'react'
import { Event } from '../interfaces/Event';
import { useParams } from "react-router-dom";

const EventDetails: React.FC = () => {
  const [details, setdetails] = useState<Event>();
  const id  = useParams().id;

  
  const fetchEvent = async () => {
      const response: Response = await fetch(`http://localhost:5000/event/${id}`, {
      method: "GET",
      headers: {
      'Content-Type': 'application/json'
      }
    });
  if (response.ok) {
    const data = await response.json();
    // TODO
    const event: Event =JSON.parse(JSON.stringify(data));
    console.log(event);
    setdetails(event);
  } else {
    console.error("Event not found!!");

    }
    }

    useEffect(() => {
      fetchEvent();
    },[])
  

  
  if(details === undefined) {
        return "LOOOOAAADIIIING"
      }
  return (
    <div>
        <h1>{details.name}</h1>
        <h3>{details.date}</h3>
        <h3>Blalalblaa</h3>
    </div>
  )
}

export default EventDetails