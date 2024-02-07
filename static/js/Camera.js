`use strict`;
const snapshot = document.getElementById("snapshot");
const canvas = document.getElementById("canvas");
const video = document.getElementById("video");
const errorMessage = document.getElementById("ErrorMessage");

const constraints = {
  audio: false,
  video: {
    width: 480,
    height: 360,
  },
};

async function init() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia(constraints);
    handleSuccess(stream);
  } catch (e) {
    errorMessage.innerHTML = `navigator.getUserMedia.error:${e.toString()}`;
  }
}

function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;
}

let cm = false;
function cam() {
  var y = document.getElementById("bef");
  var x = document.getElementById("aft");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  } else {
    x.style.display = "none";
    y.style.display = "block";
  }
  cm = !cm;
  if (cm) {
    init();
  } else {
    cm = false;
    console.log("offing camera");
    stream.getTracks().forEach((track) => track.stop());
  }
}

function snap() {
  console.log("snapshot clicked");
  var context = canvas.getContext("2d");
  context.drawImage(video, 0, 0);
}
