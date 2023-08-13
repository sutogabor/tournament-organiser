import React from "react";
import {EventCardProps} from "../../interfaces/EvenetCardProps.ts";

const EventCard: React.FC<EventCardProps> = ({ event, deleteEvent }) => {
    return (
        <div className="card" key={event.id}>
            <div className="card-details">
                <div className="card-header">{event.name}</div>
                <div className="card-body">{event.date}</div>
            </div>
            <div className="card-buttons">
                <button
                    className="card-button"
                    onClick={() => deleteEvent(event.id)}
                    value="Delete"
                >Delete</button>
            </div>
        </div>
    );
};

export default EventCard;
