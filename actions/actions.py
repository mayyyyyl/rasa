from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.events import SlotSet
import random
import sqlite3
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConfirmReservation(Action):
    def name(self) -> Text:
        return "action_confirm_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        date = tracker.get_slot("date")
        number_of_people = tracker.get_slot("number_of_people")
        reservation_name = tracker.get_slot("reservation_name")
        phone_number = tracker.get_slot("phone_number")

        confirmation_message = (
            f"Votre réservation pour {number_of_people} personnes le {date} au nom de {reservation_name} "
            f"a été confirmée. Nous avons envoyé les détails de la réservation à {phone_number}."
        )

        dispatcher.utter_message(text=confirmation_message)

        return []