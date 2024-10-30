import os
import cv2
import math
from PIL import Image
from flask import Flask, render_template
from flask_wtf import FlaskForm
from ultralytics import YOLO
from werkzeug.utils import secure_filename
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from aerialobjectdetection.pipeline.training_pipeline import TrainPipeline
  
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key1'
app.config['UPLOAD_FOLDER'] = 'Uploads'
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "models", "best.pt")


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET', 'POST'])
def predict():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))
        filepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'],
                                secure_filename(file.filename))
        extension = filepath.rsplit('.', 1)[1].lower()
        if extension == 'jpg':
            img = Image.open(filepath)
            yolo = YOLO(model_path)
            os.chdir(os.getcwd())
            yolo.predict(img, save=True)


        elif extension == 'mp4' or extension == 'avi':

            video_path = filepath
            print(video_path)
            cap = cv2.VideoCapture(video_path)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            
            out = cv2.VideoWriter('static/output.mp4', fourcc, 30.0, (frame_width,frame_height), True)

            # Loading the trained model
            model = YOLO(model_path)
            class_names = ['Aircraft','Helicopter', 'Drone', 'Ship']
            while cap.isOpened():

                success, frame = cap.read()

                if not success:
                    break

                results = model.predict(frame, stream=True)

                for r in results:

                    boxes = r.boxes
                    print(boxes.conf)

                    for box in boxes:
                        x1, y1, x2, y2 = boxes.xyxy[0]
                        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

                        img = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), thickness=4)
                        # using boxes.conf to show the confidence values of the boxes
                        conf = math.ceil((box.conf[0] * 100)) / 100
                        label = int(box.cls)
                        print(label)
                        currentClass = class_names[label]
                        print(currentClass)

                        img = cv2.putText(img, f'{currentClass}{conf}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                          (0, 255, 255), 2, cv2.LINE_AA)

                        out.write(img)
            cap.release()
            out.release()

        return render_template('video.html')
    return render_template('index.html', form=form)

@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successful"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) # For Azure
