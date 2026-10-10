# 🎬 Movie Recommender System

A content-based movie recommendation web application built with **Python**, **Streamlit**, and **Scikit-Learn**. This app suggests the top 5 most similar movies based on a selected title and automatically fetches official movie posters using the **TMDb API**.

---

## 🚀 Live Demo
Check out the deployed application here: [Streamlit Cloud App](https://movie-recommendersystem-h4nwggzenrxefkgxk9gf4x.streamlit.app)

---

## 🛠️ Tech Stack & Libraries
* **Frontend/UI:** Streamlit (configured in wide layout mode)
* **Machine Learning:** Scikit-Learn (Cosine Similarity matrix)
* **Data Manipulation:** Pandas
* **API Integration:** Requests (for fetching live poster art from The Movie Database API)
* **Deployment & Hosting:** Streamlit Community Cloud & GitHub

---

## ⚙️ Key Architectural Feature: Large File Handling
GitHub enforces a strict 100MB file limit for repositories. Because the precomputed `similarity.pkl` matrix is ~180MB, this project utilizes a custom **server-side chunk-reassembly pipeline**. 
* The large similarity matrix is split into smaller, lightweight chunk files (`similarity_part_X.pkl`) for version control.
* Upon deployment startup, **`app.py`** programmatically detects, combines, and reassembles the parts back into the complete `similarity.pkl` file on the fly, ensuring seamless cloud deployment without exceeding storage limits.

---

## 📂 Project Structure
```text
├── app.py                  # Main Streamlit application and reassembly script
├── movies.pkl              # Pickled dataset containing movie titles and IDs
├── requirements.txt        # Python dependency configuration
├── similarity_part_0.pkl   # Split chunk files for the similarity matrix
├── similarity_part_1.pkl
├── ... (parts 2 through 8)
└── README.md               # Project documentation
