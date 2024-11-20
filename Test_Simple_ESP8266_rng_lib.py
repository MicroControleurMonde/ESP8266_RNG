# Importer la bibliothèque et les classes
import esp8266_rng_lib

# Créer une instance de RandomGenerator
rng = esp8266_rng_lib.RandomGenerator()

# Générer un nombre aléatoire
random_number = rng.generate()

# Afficher le nombre aléatoire généré
print(random_number)
