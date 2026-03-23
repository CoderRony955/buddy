def html(reason: str):
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Something Went Wrong</title>

  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    body {{
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: linear-gradient(135deg, #000000, #3206f4);
      color: #fff;
      text-align: center;
      padding: 20px;
    }}

    .container {{
      max-width: 500px;
      width: 100%;
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(15px);
      border-radius: 16px;
      padding: 40px 25px;
      box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
      animation: fadeIn 0.8s ease-in-out;
    }}

    .icon {{
      font-size: 60px;
      margin-bottom: 20px;
    }}

    h1 {{
      font-size: 28px;
      margin-bottom: 10px;
    }}

    p {{
      font-size: 15px;
      opacity: 0.9;
      margin-bottom: 25px;
      line-height: 1.5;
    }}

    .error-code {{
      font-size: 72px;
      font-weight: bold;
      margin-bottom: 10px;
      opacity: 0.2;
    }}

    .buttons {{
      display: flex;
      gap: 12px;
      justify-content: center;
      flex-wrap: wrap;
    }}

    .btn {{
      padding: 10px 18px;
      border-radius: 8px;
      border: none;
      cursor: pointer;
      font-size: 14px;
      transition: all 0.3s ease;
    }}

    .btn-primary {{
      background: #fff;
      color: #4f46e5;
      font-weight: 600;
    }}

    .btn-primary:hover {{
      background: #e0e7ff;
    }}

    .btn-outline {{
      background: transparent;
      border: 1px solid #fff;
      color: #fff;
    }}

    .btn-outline:hover {{
      background: rgba(255, 255, 255, 0.1);
    }}

    @keyframes fadeIn {{
      from {{
        opacity: 0;
        transform: translateY(20px);
      }}
      to {{
        opacity: 1;
        transform: translateY(0);
      }}
    }}

    /* Responsive */
    @media (max-width: 480px) {{
      h1 {{
        font-size: 22px;
      }}

      .error-code {{
        font-size: 56px;
      }}

      .container {{
        padding: 30px 20px;
      }}
    }}
  </style>
</head>
<body>

  <div class="container">
    <div class="error-code">{reason}</div>
    <div class="icon">⚠️</div>

    <h1>Something went wrong</h1>
    <p>
    Something didn’t go as expected. Please try again in a few seconds,
    or head back home if the issue persists.
    </p>
    <div class="buttons">
  </div>

</body>
</html>


"""