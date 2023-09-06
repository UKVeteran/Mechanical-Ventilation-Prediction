# Objective

1. Use **FastAPI** to create an API for your model
2. Run that API on your machine
3. Put it in production

1. open a .py file for fastapi connection
pip install fastapi
pip install uvicorn
uvicorn build_api:app --reload | python file and api name to browse rootpage




## Docker Terminal codes
docker images | to list all images in the disk
docker rmi --force <image code> | to remove image from disk
docker run python:3.10.6-buster | to run container
docker run -it python:3.10.6-buster sh | to see inside of the container (it:interactive)
docker container ls (-a) | to list the files inside container (-a to see past)
docker build . -t mvp_api | build the new image and name it api
docker run -it mvp_api sh | run it in shell after you name it api
docker run mvp_api | to run it
docker run -p 2323:8000 mvp_api | map the 2389 port on your machine to the 8000 -
(uvicorn default) port inside container, p for port
docker ps | to list the running containers
docker stop <container ID>
docker kill <container ID> | use only is image refuses to stop
docker ps -q | xargs docker kill | to kills all
docker

## Inside docker shell codes after docker run -it mvp_api sh
ls -la | to list all files
cat requirements.txt | to see the contents
cat app/build_api.py | to see the .py file inside app folder
pip freeze | to bring the latest version of packages


## .env files how to ini
direnv allow .  | initialize environment
direnv reload . | reload everytime you make changes
make docker_build | shortcut of
echo $GCR_IMAGE | to print the variable

We may need pickle file to put the model inside
=======
# Mechanical Ventilation Prediction

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


# Deep Learning Model Exploration
## Activation Functions
| Activation Function        |  Why?          |
| ------------- |:-------------:|
| Swish      |   Smooth, differentiable, often performs well in practice  | 
| SeLU    |     Self-normalizing properties when certain conditions are met, helps with vanishing/exploding gradients  |   
| GeLU    |   Smooth, differentiable, performs well in certain deep learning applications    |   

## Models

| Deep Learning Model     | Activation Function           |   MAE  | 
| ------------- |:-------------:|:-------------:|
|LSTM      |  Swish   |    0.351  |
|      |  SeLU   |    0.350  |
|     |  GeLU   |    0.328 |
|GRU    |    Swish  |   0.299    |
|BiLSTM     | Swish      | 0.200   |
|    |      SeLU |  0.213  |
|   |      GeLU |  0.207  |
|BiGRU      |      Swish   |  0.237   |

# Our Model: GeLU Activated BiLSTM
Bidirectional LSTM (BiLSTM) is a recurrent neural network is a sequence processing model that consists of two LSTMs: one taking the input in a forward direction, and the other in a backwards direction. BiLSTMs effectively increase the amount of information available to the network, improving the context available to the algorithm.


![BiLSTMPyDot](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/2c76a192-dc65-4e75-aedd-b0bbcb88c5d1)


## MAE

| Activation Function           |   MAE  | 
|:-------------:|:-------------:|
|      GeLU |  0.213  |
|       |  0.207  |

![SwishPlotBiLSTM0 2002](https://github.com/UKVeteran/Mechanical-Ventilation-Prediction/assets/39216339/3a221dfe-db12-446c-8306-2f147a0e273a)
