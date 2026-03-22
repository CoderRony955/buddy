def html(image_path: str) -> str:
    return f"""
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Games</title>

<!-- Google Font (cool modern style) -->
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet">

<style>
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        background-color: #ffffff;
        font-family: 'Poppins', sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        text-align: center;
    }}

    .container {{
        padding: 20px;
        max-width: 600px;
        width: 100%;
    }}

    /* Logo styling */
    .logo {{
        width: 120px;
        height: auto;
        margin-bottom: 25px;
    }}

    /* Main text */
    .title {{
        font-size: 2rem;
        font-weight: 700;
        color: #111;
        line-height: 1.3;
    }}

    /* Highlight "free" word */
    .highlight {{
        color: #00c853;
    }}

    /* Responsive adjustments */
    @media (max-width: 600px) {{
        .logo {{
            width: 90px;
        }}
        .title {{
            font-size: 1.5rem;
        }}
    }}
</style>

</head>

<body>

<div class="container">
    <!-- Replace src with your logo -->
    <img src="{image_path}" alt="Logo" class="logo" width="120" style="width:120px; max-width:120px; height:auto;">

    <h1 class="title">
        Looking for <span class="highlight">free</span> to play video games?
    </h1>
</div>

</body>
</html>


"""
