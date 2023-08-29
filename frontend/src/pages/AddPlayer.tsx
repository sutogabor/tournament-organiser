import {useState, useEffect, ChangeEvent} from 'react';
import './../styles/add-player-page.css';
import {apiGet, apiPost} from "../utils/apiCalls.ts";

const PlayerRegistrationPage = () => {
    const [playerName, setPlayerName] = useState('');
    const [selectedTournaments, setSelectedTournaments] = useState<number[]>([]);
    const [tournamentList, setTournamentList] = useState<{ id: number; name: string }[]>([]);


    async function getData() {
        try {
            const response = await apiGet("https://localhost:8080/event");
            if (response && response.ok) {
                const data = await response.json();
                return data;
            } else {
                console.log("Bad response at AddPlayer page useEffect!")
            }
        } catch (error) {
            console.log(error)
        }
    }


    useEffect(() => {
        getData().then(data => setTournamentList(data))
    }, []);

    const handlePlayerNameChange = (event: ChangeEvent<HTMLInputElement>) => {
        setPlayerName(event.target.value);
    };

    const handleTournamentToggle = (tournamentId: number) => {
        setSelectedTournaments((prevSelected) =>
            prevSelected.includes(tournamentId)
                ? prevSelected.filter((id) => id !== tournamentId)
                : [...prevSelected, tournamentId]
        );
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        const playerPayload = {
            name: playerName,
            tournaments: selectedTournaments
        };
        const playerURL = 'https://localhost:8080/player';
        const successMessage = "Player added and registered successfully.";

        try {
            await apiPost(playerPayload, playerURL, successMessage);
            console.log("Player added and registered successfully.");
        } catch (error) {
            console.log(error);
        }
    };


    return (
        <div className="registration-container">
            <h2>Player Registration</h2>
            <form>
                <div className="form-group">
                    <label className="label-text" htmlFor="playerName">
                        Player Name:
                    </label>
                    <div className="input-container">
                        <input
                            type="text"
                            id="playerName"
                            value={playerName}
                            onChange={handlePlayerNameChange}
                            required
                        />
                    </div>
                </div>
                <div className="tournament-list">
                    <p className="choose-tournaments-text">Choose your tournaments:</p>
                    {tournamentList.map((tournament) => (
                        <div key={tournament.id} className="tournament-item">
                            <label className="tournament-name">{tournament.name}</label>
                            <input
                                type="checkbox"
                                id={`tournament-${tournament.id}`}
                                value={tournament.id}
                                checked={selectedTournaments.includes(tournament.id)}
                                onChange={() => handleTournamentToggle(tournament.id)}
                            />
                        </div>
                    ))}
                </div>
                <button type="button" onClick={handleSubmit} className="submit-button">
                    Register
                </button>
            </form>
        </div>
    );
};

export default PlayerRegistrationPage;
