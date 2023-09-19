# Copyright 1996-2023 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy as np
import cv2
import base64
from utils.image_processing import ImageProcessing as IP


class Camera():
    """Class to manage the retrieval and output of images from the NAO's cameras."""

    def __init__(self, robot, camera_name='CameraTop'):
        """Initialize the image processing class."""
        self.robot = robot
        self.camera = robot.getDevice(camera_name)
        self.camera.enable(robot.time_step)
        self.height = self.camera.getHeight()
        self.width = self.camera.getWidth()
        print(self.width, self.height)

    def get_image(self):
        """Get an openCV image (BGRA) from a Webots camera."""
        return np.frombuffer(self.camera.getImage(), np.uint8).reshape((self.height, self.width, 4))

    def send_to_robot_window(self, img):
        """Send an openCV image to the robot's web interface."""
        color_image = cv2.rectangle(color_image,(10,img.shape[0]-20),(10,img.shape[1]-20),(255,0,0),2)
        #img = IP.color_detection(color_image)
        _, im_arr = cv2.imencode('.png', color_image[:, :, :3])
        im_bytes = im_arr.tobytes()
        im_b64 = base64.b64encode(im_bytes).decode()
        self.robot.wwiSendText('data:image/png;base64,' + im_b64)


    # def draw(self, img, vtc, hzt):
    #     """Draw a circle on the image."""
        
    #     image = cv2.circle(img, (vtc, hzt), 30, (0, 0, 250), 5)
    #     self.draw(image,10,10)