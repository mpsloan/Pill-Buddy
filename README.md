# Pill Buddy

* The Pill Buddy will be an autonomous pill dispenser that will be set to give out medication at specified times provided by the user.

## Goals

* Sort pills and place them in storage cylinders.
* Web application to retrieve user information.
* Dispense Pills on user set schedule.
* Alert user as to when pills need refilled, and when to take them.

## Repository Structure
* `OpenCV` folder contains various files for computer vision code, as of now the only code that is able to function properly is `detection.py`.
* `images` folder contains two images used for testing color detection `one.jpg` and `two.jpg` and the `hsv-scale.png` was used for reference with the OpenCV code as that was the color scale `detection.py` abided by. 
* `mobile` folder contains files for the mobile application, the `app.py` handles the form logic and the `templates` folder contains the `.html` files for formatting the web app. The `log.txt` file is a log of the latest user's answers to the web app's form.
* `ServoControl` folder contains the `servo.py` file for the servo motor instructions.