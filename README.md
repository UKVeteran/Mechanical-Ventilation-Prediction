# Mechanical Ventilation Prediction Project

Link To The Kaggle Dataset: <a href="https://www.kaggle.com/competitions/ventilator-pressure-prediction/data">MVP Dataset</a>

Link To The Refined Dataset: <a href="https://www.kaggle.com/datasets/ukveteran/mvp-subset">MVP Refined Dataset</a>

Collaborators: <a href="https://github.com/UKVeteran">Johar</a>,
<a href="https://github.com/dilarah">Dilara</a>,
<a href="https://github.com/IhapSubasi">Ihap</a>,
<a href="https://github.com/Guillaume2126">Guillaume</a>

How Does A Ventilator Really Work?: <a href="https://www.youtube.com/watch?v=yDtKBXOEsoM
)6">Video</a>



<p align="center">
    <img  src="https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/bc6d8997-af0d-4e86-9a26-e3ea1d59e89b" alt="">
</p>


# 1️⃣ Overview 
What do doctors do when a patient has trouble breathing? They use a ventilator to pump oxygen into
a sedated patient’s lungs via a tube in the windpipe. But mechanical ventilation is a clinician-intensive
procedure, a limitation that was prominently on display during the early days of the COVID-19 pandemic. 
At the same time, developing new methods for controlling mechanical ventilators is prohibitively
expensive, even before reaching clinical trials. High-quality simulators could reduce this barrier.
Current simulators are trained as an ensemble, where each model simulates a single lung setting. However,
lungs and their attributes form a continuous space, so a parametric approach must be explored to consider
the differences in patient lungs.

In this project, we will simulate a ventilator connected to a sedated patient’s lung.
If successful, we will help overcome the cost barrier of developing new methods for controlling mechanical
ventilators. This will pave the way for algorithms that adapt to patients and reduce the burden on
clinicians during these novel times and beyond. As a result, ventilator treatments may become more
widely available to help patients breathe.


<img src="https://www.the-odd-dataguy.com/images/posts/20211101/flow_screenshot.png" height="500" width="1200" >

The first control input is a continuous variable from 0 to 100, representing the percentage of the inspiratory
solenoid valve is open to let air into the lung (i.e., 0 is completely closed and no air is let in, and 100
is completely open). The second control input is a binary variable representing whether the exploratory
valve is open (1) or closed (0) to let the air out.
Each time series represents an approximately 3-second breath. The files are organized such that each row
is a time step in a breath and gives the two control signals, the resulting airway pressure, and relevant
attributes of the lung described above.

Each time series represents an approximately 3-second breath. The files are organized such that each row
is a time step in a breath and gives the two control signals, the resulting airway pressure, and relevant
attributes of the lung described above.


## 1.1) R 

Physically, this is the change in pressure per change in flow (air volume per time). Intuitively, one can
imagine blowing up a balloon through a straw. We can change R by changing the diameter of the straw,
with higher R being harder to blow

## 1.2) C

Physically, this is the change in volume per change in pressure. Intuitively, one can imagine the same
balloon example. We can change C by changing the thickness of the balloon’s latex, with higher C having
thinner latex and easier to blow.

## 1.3) R & C Visually
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee1.png" height="500" width="1200" >

### 1.3.1) --- Varying R ---
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee2b.png" height="400" width="1200" >
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee3b.png" height="400" width="1200" >

### 1.3.2)  --- Varying C ---
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee4.png" height="400" width="1200" >
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee5.png" height="500" width="1200" >


# 2️⃣ What is u_in and pressure?

fkjhadsjfhasfnjdsfn;nadsnfkoanfcsdkocm;k s akdjasdal
Here is a nice plot: the x-axis represents time_step. Imagine that we have a lung which can be thought of as a balloon. At time t, 
we blow air into the balloon (lung) in a quantity indicated by the blue line (u_in). At time t, the pressure inside the balloon (lung)
is indicated by the orange line ('pressure'). Time to left of dotted black line has balloon's exit closed (inhale) so u_out=0, and time 
to right of dotted black line has balloon's exit open (exhale) so u_out=1.
![ex1](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/af7ae1e2-394e-4f49-98de-7d063eeba42d)

# 3️⃣ The Task

In this project, we will be looking at the mean absolute error (MAE) between the predicted and actual pressures during the inspiratory phase of each breath. The score is given by

$$|X-Y|$$

where $X$ is the vector of predicted pressure and $Y$ is the vector of actual pressures across all breaths in the test set.

