# Généralité sur la PWM 

La modulation à largeur d’impulsion où PWM est un signal carré qui a généralement une fréquence de plusieurs centaines de hertz à plusieurs dizaines de milliers de hertz. Les impulsions on une durée qui correspond à un pourcentage du temps de la période. S’il on applique une PWM de 50% on aura la tension dans la led divisé de moitié et la luminosité de même. Dans les programmes on utilise la fonction duty_u16(). La valeur de la PWM exprimée par une valeur comprise entre 0 et 65535 (16 bits) 0 correspond à absence de signal et 65535 une PWM de 100%.

# BuzzerSong.py

Le programme joue le début en boucle de la chanson « Never gonna give you up » de Rick Astley. Les notes sont décrites par une valeur de fréquence. La PWM sert ici pour régler le volume.

# LedPWMvariation.py

La led se met à clignoter mais avec une variation progressive de la luminosité. L’intensité varie grâce à une boucle qui va modifier la valeur de la PWM.


# PWMLedWithPot.py

La luminosité de la led varie en fonction du signal PWM qu’on applique. Ce dernier dépend de la valeur renvoyée par un potentiomètre. Pour lire la valeur du potentiomètre on utilise la fonction read_u16.

# PotWithLed.py

La led s’allume si le potentiomètre est positionné dans une zone où il renvoie une valeur supérieur à 20000 mais inférieur à 40000.

# SimpleBuzzer.py

Il fait sonner un buzzer avec une valeur de PWM fixe.


