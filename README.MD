# 🌐 Streamlit Cloud Deployment Guide  
## Zomato Restaurant Rating Prediction 🍽️⭐

This guide explains how to deploy the Zomato Restaurant Rating Prediction project on **Streamlit Cloud**.

---

# 🚀 Step 1: Push Project to GitHub

Upload the following files to your GitHub repository:

```bash
model.pkl
requirements.txt
streamlit_app.py
Zomato_df.csv
README.md
```

---

# 🚀 Step 2: Create Streamlit Account

Go to:

https://streamlit.io/cloud

Login using your GitHub account.

---

# 🚀 Step 3: Deploy App

1. Click:
```text
Create App
```

2. Select your GitHub repository.

3. Select branch:
```text
main
```

4. In Main file path enter:
```text
streamlit_app.py
```

5. Click:
```text
Deploy
```

---

# 🚀 Step 4: Wait for Deployment

Streamlit will:

- Install requirements
- Load model.pkl
- Deploy your app

After successful deployment, you will get a public URL like:

```text
https://zomato-rating-predictor.streamlit.app
```

---

# 📦 requirements.txt

Example requirements file:

```txt
streamlit
pandas
numpy
scikit-learn
pickle-mixin
```

---

# ▶️ Run Locally

```bash
streamlit run streamlit_app.py
```

---

# 📊 Features Used for Prediction

- Online Order
- Book Table
- Votes
- Location
- Restaurant Type
- Cuisines
- Cost
- Menu Item

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Random Forest Regressor

---

# 👨‍💻 Author

Pramod Gaikwad

GitHub:  
https://github.com/pramod-nanu

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
