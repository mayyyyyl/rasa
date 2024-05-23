## Rasa 

Vous trouverez le rendu de l'exercice 4 sur main et la branche exercice4_table

Dépôt regroupant les différents exercices réalisés pendant le cours agents conversationnel et bots

## Installation 

### Cloner le projet et installer les requirements
```
git clone https://github.com/mayyyyyl/rasa.git
git checkout exercice4_table (pas obligatoire)
cd rasa
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
rasa train
```
### Interagir avec le bot

dans un terminal lancer la commande
```
rasa run actions
```

dans un second 
```
rasa shell
```

Vous pouvez maintenant échanger avec le bot !

## Notes sur l'avancement

Pour utiliser rasa, j'ai utilisé vagrant afin de m'y connecter en ssh.
L'ajout de commentaires et l'annulation d'une réservation ne sont pas implémentés.
Le Bot n'est pas intégré sur une plateforme comme Discord.

### Schéma 

![exemple_de_story](https://github.com/mayyyyyl/rasa/assets/90853285/0ba4b7ab-3ec9-4e88-be49-0c7a30b86b4d)

### Exemples
 Réservation d'une table
![rasa_resa](https://github.com/mayyyyyl/rasa/assets/90853285/78977531-4128-4946-9baa-2d932f2c7669)

 Vérifier que le numéro de téléphone comporte 10 chiffres, un groupe ne peut dépasser 20 personnes
![exemple_resa](https://github.com/mayyyyyl/rasa/assets/90853285/eb25d8c5-c869-4edb-a0b7-517db08e77a8)

 Liste des réservations
![resa](https://github.com/mayyyyyl/rasa/assets/90853285/1a319f8b-b7e2-4dba-aca9-801bbbad302d)

 Menu et Allergènes
![rasa_allergenes_menu](https://github.com/mayyyyyl/rasa/assets/90853285/7c17cfac-9906-477e-b360-aea359a9f7cb)

Capacité de 40 couverts par jour

![plus_places_rasa](https://github.com/mayyyyyl/rasa/assets/90853285/e7020ee0-37f8-450e-a892-77e223b7300a)
