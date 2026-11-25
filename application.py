import os
import socket
from flask import Flask, render_template_string

application = Flask(__name__)

VERSION = "1.1.0"

@application.route("/")
def home():
    env = os.getenv("APP_ENV", "staging")
    debug = os.getenv("DEBUG_MODE", "false")
    color = "#22c55e" if env == "production" else "#f59e0b"

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>DeployLens</title>
        <style>
            * { box-sizing: border-box; }
            body {
                background: #0b1120;
                color: #e2e8f0;
                font-family: monospace;
                max-width: 850px;
                margin: 80px auto;
                padding: 20px;
            }
            h1 { font-size: 42px; margin-bottom: 5px; }
            .subtitle { color: #94a3b8; }
            .badge {
                display: inline-block;
                color: {{ color }};
                border: 1px solid {{ color }};
                padding: 8px 15px;
                border-radius: 6px;
                text-transform: uppercase;
            }
            .grid {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 16px;
                margin-top: 30px;
            }
            .card {
                background: #111827;
                border: 1px solid #334155;
                border-radius: 10px;
                padding: 24px;
                overflow-wrap: anywhere;
            }
            .label { color: #94a3b8; }
            .value { font-size: 23px; }
            .online { color: #22c55e; }
            footer {
                margin-top: 35px;
                color: #64748b;
            }
        </style>
    </head>
    <body>
        <h1>DeployLens</h1>
        <p class="subtitle">
            Automated Cloud Deployment Dashboard
        </p>

        <span class="badge">{{ env }}</span>

        <div class="grid">
            <div class="card">
                <p class="label">APPLICATION VERSION</p>
                <p class="value">v{{ version }}</p>
            </div>
            <div class="card">
                <p class="label">SERVER STATUS</p>
                <p class="value online">● Operational</p>
            </div>
            <div class="card">
                <p class="label">SERVER HOSTNAME</p>
                <p class="value">{{ hostname }}</p>
            </div>
            <div class="card">
                <p class="label">DEBUG MODE</p>
                <p class="value">{{ debug }}</p>
            </div>
        </div>

        <footer>
            AWS Elastic Beanstalk // CI/CD Assignment 4
        </footer>
    </body>
    </html>
    """, env=env, version=VERSION, color=color,
         hostname=socket.gethostname(), debug=debug)

if __name__ == "__main__":
    application.run(port=5000)
