# ML Pipelines Project

A comparison of traditional manual preprocessing vs. scikit-learn pipelines using the Titanic dataset.

## Project Structure

```
ML_pipelines/
├── with_pipelines/
│   └── titanic-with-pipelines.ipynb      # Pipeline implementation
├── without_pipelines/
│   └── titanic-without-pipelines (1).ipynb  # Manual preprocessing
└── data/                                  # Dataset folder
    ├── train.csv
    ├── test.csv
    └── gender_submission.csv
```

## Setup

1. **Install dependencies**:
   ```bash
   pip install scikit-learn pandas numpy jupyter
   ```

2. **Download dataset**:
   - Visit [Titanic Dataset on Kaggle](https://www.kaggle.com/c/titanic/data)
   - Download `train.csv` and place in `data/` folder

3. **Update file paths** (for local execution):
   - Change `/kaggle/input/titanic/train.csv` to `../data/train.csv` in both notebooks

4. **Run notebooks**:
   ```bash
   jupyter notebook
   ```

## Key Differences

| Aspect | Manual Approach | Pipeline Approach |
|--------|----------------|-------------------|
| **Code** | Scattered steps | Unified workflow |
| **Reproducibility** | Low | High |
| **Deployment** | Complex | Simple |
| **Maintenance** | Difficult | Easy |

## Pipeline Components

- **Imputation**: Handle missing Age and Embarked values
- **Encoding**: One-hot encode Sex and Embarked
- **Scaling**: MinMax scaling for numerical features
- **Feature Selection**: Chi-squared selection (top 8 features)
- **Model**: Decision Tree classifier

## Usage

### Pipeline Approach
```python
pipeline = Pipeline([
    ('imputation', trf1),
    ('encoding', trf2),
    ('scaling', trf3),
    ('feature_selection', trf4),
    ('classifier', trf5)
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

### Manual Approach
```python
# Multiple separate steps
X_train_age = si_age.fit_transform(X_train[['Age']])
X_train_sex = ohe_sex.fit_transform(X_train[['Sex']])
# ... more manual steps
```

## Benefits of Pipelines

- **Reproducible**: Consistent preprocessing
- **Deployable**: Single pipeline object
- **Maintainable**: Centralized workflow
- **Testable**: End-to-end testing
- **Scalable**: Easy to add/remove steps

