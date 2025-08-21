from flask import Flask, render_template, send_from_directory
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-stream')
def start_stream():
    stream_key = "gvzz-gfg3-0pa8-2v2t-9u9h"
    rtmp_url = f"rtmp://a.rtmp.youtube.com/live2/{stream_key}"
    audio_path = "static/audio/song.mp3"

    subprocess.Popen([
        "ffmpeg", "-re", "-i", audio_path,
        "-f", "flv", rtmp_url
    ])
    return "Streaming started!"

if __name__ == '__main__':
    app.run(debug=True)
