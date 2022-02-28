#script modificado por dylan. Creador>https://github.com/The-M-V/NumberScanner
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
import sys
from colorama import Fore
import os
import time
import colorama


print("<<<<INSTALANDO LOS PAQUETES NECESARIO PARA EJECUTAR EL SCRIPT>>>>")
time.sleep(1)
print("...")
os.system("pip install phonenumbers")
os.system("pip install colorama")
print("")
print("OPERACION COMPLETADA...")
time.sleep(0.2)
print("iniciando script...")
time.sleep(0.1)
os.system("clear")


print("""  _   _                       _                   
 | \ | |                     | |                  
 |  \| |  _   _   _ __ ___   | |__     ___   _ __ 
 | . ` | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
 | |\  | | |_| | | | | | | | | |_) | |  __/ | |   
 |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|
 
 
 """)
    


print("[1] Scanear numero telefonico")
print("[2] Informacion del creador")
print("[3] Salir")





opcion = input("Elije entre el [1-2-3] -> ")
if opcion == "1":
    num = input("Ingrese el numero de telefono -> ")
    numero = phonenumbers.parse(num)
    zona= timezone.time_zones_for_geographical_number(numero)
    region = geocoder.description_for_number(numero, 'en')
    Carr  = carrier.name_for_number(numero, 'en')
    valido = phonenumbers.is_valid_number(numero)
    if valido == True:
        print("Zona ->", zona)
        print("Carrier ->", Carr)
        print("Region ->", region)
    elif valido == False:
        print(Fore.RED + "El numero no existe")

elif opcion == "3":
        sys.exit()

elif opcion == "2":
    print("Hola, soy dylan no soy el dueño del script. solo le hice unas modificaciones")
    print(Fore.LIGHTGREEN_EX + "Instagram - @the_m.v_")       
else:
    print("""Esa opcion no existe
Saliendo del programa""")
