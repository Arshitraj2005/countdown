const audio = document.getElementById("audio");
const canvas = document.getElementById("waveCanvas");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
const analyser = audioCtx.createAnalyser();
const source = audioCtx.createMediaElementSource(audio);
source.connect(analyser);
analyser.connect(audioCtx.destination);

const bufferLength = analyser.frequencyBinCount;
const dataArray = new Uint8Array(bufferLength);

function draw() {
  requestAnimationFrame(draw);
  analyser.getByteFrequencyData(dataArray);

  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
  ctx.strokeStyle = "lime";
  ctx.lineWidth = 2;

  for (let i = 0; i < bufferLength; i++) {
    const angle = (i / bufferLength) * 2 * Math.PI;
    const radius = dataArray[i] / 2;
    const x = canvas.width / 2 + radius * Math.cos(angle);
    const y = canvas.height / 2 + radius * Math.sin(angle);
    ctx.lineTo(x, y);
  }
  ctx.closePath();
  ctx.stroke();
}
draw();
