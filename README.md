# Student Performance Prediction

![UI Preview](path/to/your/image.png) <!-- Replace with the actual path to your UI image -->

## Overview

This project aims to predict student performance using machine learning techniques. The workflow includes data ingestion, preprocessing, model training, and deployment of the prediction application. 

## Project Structure

```
.
├── .ebextensions
├── artifacts
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── data.csv
├── data
│   ├── test.csv
│   └── train.csv
├── notebooks
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
├── src
│   ├── components
│   │   ├── Data_ingestion.py
│   │   ├── Data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline
│   │   ├── predict_pipeline.py
│   │   ├── train_pipeline.py
│   │   └── __init__.py
│   ├── exception.py
│   ├── logger.py
│   ├── utils.py
│   └── __init__.py
├── templates
│   ├── home.html
│   └── index.html
├── .gitignore
├── README.md
├── app.py
├── application.py
├── requirements.txt
└── setup.py
```

## Getting Started

### Prerequisites

- Python 3.x
- pip
- [Anaconda](https://www.anaconda.com/products/distribution) (recommended for managing packages)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-performance-prediction.git
   cd student-performance-prediction
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env_name
   source env_name/bin/activate  # On Windows use `env_name\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Data Ingestion**: 
   The application starts by ingesting data from the `data` folder. The script `Data_ingestion.py` handles this process.

2. **Data Transformation**: 
   The data is then preprocessed using `Data_transformation.py`, which handles cleaning and feature engineering.

3. **Model Training**: 
   Train the model using the script `model_trainer.py`. This will generate the trained model and preprocessor, saved as `model.pkl` and `preprocessor.pkl` in the `artifacts` directory.

4. **Running the Flask App**:
   Start the application by running:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

### Workflow

1. **Exploratory Data Analysis (EDA)**: 
   - Use the Jupyter notebooks to understand the dataset.
   - Analyze trends and visualize student performance.

2. **Model Training**: 
   - Train various models and evaluate their performance.
   - Save the best-performing model.

3. **Deployment**: 
   - The application is built using Flask, making it easy to deploy on platforms like AWS, Heroku, or any cloud service.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [CatBoost](https://catboost.ai/) for powerful gradient boosting on decision trees.
- [Flask](https://flask.palletsprojects.com/) for building the web application.

---

Feel free to adjust the paths and any content to better fit your project!
