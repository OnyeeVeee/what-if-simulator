import pickle

with open("models/random_forest_model.pkl", "rb") as f:
    model = pickle.load(f)

print("Loaded successfully")