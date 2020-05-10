# PyMaths (Projet en cours)
Modélisation de concepts mathématiques et raisonnements sur ces derniers.

# Introduction
Pendant mes années de CPGE, je me suis intéressé à la modélisation des concepts mathématiques et logiques en informatique. J'ai alors commencé l'apprentissage de la manipulation de certains logiciels de formalisation de preuves (Coq et Isabelle). 

**Problématique :** Est-il envisageable d'implémenter un système similaire en **Python**, me donnant l'occasion de comprendre plus en détail le fonctionnement d'un assistant de preuve? Bien entendu, je n'avais pas pour projet d'implémenter un tel sysème en entier, je souhaitais seulement en implémenter les bases, comme la définition des types.

# Cheminement
PyMaths est un projet assez récent, et encore en cours de réflexion. Je ne peux donc présenter que le début de mon cheminement et des résultats que j'ai obtenus.

J'ai commencé par ce que je pense être l'objet de base : l'object **`Type`**. Cet object est représenté par une chaîne de caractères (comme par exemple `int * int -> float -> ()`, comme en **Ocaml**).

La classe `Type` comporte différente méthodes pour combiner et créer des types secondaires (comme les méthodes `combine` et `function`)

Puis, j'ai créé un type `Object`, duquel tous les objets devrait hériter. Il permet pour l'instant d'instancier des objets avec un type et, éventuellement, une valeur. Il comporte également une méthode pour transformer une liste d'objets en un objet tuple, comportant notamment le bon type.

Enfin, j'ai créé les classes `Set` et `Function`, pour représenter les objets **Ensemble** et **Fonction**.

Avec des classes de base, j'ai pu créer une formalisation de la fonction **`+`** sur **|N**, qui s'opère sur un tuple de type **`int * int`** (et renvoie une erreur sinon) et qui renvoie un objet de type **`int`** dont la valeur est l'addition des valeurs du tuple : 

```
a = Object(type = intType, value = 1)
b = Object(type = intType, value = 2)
c = Object.tuple([a, b])

IntTupleType = ObjectType.combine([intType, intType])

add = Function(setIn = Set.cartesien(N_Set, N_Set), setOut = N_Set, typeIn = IntTupleType, typeOut = intType, functionValue = lambda a, b: a + b)

d = add(c) #On applique add sur le tuple c = (a, b)
print(d.value)
```

# Pistes pour le futur
Premièrement, je pense qu'il serait déjà une bonne idée que je règle un problème qui s'est posé sur les ensembles : j'ai supposé qu'on peut définir certaisn ensembles par, notamment, une fonction (comme la fonction `Succ` pour **|N**). Pourtant, le constructeur de la classe `Function` prend en argument les ensembles de départ et d'arrivée. Or l'ensemble de départ ne peut être construit qu'avec la fonction donnée. Il me faut donc trouver une solution sur ce point.

Deuxièmement, je suis encore très loin d'une implémentation capable de gérer des types récursifs (comme le type `nat` dans le logiciel **Coq**). Je suppose qu'il faudra entièrement créer une structure récursive, étant donné que Python ne gère pas nativement ce genre de types (contrairement à **Ocaml**, par exemple).
