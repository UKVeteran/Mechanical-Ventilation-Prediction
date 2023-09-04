# Mechanical Ventilation Prediction

What do doctors do when a patient has trouble breathing? They use a ventilator to pump oxygen into
a sedated patient’s lungs via a tube in the windpipe. But mechanical ventilation is a clinician-intensive
procedure, a limitation that was prominently on display during the early days of the COVID-19 pan-
demic. At the same time, developing new methods for controlling mechanical ventilators is prohibitively
expensive, even before reaching clinical trials. High-quality simulators could reduce this barrier.
Current simulators are trained as an ensemble, where each model simulates a single lung setting. However,
lungs and their attributes form a continuous space, so a parametric approach must be explored to consider
the differences in patient lungs.

In this competition, we will simulate a ventilator connected to a sedated patient’s lung.
If successful, we will help overcome the cost barrier of developing new methods for controlling mechanical
ventilators. This will pave the way for algorithms that adapt to patients and reduce the burden on
clinicians during these novel times and beyond. As a result, ventilator treatments may become more
widely available to help patients breathe.

The first control input is a continuous variable from 0 to 100, representing the percentage of the inspiratory
solenoid valve is open to let air into the lung (i.e., 0 is completely closed and no air is let in, and 100
is completely open). The second control input is a binary variable representing whether the exploratory
valve is open (1) or closed (0) to let the air out.
Each time series represents an approximately 3-second breath. The files are organized such that each row
is a time step in a breath and gives the two control signals, the resulting airway pressure, and relevant
attributes of the lung described above.

<img src="https://www.the-odd-dataguy.com/images/posts/20211101/flow_screenshot.png" height="500" width="1200" >
