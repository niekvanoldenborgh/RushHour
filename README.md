# Rush Hour

Rush Hour is een spel waarbij het doel is om op een bord met voertuigen de rode auto naar de uitgang te rijden. Het bord is vierkant en opgebouwd uit vakjes. Er zijn twee verschillende soorten voertuigen, een auto, welke twee vakjes in beslag neemt en een vrachtwagen, welke drie vakjes in beslag neemt. Een voertuig kan alleen in de richting bewegen waarop deze georienteerd is. Een horizontaal geplaatst voertuig kan dus niet in de verticale richting bewegen. Diagonale bewegingen zijn ook niet toegestaan en voertuigen mogen niet door elkaar heen bewegen. Er zijn drie verschillende bordgroottes, 6x6, 9x9 en 12x12, zoals hieronder geïllustreerd. 

Bordgrootte 6x6: 
<img src="/visuals/board_pictures/Rushhour6x6_1.jpg" width = 20%>
<img src="/visuals/board_pictures/Rushhour6x6_2.jpg" width = 20%>
<img src="/visuals/board_pictures/Rushhour6x6_3.jpg" width = 20%>

Bordgrootte 9x9: 
<img src="/visuals/board_pictures/Rushhour9x9_1.jpg" width = 20%>
<img src="/visuals/board_pictures/Rushhour9x9_2.jpg" width = 20%>
<img src="/visuals/board_pictures/Rushhour9x9_3.jpg" width = 20%>

Bordgroote 12x12:
<img src="/visuals/board_pictures/Rushhour12x12_1.jpg" width = 20%>

Zoals eerder genoemd is het doel om de rode auto naar de uitgang te rijden en zo het spel op te lossen. Hiervoor zijn vier verschillende algoritmen geïmplementeerd: 
- Random algoritme
- Random algoritme met heuristieken
- Breadth first search algoritme
- Depth first search algoritme

## Installatie

De codebase is geschreven in python 3.12. In het bestand requirements.txt staan de benodigde packages om de code te kunnen draaien. Deze zijn te installeren door het volgende commando aan te roepen: 

> pip install -r requirements.txt

## Gebruik

Om het bord op te lossen run je het volgende command in de terminal:

> python3 main.py

Je krijgt dan het volgende te zien: 

> Welcome to Rush Hour!
> What game would you like to play?
> 1. board 1 (6x6)
> 2. board 2 (6x6)
> 3. board 3 (6x6)
> 4. board 4 (9x9)
> 5. board 5 (9x9)
> 6. board 6 (9x9)
> 7. board 7 (12x12)

> Please choose a number:

Vul bij de volgende regel in hoe vaak het spel moet runnen:

> How many times would you like to play?

There are several options to set a time limit:

> Would you like to add a time limit?
> 1. No time limit
> 2. Only time limit per game
> 3. Only overall time limit
> 4. Both overall time limit and time limit per game

>Please choose a number:

Vul hier het cijfer in van het bord dat je wilt oplossen. Je komt dan bij het volgende menu:

> Choose an algorithm to solve the board:
> 1. Random search
> 2. Breadth first search
> 3. Depth first search
> 4. Random search with Heuristics

>Please choose a number:

Hier vul je het cijfer in van het algoritme dat je wilt toepassen. 

## Structuur

Onderstaande lijst geeft de structuur van de code base weer:
- /code: bevat alle code van het project
    - /code/algoritms: bevat de code voor de algoritmen
    - /code/classes: bevat de code voor de classes waaruit het spel is opgebouwd
    - /code/functions: bevat de code voor de visualizatie en analyse
- /gameboards: bevat de verschillende borden van het spel
- /results: bevat de resultaten per algoritme

## Auteurs

- Max Schouten
- Niek van Oldenborg
- Elisa Dalemans
