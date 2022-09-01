"use strict";

document.getElementById("testButton").addEventListener("click", () => {
    const socket = new WebSocket("ws://localhost:8989");

    socket.addEventListener('open', () => {
        const msg = `{
            "message-type": "CREATE-SUITE",
            "url": "https://google.com",
            "tests": {
                "testTest": {},
                "testTestDuplicate":{},
                "test-https": {},
                "test-default-tls": {},
                "test-TLSv1.2": {},
                "test-TLSv1.3": {}
            }
        }`;
        socket.send(msg);
    });

    socket.addEventListener('message', (e) => {
        const data = e.data;
        document.getElementById("out").innerHTML += `<div>${data}</div>`;
    });
});
