

## Tech Stack

- Python
- Streamlit
- RDKit
- scikit-learn
- pandas, numpy
## How Prediction Works

1. User enters a SMILES string.
2. RDKit parses the molecule.
3. Molecular descriptors are computed in app.py.
4. Descriptor values are arranged using feature_columns.pkl.
5. The model in best_model.pkl predicts class and probability.


