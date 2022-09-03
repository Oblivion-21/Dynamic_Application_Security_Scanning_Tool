"use strict";

const {app, BrowserWindow} = require("electron");
const dev = require("electron-is-dev");

const createWindow = () => {
    const win = new BrowserWindow({
        width: 1080,
        height: 720,
        autoHideMenuBar: true
    });
    if (dev) {
        win.loadURL("http://localhost:3000");
    } else { 
        win.loadFile("../build/index.html");
    }
    win.webContents.openDevTools();
};

app.whenReady().then(() => {
    createWindow();

    app.on("activate", () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") app.quit();
});
