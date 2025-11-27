#### Imports et définition des variables globales
"""
    Exercice de tuples
"""

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme itératif (Run-length encoding).

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences).

    Exemple:
        >>> artcode_i('MMMMaaacXolloMM')
        [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]
    """
    # votre code ici
    n = len(s)
    k = 0
    l = [s[0]]
    o = [0]
    while k < n:
        if s[k] == s[k-1]:
            o[-1] += 1
            k = k + 1
        else:
            l.append(s[k])
            o.append(1)
            k = k + 1
    return list(zip(l, o))


def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères 
    passée en argument selon un algorithme récursif.

    Cette fonction identifie le premier bloc de caractères identiques,
    crée un tuple, et s'appelle récursivement sur le reste de la chaîne.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences).

    Exemple:
        >>> artcode_r('MMMMaaacXolloMM')
        [('M', 4), ('a', 3), ('c', 1), ('X', 1), ('o', 1), ('l', 2), ('o', 1), ('M', 2)]
    """

    # votre code ici
    # cas de base
    if len(s) == 0:
        return []
    # recherche nombre de caractères identiques au premier
    n = len(s)
    l = s[0]
    k = 1
    while k < n and s[k] == l:
        k = k + 1
    return [(l, k)] + artcode_r(s[k:])


#### Fonction principale
def main():
    """
    Fonction principale permettant de tester les algorithmes d'encodage.
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
