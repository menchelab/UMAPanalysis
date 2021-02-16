import pandas as pd
import numpy as np


X_unclassified = pd.read_csv("data/raw/lish-moa/test_features.csv", index_col = 0)
X_classified = pd.read_csv("data/raw/lish-moa/train_features.csv", index_col = 0)
X_classified = X_classified[~X_classified.isna().any(axis = 1)] 
X= pd.concat([X_classified, X_unclassified])


y_classified = pd.read_csv("data/raw/lish-moa/train_targets_scored.csv", index_col = 0)
MoAs = y_classified.columns
known = pd.Series({i:1 for i in y_classified.index})


y_unclassified = np.zeros((len(X_unclassified.index), len(MoAs)))
y_unclassified = pd.DataFrame(y_unclassified)
y_unclassified.columns = MoAs
y_unclassified.index= X_unclassified.index
temp = pd.Series({i:0 for i in y_unclassified.index})
known  = pd.concat([known, temp])
y = pd.concat([y_classified, y_unclassified]);


metadata_columns = ["cp_type", "cp_time", "cp_dose"]
metadata = X[metadata_columns]
metadata["known"] = known


features = X[[i for i in X.columns if i not in metadata_columns]]
features_unscaled = features.copy()
features = features_unscaled / features_unscaled.std(axis = 0)


features.to_csv("data/intermediate/lish-moa/features.csv")
features_unscaled.to_csv("data/intermediate/lish-moa/features_unscaled.csv")
metadata.to_csv("data/intermediate/lish-moa/metadata.csv")
y.to_csv("data/intermediate/lish-moa/labels.csv")


