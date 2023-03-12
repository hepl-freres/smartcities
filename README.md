# smartcities![raspbPico](https://user-images.githubusercontent.com/125506518/219489552-a02c9c55-1c30-4474-accf-235a417fcaef.JPG)

Le raspberry pico w est une carte qui dispose d'un microcontrôleur RP2040 à deux cœurs ARM cortex m0+. il a 256 ko octets de mémoire ram et une fréquence d'horloge de maximum 133 Mhz. Ce microcontrôleur a une mémoire flash externe à la puce de 2Mo. Au niveau du brochage, on retrouve des GPIO d'entrées-sorties dont certaines peuvent faire de la PWM, des communications séries de type uart/i2c/spi ou encore de la conversion de signaux analogique en signaux numériques. Le pico W défère des autres modèles car il possède une interface wifi grâce au circuit infineon CYW43439. le pico à l'avantage d'avoir de bonnes performances en plus d'une faible consommation et d'un format réduit de 25mm x 51mm. 


# Environnement software 

Le pico est compatible avec windows, Mac OS et linux. Pour le programmer on utilise le logiciel Thonny qui est utlisier pour la programmation en python ou en micro python. pour l'installation on le télécharge sur le site ( lien dans source ) puis on appuye sur le bouton bootsel du pico et on le branche sur le pc. Le raspberry apparait alors comme une clé usb et on va y mettre un fichier .uf2 qui correspond à son firmware. il ne reste plus qu'à sélectionner le bon language dans Thonny. 




# sources 

https://developer.arm.com/Processors/Cortex-M0-Plus
https://www.raspberrypi.com/products/raspberry-pi-pico/
https://thonny.org/
https://micropython.org/download/rp2-pico/

