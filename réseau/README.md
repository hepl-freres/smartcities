#  NTPavecLCD.py

Le Network Time Protocol ou NTP est un protocole qui permet de synchroniser l'horloge local d'une machine sur une référence d'heure.
Pour récupérer l'heure on créer un socket UDP/IP qui est mis sur écoute.


fonctions utilisés :

socket.getaddrinfo(host,port) : retourne des données sur l'hôte 

socket.sendto(NTP_QUERY,addr) : envoie un message de NTP_QUERY bytes à l'adresse ADR permettant d'initialiser la communication

socket.socket(socket.AF_INET, socket.SOCK_DGRAM) : création d'un socket (protocole UDP/IP)

socket.recv(48) : réception un message qui fait 48 octets

s.close() : ferme la connexion 



![IMG_20230507_175011494](https://user-images.githubusercontent.com/125506518/236701722-9a30e8fa-9ca9-4d1b-a11c-99e687bb0ecd.jpg)


# OpenWeather.py

Pour pouvoir connecter le pico utilise une série de commande, il a besoin aussi de connaître le nom du réseau ( ssid ) et le mot de passe.

WLAN.connect() : fonction de connexion au wifi

LAN.ifconfig(): configuration du réseau 

WLAN.disconnect() : fonction de connexion au wifi

WLAN.isconnected() : vérifie si la connexion est active

LAN.active() : activation/desactivation de la connexion internet

urequests.get() : effectue des requêtes à URL pour récuperer des données
 
Pour l'API on lui fournir les coordonnées ( longitude/latitude ), une clée et le type d'unité à l'ocurence le métrique.

![CaptureAPIopenWeather](https://user-images.githubusercontent.com/125506518/236701757-d3ea8d95-0ef6-48ba-b5c0-bc48fd6ab46c.JPG)





NB : j'ai mit des ****** pour ne pas mettre mon vrai mot de pas wifi.
