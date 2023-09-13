import React, { useEffect, useState } from 'react';
import { Event } from '../interfaces/Event.ts';
import { useParams } from 'react-router-dom';

interface TournamentDetailsParams {
  id: string;
}

const TournamentDetails: React.FC = () => {
  const [details, setDetails] = useState<Event | undefined>();
  const { id } = useParams<TournamentDetailsParams>();

  const fetchEvent = async () => {
    try {
      const response = await fetch(`/event/${id}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        const data = await response.json();
        const event: Event = data as Event; // Assuming the response data matches the Event interface
        setDetails(event);
      } else {
        console.error('Event not found!!');
      }
    } catch (error) {
      console.error('Error occurred while fetching event:', error);
    }
  };

  useEffect(() => {
    fetchEvent();
  }, []);

  if (details === undefined) {
    return <div>LOOOOAAADIIIING</div>;
  }

  return (
    <div>
      <h1>{details.name}</h1>
      <h3>{details.date}</h3>
      <h3>Blalalblaa</h3>
    </div>
  );
};

export default TournamentDetails;