#  4️⃣ Data Visualization

![__results___5_0](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/428fadaf-cb06-4e2e-b469-b0b24fa04db7)

![__results___6_0](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/62382b3d-e27c-41c2-83cf-fd962222136a)


# 5️⃣ Deep Learning Model Exploration
## 5.1) Activation Functions

| Activation Function        |  Why?          |
| ------------- |:-------------:|
| Swish      |   Smooth, differentiable, often performs well in practice  | 
| SELU (Scaled Exponential Linear Unit) |     Self-normalizing properties when certain conditions are met, helps with vanishing/exploding gradients  |   
| GELU  (Gaussian Error Linear Unit)  |   Smooth, differentiable, performs well in certain deep learning applications    |   

## 5.2) Models

| Deep Learning Model     | Activation Function         | 
| ------------- |:-------------:|
|LSTM      |  Swish     |
|      |  SELU    |
|     |  GELU   |
|GRU    |    Swish    |
|BiLSTM     | Swish     |
|    |      SELU | 
|   |      GELU |  
|BiGRU      |      Swish   | 

# 6️⃣ A Comparative Study 

1) GELU Activated BiLSTM - Complex Architecture - More Layers - Batch Size = 512
2) Tanh Activated BiLSTM - Complex Architecture - More Layers - Batch Size = 512

## 6.1) Breath-ID Examples

## 6.1.1) Breath-ID = 100616
MAE: 0.20352394496343126

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/be30ec8d-1243-48bd-9b7f-9a97f5410c22)

MAE: 0.1927886219909601

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/3f115953-ca1f-47af-8025-7b0839717f69)



##  6.1.2)Breath-ID = 122413
MAE: 0.20186762255066518

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/e1d547f8-5ed4-476b-af46-06e55a1ee97c)

MAE: 0.17174334217205064

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/f0687098-b9f9-46bc-8640-51a53fdfe964)

##  6.1.3) Breath-ID =  125749
MAE: 0.48377817099546744

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/667fcc10-f39d-444b-80da-1cdd923dcdc9)

MAE: 0.7943930315136575
![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/b8933dd4-f76e-464e-ac1a-a754d2df12ef)


##  6.1.4) Breath-ID = 125680
MAE: 0.17760752381367167

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/5a3fdc44-7936-4944-93a2-81913cc96a08)


MAE: 0.27696521379286076
![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/2f79b937-35d7-49bf-afb7-eb7359d707b1)

## 6.2) MAE

| Activation Function        |  Model MAE        |
| ------------- |:-------------:|
|  GELU    |0.31442668853492356  | 
| Tanh |    0.28797522659582786  | 


# 7️⃣ Our Model: Tanh Activated BiLSTM
![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/33dbd3e9-4d3a-47d1-a9ca-a1aa689ccbaf)

The hyperbolic tangent (tanh) activation function is a widely used activation function in neural networks. It is similar to the sigmoid activation function but has a range between -1 and 1, which allows it to model both positive and negative values.

1) Range: The tanh function outputs values between -1 and 1. This property makes it centered around 0, which can help mitigate the vanishing gradient problem in deep neural networks.

2) S-shaped: The tanh function has an S-shaped curve similar to the sigmoid function, which means it is continuous and differentiable, making it suitable for gradient-based optimization.

3) Zero-centered: One of the main advantages of tanh over the sigmoid function is that it is zero-centered, which means that its outputs have a mean of 0. This property simplifies optimization because the gradients are centered around zero, making convergence faster.

4) Symmetric: The tanh function is symmetric around the origin (0,0), which means it has both positive and negative values.


![1_WeuJzmlt3iNVWsUsvf24Eg](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/d4837939-a031-4c2c-a7cb-2ff8e701dbd9)


Tanh activations are commonly used in recurrent neural networks (RNNs) and long short-term memory networks (LSTMs) due to their zero-centered property.


## BiLSTM
Bidirectional LSTM (BiLSTM) is a recurrent neural network is a sequence processing model that consists of two LSTMs: one taking the input in a forward direction, and the other in a backwards direction. BiLSTMs effectively increase the amount of information available to the network, improving the context available to the algorithm.


