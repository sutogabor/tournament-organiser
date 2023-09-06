import React, { useState } from 'react';
import { apiPost } from '../utils/apiCalls.ts';
import '../styles/add-tournament-page.css';

const AddTournament: React.FC = () => {
  const [name, setName] = useState<string>('');
  const [date, setDate] = useState<string>('');
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const payload = { name, date };
    const URL = 'https://localhost:8080/event/add';
    const successMessageText = 'Event created successfully.';

    try {
      await apiPost(payload, URL, successMessageText);
      setSuccessMessage(successMessageText);
      console.log(successMessageText);
    } catch (error) {
      console.log(error);
    }
  };

  const handleBackClick = () => {
    window.location.href = '/add-tournament'; // Replace '/original-page' with the actual URL of your original page
  };

  return (
      <div className="add-event-container">
        <h2>Add New Event</h2>
        {successMessage ? (
            <div className="success-message">
              <p>{successMessage}</p>
              <button onClick={handleBackClick}>Back</button>
            </div>
        ) : (
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="event-name">Please name your event:</label>
                <input
                    type="text"
                    id="event-name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    placeholder="Event Name"
                    required
                />
              </div>
              <div className="form-group">
                <label htmlFor="event-date">When will it start?</label>
                <input
                    type="datetime-local"
                    id="event-date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    required
                />
              </div>
              <button type="submit">Add Event</button>
            </form>
        )}
      </div>
  );
};

export default AddTournament;
