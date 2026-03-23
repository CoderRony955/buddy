def html(message: str):
    return f"""

<html>
<head>
<style>
    body {{
        margin: 0;
        height: 100vh;
        background: linear-gradient(135deg, #0f172a, #020617);
        font-family: 'Segoe UI', sans-serif;
        color: #e5e7eb;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .card {{
        background: rgba(30, 41, 59, 0.9);
        padding: 40px;
        border-radius: 12px;
        text-align: center;
        width: 380px;
        box-shadow: 0 0 25px rgba(0,0,0,0.6);
    }}

    .icon {{
        font-size: 50px;
        margin-bottom: 10px;
    }}

    .title {{
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #f87171;
    }}

    .message {{
        font-size: 14px;
        color: #9ca3af;
        margin-bottom: 25px;
        line-height: 1.5;
    }}

    .divider {{
        height: 1px;
        background: #374151;
        margin: 20px 0;
    }}

    .btn {{
        display: inline-block;
        padding: 10px 18px;
        background: #3b82f6;
        color: white;
        text-decoration: none;
        border-radius: 6px;
        font-size: 14px;
        transition: 0.2s;
    }}

    .btn:hover {{
        background: #2563eb;
    }}

    .secondary {{
        display: block;
        margin-top: 12px;
        font-size: 12px;
        color: #6b7280;
    }}
</style>
</head>

<body>
    <div class="card">
        <div class="icon">⚠️</div>

        <div class="title">Oops! Something went wrong</div>

        <div class="message">
            {message}
        </div>

    </div>
</body>
</html>
"""