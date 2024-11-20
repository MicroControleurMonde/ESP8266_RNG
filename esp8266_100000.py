import esp8266_rng_lib
import utime
import time


# Fonction pour afficher l'heure actuelle
def display_current_time():
    # Obtenir l'heure locale à partir de l'horloge système
    current_time = time.localtime()  # Récupérer l'heure locale (format struct_time)
    
    # Formater manuellement l'heure, les minutes et les secondes
    hour = current_time[3]
    minute = current_time[4]
    second = current_time[5]
    
    # Afficher l'heure au format: HH:MM:SS
    formatted_time = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    print("Heure", formatted_time)

print("Démarrage du génerateur")
# Afficher l'heure courante toutes les secondes
display_current_time()

# Créer une instance de RandomGenerator
rng = esp8266_rng_lib.RandomGenerator()

# Nombre de nombres aléatoires à générer
num_random_numbers = 100000
block_size = 10000  # Taille du bloc (10 000 valeurs)

# Ouvrir un fichier pour enregistrer les nombres aléatoires
file_name = 'esp8266_rng.txt'
with open(file_name, 'w') as f:
    # Mesurer le temps de début
    start_time = utime.ticks_ms()

    # Générer les nombres aléatoires et les écrire dans le fichier
    for i in range(num_random_numbers):
        random_number = rng.generate()
        f.write(f"{random_number}\n")

        # Afficher un message tous les 10 000 nombres générés
        if (i + 1) % block_size == 0:
            print(f"Bloc de {block_size} nombres générés (total {i + 1} sur {num_random_numbers})")

    # Mesurer le temps de fin
    end_time = utime.ticks_ms()

# Calculer le temps écoulé en secondes
elapsed_time_ms = utime.ticks_diff(end_time, start_time)
elapsed_time_s = elapsed_time_ms / 1000.0

# Calculer le débit en octets par seconde
# Chaque nombre aléatoire généré est un entier de 64 bits (8 octets)
total_bytes = num_random_numbers * 8  # 8 octets par nombre
bytes_per_second = total_bytes / elapsed_time_s

# Afficher les résultats
print(f"Temps écoulé pour générer {num_random_numbers} nombres aléatoires: {elapsed_time_s:.2f} secondes")
print(f"Débit de génération des nombres aléatoires: {bytes_per_second:.2f} bytes par seconde")
print("Arret du génerateur")
display_current_time()
