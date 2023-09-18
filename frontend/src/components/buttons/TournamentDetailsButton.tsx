import { Link } from 'react-router-dom';
import '../../styles/tournament-card.css'; // Import the CSS file for styling

interface EventDetailsButtonProps {
    eventId: number; // or whatever type your event IDs are
}

function TournamentDetailsButton({ eventId }: EventDetailsButtonProps) {
    return (
        <Link to={`/tournament/${eventId}`} className="event-details-button">
            View Details
        </Link>
    );
}

export default TournamentDetailsButton;
