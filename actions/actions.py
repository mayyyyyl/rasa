from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random
import re

class ActionMakeReservation(Action):
    def name(self) -> Text:
        return "action_make_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        date = tracker.get_slot('date')
        number_of_people = tracker.get_slot('number_of_people')
        phone_number = tracker.get_slot('phone_number')
        reservation_name = tracker.get_slot('reservation_name')
        
        if not re.match(r'^\d{10}$', phone_number):
            dispatcher.utter_message(text="Le numéro de téléphone doit être composé de 10 chiffres. Veuillez réessayer.")
            return [SlotSet("phone_number", None), SlotSet("reservation_number", None)]
        
        disponible = True
        
        if disponible:
            reservation_number = f"R{str(random.randint(10000, 99999))}"
            dispatcher.utter_message(text=f"Réservation pour {number_of_people} personnes au nom de {reservation_name} le {date}. Votre numéro de réservation est {reservation_number}.")
            return [SlotSet("reservation_number", reservation_number)]
        else:
            dispatcher.utter_message(text=f"Désolé, aucune table disponible pour {number_of_people} personnes le {date}.")
            return [SlotSet("reservation_number", None)]

class ActionConfirmReservation(Action):

    def name(self) -> Text:
        return "action_confirm_reservation"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        reservation_number = tracker.get_slot('reservation_number')

        if reservation_number is None:
            dispatcher.utter_message(text="Désolé, je n'ai pas trouvé votre numéro de réservation.")
            return []

        dispatcher.utter_message(text=f"Votre réservation numéro {reservation_number} a été confirmée.")
        return []