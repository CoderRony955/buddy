html = """
<html>
<head>
<style>
    body {
        margin: 0;
        background: #0a0f1c;
        font-family: 'Segoe UI', sans-serif;
        color: #e5e7eb;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .wrapper {
        width: 400px;
        text-align: center;
    }

    .logo {
        font-size: 28px;
        font-weight: bold;
        letter-spacing: 4px;
        margin-bottom: 30px;
        color: #60a5fa;
    }

    @keyframes scan {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

    .status {
        font-size: 13px;
        color: #9ca3af;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }

    .progress-container {
        display: flex;
        gap: 5px;
        justify-content: center;
    }

    .block {
        width: 20px;
        height: 8px;
        background: #1f2937;
        border-radius: 2px;
        animation: blink 1.2s infinite;
    }

    .block:nth-child(2) { animation-delay: 0.1s; }
    .block:nth-child(3) { animation-delay: 0.2s; }
    .block:nth-child(4) { animation-delay: 0.3s; }
    .block:nth-child(5) { animation-delay: 0.4s; }
    .block:nth-child(6) { animation-delay: 0.5s; }
    .block:nth-child(7) { animation-delay: 0.6s; }
    .block:nth-child(8) { animation-delay: 0.7s; }

    @keyframes blink {
        0%, 100% {
            background: #1f2937;
        }
        50% {
            background: #60a5fa;
            box-shadow: 0 0 6px #60a5fa;
        }
    }

    .percent {
        margin-top: 20px;
        font-size: 14px;
        color: #60a5fa;
        letter-spacing: 2px;
    }

    .tip {
        margin-top: 25px;
        font-size: 12px;
        color: #6b7280;
        font-style: italic;
    }
</style>
</head>

<body>
    <div class="wrapper">
        <div class="logo">Fetching Assets</div>

        <div class="status">LOADING ASSETS...</div>

        <div class="progress-container">
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
            <div class="block"></div>
        </div>

        <div class="percent">PLEASE WAIT</div>

        <div class="tip">Tip: Stay in cover while reloading</div>
    </div>
</body>
</html>

"""