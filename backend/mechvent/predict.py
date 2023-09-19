#Calling Libraries
import pandas as pd
import tensorflow as tf
import numpy as np

#read csv from local
csv_path = "demo_samples/demo_test.csv"
df = pd.read_csv(csv_path)

# change the shape of dataframe to prepare for the model
n_steps = 80
n_columns = len(df.columns)
n_samples = len(df) // n_steps  # Calculate the number of breath

divided_df = df.values[:n_samples * n_steps].reshape(-1, n_steps, n_columns)


#loading the model from h5 version
loaded_model = tf.keras.models.load_model("model/model_tanh.h5")

# you can use loaded model to compute predictions
def demo_predict(idx):
    if idx < 201:
        features = divided_df[idx-1,:,0:4].reshape(-1,n_steps,4)
        return dict(actual_pressure = divided_df[idx-1,:,4:5].reshape(80).tolist(),
                    predicted_pressure = (loaded_model.predict(features)).reshape(80).tolist())
    return dict(invalid_number="out of range")
    # return "index is out of range or invalid format.\n Please enter an integer between 1 to 200!"

def demo_predict_csv(R,C,u_in,u_out):
    if len(R)==80:
        features = np.column_stack([R,C,u_in,u_out]).reshape(-1,80,4)

        return dict(predicted_pressure = loaded_model.predict(features).reshape(80))

    return dict(invalid_file="Please upload file with R,C,u-in,u-out,pressure and time_step columns")
