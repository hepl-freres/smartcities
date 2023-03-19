#Afficheur lcd

Les ecrans LCD fonctionnent grace à une multitude de cristaux qui vont se mettre à pivoter lorsqu'ils sont soumis à un champ électrique. En pivotant ils vont laisser passer plus ou moins de la lumière polarisé provenant d'un rétroéclairage. Le lcd utilisé est contrôlé via un bus i2c


#LCDdisplay

Affiche un simple "Hello world"

![IMG_20230319_110524912](https://user-images.githubusercontent.com/125506518/226207083-462376cf-634b-4ab2-af37-8760bd1f3d4f.jpg)


#LCDdisplayWithPot

Affiche la position angulaire d'un potentiometre. la position va jusqu'à 300°

https://user-images.githubusercontent.com/125506518/226207432-1c762def-f230-40e7-98f1-8f98587b6997.mp4

pour Le caractere ° je me réfère à cette documentation 

https://www.waveshare.com/datasheet/LCD_en_PDF/LCD1602.pdf?fbclid=IwAR07Lddnesdv46NQWkOb8BcVdyY57cBhsrMp91Bv0k9i2vcBRHJ4KDJFnaQ



#lcd1602

Ce code est la bibliotheque nécessaire à l'utilisation du LCD.

Les programmes contiennent des méthodes qui peremttent differentes action:

setCursor : positionne le curseur 
clear : met le curseur à la position zéro après avoir effacer l'affichage 
write : est utilisé pour afficher des character spéciaux
print : affiche du texte ou des valeurs 
home : définit le curseur sur la position zéro


