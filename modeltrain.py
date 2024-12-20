from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib 
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_preddd=model.predict(X_test)
accuracy=accuracy_score(y_test,y_preddd)
precision=precision_score(y_test,y_preddd,average="weighted")
recall=recall_score(y_test,y_preddd,average="weighted")
f1=f1_score(y_test,y_preddd,average="weighted")
print("Accuracy is",accuracy,"\nPrecison is",precision,"\nRecall is",recall,"\nF1 score is",f1)

# Save model
joblib.dump(model, 'iris_model.pkl')
print("Model saved as 'iris_model.pkl'")
print(iris)