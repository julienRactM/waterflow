# Projet La plateforme - apartment-hunter

Projet sur le Deep Learning & MLFlow réalisé par :

```Ruta Tamosiunaite```

```Aurélien Papillon```

```Julien Ract-Mugnerot```

## Notes importantes à l'appréciation du projets :

- Lien du Trello : https://trello.com/b/wJFkiK3o/waterflow-highline-team
- Pour lancer mlflow : mlflow server --host 127.0.0.1 --port 5000
- Instructions our appeller l'api :
python script.py ph(float range[0-14]) Hardness(float range[0-100])  Solids(float range[0-1000]) Chloramines(float range[0-10]) Sulfate(float range[0-500]) Conductivity(float range[0-100]) Organic_carbon(float range[0-50]) Trihalomethanes(float range[0-200]) Turbidity(float range[0-10])
ex : python script.py 7.5 50 500 5 250 50 25 100 5

### Présentation :

-

## Explication du projet

Développement d'un outil visant à estimer la qualité de l'eau.

The original dataset contains the records of water acceptability reflected by metrics like chemically derived contaminants:
- `ph` - evaluates the acid–base balance of water. WHO recommendation limit of pH: from 6.5 to 8.5
- `Hardness`
- `Solids`
- `Chloramines`
- `Sulfate`
- `Conductivity` - or in other words - total dissolved solids, WHO reccommended to be less than 600 mg/l, but no health-based guideline value has been proposed https://iris.who.int/bitstream/handle/10665/352532/9789240045064-eng.pdf?sequence=1&isAllowed=y#page=29
- `Organic_carbon`
- `Trihalomethanes`
- `Turbidity`

The resulting feature defining drinking water acceptability is:
- `Potability` Boolean variable
0 for **not** potable water and
1 for potable water

## Data exploration:

Le Dataset est en réalité inexploitable, étant généré artificiellement.

### Feature analysis

Les Features n'impactent réellement que très peu le caractère potable de l'eau

## Veille technique





## Feature Selection

#### `(VarianceThreshold, SelectKBest, Boruta, Forward feature selection, VIF)`


## Deep Learning

### Evaluating the model's performance:
Peak à 68% d'accuracy


##  Conclusion

### Pistes d'amélioration du projet
