# Mechanical Ventilation Prediction Project

Link To The Kaggle Dataset: <a href="https://www.kaggle.com/competitions/ventilator-pressure-prediction/data">MVP Dataset</a>

Link To The Refined Dataset: <a href="https://www.kaggle.com/datasets/ukveteran/mvp-subset">MVP Refined Dataset</a>

Collaborators: <a href="https://github.com/UKVeteran">Johar</a>,
<a href="https://github.com/dilarah">Dilara</a>,
<a href="https://github.com/IhapSubasi">Ihap</a>,
<a href="https://github.com/Guillaume2126">Guillaume</a>

How Does A Ventilator Really Work?: <a href="https://www.youtube.com/watch?v=yDtKBXOEsoM
)6">Video</a>

# Overview 
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


## R 

Physically, this is the change in pressure per change in flow (air volume per time). Intuitively, one can
imagine blowing up a balloon through a straw. We can change R by changing the diameter of the straw,
with higher R being harder to blow

## C

Physically, this is the change in volume per change in pressure. Intuitively, one can imagine the same
balloon example. We can change C by changing the thickness of the balloon’s latex, with higher C having
thinner latex and easier to blow.

## R & C Visually
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee1.png" height="500" width="1200" >

### --- Varying R ---
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee2b.png" height="400" width="1200" >
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee3b.png" height="400" width="1200" >

### --- Varying C ---
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee4.png" height="400" width="1200" >
<img src="https://raw.githubusercontent.com/cdeotte/Kaggle_Images/main/Oct-2021/ee5.png" height="500" width="1200" >


# The Task

In this project, we will be looking at the mean absolute error (MAE) between the predicted and actual pressures during the inspiratory phase of each breath. The score is given by

$$|X-Y|$$

where $X$ is the vector of predicted pressure and $Y$ is the vector of actual pressures across all breaths in the test set.

# Data Visualization

![__results___5_0](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/428fadaf-cb06-4e2e-b469-b0b24fa04db7)

![__results___6_0](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/62382b3d-e27c-41c2-83cf-fd962222136a)


# Deep Learning Model Exploration
## Activation Functions

| Activation Function        |  Why?          |
| ------------- |:-------------:|
| Swish      |   Smooth, differentiable, often performs well in practice  | 
| SELU (Scaled Exponential Linear Unit) |     Self-normalizing properties when certain conditions are met, helps with vanishing/exploding gradients  |   
| GELU  (Gaussian Error Linear Unit)  |   Smooth, differentiable, performs well in certain deep learning applications    |   

## Models

| Deep Learning Model     | Activation Function           |   MAE  | 
| ------------- |:-------------:|:-------------:|
|LSTM      |  Swish   |    0.351  |
|      |  SELU   |    0.350  |
|     |  GELU   |    0.328 |
|GRU    |    Swish  |   0.299    |
|BiLSTM     | Swish      | 0.200   |
|    |      SELU |  0.213  |
|   |      GELU |  0.207  |
|BiGRU      |      Swish   |  0.237   |

# Our Model: GELU Activated BiLSTM
![60be260e5e9ac0bc4d8beac9_math-20210607 (17)](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/7299af04-a1d7-44c2-9489-32fbad2ed8e7)
GELU combines elements of the sigmoid and the rectifier (ReLU) functions, resulting in a smooth and differentiable curve. 
### Properties
1) GELU is continuous and differentiable everywhere, making it suitable for gradient-based optimization methods like (SGD).
2) It approaches zero for inputs with large negative values and approaches 1 for inputs with large positive values, similar to the behavior of the sigmoid function.
3) In the range near zero, it behaves like the linear portion of the ReLU function.
### Advantages
1) GELU tends to perform well in deep neural networks.
2) It helps mitigate the vanishing gradient problem compared to sigmoid and tanh, making it more useful.
### Drawbacks
It may not always outperform ReLU or other activation functions in all scenarios.

<img width="1000" alt="Screen_Shot_2020-05-27_at_12 48 44_PM" src="https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/b2bbf605-f230-4035-9707-c0e057f63cb0">

## BiLSTM
Bidirectional LSTM (BiLSTM) is a recurrent neural network is a sequence processing model that consists of two LSTMs: one taking the input in a forward direction, and the other in a backwards direction. BiLSTMs effectively increase the amount of information available to the network, improving the context available to the algorithm.


![BiLSTMPyDot](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/2c76a192-dc65-4e75-aedd-b0bbcb88c5d1)


## The Deep Learned Model: MAE

| Activation Function           |   MAE  | 
|:-------------:|:-------------:|
|      GELU |  0.207  |

![SwishPlotBiLSTM0 2002](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/3a221dfe-db12-446c-8306-2f147a0e273a)


## Some Results

![Test1](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/89e9bb20-1965-442c-b8e2-a6f088fc70a7)

![Test2](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/a05bf186-2a3f-4224-b008-954d63769c2c)

![Test3](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/4cf3a202-6090-4277-b8d1-82fffb2858cc)

# Grid Searches

## GELU Activated BiLSTM Grid Searching: learning rate, number of neurons, dropout rate

## Grid Searching: activation, learning rate, number of neurons, dropout rate

# API & Deployment

1. Use **FastAPI** to create an API for our model
2. Run that API on the machine
3. Put it in production using Cloud Run

![FastAPI](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/6dce47ae-5ba8-4e42-ba16-d4ab6a8db2c5)


## Output


# The User Interface
-) Using **Streamlit** to create the UI

![download](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/7b789a1d-2078-43f4-ab69-23f9df782c2c)

## Output

# The Tech Stack: Bringing It All Together
