html = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>No Giveaway</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&display=swap');

  :root {
    --neon-blue: #00d4ff;
    --neon-purple: #bf5af2;
    --neon-dim: rgba(0, 212, 255, 0.3);
    --dark: #04050f;
    --grid: rgba(0, 212, 255, 0.05);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html, body {
    width: 100%; height: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    background: var(--dark);
    font-family: 'Rajdhani', sans-serif;
    color: #fff;
  }

  /* ── BACKGROUND ── */
  .bg {
    position: fixed; inset: 0; z-index: 0;
    background:
      radial-gradient(ellipse 70% 50% at 50% 40%, rgba(191,90,242,0.07) 0%, transparent 70%),
      radial-gradient(ellipse 50% 60% at 20% 80%, rgba(0,212,255,0.06) 0%, transparent 60%),
      #04050f;
  }
  .grid {
    position: fixed; inset: 0; z-index: 0;
    background-image:
      linear-gradient(var(--grid) 1px, transparent 1px),
      linear-gradient(90deg, var(--grid) 1px, transparent 1px);
    background-size: 52px 52px;
    animation: gridScroll 25s linear infinite;
  }
  @keyframes gridScroll {
    from { background-position: 0 0; }
    to   { background-position: 0 104px; }
  }
  .scanlines {
    position: fixed; inset: 0; z-index: 0;
    background: repeating-linear-gradient(
      0deg, transparent, transparent 3px,
      rgba(0,0,0,0.07) 3px, rgba(0,0,0,0.07) 4px
    );
    pointer-events: none;
  }

  /* ── CORNERS ── */
  .corner { position: fixed; width: 42px; height: 42px; }
  .tl { top:0; left:0;  border-top: 1.5px solid var(--neon-blue); border-left: 1.5px solid var(--neon-blue); }
  .tr { top:0; right:0; border-top: 1.5px solid var(--neon-purple); border-right: 1.5px solid var(--neon-purple); }
  .bl { bottom:0; left:0;  border-bottom: 1.5px solid var(--neon-purple); border-left: 1.5px solid var(--neon-purple); }
  .br { bottom:0; right:0; border-bottom: 1.5px solid var(--neon-blue); border-right: 1.5px solid var(--neon-blue); }

  /* ── STAGE ── */
  .stage {
    position: relative; z-index: 1;
    width: 100%;
    min-height: calc(100vh - 36px);
    display: flex; flex-direction: column;
    align-items: center; justify-content: flex-start;
    padding: 24px 14px 8px;
    gap: 0;
  }

  /* ── BROKEN CONTROLLER ICON ── */
  .icon-wrap {
    position: relative;
    margin-bottom: 14px;
    animation: fadeUp 0.8s ease 0.1s both;
  }

  .controller-svg {
    width: 86px; height: 58px;
    opacity: 0.35;
    filter: drop-shadow(0 0 12px rgba(0, 212, 255, 0.3));
    animation: iconFloat 5s ease-in-out infinite;
  }
  @keyframes iconFloat {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-8px); }
  }

  /* Question mark floating above icon */
  .qmark {
    position: absolute;
    top: -12px; left: 50%;
    transform: translateX(-50%);
    font-family: 'Orbitron', monospace;
    font-size: 20px; font-weight: 900;
    color: transparent;
    -webkit-text-stroke: 1.5px rgba(0,212,255,0.4);
    animation: qPulse 3s ease-in-out infinite;
  }
  @keyframes qPulse {
    0%, 100% { -webkit-text-stroke-color: rgba(0,212,255,0.3); transform: translateX(-50%) scale(1); }
    50%       { -webkit-text-stroke-color: rgba(191,90,242,0.6); transform: translateX(-50%) scale(1.08); }
  }

  /* ── OOPS HEADLINE ── */
  .headline-wrap {
    text-align: center;
    margin-bottom: 10px;
    animation: fadeUp 0.9s ease 0.25s both;
  }
  .oops-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: rgba(0,212,255,0.5);
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .oops-main {
    font-family: 'Orbitron', monospace;
    font-size: clamp(28px, 5vw, 52px);
    font-weight: 900;
    line-height: 1;
    letter-spacing: -1px;
    color: transparent;
    -webkit-text-stroke: 2px rgba(255,255,255,0.12);
    background: linear-gradient(135deg, rgba(255,255,255,0.6) 0%, rgba(120,120,180,0.5) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    position: relative;
  }

  /* Glitch layers */
  .oops-main::before {
    content: 'OOPS!';
    position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(0,212,255,0.5) 0%, rgba(191,90,242,0.5) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glitchA 7s infinite;
    clip-path: polygon(0 30%, 100% 30%, 100% 50%, 0 50%);
  }
  .oops-main::after {
    content: 'OOPS!';
    position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(191,90,242,0.5) 0%, rgba(0,212,255,0.5) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glitchB 7s infinite;
    clip-path: polygon(0 65%, 100% 65%, 100% 80%, 0 80%);
  }
  @keyframes glitchA {
    0%,85%,100% { transform: translate(0); opacity:0; }
    86% { transform: translate(-4px,1px); opacity:0.8; }
    88% { transform: translate(3px,-1px); opacity:0.8; }
    90% { transform: translate(0); opacity:0; }
  }
  @keyframes glitchB {
    0%,82%,100% { transform: translate(0); opacity:0; }
    83% { transform: translate(4px,1px); opacity:0.8; }
    85% { transform: translate(-3px,-1px); opacity:0.8; }
    87% { transform: translate(0); opacity:0; }
  }

  /* ── DIVIDER ── */
  .divider {
    width: 200px; height: 1px;
    margin: 0 auto 10px;
    background: linear-gradient(90deg, transparent, rgba(0,212,255,0.3), rgba(191,90,242,0.3), transparent);
    animation: fadeUp 0.9s ease 0.4s both;
  }

  /* ── MESSAGE BOX ── */
  .msg-box {
    position: relative;
    max-width: 420px;
    width: 100%;
    text-align: center;
    padding: 16px 16px;
    border: 1px solid rgba(0,212,255,0.1);
    border-radius: 8px;
    background: rgba(0,0,0,0.3);
    margin-bottom: 12px;
    animation: fadeUp 1s ease 0.5s both;
    overflow: hidden;
  }
  /* top accent line */
  .msg-box::before {
    content: '';
    position: absolute; top: 0; left: 50%;
    transform: translateX(-50%);
    width: 60%; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,212,255,0.5), transparent);
  }
  /* shimmer sweep */
  .msg-box::after {
    content: '';
    position: absolute; top: 0; left: -100%;
    width: 50%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.025), transparent);
    animation: sweep 6s ease-in-out infinite;
  }
  @keyframes sweep {
    0%,100% { left: -100%; }
    50%      { left: 150%; }
  }

  .msg-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(13px, 2vw, 16px);
    font-weight: 700;
    letter-spacing: 1px;
    color: rgba(255,255,255,0.7);
    margin-bottom: 8px;
    line-height: 1.4;
  }
  .msg-sub {
    font-family: 'Rajdhani', sans-serif;
    font-size: clamp(13px, 1.8vw, 15px);
    font-weight: 600;
    color: rgba(255,255,255,0.3);
    letter-spacing: 0.5px;
    line-height: 1.45;
  }
  .msg-sub span {
    color: rgba(0,212,255,0.55);
  }

  /* ── STATUS CHIPS ── */
  .chips {
    display: flex; gap: 12px; flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 10px;
    animation: fadeUp 1s ease 0.65s both;
  }
  .chip {
    display: flex; align-items: center; gap: 7px;
    padding: 6px 12px;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 4px;
    background: rgba(0,0,0,0.25);
    font-family: 'Share Tech Mono', monospace;
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.3);
  }
  .chip-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: rgba(0,212,255,0.3);
  }

  /* ── RETRY / NOTIFY BUTTON ── */
  .btn-wrap {
    animation: fadeUp 1s ease 0.8s both;
  }
  .btn {
    font-family: 'Orbitron', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.5);
    background: transparent;
    border: 1px solid rgba(0,212,255,0.2);
    padding: 13px 40px;
    border-radius: 4px;
    cursor: pointer;
    clip-path: polygon(10px 0%, 100% 0%, calc(100% - 10px) 100%, 0% 100%);
    transition: color 0.3s, border-color 0.3s, box-shadow 0.3s;
  }
  .btn:hover {
    color: var(--neon-blue);
    border-color: rgba(0,212,255,0.5);
    box-shadow: 0 0 20px rgba(0,212,255,0.2), inset 0 0 20px rgba(0,212,255,0.04);
  }

  /* ── TICKER ── */
  .ticker-wrap {
    position: sticky; bottom: 0; left: 0; right: 0;
    padding: 7px 0;
    background: rgba(0,0,0,0.5);
    border-top: 1px solid rgba(0,212,255,0.08);
    overflow: hidden;
    animation: fadeUp 1s ease 1s both;
    z-index: 2;
  }
  .ticker-inner {
    display: flex;
    white-space: nowrap;
    animation: ticker 22s linear infinite;
  }
  .ticker-item {
    font-family: 'Share Tech Mono', monospace;
    font-size: 9px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.18);
    padding-right: 44px;
  }
  .ticker-item span {
    color: rgba(0,212,255,0.3);
  }
  @keyframes ticker {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── RESPONSIVE ── */
  @media (max-height: 700px) {
    .stage { padding-top: 18px; }
    .icon-wrap { margin-bottom: 10px; }
    .controller-svg { width: 76px; height: 50px; }
    .msg-box { padding: 12px 12px; margin-bottom: 10px; }
    .chips { margin-bottom: 8px; }
  }
</style>
</head>
<body>

<div class="bg"></div>
<div class="grid"></div>
<div class="scanlines"></div>

<!-- corner accents -->
<div class="corner tl"></div>
<div class="corner tr"></div>
<div class="corner bl"></div>
<div class="corner br"></div>

<div class="stage">

  <!-- broken controller -->
  <div class="icon-wrap">
    <div class="qmark">?</div>
    <svg class="controller-svg" viewBox="0 0 120 80" fill="none" xmlns="http://www.w3.org/2000/svg">
      <!-- body left -->
      <path d="M10 38 C8 28, 14 16, 28 14 L50 14 L50 52 L28 56 C14 56, 10 50, 10 38Z"
            fill="rgba(0,212,255,0.08)" stroke="rgba(0,212,255,0.4)" stroke-width="1.5"/>
      <!-- body right -->
      <path d="M110 38 C112 28, 106 16, 92 14 L70 14 L70 52 L92 56 C106 56, 110 50, 110 38Z"
            fill="rgba(0,212,255,0.08)" stroke="rgba(0,212,255,0.4)" stroke-width="1.5"/>
      <!-- middle bridge -->
      <rect x="50" y="18" width="20" height="30" rx="2"
            fill="rgba(0,212,255,0.05)" stroke="rgba(0,212,255,0.25)" stroke-width="1"/>
      <!-- d-pad vertical -->
      <rect x="22" y="28" width="6" height="18" rx="1" fill="rgba(0,212,255,0.3)"/>
      <!-- d-pad horizontal -->
      <rect x="18" y="32" width="14" height="6" rx="1" fill="rgba(0,212,255,0.3)"/>
      <!-- buttons right side -->
      <circle cx="90" cy="28" r="3" fill="rgba(191,90,242,0.45)"/>
      <circle cx="98" cy="34" r="3" fill="rgba(0,212,255,0.45)"/>
      <circle cx="90" cy="40" r="3" fill="rgba(255,180,0,0.3)"/>
      <circle cx="82" cy="34" r="3" fill="rgba(80,220,80,0.3)"/>
      <!-- analog sticks -->
      <circle cx="38" cy="46" r="5" fill="none" stroke="rgba(0,212,255,0.3)" stroke-width="1"/>
      <circle cx="82" cy="46" r="5" fill="none" stroke="rgba(0,212,255,0.3)" stroke-width="1"/>
      <!-- crack / broken line across middle -->
      <path d="M48 18 L52 28 L58 22 L64 34 L72 26 L72 48"
            stroke="rgba(255,80,80,0.5)" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 2" fill="none"/>
    </svg>
  </div>

  <!-- headline -->
  <div class="headline-wrap">
    <div class="oops-label">// Status: No Active Drop</div>
    <h1 class="oops-main">OOPS!</h1>
  </div>

  <div class="divider"></div>

  <!-- message -->
  <div class="msg-box">
    <div class="msg-title">No Giveaway Happening Right Now</div>
    <div class="msg-sub">
      Looks like there's <span>no active loot drop</span> or free title available at the moment.<br>
      Check back later — free games don't stay quiet for long.
    </div>
  </div>

  <!-- status chips -->
  <div class="chips">
    <div class="chip"><div class="chip-dot"></div>Active drops: 0</div>
    <div class="chip"><div class="chip-dot"></div>Free titles: None</div>
    <div class="chip"><div class="chip-dot"></div>Loot available: Nope</div>
  </div>

</div>

<!-- bottom ticker -->
<div class="ticker-wrap">
  <div class="ticker-inner">
    <span class="ticker-item">No active giveaways &nbsp;·&nbsp; <span>0 free games available</span> &nbsp;·&nbsp; Come back soon &nbsp;·&nbsp; Free loot will return &nbsp;·&nbsp; No drops active &nbsp;·&nbsp;</span>
    <span class="ticker-item">No active giveaways &nbsp;·&nbsp; <span>0 free games available</span> &nbsp;·&nbsp; Come back soon &nbsp;·&nbsp; Free loot will return &nbsp;·&nbsp; No drops active &nbsp;·&nbsp;</span>
  </div>
</div>

</body>
</html>
"""
