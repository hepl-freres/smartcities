# Blink.py : 

Le programme blink.py permet de faire clignoter une led à une fréquence de 500ms. On peut utiliser effectuer une boucle en allumant (led.high()) puis en étaignant (led.high()) les leds la led avec un délai entre (utime.sleep_ms(500)). ou bien on peut utiliser la fonction toggle() qui change l'état sortie. la led utilisé est celle qui est sur le pico


# ledWithButton.py:

La led s'allume s'il on un presse le bouton. On utilise une condition if, si la valeur du GPIO est à 1 donc quand on appuye sur le bouton, on allume la led. dans le cas contraire (elsif), led est éteinte.



# blinkExternalLed.py:

Le code est similaire à Blink sauf qu'on utilise une led externe ( pin 20 ).


# LedButtonWithInterrup : 

La led s'allume 









