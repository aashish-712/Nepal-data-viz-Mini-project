# 🇳🇵 Nepal Data Visualization

An interactive geospatial dashboard built with Python, Streamlit, Pandas, and Plotly to explore and visualize district-level data across Nepal. Users can select a province and compare different data parameters through an interactive map.

## ✨ Features

- 🗺️ **Interactive Map:** Explore geographical data across Nepal.
- 📍 **Province Filtering:** View data for Overall Nepal or a selected province.
- 📊 **Dynamic Parameters:** Choose primary and secondary parameters.
- 🔵 **Bubble Size:** Marker size represents the primary parameter.
- 🌈 **Color Mapping:** Marker color represents the secondary parameter using the Turbo color scale.
- 🔎 **Interactive Exploration:** Hover over markers to view district names.
- 💻 **Streamlit Dashboard:** Simple sidebar controls and a wide visualization layout.

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Streamlit
- Plotly Express

## 📂 Project Structure

```text
Nepal-Data-Visualization/
│
├── app.py
├── Nepal_df.csv
├── requirements.txt
└── README.md
```

*Replace `app.py` with your actual Python script filename if it differs.*

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd Nepal-Data-Visualization
```

Replace `YOUR_REPOSITORY_URL` with your GitHub repository URL.

### 2. Install Dependencies

Install the required Python libraries using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

The dashboard will open in your browser, usually at:

`http://localhost:8501`

## 📈 How to Use

1. Open the dashboard.
2. Select **Overall Nepal** or a province from the sidebar.
3. Select a primary parameter to control marker size.
4. Select a secondary parameter to control marker color.
5. Click **Plot Graph** to generate the map.
6. Hover over the markers to explore district names.

## 🗺️ Map Details

| Component | Description |
|---|---|
| Location | Latitude and longitude |
| Marker size | Primary parameter |
| Marker color | Secondary parameter |
| Hover information | District name |
| Color scale | Turbo |
| Map style | Carto Positron |
| Initial center | 28.4° N, 84.1° E |

## 📁 Dataset

The dashboard loads its data from `Nepal_df.csv`.

Expected columns include:

- `State` — Province name
- `District` — District name
- `Latitude` — Geographic latitude
- `Longitude` — Geographic longitude
- Additional numerical columns — Parameters available for visualization

The dataset must be placed in the project directory. The selected parameters should contain valid numerical values suitable for the map's marker sizes and colors.

## 🎯 Project Objectives

- Practice data analysis and visualization with Python.
- Explore geographical and district-level data from Nepal.
- Build interactive dashboards using Streamlit.
- Compare multiple parameters through geospatial visualization.
- Strengthen practical data science skills.

## 🔮 Future Improvements

- Add district search functionality.
- Display summary statistics for selected provinces.
- Add charts comparing different provinces.
- Enable filtered dataset downloads.
- Deploy the dashboard online.
- Improve the dashboard's mobile experience.

## 👨‍💻 Author

**Aashish Bhandari**

BSc CSIT Student | Aspiring AI/ML Engineer

Interested in Python, Data Science, Machine Learning, and interactive data visualization.

---

My linkdlen profile : www.linkedin.com/in/aashishb712

⭐ If you find this project interesting, consider giving the repository a star!

*Built with Python to explore Nepal's data, one district at a time.* 🇳🇵
