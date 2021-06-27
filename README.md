# Mémoire Pipelinée - Ordenancement d'accès mémoire
**Version 1.0**

Simulation d'ordenancement d'accès mémoire de fonctions sur bancs mémoire et calcul de temps de simulation en CLI


## Requis
- Python 3+

## Dépendances
- Modules python `sys`

## Utilisation
Télécharger le projet, et ouvrir le dossier en invite de commande
```shell
py memoirepipeline.py [nb_bancs] [tps_exec] [nb_iter] [coef2,coef1,...] [pst_init1,pst_init2,...]
```
`nb_bancs`                : Nombre de bancs de mémoire total utilisés *(ex: 4)*

`tps_exec`                : Temps d'exécution d'une instruction accès mémoire *(ex: 4)*

`nb_iter`                 : Nombre d'itérations des fonctions *(ex: 1000)*

`coef1,coef2,...`         : Coefficients itératifs de chaque variable, séparés par des espaces, sous la forme *n***i**[+n] *(ex: 2i+1,3i,i+2)*

`pst_init1,pst_init2,...` : Numéro du banc mémoire d'origine de chaque variable d'accès mémoire *(ex: 0,1,2)*


## Exemple d'utilisation
Pour l'énoncé suivant :
```c
// On dispose d’une mémoire organisée en 4 bancs, numérotés de 0 à 3 (chacun de cycle 4T) et fonctionnant en mode pipeline (i.e. capable de fournir en régime maximal un mot à chaque T). On considère le code suivant :
for (i=0 ; i < 1000 ; i++)
    f(A[i],B[2*i+1],C[2*i]);
```
On aura la commande suivante pour les positions initiales A en banc 0, B et C en banc 1 :
```shell
py memoirepipeline.py 4 4 1000 i,2i+1,2i 0,1,1
```
Output : 
![Exemple d'utilisation](https://github.com/fm16191/memoirepipeline/blob/main/usage.png?raw=true)