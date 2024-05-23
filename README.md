## Rasa 

Vous trouverez le rendu de l'exercice 4 sur la branche exercice4_table.
Dépôt regroupant les différents exercices réalisés pendant le cours agents conversationnel et bots

## Installation 

### Cloner le projet et installer les requirements
```
git clone https://github.com/mayyyyyl/rasa.git
git checkout exercice4_table
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
