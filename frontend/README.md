# Micro Frontends

## Add new Micro Frontend
First, you need to know the architecture of this application.
- **container** is app manager. `src/components/MicroFrontend` loads the micro frontends into the routes.
- Your new Micro Frontend url must defined in `.env` and in `src/routers` of **container**.
1. Go to this directory and create new app with command:
    ```bash
    npx create-react-app <your-app-name>
    ```

2. Open `package.json` of the application you just created. Change `"scripts"` to: 
    ```json
    "scripts": {
        "start": "set PORT=<your-port> && react-scripts start",
        ...
    }
    ```

3. Go to `src/index`, define render and unmount functions:
    ```jsx
    import React from 'react';
    import ReactDOM from 'react-dom/client';
    import App from './App';
    // import * as serviceWorker from "./serviceWorker";

    const appName = "YourAppName" // No space
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
    ```

4. Back to `container` directory, add new environment variable in `.env` file.
    ```bash
    ...
    REACT_APP_SUB_APP_1_HOST="http://localhost:4001"
    REACT_APP_SUB_APP_2_HOST="http://localhost:4002"
    ...
    ```
    *Note: You must create custom environment variables beginning with `REACT_APP_`*

    After that, open `src/routers` and define your new app component:
    ```jsx
    const appHost = process.env.REACT_APP_SUB_APP_1_HOST;

    const YourAppName = ({ history }) => (
        <MicroFrontend history={history} host={appHost} name="YourAppName" />
    );

    const ContainerRoutes = () => {
        return (
            <Routes>
                <Route exact path="/" element={<Main/>}/>
                <Route path="/your-app-path" element={<YourAppName/>} />
                <Route path="*" element={<NotFound/>} />
            </Routes>
        )
    };
    ```

5. Run all apps to make sure it works properly.
    ```bash
    npm start
    ```