from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
import random

# class ActionCheckAvailability(Action):
#     def name(self) -> Text:
#         return "action_check_availability"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Logique pour vérifier la disponibilité
#         return []

# class ActionInformAvailability(Action):
#     def name(self) -> Text:
#         return "inform_availability"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Logique pour informer de la disponibilité
#         return []

# class ActionMakeReservation(Action):
#     def name(self) -> Text:
#         return "action_make_reservation"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Logique pour faire une réservation
#         return []

class ActionGetReservationNumber(Action):
    def name(self) -> Text:
        return "action_get_reservation_number"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        phone_number = tracker.latest_message.get('text')
        
        if phone_number:
            reservation_number = generate_reservation_number(phone_number)
            
            dispatcher.utter_message(text=f"Votre réservation a été confirmée. Voici votre numéro de réservation : {reservation_number}")
        else:
            dispatcher.utter_message(text="Désolé, je n'ai pas pu récupérer votre numéro de téléphone.")
        
        return []

def generate_reservation_number(phone_number: Text) -> Text:
    random_number = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    return f"RV{phone_number[-6:]}{random_number}"