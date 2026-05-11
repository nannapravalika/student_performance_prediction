 
# Student Performance Prediction System

A Machine Learning based web application developed using Python and Flask that predicts whether a student is likely to pass or fail based on academic factors such as study hours, attendance, and previous marks.

 

# Project Overview

The Student Performance Prediction System is designed to analyze student academic data and predict performance outcomes using Machine Learning algorithms.

This project demonstrates concepts of:

- Machine Learning
- Data Science
- Predictive Analytics
- Web Development
- Model Training and Testing

The application helps in identifying students who may require academic support and performance improvement strategies.

 

# Features

- Predicts student performance
- Pass/Fail classification
- User-friendly web interface
- Machine Learning model integration
- Real-time prediction
- Flask-based deployment

 

# Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML
- CSS
- Joblib

 

# Machine Learning Algorithm Used

- Random Forest Classifier

The model is trained using student academic performance data and predicts outcomes based on:

- Study Hours
- Attendance Percentage
- Previous Marks

 

# Dataset Information

The dataset contains:

| Feature        | Description             |
| -------------- | ----------------------- |
| study_hours    | Number of study hours   |
| attendance     | Attendance percentage   |
| previous_marks | Previous academic marks |
| result         | Pass/Fail outcome       |

### Result Values

* 0 → Fail
* 1 → Pass

 

# Installation

## Step 1: Clone Repository

 
git clone https://github.com/yourusername/student_performance_prediction.git
 

## Step 2: Move to Project Folder

 
cd student_performance_prediction
 

## Step 3: Install Dependencies

 
pip install -r requirements.txt
 
# Train the Machine Learning Model

Run:

 
python model.py
 

This generates:

 
model.pkl
 

# Run the Flask Application

 
python app.py
 

Open browser:

 
http://127.0.0.1:5000
 

 

# How the System Works

1. User enters student details
2. Data is sent to Flask backend
3. Machine Learning model processes the input
4. Prediction is generated
5. Result displayed on web page

 
# Sample Input

| Study Hours | Attendance | Previous Marks |
| ----------- | ---------- | -------------- |
| 6           | 80         | 70             |

### Predicted Output

 
Student is likely to PASS
 

# Future Enhancements

* Grade prediction system
* Student dashboard
* Data visualization charts
* Performance analytics
* AI-based academic recommendations
* Database integration
* Admin panel
* Deep learning implementation

 

# Learning Outcomes

Through this project, I learned:

* Machine Learning model training
* Data preprocessing
* Flask web application development
* Predictive analytics
* Model deployment
* Real-world AI applications


 

# Use Cases

This system can be useful for:

* Schools
* Colleges
* Educational institutions
* Academic analytics platforms
* Student performance monitoring systems

 

# Resume Description

### Student Performance Prediction System

Developed a Machine Learning-based web application using Python and Flask to predict student academic performance using Random Forest classification based on study hours, attendance, and previous academic scores.


# Author

Pravalika
B.Tech Computer Science Engineering
Freelance Full Stack Developer


# License

This project is developed for educational and learning purposes.

 
