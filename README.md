# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : VEDANT RAMESH KAWARE

*INTERN ID* : CT08DN595

*DOMAIN* : DATA SCIENCE

*DURATION* : 8 WEEKS

*MENTOR* : NEELA SANTOSH

# Project 4: End-to-End Mental Health Prediction Web App

This project is a complete end-to-end implementation of a data science solution that predicts whether an individual is likely to need mental health treatment based on a range of personal, professional, and organizational factors. The application is designed with the aim of promoting awareness and proactive action around mental health challenges, especially in high-stress work environments like the tech industry. It covers the full pipeline of a data science workflow, including data cleaning, exploratory analysis, model building, deployment, and frontend integration through a web interface.

The dataset used for this project is a public mental health survey dataset sourced from Kaggle. It includes responses from individuals working in the tech sector and contains features like age, gender, self-employment status, remote work, mental health benefits at the workplace, anonymity, comfort in discussing mental health with supervisors and coworkers, family history of mental illness, and other workplace-related variables. This dataset was carefully preprocessed by handling missing values, encoding categorical data using numerical values, and selecting relevant features that have predictive significance.

For the machine learning model, a binary classification task was implemented to predict whether an individual may require mental health treatment. After experimentation with various models, a suitable classifier such as Logistic Regression or Random Forest was selected based on performance and interpretability. The model was trained and validated using scikit-learn, and the final trained model was exported as a .pkl file using the pickle library, making it ready for real-time use in a production environment.

The backend of the web application is powered by Flask. It acts as the server that receives user input from the frontend, processes it into the format expected by the machine learning model, and returns the prediction result. The application includes structured error handling, clean data formatting, and a prediction pipeline that converts raw form data into a structured DataFrame that matches the trained model’s feature schema. Once the prediction is made, the result is shown to the user in a clean and simple format — either suggesting that mental health treatment may be needed or not.

The frontend of the application is designed using HTML, CSS, and JavaScript. It features a responsive, multi-page form that guides users through a smooth input experience. Each section of the form gathers different types of information: personal demographics, workplace environment, and mental health resources. JavaScript is used to manage page transitions and show a progress bar, making the user experience smooth and interactive. The result page is styled to be clear, empathetic, and easy to understand, with messages tailored to encourage self-awareness without judgment or diagnosis.

This project serves multiple purposes. First, it acts as a portfolio-worthy demonstration of an end-to-end data science solution — from raw data to deployed app. Second, it provides a socially meaningful application that brings attention to the topic of mental health in modern workplaces. It also sets a reusable foundation for similar classification-based apps that rely on survey input and predictive modeling. From a technical learning perspective, it integrates real-world machine learning, web development, and deployment workflows in one cohesive project.

In conclusion, this mental health prediction web app demonstrates how machine learning can be applied responsibly and effectively in areas that matter. It showcases not only technical skills but also empathy and problem-solving applied to real-world issues. The project reflects a strong grasp of full-stack data science and serves as an impactful example of how AI can be used to create awareness, drive meaningful conversations, and encourage early reflection or action when it comes to mental wellness.

<img width="1057" height="831" alt="Image" src="https://github.com/user-attachments/assets/3feef06a-3aee-44d3-af7b-ad0dac79bf3b" />
