# AI Life OS

A personal dashboard that integrates health, productivity, and emotional wellness data to provide personalized insights and coaching.

## Features

- Google Fit data integration
- Health metrics visualization
- Sleep tracking
- Heart rate monitoring
- Calorie tracking
- Privacy-first approach

## Project Structure

```
ai-life-os/
├── backend/           # Data processing and storage
├── frontend/         # Streamlit dashboard
└── data/            # Sample data and exports
```

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-life-os.git
cd ai-life-os
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the dashboard:
```bash
streamlit run frontend/app.py
```

## Development

- Backend: Python
- Frontend: Streamlit
- Data Storage: Local JSON (encrypted storage coming soon)

## License

Open Source - Privacy First
