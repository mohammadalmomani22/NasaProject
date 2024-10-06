
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
   git clone [https://github.com/your-username/planetary-seismic-detection.git](https://github.com/mohammadalmomani22/NasaProject.git)
   cd Mars-detection
   ```

2. **Run the Jupyter Notebook**:
   Launch the Jupyter notebook and follow along with the steps for seismic data preprocessing and machine learning model applications.
   ```bash
   jupyter notebook mars.ipynb
   ```

## Data Sources
- Apollo 12 Seismic Data
- Mars InSight Lander SEIS Data

## License
This project is licensed under the MIT License. Feel free to use and modify the code as per your requirements.

## Contributions
We welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request.

## Contact
For any inquiries or support, please contact majedaaljunaidy@gmail.com.

---

Thank you for exploring planetary seismology with us!
