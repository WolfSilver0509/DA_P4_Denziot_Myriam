# Développez un programme logiciel en Python


Projet n°4 de la formation développeur d'Application Python.


:pushpin: ## Utilisation : Voici la liste des outils utilisées pour ce projet :

#### Python

* Python : Version 3.9 (minimum requis pour faire marcher le script)

### Librairies Python :

* A remplire 


:pushpin: ## Installation de la Démo du logiciel de tournoi :chess_pawn:



:computer: ### Python
Vous devez avoir Python, version 3.9 minimum, installé sur votre ordinateur (si ce n'est pas le cas vous pouvez le télécharger [ici - Python](https://www.python.org/downloads/))


:chess_pawn: Ensuite téléchargez le repo version zip sur github  :


:point_right: Créez un nouveau dossier sur votre bureau avec le nom que vous souhaitez par exemple : DemoChess



:point_right: Dé-zippez le contenu du dossier zip dans ce nouveau dossier : DemoChess




Une fois cela fait ouvrez le terminal de commande (Invite de commande) :



:point_right: Une fois le terminal ouvert nous allons rejoindre notre bureau dans un premier temps
```
cd desktop
```
:point_right: Ensuite nous allons rejoindre notre nouveau dossier sur le bureau
```
cd DemoChess
```
:point_right: Une fois là nous allons créer notre environnement virtuel ( exemple : envVirtuel ) sur python avec cette commande
```
python -m venv envVirtuel
```
:point_right: Une fois l'environnement créé nous allons nous rendre dans le dossier de l'environnement virtuel afin de l'activer:



Pour cela il nous faut récupérer le chemin du dossier:



* Rendez-vous sur votre bureau
* Allez dans le dossier "DemoChess"
* Maj + Clic Droit sur le dossier "envVirtuel"
* Faire : "Copier en tant que chemin d'accès"



:point_right: Une fois cela fait, retournez sur le terminal copiez votre chemin d'accès en rajoutant "\Scripts\activate" à la fin :
```
C:\Users\wolf\Desktop\DemoChess\envVirtuel\Scripts\activate
```
:point_right: Si tout va bien vous devez voir apparaître un (env) à côté de votre chemin d'accès, comme ceci
```
(env) C:\Users\wolf\Desktop\DemoChess>
```
:point_right: Maintenant nous allons télécharger les librairies python nécessaire pour cela
```
pip install -r requirements.txt
```



:computer: ### Tout est fin prêt, pour lancer votre programme !



:point_right: Ecrivez le lancement du script python
```
python main.py
```



:bar_chart: Il ne vous reste plus qu'à suivre les questions pour profiter au mieux de la démonstration de scrapping !



:warning: Après chaque question n'oubliez pas, pour relancer le script il suffit de :



:point_right: Démarrer le script
```
python main.py
```


### Générer un rapport Flake8 HTML sur le programme Python :

:point_right: Dans le terminal dans votre dossier :
```
(env) C:\Users\wolf\Desktop\DemoChess>
```

:point_right: Pour voir si il y a des erreur de Flake8 :
```
(env) C:\Users\wolf\Desktop\DemoChess> Flake8
```

:point_right: Si il n'y a pas d'erreur il ne vous affichera rien et vous aurez de nouveau :
```
(env) C:\Users\wolf\Desktop\DemoChess> 
```

:point_right: Pour générer un rapport Flake8 HTML :
```
flake8 --format=html --htmldir=flake-report
```
:point_right: Celà fait un nouveau dossier nommée "Flake-report" est apparue !

:point_right: Vous pouvez vous rendre dedans et ouvrire dans un navigateur le fichier Index.html 

:point_right:La page s'ouvre , si il vous affiche un bandeau vert avec all Good !  - Tout est bon !!  :

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


