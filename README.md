

# Better-News Article Classifier

This Streamlit application is designed to classify news articles into different categories using machine learning models. The classification is based on the text content of the articles.

## Overview

The application allows users to input the text of a news article manually or upload a PDF file containing the article. After providing the input, users can click the "Classify" button to see the predicted category for the article.

## Setup

To run the application, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.
   
2. **Install Dependencies**: Navigate to the project directory and install the required Python libraries by running:
    ```
    pip install -r requirements.txt
    ```

3. **Download NLTK Resources**: Make sure you have downloaded the necessary NLTK resources by running:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

4. **Download Dataset**: Place the dataset file named `news-article-categories.csv` in a directory named `datasets` within the project directory.

5. **Run the Streamlit App**: Execute the following command to run the Streamlit app:
    ```
    streamlit run betternews_test_app.py
    ```

This command will start a local server, and you can access the app through your web browser at the specified URL (typically `http://localhost:8501`).

## Usage

1. **Enter Text**: Type or paste the text of the news article into the text area provided.
   
2. **Upload PDF**: Alternatively, upload a PDF file containing the news article by clicking on the "Upload PDF" button.

3. **Classify**: Click the "Classify" button to generate the predicted category for the news article.

## Model Training

The application utilizes an ensemble model consisting of Multinomial Naive Bayes, Random Forest, and XGBoost classifiers. The models are trained on a dataset of news articles with corresponding categories. Model training involves the following steps:

- Data preprocessing, including text cleaning and vectorization.
- Hyperparameter tuning for the Random Forest classifier using GridSearchCV.
- Training the ensemble model using a Voting Classifier.

The trained models are serialized and saved to disk for future use.

## Model Evaluation

The performance of the trained model is evaluated based on accuracy and classification report metrics.

## Files

- **betternews_test_app.py**: Streamlit application code for user interface.
- **betternews_testmodel.ipynb**: Jupyter Notebook containing model training code.
- **datasets/news-article-categories.csv**: Dataset containing news articles and categories.
- **models/**: Directory containing serialized models and vectorizer.

## Additional Notes

- Ensure that you have sufficient computational resources available for model training, especially if using large datasets or complex models.
- Feel free to customize the preprocessing steps or experiment with different machine learning algorithms for improved performance.

