# Documentation of INDAthon - Data Scientist Solution

Novia Permatasari  
Directorat of Census and Survey Methodology (PMSS)

## Library Used
* numpy: 1.26.4
* pandas: 2.2.2
* matplotlib: 3.7.5
* seaborn: 0.12.2
* datetime: unknown
* math: unknown
* prophet: 1.1.1
* holidays: 0.24
* sklearn: 1.2.2
* catboost: 1.2.5
* warnings: unknown

This code will be running well on Python 3.10.13

  
## Data
### INDATHON ROUND 1 - 2024
**Variable of Interest**  
* Jumlah Penumpang Transjakarta (training and testing data)

**Aux Variables**  
* Jumlah Armada TransJakarta
* Jumlah Penumpang LRT
* Jumlah Penumpang LRT
* Jumlah Penumpang MRT
* Jumlah Penumpang MRT

### Additional Aux Variables
* National Holiday (number of day)
* Ramadan
* Eid al-Fitr & Eid al-Fitr leave
* School Holoday
* Beginning of Covid (Jan - June 2020)
* Start of Pandemic until today (aaccomodate the behavior chaanges)
* End of Pandemic
* Community Activities Restrictions Enforcement (PPKM Policy)

# Code Description
*  full_script.ipynb : full code of exploration and modelling on python notebook
*  prophet_regressor.py : get forecast the number of transjakarta passengers on Jan - June 2024, using Prophet algorithm, utilizing additional aux variables
*  linreg_prophet_regressor.py : get forecast the number of transjakarta passengers on Jan - June 2024, using Linear Regression to accomodate the Aux variables and Prophet to utilize additional aux variables
*  linreg_prophet_regressor2.py : get forecast the number of transjakarta passengers on Jan - June 2024, using Linear Regression to accomodate the Aux variables and Prophet to utilize additional aux variables (only for last obvservation)


## How to Run
* Clone the project
* Install python and library (based on the requirement)
* Run the .py or explore the .ipynb


## Note
Total Processing Time : 105.2s
Prediction Time : 0.321617s
Data Size : 8.47 KB 


## About Repository
### Repo Structure

    ├─ data
    │  ├─ regressor.csv
    │  ├─ indathon-round1-2024/
    ├─ model
    │  ├─ prophet_regressor.pkl
    │  ├─ linreg_prophet_regressor.pkl
    ├─ full_script.ipynb
    ├─ prophet_regressor.py
    ├─ README.md

