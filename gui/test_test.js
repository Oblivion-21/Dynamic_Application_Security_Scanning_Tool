"use strict";

document.getElementById("test_button").addEventListener("click", () => {
    const socket = new WebSocket("ws://localhost:8989");

    socket.addEventListener('open', () => {
        const msg = `{
            "message-type": "CREATE_SUITE",
            "sut": "https://site-under-test.com",
            "tests": {
                "test-test": {}
            }
        }`;
        socket.send(msg);
    });

    socket.addEventListener('message', (e) => {
        const data = e.data;
        document.getElementById("out").innerHTML += `<div>${data}</div>`;
    });
});
