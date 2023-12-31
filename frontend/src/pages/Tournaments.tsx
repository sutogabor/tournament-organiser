import React, {useState, useEffect} from 'react';
import TournamentCard from "../components/cards/TournamentCard.tsx";
import {Event} from "../interfaces/Event.ts";
import {apiGet} from "../utils/apiCalls.ts";
import "../styles/tournaments-page.css"
import "./../styles/styles.css"


const Tournaments: React.FC = () => {


    const [events, setEvents] = useState<Event[]>([]);
    const [refresh, setRefresh] = useState<boolean>(false);
    const currentDate = new Date();
    const ongoingEvents = events.filter(event => new Date(event.date) <= currentDate);
    const upcomingEvents = events.filter(event => new Date(event.date) > currentDate);
    const [searchQuery, setSearchQuery] = useState<string>("");

    let displayedOngoingEvents = ongoingEvents;
    let displayedUpcomingEvents = upcomingEvents;

    if (searchQuery !== "") {
        displayedOngoingEvents = ongoingEvents.filter(event => event.name.toLowerCase().includes(searchQuery.toLowerCase()));
        displayedUpcomingEvents = upcomingEvents.filter(event => event.name.toLowerCase().includes(searchQuery.toLowerCase()));
    }


    const testData: Event[] = [
        {
            "date": "2022-12-27T18:00",
            "id": 2,
            "name": "FIFA"
        },
        {
            "date": "2024-12-27T18:00",
            "id": 3,
            "name": "TEKKEN"
        },
        {
            "date": "2022-12-27T18:00",
            "id": 5,
            "name": "Smash Bros"
        },
        {
            "date": "2024-08-14T13:53",
            "id": 6,
            "name": "Wind Jammers"
        },
        {
            "date": "2024-08-14T13:53",
            "id": 7,
            "name": "Mario Kart"
        },
        {
            "date": "2023-08-24T13:53",
            "id": 8,
            "name": "Foosball"
        }
    ]


    async function getData() {
        try {
            const response = await apiGet("https://localhost:8080/event");
            if (response && response.ok) {
                const data = await response.json();
                return data;
            } else {
                console.log("Bad response at Tournaments.getData")
            }
        } catch (error) {
            console.log(error)
        }
    }

    async function refreshData() {
        try {
            const data = await getData();
            setEvents(data);
            console.log(events);
        } catch (error) {
            console.log("Error in refreshing data on the UpComingEvents page:", error)
        }
    }

    function addTestData() {
        setEvents(testData);
    }

    useEffect(() => {
        // refreshData().then(() => {
        //     setRefresh(false);
        // });
        addTestData();
    }, [refresh]);

    if (events.length == 0) {
        return (
            <div className="content">
                <h2 className="message">No Tournaments to show</h2>
            </div>
        )
    }

    return (
        <div className="tournaments-container">
            <h1 className="page-title">Tournaments</h1>
            <div className="search-bar">
                <input
                    type="text"
                    placeholder="Search tournaments..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="search-input"
                />
            </div>
            <div className="tournament-cards-container">
                {displayedOngoingEvents.length > 0 && (
                    <div className="event-section">
                        <h2>Ongoing Tournaments</h2>
                        <div className="event-cards">
                            {displayedOngoingEvents.map(event => (
                                <TournamentCard key={event.id} event={event}/>
                            ))}
                        </div>
                    </div>
                )}
                {displayedUpcomingEvents.length > 0 && (
                    <div className="event-section">
                        <h2>Upcoming Tournaments</h2>
                        <div className="event-cards">
                            {displayedUpcomingEvents.map(event => (
                                <TournamentCard key={event.id} event={event}/>
                            ))}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Tournaments;
