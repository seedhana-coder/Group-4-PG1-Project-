# Module 4 – ngrok Commands

## 1. Start the Flask Application

Open Command Prompt in the project folder and run:

```bash
python app.py
```

This starts the Flask application on port 5000.

## 2. Start ngrok

Open a second Command Prompt and run:

```bash
ngrok http 5000
```

This creates a public ngrok tunnel that forwards internet traffic to the Flask application running on port 5000.

## 3. Public URL

ngrok will display a public HTTPS forwarding address.

The forwarding destination is:

```text
http://localhost:5000
```

## 4. Test the Connection

Open the public ngrok HTTPS address on another device, such as a mobile phone, to access the Flask application.

## 5. Stop ngrok

To stop the ngrok tunnel, press:

```text
Ctrl + C
```

in the ngrok Command Prompt.

## Main Commands

```bash
python app.py
ngrok http 5000
```
