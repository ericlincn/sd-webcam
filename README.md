# sd-web-cam
A Flask app that sends webcam raw images to ComfyUI and displays the rendered images.

https://github.com/ericlincn/sd-web-cam/assets/20105350/624cc6aa-c94c-41d6-bb76-78a43f93c293

# Usage
1. Install ComfyUI with lcm lora.
2. Install [toyxyz/ComfyUI_toyxyz_test_nodes](https://github.com/toyxyz/ComfyUI_toyxyz_test_nodes)
3. `git clone https://github.com/ericlincn/sd-web-cam.git`
4. Drag workflow.json into ComfyUI.
5. Check "Auto queue" in ComfyUI, click "queue prompt"
6. Prepare the Python environment based on requirements.txt.
7. Modify the "node_directory" in app.py to the path where ComfyUI_toyxyz_test_nodes is located.
8. Run app.py
