Linear Regression Project
Description
This project is a practical exercise (TP) on linear regression using Python. It demonstrates how to:

Load and explore data
Create a linear regression model with scikit-learn
Evaluate the model with metrics (R², slope, intercept)
Visualize results with matplotlib
Make predictions
Project Example
Sample Data: Relationship between study hours and grades obtained
External Dataset: File data.csv with additional data
Prerequisites
Python 3.7+
pip (Python package manager)
Installation
1. Clone the repository (optional if you already have the files)
2. git clone https://github.com/zainablamouini-netizen/tp.regression.lineaire.git
cd tp.regression.lineaire
3. Create a virtual environment (recommended)
4. python -m venv venv
Activate the virtual environment:
On Windows (PowerShell):
venv\Scripts\Activate.ps1
On Windows (CMD):
venv\Scripts\activate.bat
On Mac/Linux:
source venv/bin/activate
3. Install dependencies
4. pip install -r requirements.txt
Or install packages manually:
pip install numpy pandas matplotlib scikit-learn
Project Structure
How to Run the Program
Option 1: Run the Python Script
python TP_regression.py
The script will display:
Graphs showing the relationship between the data
The regression line
Model coefficients:
Slope: coefficient of the independent variable
Intercept: value when X = 0
R² Score: quality of model fit (0 to 1, closer to 1 = better)
A prediction for a given value
Graphs showing the relationship between the data
The regression line
Model coefficients:
Slope: coefficient of the independent variable
Intercept: value when X = 0
R² Score: quality of model fit (0 to 1, closer to 1 = better)
A prediction for a given value
Option 2: Run with Jupyter Notebook
Then click on "Run All" to execute all cells.
upyter notebook TP_regression.ipynb
Expected Results
The program will generate:
Graph 1: Scatter plot (study hours vs grades)
Graph 2: Linear regression line overlaid on the data
Console Output
Slope (coefficient) : 6.0
Intercept : 44.0
Coefficient of determination R² : 0.9945
Prediction for 4.5 hours : 71.0
Graph 1: Scatter plot (study hours vs grades)
Graph 2: Linear regression line overlaid on the data
Console Output:
Key Concepts
Linear Regression: Model to predict a continuous variable based on one or more independent variables
Coefficient (Slope): Indicates how Y changes with X
Intercept: Value of Y when X = 0
R² Score: Proportion of variance explained by the model (0-1)
Troubleshooting
pip install scikit-learn
Error: "ModuleNotFoundError: No module named 'sklearn'"
Error: "No such file or directory: 'data.csv'"
Make sure the data.csv file is in the same directory as the script.
import matplotlib
matplotlib.use('TkAgg')
Graphs are not displayed
Try adding this line at the beginning of the script:

License
Free to use for educational purposes.

Resources
Scikit-learn Documentation
NumPy Documentation
Matplotlib Documentation
Generate
Code
Markdown
Run All
Clear All Outputs
Select Kernel
