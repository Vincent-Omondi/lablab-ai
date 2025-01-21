
# Network AI Predictive Maintenance System

This program is a predictive maintenance system designed to monitor and analyze network health using machine learning and real-time metrics. It consists of a Flask API for serving predictions, a Prometheus exporter for collecting network metrics, and a model training script for predictive maintenance. The system generates reports and provides insights into network status, helping to identify potential issues before they escalate.

## Key Features
- **Flask API**: Serves predictions and network status reports.
- **Prometheus Exporter**: Collects and exposes network metrics for monitoring.
- **Model Training**: Trains a machine learning model for predictive maintenance.
- **Report Generation**: Uses Hugging Face for generating text-based reports.
- **Scalable Deployment**: Uses Gunicorn for running the Flask API in production.

## How It Works
1. **Setup**: Create a virtual environment and install dependencies.
2. **Training**: Train the predictive maintenance model using historical data.
3. **Monitoring**: Start the Prometheus exporter to collect real-time network metrics.
4. **API**: Run the Flask API to serve predictions and reports.
5. **Testing**: Query the API to retrieve network status and predictions.

## Getting Started

### Prerequisites
- Python 3.x
- `pip` for installing dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Vincent-Omondi/lablab-ai.git
   cd lablab-ai
   ```
2. Create a virtual environment:
   ```bash
   python -m venv network-ai
   source network-ai/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Train the model:
   ```bash
   python ai/train_model.py
   ```
2. Start the Prometheus exporter:
   ```bash
   python ai/prometheus_exporter.py
   ```
3. Run the Flask API:
   ```bash
   gunicorn --workers 4 --bind 0.0.0.0:5000 ai.app:app
   ```
4. Test the API:
   Visit `http://localhost:5000/network-status` in your browser or use a tool like `curl`.

## File Structure
```
ai/
├── app.py                  # Flask API for serving predictions and reports
├── prometheus.yml          # Prometheus configuration file
├── prometheus_exporter.py  # Script to collect and expose network metrics
├── report_generator.py     # Text report generation using Hugging Face
├── requirements.txt        # Python dependencies
├── train_model.py          # Script to train the predictive maintenance model
└── network-ai/             # Virtual environment (auto-generated)
    ├── bin/
    ├── include/
    ├── lib/
    ├── lib64 -> lib/
    ├── pyvenv.cfg
    └── share/
```

## Related Projects
- **Clove**: A related project for AI-driven network analysis. Check out the repository [here](https://github.com/Vincent-Omondi/lablab-ai.git).

