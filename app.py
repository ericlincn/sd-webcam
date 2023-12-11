import threading
from flask import Flask, render_template, send_file
from flask_socketio import SocketIO, emit
from PIL import Image
from io import BytesIO
import base64

node_directory = 'E:/projects/ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI_toyxyz_test_nodes/CaptureCam'
capture_path = '/captured_frames/capture.jpg'
render_path = '/rendered_frames/render.jpg'

app = Flask(__name__)
app.config['SECRET_KEY'] ='secret!'
socketio = SocketIO(app, cors_allowed_origins = '*')

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/render.jpg')
def get_rendered_image():
    return send_file(node_directory + render_path)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('video-feed')
def handle_video_feed(image_data):

    def process_image():
        try:
            # Convert base64 data to binary
            binary_data = base64.b64decode(image_data)
            # Process the image data and save it as a JPEG file
            img = Image.open(BytesIO(binary_data))
            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
            # flipped_img.save('image.jpg')
            flipped_img.save(node_directory + capture_path)
            # print('Image saved successfully')
        except Exception as e:
            print('Error saving image:', str(e))
    
    threading.Thread(target = process_image).start()

if __name__ == "__main__":
    socketio.run(app, host = "0.0.0.0", port = 5000, debug = True)