import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Sample dataset
data = {
    'cpu_load': [78, 45, 92, 31, 88, 50, 95, 30],
    'packet_loss': [2.1, 0.5, 4.8, 1.2, 3.5, 0.9, 5.0, 1.0],
    'failure': [1, 0, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df[['cpu_load', 'packet_loss']], 
    df['failure'], 
    test_size=0.2
)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'failure_predictor.pkl')
print("Model trained and saved to 'failure_predictor.pkl'")