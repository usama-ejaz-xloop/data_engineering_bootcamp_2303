import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt


def get_feature_names(pipeline, all_feature_names):
    fs_name = "sequentialfeatureselector"
    if fs_name in pipeline.named_steps.keys():
        mangled_fnames = pipeline.named_steps[fs_name].get_feature_names_out()
        fname_indices = [int(fname.replace("x", "")) for fname in mangled_fnames]
        return all_feature_names[fname_indices]
    else:
        return all_feature_names


def show_linear_model_importances(clf_pipeline, all_feature_names, max_num_features):
    __, model = clf_pipeline.steps[-1]
    importances = model.coef_[0]
    feature_names = get_feature_names(clf_pipeline, all_feature_names)
    pd.Series(importances, index=feature_names).sort_values(
        ascending=False, key=abs
    ).iloc[:10][::-1].plot.barh()
    plt.show()


def show_model_results(name, clf_pipeline, X_test, y_test, digits, max_num_features):

    y_pred = clf_pipeline.predict(X_test)
    y_pred_proba = clf_pipeline.predict_proba(X_test)[:, 1]
    print("#" * 50)
    print(name)
    print(metrics.classification_report(y_test, y_pred, digits=3))

    print(
        "ROC AUC:",
        metrics.roc_auc_score(y_test, y_pred_proba),
    )
    show_linear_model_importances(name, clf_pipeline, X_test, max_num_features)
