import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, confusion_matrix
import matplotlib.pyplot as plt
import joblib
def preprocess_text(text):
    if not isinstance(text, str):
        text = str(text)
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = ' '.join(text.split())
    return text
fake_df_rf = pd.read_csv("C:\\Users\\nehal\\Downloads\\image_det\\Fake_1.csv")
true_df_rf = pd.read_csv("C:\\Users\\nehal\\Downloads\\image_det\\True_1.csv")
fake_df_rf["label_rf"] = 0
true_df_rf["label_rf"] = 1
data_rf = pd.concat([fake_df_rf, true_df_rf], ignore_index=True)
duplicate_count = data_rf.duplicated().sum()
print("Number of duplicate rows:", duplicate_count)
if duplicate_count > 0:
    data_rf = data_rf.drop_duplicates().reset_index(drop=True)
    print("Duplicates removed. New dataset size:", data_rf.shape[0])
data_rf["text"] = data_rf["text"].apply(preprocess_text)
X_rf = data_rf["text"]
y_rf = data_rf["label_rf"]
print("Class distribution:", y_rf.value_counts())
X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X_rf, y_rf, test_size=0.2, random_state=46, stratify=y_rf)
vectorizer_rf = TfidfVectorizer(max_features=1000, stop_words="english", ngram_range=(1, 2))
X_train_tfidf_rf = vectorizer_rf.fit_transform(X_train_rf)
X_test_tfidf_rf = vectorizer_rf.transform(X_test_rf)
model_rf = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=46)
model_rf.fit(X_train_tfidf_rf, y_train_rf)
X_tfidf_rf = vectorizer_rf.transform(X_rf)
cv_scores = cross_val_score(model_rf, X_tfidf_rf, y_rf, cv=5, scoring='roc_auc')
print("Cross-validation AUC scores:", cv_scores)
print("Mean Cross-validation AUC:", cv_scores.mean(), "+/-", cv_scores.std())
y_prob_rf = model_rf.predict_proba(X_test_tfidf_rf)[:, 1]
y_pred_rf = model_rf.predict(X_test_tfidf_rf)
fpr_rf, tpr_rf, _ = roc_curve(y_test_rf, y_prob_rf)
roc_auc_rf = auc(fpr_rf, tpr_rf)
print("Train set size:", X_train_rf.shape[0])
print("Test set size:", X_test_rf.shape[0])
print("Confusion Matrix:\n", confusion_matrix(y_test_rf, y_pred_rf))
print("Accuracy on test set:", (y_pred_rf == y_test_rf).mean())
# plt.figure()
# plt.plot(fpr_rf, tpr_rf, color="purple", lw=2, label=f"ROC curve (AUC = {roc_auc_rf:.2f})")
# plt.plot([0, 1], [0, 1], color="navy", lw=2, linestyle="--")
# plt.xlim([0.0, 1.0])
# plt.ylim([0.0, 1.05])
# plt.xlabel("False Positive Rate")
# plt.ylabel("True Positive Rate")
# plt.title("ROC Curve - Random Forest (Tuned)")
# plt.legend(loc="lower right")
# plt.show()
print(f"AUC Score for Random Forest: {roc_auc_rf:.2f}")
# Save model and vectorizer
joblib.dump(model_rf, "random_forest_fake_news_model.pkl")
joblib.dump(vectorizer_rf, "tfidf_vectorizer_rf.pkl")
print("Model and vectorizer saved.")
