# Projet La plateforme - apartment-hunter

Projet sur le Deep Learning & MLFlow réalisé par :
```Ruta Tamosiunaite```

```Aurélien Papillon```

```Julien Ract-Mugnerot```

## Notes importantes à l'appréciation du projets :

- Lien du Trello : https://trello.com/b/wJFkiK3o/waterflow-highline-team
-

### Présentation :

-

## Explication du projet

Développement d'un outil visant à estimer la qualité de l'eau.


## Data exploration:

### Feature analysis

## Veille technique

$\min_{\theta} \left( ||Y - X\theta||^2 + \lambda||\theta|| \right)$

### Evaluating the model's performance:


## Feature Selection

#### `(VarianceThreshold, SelectKBest, Boruta, Forward feature selection, VIF)`


## Deep Learning

### With a Single feature

| **Model** | Baseline| Linear | Decision Tree R | Ridge |
|-----------------|-----------------|-----------------|-----------------|-----------------|
| **RMSE**  | 161756 | 102003 | 163420 | ```159645``` |
| **R2** | X | ````0.37```` | 0.4067 | 0.3691  |


### With multiple features and Grid Search

| **Model** | Baseline| Linear | Decision Tree R | Ridge | ElasticNet | SVR | KNN Regressor | XGBoost |
|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| **RMSE**  | 161756 | 160665.2 | 156118 | 105344 | 102667 | 107301 | ```96308``` | 96361 |
| **R2** | X | 0.7512 | 0.3586 | 0.7320 | 0.7465 | 0.7108 | ```0.7636``` | 0.7571 |


##  Conclusion

### Pistes d'amélioration du projet
