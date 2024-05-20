import json
import os
import random
import re

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

RESERVATIONS_FILE_PATH = 'reservations.json'

def load_reservations():
    if os.path.exists(RESERVATIONS_FILE_PATH):
        with open(RESERVATIONS_FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_reservations(reservations):
    with open(RESERVATIONS_FILE_PATH, 'w') as file:
        json.dump(reservations, file)

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
        
        # Validate phone number format
        if not re.match(r'^\d{10}$', phone_number):
            dispatcher.utter_message(text="Le numéro de téléphone doit être composé de 10 chiffres. Veuillez réessayer.")
            return [SlotSet("phone_number", None), SlotSet("reservation_number", None)]
        
        # Validate number of people
        try:
            number_of_people = int(number_of_people)
            if number_of_people > 20:
                dispatcher.utter_message(text="Le nombre de personnes est trop important, nous ne pouvons accueillir des groupes supérieurs à 20 personnes. Veuillez réessayer.")
                return [SlotSet("number_of_people", None), SlotSet("reservation_number", None)]
        except ValueError:
            dispatcher.utter_message(text="Le nombre de personnes est trop important, nous ne pouvons accueillir des groupes supérieurs à 20 personnes. Veuillez réessayer.")
            return [SlotSet("number_of_people", None), SlotSet("reservation_number", None)]
        
        disponible = True
        
        if disponible:
            reservation_number = f"R{str(random.randint(10000, 99999))}"
            reservation_details = {
                "reservation_number": reservation_number,
                "date": date,
                "number_of_people": number_of_people,
                "phone_number": phone_number,
                "reservation_name": reservation_name
            }
            reservations = load_reservations()
            reservations.append(reservation_details)
            save_reservations(reservations)
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

class ActionListReservations(Action):

    def name(self) -> Text:
        return "action_list_reservations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        reservations = load_reservations()
        if not reservations:
            dispatcher.utter_message(text="Il n'y a aucune réservation confirmée.")
            return []
        
        reservations_text = "Réservations confirmées:\n"
        for reservation in reservations:
            reservations_text += (
                f"- Numéro: {reservation['reservation_number']}, "
                f"Nom: {reservation['reservation_name']}, "
                f"Date: {reservation['date']}, "
                f"Nombre de personnes: {reservation['number_of_people']}, "
                f"Téléphone: {reservation['phone_number']}\n"
            )
        
        dispatcher.utter_message(text=reservations_text)
        return []