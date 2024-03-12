// code_execution.js
const socket = new WebSocket("ws://" + window.location.host + "/ws/code_execution/");

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    console.log("Received:", data.result);
    // Handle the result, update UI, etc.
};

function sendCode(code) {
    socket.send(code);
}