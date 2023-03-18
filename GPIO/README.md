# Blink.py : 

Le programme blink.py permet de faire clignoter une led à une fréquence de 500ms. On effectue une boucle en allumant (led.high()) puis en étaignant (led.high()) les leds la led avec un délai entre (utime.sleep_ms(500)). ou bien on peut utiliser la fonction toggle() qui change l'état sortie. la led utilisé est celle qui est sur le pico
![Blink](https://user-images.githubusercontent.com/125506518/226099917-de34544b-545c-487d-b7d8-b9f3ae00d720.gif)


# ledWithButton.py:

La led s'allume s'il on un presse le bouton. On utilise une condition if, si la valeur du GPIO est à 1 donc quand on appuye sur le bouton, on allume la led. dans le cas contraire (elsif), led est éteinte.



# blinkExternalLed.py:

Le code est similaire à Blink sauf qu'on utilise une led externe ( pin 20 ).


# LedButtonWithState

La Led s'allume ou s'éteint après une pression sur le bouton. pour maintenir l'etat en sortie, on utilise une variable ( val ) qui est initié à 0. s'il on presse une fois, on fait +1 dans val et la led s'alume car (led.value(val)). s'il on appuye une deuxieme fois, on remet val à 0 ce qui éteint la led. Dans ce code le déclenchement de la sortie led est temporisé.

# LedButtonWithInterrup : 

le programme à la même fonction que LedButtonWithState mais sans les délais. Dans ce cas ci on utilise une interruption iqr
qui se déclenche sur les fronts descendans, cet à dire quand on relache le bouton.



[interruptiobouton.zip](https://github.com/hepl-freres/smartcities/files/10952294/interruptiobouton.zip)




NB: compte tenue de l'espace max que prend les videos je suis en train de les retravailler de m^me que les photos 


