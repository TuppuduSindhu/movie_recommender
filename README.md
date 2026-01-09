
# 🎬 Movie Recommendation System

## 📌 Project Description

This project is a **Movie Recommendation System** built using **content-based filtering**.
The system recommends movies based on similarity between movie descriptions and genres.
This project was developed by following step-by-step guidance from YouTube tutorials and implemented using **Python, Machine Learning, and Streamlit**.

---
output: 
![Description](screenshots/output.png)


## 🧾 Dataset Collection

* Dataset collected from **Kaggle**
* Dataset Name: **TMDB Movie Dataset**
* Contains movie details like:

  * Movie ID
  * Movie Title
  * Overview
  * Genres

---

## ⚙️ Project Implementation Steps

### 1️⃣ Dataset Setup

* Downloaded TMDB movie dataset from Kaggle
* Kept the dataset inside the project folder
* Opened the project folder in **VS Code**

---

### 2️⃣ Initial Python Execution

* Created a `main.py` file
* Loaded the dataset and checked output by running:

  ```bash
  python main.py
  ```

---

### 3️⃣ Model Building (Google Colab / Jupyter Notebook)

* Opened **Google Colab / Jupyter Notebook**
* Uploaded the dataset
* Created a notebook file: `main.ipynb`
* Performed the following:

  * Data cleaning
  * Feature selection
  * Combined **overview + genre** into a single column
  * Applied **CountVectorizer**
  * Calculated **Cosine Similarity**

---

### 4️⃣ Generating Pickle Files

After executing all the code in the notebook, two `.pkl` files were generated:

* `movies_list.pkl`
* `similarity.pkl`

These files store:

* Processed movie data
* Similarity matrix for recommendations

---

### 5️⃣ Streamlit Application

* Created `app.py`
* Loaded both `.pkl` files
* Built the Streamlit UI:

  * Movie selection dropdown
  * Recommendation button
  * Display recommended movies

Run the app using:

```bash
python -m streamlit run app.py
```

---



* Used HTML, CSS, and JavaScript for enhanced UI

---

### 7️⃣ TMDB API Integration

* Created an account on **TMDB website**
* Generated a **TMDB API Key**
* Used **Postman** to test API requests
* Copied the working GET request URL
* Integrated the API into `app.py`
* Used the API to fetch and display **movie posters**

---

### 8️⃣ Final Execution

* Ran the Streamlit application
* Selected a movie
* Received recommended movies with posters
* Project executed successfully 🎉

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* TMDB API
* HTML, CSS, JavaScript
* Node.js
* Postman

---

## 📂 Project Structure

```
├── app.py
├── main.py
├── main.ipynb
├── movies_list.pkl
├── similarity.pkl
├── frontend/
├── requirements.txt
└── README.md
```

---



## 🎯 Conclusion

This project demonstrates a practical implementation of a **content-based movie recommendation system** using machine learning concepts and a user-friendly web interface. It helped in understanding data preprocessing, similarity algorithms, API integration, and frontend-backend connection.


