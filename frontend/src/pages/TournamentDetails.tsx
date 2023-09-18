import {SingleEliminationBracket, Match, SVGViewer} from '@g-loot/react-tournament-brackets';

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
