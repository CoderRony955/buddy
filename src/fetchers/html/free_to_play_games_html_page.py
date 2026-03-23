html = """
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<style>
    * {
        box-sizing: border-box;
    }
    body {
        margin: 0;
        padding: 16px;
        font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
        background: #0c1422;
        color: #eaf3ff;
    }
    .hero {
        background: #15253b;
        border: 1px solid #264c78;
        border-radius: 12px;
        padding: 14px;
        margin-bottom: 14px;
    }
    .hero h2 {
        margin: 0 0 2px 0;
        font-size: 22px;
        color: #ffffff;
    }
    .hero p {
        margin: 0;
        color: #c1d7f1;
        font-size: 13px;
    }
    .container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
        gap: 14px;
        width: 100%;
    }
    .card {
        background: #132033;
        border: 1px solid #2d4f79;
        border-radius: 12px;
        padding: 10px;
        overflow: hidden;
        box-shadow: 0 8px 20px rgba(1, 7, 18, 0.35);
    }
    .thumb {
        width: 100%;
        aspect-ratio: 16 / 9;
        object-fit: cover;
        border-radius: 10px;
        border: 1px solid #355b89;
        background: #101928;
    }
    .content {
        padding: 10px 4px 4px 4px;
    }
    .title {
        font-size: 19px;
        font-weight: bold;
        color: #f0f7ff;
        margin-bottom: 5px;
    }
    .desc {
        font-size: 13px;
        color: #c8dbf3;
        margin-bottom: 8px;
        line-height: 1.35;
    }
    .meta {
        font-size: 12px;
        color: #abd0f8;
        line-height: 1.45;
        margin-bottom: 10px;
    }
    .meta b {
        color: #dbedff;
    }
    .btn {
        display: inline-block;
        padding: 8px 14px;
        background: #26d38a;
        color: #072218;
        text-decoration: none;
        border-radius: 8px;
        font-size: 12px;
        font-weight: bold;
    }
    .btn:hover {
        background: #31e79b;
    }
    @media (max-width: 620px) {
        body {
            padding: 10px;
        }
        .hero h2 {
            font-size: 19px;
        }
        .title {
            font-size: 17px;
        }
    }
</style>
</head>
<body>
    <div class="container">
"""
