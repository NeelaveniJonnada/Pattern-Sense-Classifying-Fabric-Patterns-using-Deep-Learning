
# 🎨 Pattern Sense: Classifying Fabric Patterns using Deep Learning

**Pattern Sense** is a deep learning-based web application that classifies fabric patterns (e.g., Striped, Polka-Dotted, Checked, and Plain) using a Convolutional Neural Network (CNN) model. Built with TensorFlow/Keras and deployed using Flask, the project demonstrates how machine learning can be applied to real-world textile classification.

---

## 📌 Features

- Upload fabric images via a web interface
- Preprocessing of images for consistent model input
- Real-time prediction of pattern class using trained CNN
- Displays prediction with confidence score
- Simple and responsive UI using HTML/CSS/JS

---

## 📁 Project Structure

```

Pattern-Sense/
│
├── static/
│ └── assets/
│ └── uploads/
│ └── fabric-background.jpeg # Background or reference image
│
├── templates/
│ ├── home.html # Landing page
│ ├── about.html # About project
│ ├── contact.html # Contact form or details
│ ├── predict.html # Image upload form
│ └── predictionpage.html # Result display page
│
├── app.py # Main Flask application
├── model_cnn.h5 # Trained CNN model
├── requirements.txt # Python dependencies
├── .gitignore # Files to ignore in Git
└── .gitattributes # Git attributes

````

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/NeelaveniJonnada/Pattern-Sense-Classifying-Fabric-Patterns-using-Deep-Learning.git
cd Pattern-Sense-Classifying-Fabric-Patterns-using-Deep-Learning
````

### 2. Create Virtual Environment (optional)

```bash
python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate       # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt or
pip install flask keras tensorflow

```

### 4. Run the App

```bash
python app.py
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---


### 4. Output


![image](https://github.com/user-attachments/assets/8c240fb2-285a-4981-aecb-bb5727ba4290)

Home Page:
![image](https://github.com/user-attachments/assets/8b4a5329-af44-48db-a97c-4bc46ed7cb49)

About Page:
![image](https://github.com/user-attachments/assets/8e1cd8e2-814a-4dba-adfe-5a35680cec25)

Contact Page:
![image](https://github.com/user-attachments/assets/202b0c4d-7ca3-4f3d-bd6f-220cbb843c80)

Get Started Page:
![image](https://github.com/user-attachments/assets/36509160-c4a3-47ff-b14c-fcfedc7733e6)

Result:
![Screenshot 2025-06-29 211244](https://github.com/user-attachments/assets/d0d1b57a-35e5-4a20-970f-306794783cfa)

![Screenshot 2025-06-29 211322](https://github.com/user-attachments/assets/b1cbf0ed-70db-4d08-a295-fe03cb94f8fd)


## 🧠 Technologies Used

* **Frontend**: HTML, CSS, Bootstrap
* **Backend**: Python, Flask
* **Machine Learning**: TensorFlow, Keras
* **Image Processing**: OpenCV, NumPy

---

## 🧪 Dataset

The CNN model is trained on a labeled dataset of fabric images categorized as:

* Striped
* Plain
* Checked
* Polka-Dotted
* tribal
* floral
* Squares
* ikat
* Animal
* Geometry
* Cartoon

📦 **Dataset Link**: https://www.kaggle.com/datasets/nguyngiabol/dress-pattern-dataset

---

## 💡 Future Enhancements

* Add more fabric pattern types (e.g., floral, geometric)
* Deploy as a mobile app
* Enable user feedback for model improvement
* Cloud deployment (Render, Firebase, etc.)

---
## 🌐 Demo Video

👉 [Click here to see the app](https://www.youtube.com/watch?v=u5t3oczmFHA)
## 👩‍💻 Author

**Jonnada Neelaveni**
Vishnu Institute of Technology
[LinkedIn](https://www.linkedin.com/in/neelaveni-jonnada-901ba02ab/) 

---

## 📌 License

This project is open-source and available under the MIT License.


