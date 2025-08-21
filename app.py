from flask import Flask, render_template
import subprocess
import os

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
    return "✅ Streaming started to YouTube!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
