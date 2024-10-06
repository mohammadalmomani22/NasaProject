
# Planetary Seismic Data Detection and Visualization

## Project Overview
This project focuses on analyzing seismic data from planetary missions, specifically the Apollo 12 mission and the Mars InSight Lander. The goal is to preprocess the data, apply various machine learning algorithms, and visualize the seismic events to detect quakes amidst noisy data.

## Key Features
1. **Interactive Visualization Platform**: A website that visualizes 3D models of Mars and the Moon, with drop-down pins for user-selected periods showing seismic quakes.
2. **Data Preprocessing**: Includes cleaning, filtering, and resampling seismic data from CSV files.
3. **Machine Learning Models**: 
   - Isolation Forest for anomaly detection.
   - Time series analysis models (ARIMA, SARIMA, SARIMAX).
   - LSTM-AE (Autoencoder) for deep learning-based event detection.
4. **Signal Processing**: Includes filtering techniques like the Butterworth filter and STA/LTA for signal-to-noise ratio improvement.
5. **Results Visualization**: Plots and 2D diagrams representing detected seismic events, with details like location, strength, and cause.

## Tech Stack
- **Python**: For data processing, analysis, and machine learning.
- **Libraries**: NumPy, Pandas, ObsPy, SciPy, Statsmodels, Matplotlib, and PyTorch.
- **Machine Learning**: scikit-learn for Isolation Forest, and PyTorch for LSTM-AE.
- **PostgreSQL & Django**: Backend database and framework used for the interactive visualization website.
- **AngularJS**: For front-end web development and 3D visualization.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/planetary-seismic-detection.git
   cd planetary-seismic-detection
   ```

2. **Install Dependencies**:
   Make sure to install the necessary Python libraries listed in `requirements.txt`. You can do this using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**:
   Launch the Jupyter notebook and follow along with the steps for seismic data preprocessing and machine learning model applications.
   ```bash
   jupyter notebook mars.ipynb
   ```

4. **Launch the Web Visualization (Optional)**:
   If you want to explore the visualization platform, set up the backend using Django and PostgreSQL, and start the server:
   ```bash
   python manage.py runserver
   ```

## Data Sources
- Apollo 12 Seismic Data
- Mars InSight Lander SEIS Data

## License
This project is licensed under the MIT License. Feel free to use and modify the code as per your requirements.

## Contributions
We welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request.

## Contact
For any inquiries or support, please contact [your-email@example.com].

---

Thank you for exploring planetary seismology with us!
