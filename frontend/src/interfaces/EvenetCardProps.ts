import {Event} from "./Event.ts";


export interface EventCardProps {
    event: Event;
    deleteEvent: (id: number) => void;
}