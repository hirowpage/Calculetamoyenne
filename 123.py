def main():
    print("Bonjour a toi,ceci vas t'aidez a calculer ta moyenne")
    print("(Merci de saisir seulement des nombres entier)")
    #recolter les notes
    note1= int(input("Inserez votre note:"))
    note2= int(input("Inserez votre note:"))
    note3= int(input("Inserez votre note:"))
    note4= int(input("Inserez votre note:"))
    note5= int(input("Inserez votre note:"))
    result= (note1 + note2 + note3 + note4 + note5)/5
    #afficher le resultat
    print("Votre moyenne est de:" + str(result) +"/20")
    if result <= 9:
        print("Votre Moyenne n'est pas assez elever,il faut fournir plus d'efforts")
        if result == 10:
            print("Vous avez tous juste la moyenne il faut plus s'invertire dans son travail vous pouvez mieux faire ")
    else:
          print("Vous avez la moyenne continuer ainsi")

if __name__ == '__main__':
 main()