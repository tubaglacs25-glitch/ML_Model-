import streamlit as st
import pandas as pd
import pickle
from rdkit import Chem
from rdkit.Chem import Descriptors
from sklearn.preprocessing import StandardScaler

st.title("🧬 Sertraline Activity Predictor")
st.write("Predict molecular activities for cancer chemosensitization")

model = pickle.load(open('best_model.pkl', 'rb'))
features = pickle.load(open('feature_columns.pkl', 'rb'))
def get_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return {
        'MolWt': Descriptors.MolWt(mol),
        'LogP': Descriptors.MolLogP(mol),
        'NumHDonors': Descriptors.NumHDonors(mol),
        'NumHAcceptors': Descriptors.NumHAcceptors(mol),
        'NumRotatableBonds': Descriptors.NumRotatableBonds(mol),
        'TPSA': Descriptors.TPSA(mol),
        'NumAromaticRings': Descriptors.NumAromaticRings(mol),
        'NumAliphaticRings': Descriptors.NumAliphaticRings(mol),
        'NumHeavyAtoms': Descriptors.HeavyAtomCount(mol),
        'RingCount': Descriptors.RingCount(mol),
        'FractionCsp3': Descriptors.FractionCSP3(mol),
        'MolMR': Descriptors.MolMR(mol),
        'BertzCT': Descriptors.BertzCT(mol),
        'Chi0v': Descriptors.Chi0v(mol),
        'Chi1v': Descriptors.Chi1v(mol),
        'Kappa1': Descriptors.Kappa1(mol),
        'Kappa2': Descriptors.Kappa2(mol),
        'Kappa3': Descriptors.Kappa3(mol),
        'NumSaturatedRings': Descriptors.NumSaturatedRings(mol),
        'MaxPartialCharge': Descriptors.MaxPartialCharge(mol),
        'MinPartialCharge': Descriptors.MinPartialCharge(mol)
    }

if model and features:
    st.write("---")
    
    st.subheader("Enter SMILES String")
    smiles = st.text_input("SMILES:", placeholder="e.g., CCO or CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
    
    if smiles:
        descriptors = get_descriptors(smiles)
        
        if descriptors is None:
            st.error("❌ Invalid SMILES string. Please check and try again.")
        else:
            st.success("✅ Valid SMILES! Descriptors extracted.")
            
            with st.expander("View Extracted Descriptors"):
                scaler = StandardScaler()
                desc_df = pd.DataFrame([descriptors], columns=features)
                st.dataframe(desc_df)
            
            if st.button("Predict from SMILES"):
                
                prediction = model.predict(desc_df)[0]
                probability = model.predict_proba(desc_df)[0]
                
                if prediction == 1:
                    st.success(f"✅ POSITIVE - Probability: {probability[1]:.2%}")
                    st.write("The compound shows sertraline-like activity")
                else:
                    st.error(f"❌ NEGATIVE - Probability: {probability[1]:.2%}")
                    st.write("The compound does not show sertraline-like activity")
    
    st.write("---")