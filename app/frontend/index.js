/*document.getElementById('submit').onclick = () => {
    window.location.replace('./id.html')
}*/

//Selector for your <video> element
// import { io } from "https://cdn.socket.io/4.8.1/socket.io.esm.min.js";

const video = document.querySelector('#myVidPlayer');

//Core
window.navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
        video.onloadedmetadata = (e) => {
            video.play();
        };
    })
    .catch( () => {
        alert('You have give browser the permission to run Webcam and mic');
    })
function takeASnap(){

    const canvas = document.createElement('canvas')
    const ctx = canvas.getContext('2d'); // get its context
    canvas.width = video.videoWidth; // set its size to the one of the video
    canvas.height = video.videoHeight;
    ctx.drawImage(video, 0,0); // the video
    return new Promise((res, rej)=>{
        canvas.toBlob(res, 'image/jpeg'); // request a Blob from the canvas
    });
}       

function download(blob){
    fetch("http://localhost:5000/upload", { method: 'POST', body: blob })
        .then(res=>res.json()).then(res=>{
        idTrash(res.cat)
    })
};

// Pauses the live feed, shows the prediction if item should be in trash or recycling, then advances to ID scanning
function idTrash(receptacle) {
    video.pause(); 
    const subh = document.getElementById('prompt');
    subh.innerHTML = 'I think this should be in the ' + receptacle;
    
    // Advance to id scanning page after 3 seconds
    setTimeout(() => {
        window.location.replace('./id.html')
    }, 3000)
}

// Establishing connection with the server hosted at domain:port
var socket = io.connect('http://localhost:8080');
// Listening for event named `any event`
socket.on('predictionMade', idTrash);
