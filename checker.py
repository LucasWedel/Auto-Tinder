from sklearn.svm import SVC

# Sample HOG features (replace with your actual data)
hog_feature_attractive = [0.3074591, 0.02360967, 0.05977629, 0.15400156, 0.2595685, 0.26250637]
hog_feature_unattractive = [0.08040722, 0.06814343, 0.04455374, 0.08834514, 0.02010193, 0.12894224]

# Assuming you already have a trained SVM classifier
svm_classifier = SVC()

# Assuming X_train and y_train are your training data
X_train = [hog_feature_attractive, hog_feature_unattractive]
y_train = ['attractive', 'unattractive']

# Train the SVM classifier
svm_classifier.fit(X_train, y_train)

# Now, let's predict whether a new HOG feature (e.g., from a new image) is attractive or not
# Sample HOG feature for a new image (replace with your actual data)
new_hog_feature = [0.03905004, 0.00530785, 0.00759077, 0.02130414, 0.07296164, 0.33949408]

# Make prediction
prediction = svm_classifier.predict([new_hog_feature])

# Print the prediction
print("Prediction:", prediction)