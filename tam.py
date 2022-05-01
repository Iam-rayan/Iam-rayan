

from tkinter import *
import nmap
import os




global sc
sc = nmap.PortScanner()

def nmap():
    sc.scan(input_ip, '1-6')
    if scan_port:
        sc




"""def main():
    input_ip = Entry(frame, font=("arial", 20), bg='#637671', fg='#fefefe')
    input_ip.pack(expand=YES)
    scan_A = Button(frame, text="Scan aggressif", font=("Arial", 15), bg='#5b6a66', fg='#fefefe')
    scan_A.pack(pady=70, fill=X)
    
    scan_port = Button(frame, text="Scan de tous les port", command=nmap, font=("Arial", 15), bg='#5b6a66', fg='#fefefe' )
    scan_port.pack(fill=X) """





##############################################################

# creer une fenetre
fenetre = Tk()



# personnaliser la fenetre
fenetre.title("Mes outils")
fenetre.geometry("1080x720")
fenetre.minsize(480, 360)
fenetre.iconbitmap("pp.ico")
fenetre.config(background='#637671')

# la frame
frame = Frame(fenetre, bg='#637671')


#1er text
label_title = Label(fenetre, text="Bienvenue sur ton application garçon", font=("arial", 40), bg='#637671', fg='#fefefe', bd=1, relief=SUNKEN)
label_title.pack()


# text de choix
label_choix = Label(frame, text="Entrez votre addresse IP", font=("arial", 20), bg='#637671', fg='#fefefe')
label_choix.pack(expand=YES)




# input
input_ip = Entry(frame, font=("arial", 20), bg='#637671', fg='#fefefe')
input_ip.pack(expand=YES)




# boutton de scan -A
scan_A = Button(frame, text="Scan aggressif", font=("Arial", 15), bg='#5b6a66', fg='#fefefe')
scan_A.pack(pady=70, fill=X)

# ajouter un boutton
scan_port = Button(frame, text="Scan de tous les port", command=nmap, font=("Arial", 15), bg='#5b6a66', fg='#fefefe' )
scan_port.pack(fill=X)




# ajouter
frame.pack(expand=YES)

# afficher
fenetre.mainloop()


