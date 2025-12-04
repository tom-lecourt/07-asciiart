#### Imports et définition des variables globales
'''
Main.py ASCIIART
'''
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    c = s[0]
    compt = 1
    listeF = []
    for elem in s[1:]:
        if c == elem:
            compt += 1
        else:
            listeF.append((c, compt))
            c = elem
            compt = 1
    listeF.append((c, compt))
    return listeF

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères
    passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if len(s) == 0:
        return []
    
    s_cour = s[0]
    compt = 1
    
    for elem in s[1:]:
        if elem == s_cour:
            compt += 1
        else:
            break 
            
    return [(s_cour, compt)] + artcode_r(s[compt:])
#### Fonction principale

def main():
    '''
    Fonction principale
    '''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
