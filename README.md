# Yoga Playlist Generator
AI-powered yoga video recommendations based on user-described concerns (for example: stress, anxiety, or neck tension).  
The app maps input text to yoga categories, then returns matching YouTube yoga videos.

## Tech Stack
- Frontend: HTML + Tailwind CSS
- Backend: Flask (Python)
- Data: CSV mapping files in `backend/`

## Project Structure
- `src/index.html` – UI and client-side fetch logic
- `src/input.css` – Tailwind input stylesheet
- `src/output.css` – generated Tailwind output
- `backend/app.py` – Flask server and recommendation API
- `backend/*.csv` – keyword/category/yoga-video mappings

## Prerequisites
- Node.js + npm
- Python 3
- Python virtual environment at `backend/.venv` with required packages installed (`flask`, `flask-cors`, `pandas`)

## Install
1. Install Node dependencies:
   - `npm install`
2. (If needed) create and activate Python virtual environment in `backend`, then install packages:
   - `pip install flask flask-cors pandas`

## Run Locally
- First Start backend : 
  - `cd backend`
  - `python -m venv venv`
- Activate Virtual Environment : 
  - `venv\Scripts\activate`
- To Run backend + Tailwind watcher together:
  - `npm run dev`
- Open:
  - `http://127.0.0.1:5000`

## API
- `POST /recommend`
- JSON body:
  - `{ "user_text": "your concern here" }`
- Returns an array of recommended yoga entries with video links.
