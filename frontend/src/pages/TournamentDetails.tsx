import {SingleEliminationBracket, Match, SVGViewer} from '@g-loot/react-tournament-brackets';

interface TournamentDetailsParams {
  id: string;
}

const TournamentDetails: React.FC = () => {
  const [details, setDetails] = useState<Event | undefined>();
  const { id } = useParams<TournamentDetailsParams>();

const matchesData = [
    {
        "id": 10001,
        "name": "NAME",
        "nextMatchId": 10101,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "c016cb2a-fdd9-4c40-a81f-0cc6bdf4b9cc",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Zoli"
            },
            {
                "id": "9ea9ce1a-4794-4553-856c-9a3620c0531b",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Peti"
            }
        ]
    },
    {
        "id": 10002,
        "name": "NAME",
        "nextMatchId": 10102,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "c016cb2a-fdd9-4c57-a81f-0cc6bdf4b9cc",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Imi"
            },
            {
                "id": "9ea9ce1a-4794-7153-856c-9a3620c0531b",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Feri"
            }
        ]
    },
    {
        "id": 10003,
        "name": "NAME",
        "nextMatchId": 10103,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "c016cb2a-fdd9-4c40-a54f-0cc6bdf4b9cc",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Geza"
            },
            {
                "id": "9ea9ce1a-4729-4553-856c-9a3620c0531b",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Roli"
            }
        ]
    },
    {
        "id": 10004,
        "name": "NAME",
        "nextMatchId": 10104,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "c088cb2a-fdd9-4c40-a81f-0cc6bdf4b9cc",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Liza"
            },
            {
                "id": "9ea9ce1a-4345-4553-856c-9a3620c0531b",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Karcsi"
            }
        ]
    },
    {
        "id": 10005,
        "name": "NAME",
        "nextMatchId": 10104,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "c016cb2a-fdd9-4c40-a23f-0cc6bdf4b9cc",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Kata"
            },
            {
                "id": "9ea9ce1a-4794-4553-958c-9a3620c0531b",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Eszter"
            }
        ]
    },
    {
        "id": 10101,
        "name": "NAME",
        "nextMatchId": 10201,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "c016cb2a-fdd9-4c50-a77f-0cc6bdf4b9cc",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Samu"
            }
        ]
    },
    {
        "id": 10102,
        "name": "NAME",
        "nextMatchId": 10201,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "9ea9ce1a-4794-3333-856c-9a3620c0531b",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Ati"
            }
        ]
    },
    {
        "id": 10103,
        "name": "NAME",
        "nextMatchId": 10202,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": [
            {
                "id": "9ea9ce1a-5566-3353-856c-9a3620c0531b",
                "resultText": null,
                "isWinner": false,
                "status": null,
                "name": "Ede"
            }
        ]
    },
    {
        "id": 10104,
        "name": "NAME",
        "nextMatchId": 10202,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": []
    },
    {
        "id": 10201,
        "name": "NAME",
        "nextMatchId": 10301,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": []
    },
    {
        "id": 10202,
        "name": "NAME",
        "nextMatchId": 10301,
        "tournamentRoundText": "0",
        "startTime": "2024-05-30T14:15:00",
        "state": "DONE",
        "participants": []
    },
]

  useEffect(() => {
    fetchEvent();
  }, []);

const TournamentDetails = () => {
    console.log("TournamentDetails component rendered");
    console.log("matchesData:", matchesData);

    return (
        <div>
            <h2>Bracket Details</h2>
            <SingleEliminationBracket
                matches={matchesData}
                matchComponent={Match}
                svgWrapper={({ children, ...props }) => (
                    <SVGViewer width={500} height={500} {...props}>
                        {children}
                    </SVGViewer>
                )}
            />
        </div>
    );
};

export default TournamentDetails;
