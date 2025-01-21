# Steps

1. Create a virtual environment:
   ```bash
   python -m venv network-ai
   source network-ai/bin/activate
   ```

2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the Model:
   ```bash
   python ai/train_model.py
   ```

4. Start Prometheus Exporter:
   ```bash
   python ai/prometheus_exporter.py
   ```

5. Run the Flask API with Gunicorn:
   ```bash
   gunicorn --workers 4 --bind 0.0.0.0:5000 ai.app:app
   ```

6. Test the API:
   Visit the following URL in your browser or use a tool like `curl`:
   ```
   http://localhost:5000/network-status
   ```

---

# File System

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