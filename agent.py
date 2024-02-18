import subprocess

previous_prediction = 1


def notify_user(prediction):
    global previous_prediction

    if previous_prediction is None:
        previous_prediction = prediction
    else:
        if prediction != previous_prediction:
            if prediction == 0:
                subprocess.run(['notify-send', '-i', '/Desktop/3d.jpg', 'Warning!', '💢Ты потерял фокус!💢❗️'])
            else:
                subprocess.run(['notify-send', '-i', '/Desktop/3d.jpg', 'Come back', 'С Возвращением!🕯'])
            previous_prediction = prediction


prediction = 0
notify_user(prediction)
