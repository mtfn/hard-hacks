document.getElementById('submit').onclick = () => {
    window.location.replace('./id.html')
}

//Selector for your <video> element
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
    fetch("http://localhost:5000/upload", { method: 'POST', body: blob });
};
