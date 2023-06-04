#Uber-App

The Uber Supply-Demand Gap problem involves predicting the gap between the supply of Uber drivers and the demand for their services in different regions of City M 
at different times of the day. The problem is divided into non-overlapping square regions, each with a unique region ID.
Each day is uniformly divided into 144 time slots, each ten minutes long. 
The problem involves predicting the gap between the number of passengers' requests and the number of drivers who answer these requests in each region and time slot.
To predict the gap, we have used a rolling window and predicted the gap of the next slot by training the window data on models.
Models used for training:
1. Decision Tree
2. Linear Regression
