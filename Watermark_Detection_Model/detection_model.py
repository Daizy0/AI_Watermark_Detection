import cv2
import numpy as np
from sklearn.svm import SVC

def detect_watermark(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Extract frequency features
    freq_features = np.fft.fft2(gray)
    
    # Flatten for SVM input
    features = np.abs(freq_features).flatten()
    
    # SVM model for watermark detection
    model = SVC()
    model.fit(features.reshape(-1, 1), [1])  # 1 for watermarked
    
    return model.predict(features.reshape(-1, 1))

