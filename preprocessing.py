def preprocessing(df):

    from google.colab import drive
    drive.mount('/content/drive')

    import pandas as pd
    from sklearn.preprocessing import RobustScaler
    from sklearn.compose import make_column_transformer

    X = df.drop(columns=["breath_id", "pressure"])
    y = df["pressure"]

    rb_scal = RobustScaler()
    preprocessor = make_column_transformer((rb_scal, ["R", "C", "time_step", "u_in"]), remainder='passthrough')

    X_preprocessed = pd.DataFrame(preprocessor.fit_transform(X), columns=preprocessor.get_feature_names_out())

    feature_cols = ["R","C", "u_in", "u_out", "time_step"]
    n_steps = 80
    n_features = len(feature_cols)
    target_column_name = 'pressure'  # Replace with the actual target column name

    # Assuming "train" is a DataFrame containing your training data
    n_samples_train = len(df) // n_steps  # Calculate the number of breaths

    y_train = y.values[:n_samples_train * n_steps].reshape(-1, n_steps)
    X_train = X_preprocessed.values[:n_samples_train * n_steps].reshape(-1, n_steps, n_features)

    return X_train, y_train
