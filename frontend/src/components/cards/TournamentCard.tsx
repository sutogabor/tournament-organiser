import React from "react";
import { Event } from "../../interfaces/Event.ts";
import DeleteButton from "../buttons/DeleteButton.tsx";
import useDeleteEvent from "../../hooks/useDeleteEvent.tsx";
import "../../styles/tournament-card.css";
import { Link } from 'react-router-dom';

export interface EventCardProps {
    event: Event;
}

const TournamentCard: React.FC<EventCardProps> = ({ event }) => {
    const { deleteEvent, isLoading } = useDeleteEvent();
    const eventDate = new Date(event.date);
    const formattedDate = `${eventDate.getFullYear()}.${(eventDate.getMonth() + 1)
        .toString().padStart(2, '0')}.${eventDate.getDate()
        .toString().padStart(2, '0')}. ${eventDate.getHours()
        .toString().padStart(2, '0')}:${eventDate.getMinutes()
        .toString().padStart(2, '0')}`;


    return (
        <div className="event-card" key={event.id}>
            <div className="card-details">
                <div className="card-header">{event.name}</div>
                <div className="card-body">
                    <p>Start time:</p>
                    {formattedDate}
                </div>
            </div>
            <div className="card-buttons">
                <Link to={`/tournament/${event.id}`} className="event-details-link">
                    Event Details
                </Link>
                <DeleteButton onDelete={() => deleteEvent(event.id)} isLoading={isLoading} />
            </div>
        </div>
    );
};

export default TournamentCard;
