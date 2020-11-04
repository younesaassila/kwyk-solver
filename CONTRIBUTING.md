# Contribuer au projet Kwyk Solver

Vous avez la possibilité de contribuer au projet en rapportant un bug, en suggérant une nouvelle fonctionnalité ou en ajoutant le support d'un exercice.

Pour contribuer au projet, vous devez avoir installé le module `pipenv`.
Celui-ci permet d'enregistrer les dépendances du programme dans le fichier
`Pipfile.lock`. Ce fichier facilite le développement de Kwyk Solver.

Pour plus d'informations sur `pipenv` rendez-vous à
[https://github.com/pypa/pipenv](https://github.com/pypa/pipenv).

## Rapporter un bug ou suggérer une nouvelle fonctionnalité

Pour rapporter un bug ou suggérer une nouvelle fonctionnalité, veuillez vous rendre dans [l'onglet "Issues" et cliquer sur le bouton "New issue"](https://github.com/younesaassila/Kwyk-Solver/issues/new/choose).

## Ajouter le support d'un exercice

Pour ajouter le support d'un exercice, vous aurez besoin d'effectuer un fork du projet Kwyk Solver puis de proposer vos améliorations à l'aide d'une pull request.

Pour plus d'informations sur le fonctionnement de Git et de GitHub, nous vous recommandons [la playlist YouTube dédiée à ces sujets sur la chaîne YouTube "The Coding Train" (anglais)](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6ZF9C0YMKuns9sLDzK6zoiV).

Pour ajouter le support d'un exercice, veuillez :

- Ajouter un fichier dans le dossier `kwyk-solver/solvers/` nommé `solver_`_numéro de l'exercice_`.py`,
- Importer dans ce fichier les modules nécessaires à sa conception (évitez néanmoins d'ajouter de nouvelles dépendances au programme),
- Créer une fonction `solve()` dans ce fichier à la suite de ces importations. Celle-ci contient toute la logique du solveur (récupération de données avec `input()`, traitement des données, affichage des résultats de l'exercice avec `print()`).
