import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
// import * as serviceWorker from "./serviceWorker";

const appName = "ClubAdmin" // No space
let container = null

window["render" + appName] = (containerId, history) => {
    container = ReactDOM.createRoot(document.getElementById(containerId));
    container.render(
        <React.StrictMode>
            <App history={history} />
        </React.StrictMode>
    );
};
window["unmount" + appName] = containerId => {
    container.unmount();
};
// Mount to root if it is not a micro frontend
if (!document.getElementById(appName + '-container')) {
    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(
        <React.StrictMode>
            <App />
        </React.StrictMode>
    );
}
// serviceWorker.unregister();