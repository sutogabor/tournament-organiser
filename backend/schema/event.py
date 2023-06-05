from ma import ma
from ..model.event_model import Event


class EventSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        fields = ("id", "name", "date")
