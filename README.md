 Sertraline Activity Predictor

This project is a Streamlit web app that predicts whether a compound shows sertraline-like activity for cancer chemosensitization, based on a SMILES string input.

The app uses RDKit to calculate molecular descriptors, then runs inference using a pre-trained scikit-learn classification model.

## Features

- SMILES input validation using RDKit
- Automatic descriptor extraction from valid molecules
- Binary prediction: POSITIVE or NEGATIVE
- Class probability output
- Streamlit UI for quick interactive testing

## Project Structure

- app.py: Streamlit application
- best_model.pkl: Trained classification model used for prediction
- feature_columns.pkl: Ordered feature list expected by the model
- scaler.pkl: Saved scaler artifact from training workflow
- modelDevelopment.ipynb: Model development and experimentation notebook
- bixuchenggong11.CSV: Dataset file
- requirements.txt: Local Python dependencies
- requirements-docker.txt: Docker-specific Python dependencies
- Dockerfile: Container build instructions

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

## Example SMILES

- Ethanol: CCO
- Caffeine: CN1C=NC2=C1C(=O)N(C(=O)N2C)C

## Notes

- Ensure best_model.pkl and feature_columns.pkl are present in the same directory as app.py.
- The app currently uses direct descriptor values for inference.
- scaler.pkl is included as a training artifact and may be useful if preprocessing is reintroduced in inference.

## License

This project is for academic and research use.

