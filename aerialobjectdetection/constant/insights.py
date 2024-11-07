import google.generativeai as genai
from IPython.display import Markdown
import PIL.Image
import os

GOOGLE_API_KEY = 'AIzaSyByFoyQYuNDC9jsCwdNfs8_UhgmPNJWHJI'
runs_folder = '/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train'
genai.configure(api_key=GOOGLE_API_KEY)


model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
prompt = """
Give me insights about the performance of the YOLOv8 detection model based on the following metrics:
- Confusion Matrix: Explain the true positives, false positives, and class-specific accuracy.
- F1 Curve: Interpret the F1 scores for different confidence thresholds.
- Precision and Recall Curves: Describe how precision and recall change across thresholds.
- PR Curve: Provide insights on the precision-recall trade-off.
- Results: Summarize overall model performance.

Format the response in Markdown.
"""

image_1 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/confusion_matrix_normalized.png')
image_2 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/confusion_matrix.png')
image_3 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/F1_curve.png')
image_4 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/labels.jpg')
image_5 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/P_curve.png')
image_6 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/PR_curve.png')
image_7 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/R_curve.png')
image_8 = PIL.Image.open('/Users/kumarrohit/Desktop/Aerial-Object-Detection/Aerial-Object-Detection/runs/detect/train/results.png')

response = model.generate_content([prompt, image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8])

with open('insights.md','w+') as f:
    f.write(response.text)
