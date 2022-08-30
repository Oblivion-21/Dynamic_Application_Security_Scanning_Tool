"use strict";

document.getElementById("testButton").addEventListener("click", (event) => {
    event.preventDefault();
    console.log("Test button pressed");
    const socket = new WebSocket("ws://localhost:8989");

    socket.addEventListener('open', () => {
        const msg = `{
            "message-type": "CREATE-SUITE",
            "url": "https://google.com",
            "tests": {
                "testTest": {},
                "testTestDuplicate":{}
            }
        }`;
        socket.send(msg);
        console.log("Sent CREATE-SUITE message");
    });

    socket.addEventListener('message', (e) => {
        const data = e.data;
        console.log(`Recived message ${data}`);
        document.getElementById("out").innerHTML += `<div class="data">${data}</div>`;
    });
});
