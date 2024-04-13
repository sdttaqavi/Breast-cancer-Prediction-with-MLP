
**Breast Cancer Prediction with MLP**

This section aims to implement a Multilayer Perceptron (MLP) model for predicting breast cancer using the Breast Cancer dataset. The dataset comprises features extracted from digital images of breast mass sampling, describing characteristics of cell nuclei.

**Implementation Guidelines:**

1. **Data Preparation:**
   - Divide the dataset into Train and Test sets with 80/20 ratio.
   - Pre-process data by normalizing values and selecting important features. Utilize correlation matrix or Random Forest model for feature selection.

2. **Model Design:**
   - Design and implement an MLP model using TensorFlow.
   - Specify model architecture including the number of hidden layers, neurons per layer, activation functions, input and output layer dimensions.

3. **Hyperparameter Tuning:**
   - Experiment with two different learning rates and epochs combinations, totaling four models.
   - Train each model and report accuracy on both Train and Test data to understand hyperparameter effects.

4. **Evaluation:**
   - Use validation split parameter to prevent overfitting during training.
   - Evaluate model performance using precision, recall, F1-score, and confusion matrix.
   - Utilize scikit-learn library for simplifying evaluation process.


**Report:**

In the submitted report, provide comprehensive details of model architecture, hyperparameter configurations, and analysis of model performance metrics. Include insights from confusion matrix analysis and evaluation criteria.
