Create a Python virtual environment, then `pip install -r requirements.txt`.
Run `uvicorn app:app --host 127.0.0.1 --port 8000` from this folder and open http://127.0.0.1:8000.
Fish tracking: `python fish_tracking.py --weights YOUR_FISH_WEIGHTS.pt --video YOUR_VIDEO.mp4`.
Plant analysis: set GEMINI_API_KEY and GEMINI_MODEL in your local environment, then `python plant_health.py plant.jpg`. Calls can incur API charges. Never commit keys.
The serial firmware is a separate hardware example, not wired into the simulated WebSocket demo. Calibration and an authenticated ingestion bridge remain future work. No automatic actuation is implemented. Check Ultralytics licensing before distribution or deployment.
