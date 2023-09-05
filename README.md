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

In this project, we will be looking at the mean absolute error between the predicted and actual pressures during the inspiratory phase of each breath. The score is given by
\begin{center}
$|X-Y|$
\end{center}
where $X$ is the vector of predicted pressure and $Y$ is the vector of actual pressures across all breaths in the test set.


# Deep Learning Model Exploration
