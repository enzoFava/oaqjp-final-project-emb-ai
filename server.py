"""
Deployment
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('emotionDetector')

@app.route('/')
def home():
    """
    Create home route
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def emotion_detector_route():
    """
    Create functionality
    """
    if request.method == 'POST':
        text = request.form.get('text')
    elif request.method == 'GET':
        text = request.args.get('textToAnalyze')
    else:
        text = None

    emotions, status_code = emotion_detector(text)
    if emotions['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
    if status_code == 400:
        output_str = "Invalid text! Please try again."
    else:
        output_str = (
            f"For the given statement, the system response is 'anger': {emotions['anger']}, "
            f"'disgust':{emotions['disgust']}, 'fear':{emotions['fear']}, 'joy':{emotions['joy']} "
            f"and 'sadness': {emotions['sadness']}. The dominant emotion is "
            f"{emotions['dominant_emotion']}."
        )
    return output_str, status_code



if __name__ == '__main__':
    app.run(debug=True)
