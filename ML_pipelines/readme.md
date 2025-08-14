# ML Pipelines Project

A comprehensive demonstration of Machine Learning pipelines using the Titanic dataset, showcasing the benefits and implementation of scikit-learn pipelines versus traditional manual preprocessing approaches.

## 🎯 Project Overview

This project demonstrates two different approaches to building machine learning workflows:
1. **Traditional Approach**: Manual preprocessing steps without pipelines
2. **Pipeline Approach**: Using scikit-learn pipelines for streamlined, reproducible ML workflows

The project uses the classic Titanic dataset to predict passenger survival, making it an excellent case study for understanding ML pipeline implementation.

## 📁 Project Structure

```
ML_pipelines/
├── with_pipelines/
│   └── titanic-with-pipelines.ipynb      # Pipeline-based implementation
├── without_pipelines/
│   └── titanic-without-pipelines (1).ipynb  # Traditional manual approach
├── data/                                  # Dataset folder (create this)
│   ├── train.csv                         # Training data with survival labels
│   ├── test.csv                          # Test data for predictions (optional)
│   └── gender_submission.csv             # Sample submission file (optional)
└── readme.md                              # This file
```

## 🚀 Key Features

### Pipeline Implementation (`with_pipelines/`)
- **ColumnTransformer**: Efficient handling of different column types
- **Imputation**: Automatic handling of missing values (Age, Embarked)
- **Encoding**: One-hot encoding for categorical variables (Sex, Embarked)
- **Scaling**: MinMax scaling for numerical features
- **Feature Selection**: Chi-squared based feature selection (top 8 features)
- **Model Training**: Decision Tree classifier
- **Unified Pipeline**: All preprocessing steps combined in a single pipeline

### Traditional Implementation (`without_pipelines/`)
- **Manual Steps**: Separate preprocessing for each transformation
- **Individual Fitting**: Each transformer fitted separately
- **Step-by-step**: Manual application of transformations
- **No Reproducibility**: Harder to maintain and reproduce results
- **Data Concatenation**: Combines train data with gender submission data

## 🛠️ Technologies Used

- **Python 3.x**
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **Jupyter Notebooks**: Interactive development environment

## 📊 Dataset

The project uses the **Titanic dataset** from Kaggle which includes:
- Passenger information (age, sex, class, etc.)
- Target variable: Survival (0 = No, 1 = Yes)
- Features: Age, Sex, Pclass, Fare, Embarked, etc.

**Dataset Links:**
- **Main Dataset**: [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/data)
- **Train Data**: `train.csv` - Contains passenger data with survival labels
- **Test Data**: `test.csv` - Contains passenger data without survival labels (for predictions)
- **Gender Submission**: `gender_submission.csv` - Sample submission file

**Note**: The notebooks use the Kaggle input paths (`/kaggle/input/titanic/`) which are automatically available when running on Kaggle. For local execution, you'll need to download the dataset and update the file paths accordingly.

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd ML_pipelines
   ```

2. **Install dependencies**:
   ```bash
   pip install scikit-learn pandas numpy jupyter
   ```

3. **Download the dataset**:
   - Visit [Titanic Dataset on Kaggle](https://www.kaggle.com/c/titanic/data)
   - Download the following files:
     - `train.csv`
     - `test.csv` (optional, for making predictions)
     - `gender_submission.csv` (optional, for reference)
   - Place them in a `data/` folder within the project directory

4. **Update file paths** (if running locally):
   - In `with_pipelines/titanic-with-pipelines.ipynb`: Change `/kaggle/input/titanic/train.csv` to `../data/train.csv`
   - In `without_pipelines/titanic-without-pipelines (1).ipynb`: Change `/kaggle/input/titanic/train.csv` to `../data/train.csv`

5. **Launch Jupyter**:
   ```bash
   jupyter notebook
   ```

6. **Open notebooks**:
   - Start with `without_pipelines/` to understand the traditional approach
   - Then explore `with_pipelines/` to see the pipeline implementation

## 📚 Learning Objectives

By working through this project, you will learn:

1. **Pipeline Benefits**:
   - Reproducible workflows
   - Easier deployment
   - Consistent preprocessing
   - Reduced code duplication

2. **scikit-learn Components**:
   - `Pipeline` and `make_pipeline`
   - `ColumnTransformer`
   - `SimpleImputer`
   - `OneHotEncoder`
   - `MinMaxScaler`
   - `SelectKBest`

3. **Best Practices**:
   - Proper train/test splitting
   - Handling missing values
   - Categorical encoding
   - Feature scaling
   - Feature selection

## 🎓 Usage Examples

### Pipeline Approach
```python
# Create a complete pipeline
pipeline = Pipeline([
    ('imputation', trf1),      # Handle missing Age and Embarked
    ('encoding', trf2),        # One-hot encode Sex and Embarked
    ('scaling', trf3),         # MinMax scale all features
    ('feature_selection', trf4), # Select top 8 features using chi2
    ('classifier', trf5)       # Decision Tree classifier
])

# Fit and predict in one go
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

### Traditional Approach
```python
# Manual preprocessing steps
X_train_age = si_age.fit_transform(X_train[['Age']])
X_train_fare = si_fare.fit_transform(X_train[['Fare']])
X_train_sex = ohe_sex.fit_transform(X_train[['Sex']])
X_train_embarked = ohe_embarked.fit_transform(X_train[['Embarked']])
# ... more manual steps and concatenation
```

## 🔍 Key Differences

| Aspect | Traditional Approach | Pipeline Approach |
|--------|---------------------|-------------------|
| **Code Organization** | Scattered, manual | Unified, structured |
| **Reproducibility** | Low | High |
| **Maintenance** | Difficult | Easy |
| **Deployment** | Complex | Simple |
| **Testing** | Individual steps | End-to-end |
| **Cross-validation** | Manual | Automatic |

## 🚀 Benefits of Pipelines

1. **Reproducibility**: Same preprocessing applied consistently
2. **Maintainability**: Centralized workflow management
3. **Deployment**: Easy to save and load complete models
4. **Cross-validation**: Automatic handling of preprocessing in CV
5. **Testing**: End-to-end testing of the complete workflow
6. **Production**: Simplified model serving

## 📈 Performance Comparison

The pipeline approach typically results in:
- **Better generalization**: Proper handling of data leakage
- **Consistent preprocessing**: Same transformations on train/test sets
- **Faster development**: Less time spent on manual preprocessing
- **Easier debugging**: Centralized workflow makes issues easier to identify
- **Automatic feature selection**: Chi-squared based selection of top 8 features
- **Streamlined deployment**: Single pipeline object for production use

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new pipeline examples
- Improving documentation
- Adding more datasets
- Enhancing the comparison analysis
- Adding evaluation metrics and model performance comparison
- Creating additional preprocessing techniques
- Adding cross-validation examples

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Titanic dataset from Kaggle
- scikit-learn development team
- Open source community