```python 
def get_model():
    act = "tanh"
    model = tf.keras.Sequential([
        layers.InputLayer(input_shape=(n_steps,n_features)),
        layers.Bidirectional(layers.LSTM(150, return_sequences=True)),
        layers.Bidirectional(layers.LSTM(150, return_sequences=True)),
        layers.Bidirectional(layers.LSTM(150, return_sequences=True)),
        layers.Bidirectional(layers.LSTM(150, return_sequences=True)),
        layers.Dropout(0.2),
        layers.Flatten(),
        layers.Dense(128, activation=act),
        layers.Dense(256, activation=act),
        layers.Dense(512, activation=act),
        layers.Dense(80)
    ])
    return model
with strategy.scope():
    model = get_model()
    model.compile(optimizer="adam", loss="mae")
```



![BiLSTMPyDot](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/2c76a192-dc65-4e75-aedd-b0bbcb88c5d1)

## Total Number Of Parameters
![TanhModelParams](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/eae5f95e-f635-47dc-9cb5-d6504de0205b)



# 8️⃣ API & Deployment

1. Use **FastAPI** to create an API for our model
2. Run that API on the machine
3. Put it in production using Cloud Run

![FastAPI](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/6dce47ae-5ba8-4e42-ba16-d4ab6a8db2c5)


## Output
![API](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/dfa8512e-a372-4f80-b037-7b834f742c31)


#  9️⃣ The User Interface
-) Using **Streamlit** to create the UI

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/7b789a1d-2078-43f4-ab69-23f9df782c2c)

## Output

![MVPPredictor1](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/8eb3da16-de6f-4a58-a8e4-0ccea135adc6)

## The Deployment Link
 <a href="https://lewagon-test-gb-streamilitforteam.streamlit.app/">Mechanical Ventilation Predictor</a>
# TechStack
| 🦾 The Stack 🦾 | 
|:------------------------------------------:|
|Docker        |
| GCP |
|Google Colab|
| Keras |
| Numpy |
| Pandas |
| Python |
| Scikit Learn|
| Streamlit |
| Tensforflow| 

# 🔟 Future Work & Conclusion
This project is part of the ongoing effort and improvements can take place at 2 levels:<br>
• Data<br>
• Deep Learning Models
## Data
1. Feature Engineering: Consider whether there are additional features we can engineer from the
data that might help the model. Sometimes, domain-specific feature engineering can significantly
improve model performance.
2. More Data: Consider comorbidities like<br>
• emphysema<br>
• asthma<br>
• pneumonia<br>
• COPD<br>
• pulmonary edema<br>
• bronchitis<br>
• cystic fibrosis

## Deep Learning Models
### Example 1: Adding More Dense Layers

Epoch 164/200  <br>
95/95 [==============================] - 24s 252ms/step - loss: 0.4476 - val_loss: 0.4716 - lr: 8.2890e-05

### Example 2: Changing The Optimizer: RMSprop Optimizer

RMSprop is a gradient-based optimization technique used in training neural networks. It was proposed by the father of back-propagation, Geoffrey Hinton. 
Gradients of very complex functions like neural networks have a tendency to either vanish or explode as the data propagates through the function. RMSprop was developed
as a stochastic technique for mini-batch learning. 

RMSprop deals with the above issue by using a moving average of squared gradients to normalize the gradient. 
This normalization balances the step size (momentum), decreasing the step for large gradients to avoid exploding and increasing the step for small gradients to avoid vanishing.

Simply put, RMSprop uses an adaptive learning rate instead of treating the learning rate as a hyperparameter. This means that the learning rate changes over time.

Epoch 130/200  <br>
95/95 [==============================] - 23s 242ms/step - loss: 0.3616 - val_loss: 0.4030 - lr: 8.6199e-04

### Example 3: Batch Normalization
Batch normalization which is also known as batch norm is a method used to make training of neural networks faster and more stable through normalization of the layers' inputs by recentering and rescaling.
It was proposed by Sergey Ioffe and Christian Szegedy in 2015.

Epoch 170/200 <br>
95/95 [==============================] - 8s 86ms/step - loss: 0.6881 - val_loss: 0.6929 - lr: 8.2319e-05

### Example 4: Increasing The Number Of Neurons Per Layer
        layers.Bidirectional(layers.LSTM(1024, return_sequences=True)),
        layers.Bidirectional(layers.LSTM(512, return_sequences=True)),
        layers.Bidirectional(layers.LSTM(256, return_sequences=True)),
        layers.Bidirectional(layers.LSTM(128, return_sequences=True)


## Conclusion
In conclusion, our findings demonstrate that a deep learning model can reliably predict the pressure. There remain, however, a number of areas to explore. 
The lung settings we examined are by no means representative of all lung characteristics (e.g., neonatal, child, non-sedated) and lung characteristics are not static over time; a
patient may improve or worsen, or begin coughing. Ventilator costs also drive further research.
