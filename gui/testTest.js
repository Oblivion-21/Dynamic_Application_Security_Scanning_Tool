"use strict";

document.getElementById("testButton").addEventListener("click", () => {
    const socket = new WebSocket("ws://localhost:8989");

    socket.addEventListener('open', () => {
        const msg = `{
            "message-type": "CREATE-SUITE",
            "url": "www.google.com",
            "tests": {
                "testTest": {},
                "testTestDuplicate": {}
            }
        }`;
        socket.send(msg);
    });

    socket.addEventListener('message', (e) => {
        const data = e.data;
        document.getElementById("out").innerHTML += `<div>${data}</div>`;
    });
});
