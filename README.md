
UMAP Analysis
==============================

Ever wanted to directly cluster on the output of UMAP, but felt too guilty too try it?

Ever wanted to say "look, those clusters are obviously distinct, they're seperated on the UMAP plot!"

Now, you too can use UMAP in your downstream analysis to you hearts' content, without having to throw away huge amounts of information in the process of making a 2D representation of your data.

UMAP analysis makes a similarity network for you data that using UMAP as a feature selection/manifold learning tool (these two concepts are much more closely linked than they seem!).

Then you can use alll the tools of network science to further analyse your data!

To get started download or pull this github page, navigate into the directory and:
```bash
pip install -r requirements.txt
pip install .
```

Then get your data into the necessary format, a pandas dataframe with an index representing the names of your datapoints that will become the names for their representative nodes for the network.

If you don't like pandas and prefer raw numpy arrays, you can fix this is a couple of lines, like this:

```python
import pandas as pd
df = pd.DataFrame(yourArray, index = yourDataPointsName)
```

Now the interesting step:

```python
from UMAP_analysis import umap_network
G = umap_network(df, 5)
```

the second argument is the out-degree of nodes in your network

G will be a networkx network representing the similarity between the datapoints.This step might take a minute or so. My dataframe with 10,000 rows and 20 columns takes a couple of minutes.

After this, play around with the resulting network.


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
=======
# UMAPanalysis
Do data analysis, but with networks instead

