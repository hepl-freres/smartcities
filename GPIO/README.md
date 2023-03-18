# Blink.py : 

Le programme blink.py permet de faire clignoter une led à une fréquence de 500ms. On effectue une boucle en allumant (led.high()) puis en étaignant (led.high()) les leds la led avec un délai entre (utime.sleep_ms(500)). ou bien on peut utiliser la fonction toggle() qui change l'état sortie. la led utilisé est celle qui est sur le pico



https://user-images.githubusercontent.com/125506518/226100754-a11874bc-5610-40bc-8ae9-67af86104ccc.mp4



# ledWithButton.py:

La led s'allume s'il on un presse le bouton. On utilise une condition if, si la valeur du GPIO est à 1 donc quand on appuye sur le bouton, on allume la led. dans le cas contraire (elsif), led est éteinte.



https://user-images.githubusercontent.com/125506518/226102009-9a24a60f-fcf1-43c9-baa1-b3ffb6097a1f.mp4



# blinkExternalLed.py:

Le code est similaire à Blink sauf qu'on utilise une led externe ( pin 20 ).


https://user-images.githubusercontent.com/125506518/226100784-0e82282a-3c00-43f6-9272-37be919e19af.mp4



# LedButtonWithState

La Led s'allume ou s'éteint après une pression sur le bouton. pour maintenir l'etat en sortie, on utilise une variable ( val ) qui est initié à 0. s'il on presse une fois, on fait +1 dans val et la led s'alume car (led.value(val)). s'il on appuye une deuxieme fois, on remet val à 0 ce qui éteint la led. Dans ce code le déclenchement de la sortie led est temporisé.


![LedButtonWithState](https://user-images.githubusercontent.com/125506518/226101612-1e453e90-9791-4f15-af84-57e5806115d8.gif)

# LedButtonWithInterrup : 

le programme à la même fonction que LedButtonWithState mais sans les délais. Dans ce cas ci on utilise une interruption iqr
qui se déclenche sur les fronts descendans, cet à dire quand on relache le bouton.



[interruptiobouton.zip](https://github.com/hepl-freres/smartcities/files/10952294/interruptiobouton.zip)



![LedButtonWithInterrupt](https://user-images.githubusercontent.com/125506518/226101925-38d7d2c4-8a47-4b8e-ad93-a1458de79006.gif)






