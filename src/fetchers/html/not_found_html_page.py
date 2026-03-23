html = """
<html>
<head>
<style>
    body {
        margin: 0;
        height: 100vh;
        background: #020617;
        font-family: 'Segoe UI', sans-serif;
        color: #e5e7eb;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .container {
        text-align: center;
        max-width: 400px;
    }

    .code {
        font-size: 80px;
        font-weight: bold;
        color: #38bdf8;
        letter-spacing: 5px;
    }

    .title {
        font-size: 22px;
        margin: 10px 0;
    }

    .desc {
        font-size: 14px;
        color: #9ca3af;
        margin-bottom: 25px;
    }

    .btn {
        display: inline-block;
        padding: 10px 18px;
        background: #38bdf8;
        color: #020617;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        transition: 0.2s;
    }

    .btn:hover {
        background: #0ea5e9;
    }

    .glitch {
        position: relative;
        display: inline-block;
    }

    .glitch::before,
    .glitch::after {
        content: "404";
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0.6;
    }

    .glitch::before {
        color: #f87171;
        transform: translate(-2px, -2px);
    }

    .glitch::after {
        color: #22c55e;
        transform: translate(2px, 2px);
    }
</style>
</head>

<body>
    <div class="container">
        <div class="code glitch">404</div>

        <div class="title">Not Found</div>

        <div class="desc">
            The game you're looking for doesn’t exist<br>
        </div>
    </div>
</body>
</html>
"""