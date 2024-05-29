import joblib
import os
import pandas as pd

from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_regression, f_classif, chi2
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def save_model_if_best(new_score, pipeline, model_name):
    # joblib model only, could add a param joblib/pickle options
    files = os.listdir('app/app_model')
    previously_used_models = []

    if files:
        for f in files:
            previously_used_models.append(f.split('_')[1])
            if model_name == f.split('_')[1] and int(f.split('_')[0]) > new_score:
                joblib.dump(pipeline, f"app/app_model/{new_score}_{model_name}_model.pkl")
                print(new_score)
                # could be moved to a backup dir instead of deleting it
                os.remove(f"app/app_model/{f}")
                return True

            # if we arrive there it means score was too low or the model of this name haven't been saved yet.
            # if a new model algorythm is used we save it.
        if  model_name not in previously_used_models:
            print('new model ran')
            joblib.dump(pipeline, f"app/app_model/{new_score}_{model_name}_model.pkl")
    # if no model has been saved yet save it.
    else:
        print('first saved model')
        joblib.dump(pipeline, f"app/app_model/{new_score}_{model_name}_model.pkl")

def load_best_model(model_name=False, path='app/app_model/'):
    # joblib model only, could add a param joblib/pickle options
    files = os.listdir(path)
    score_dict = {}

    if files:
        for f in files:
            if f.split('_')[1] == model_name:
                return joblib.load(f"{path}{int(f.split('_')[0])}_{f.split('_')[1]}_model.pkl")
            else :
                score_dict[f.split('_')[1]] = int(f.split('_')[0])

        return joblib.load(f"{path}{score_dict[min(score_dict, key=score_dict.get)]}_{min(score_dict, key=score_dict.get)}_model.pkl")


# price_column is a str name of the numeric column
def iqr_range_price_filter(df, price_column):
    q3 = df.price.describe()['75%']
    q1 = df.price.describe()['25%']
    iqr_range = q3-q1
    new_df = df[(df[price_column] > q1-iqr_range*1.5) & (df[price_column] < q3+(iqr_range*1.5))]
    print("old number of rows", df.shape[0])
    print("new number of rows", new_df.shape[0])
    return new_df


def variance_threshold_selector(data, threshold=0.2):
    selector = VarianceThreshold(threshold)
    selector.fit(data)
    new_df = data[data.columns[selector.get_support(indices=True)]]
    dropped_features = [feature for feature in data.columns if feature not in new_df.columns]
    if dropped_features:
        print('columns dropped :', dropped_features)
    else :
        print('no features dropped')
    return new_df

# k is number of feature to keep
def KBest_selector(data, target_name, k=1, score_function = 'f_regression'):
    # Create and fit selector
    if score_function == 'f_regression':
        selector = SelectKBest(f_regression, k=k)
    elif score_function == 'f_classif':
        selector = SelectKBest(f_classif, k=k)
    else :
        selector = SelectKBest(chi2, k=k)
        print('using chi2')

    selector.fit(data.drop(columns=[target_name]), data[target_name])
    # Get columns to keep and create new dataframe with those only
    cols_idxs = selector.get_support(indices=True)
    new_df = data.iloc[:,cols_idxs]

    # display the names of dropped columns
    dropped_features = [feature for feature in data.columns if feature not in new_df.columns]
    dropped_features.remove(target_name)
    if dropped_features:
        print('columns dropped :', dropped_features)
    else :
        print('no features dropped')

    pd.options.mode.chained_assignment = None
    new_df.loc[:, target_name] = data[target_name].copy()
    pd.options.mode.chained_assignment = 'warn'
    return new_df


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


# Create a Countplot of the distribution of a numerical serie based on given bin ranges
# Bins must be a list of at least 2 numbers
def countplot_with_bins(serie, bins_list, plt_title="Distribution", plt_label="", fig_size=(12,7)):
    serie = abs(serie)

    classes = [f"Under {bins_list[0]}"]
    for i in range(len(bins_list) - 1):
        classes.append(f"Between {bins_list[i]} and {bins_list[i+1]}")
    classes.append(f"Above {bins_list[-1]}")

    residuals_class = pd.cut(serie, bins=[-float('inf')] + bins_list + [float('inf')], labels=classes)

    plt.figure(figsize=fig_size)
    ax = sns.countplot(x=residuals_class)
    plt.title(plt_title)
    if plt_label:
        plt.xlabel(plt_label)
    else :
        plt.xlabel('Classes')
    plt.xlabel('Residuals Class')
    plt.ylabel('Count')

    # Add percentage annotations
    total = len(residuals_class)
    for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height() / total)
        x = p.get_x() + p.get_width() / 2
        y = p.get_height()
        ax.annotate(percentage, (x, y), ha='center', va='bottom')

    plt.show()
