from flask import Flask, jsonify
from prometheus_client import CollectorRegistry, generate_latest
import joblib
from report_generator import generate_report
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('failure_predictor.pkl')

@app.route('/network-status')
def get_status():
    # Simulate fetching metrics (replace with real data)
    cpu_load = 78.5  # Replace with actual CPU load
    packet_loss = 2.3  # Replace with actual packet loss
    
    # Predict failure
    input_data = pd.DataFrame([[cpu_load, packet_loss]], columns=['cpu_load', 'packet_loss'])
    failure = int(model.predict(input_data)[0])  # Convert to native Python int
    
    # Generate report
    metrics = {
        'cpu_load': cpu_load,
        'packet_loss': packet_loss,
        'failure': failure
    }
    report = generate_report(metrics)
    
    return jsonify({
        'metrics': metrics,
        'report': report
    })

if __name__ == '__main__':
    app.run(port=5000)