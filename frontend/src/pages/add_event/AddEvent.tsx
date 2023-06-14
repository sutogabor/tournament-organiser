
import { useState, ChangeEvent, FormEvent } from 'react';

const AddEvent = (): JSX.Element => {
  const [name, setName] = useState<string>("");
  const [date, setDate] = useState<string>("");

  const handleSubmit = async (e: FormEvent<HTMLFormElement>): Promise<void> => {
    e.preventDefault();
    try {
      const response = await fetch('/event/add', {
        method: "POST",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, date })
      });

      console.log(name, date);

      if (response.ok) {
        console.log("Event created successfully.");
      } else {
        console.error("Failed to create event.");
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleNameChange = (e: ChangeEvent<HTMLInputElement>): void => {
    setName(e.target.value);
  };

  const handleDateChange = (e: ChangeEvent<HTMLInputElement>): void => {
    setDate(e.target.value);
  };

  return (
      <div>
        <form onSubmit={handleSubmit}>
          <input
              type="text"
              value={name}
              onChange={handleNameChange}
              placeholder="Your Event name"
          />
          <input
              type="datetime-local"
              value={date}
              onChange={handleDateChange}
          />
          <button type="submit">Add</button>
        </form>
      </div>
  );
}

export default AddEvent;
