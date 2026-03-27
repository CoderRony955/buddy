def html(logo: str, name: str) -> str:
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Games Giveaway</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@400;600;700&family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

  :root {
    --neon-blue: #00d4ff;
    --neon-purple: #bf5af2;
    --neon-pink: #ff2d78;
    --epic-white: #f0f0f0;
    --dark-base: #050510;
    --grid-color: rgba(0, 212, 255, 0.06);
    --card-bg: rgba(0, 212, 255, 0.04);
    --glow-blue: 0 0 20px rgba(0, 212, 255, 0.5), 0 0 60px rgba(0, 212, 255, 0.2);
    --glow-purple: 0 0 20px rgba(191, 90, 242, 0.5), 0 0 60px rgba(191, 90, 242, 0.2);
    --glow-pink: 0 0 20px rgba(255, 45, 120, 0.6), 0 0 60px rgba(255, 45, 120, 0.25);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html, body {
    width: 100%; height: 100%;
    overflow-x: hidden;
    overflow-y: auto;
    font-family: 'Rajdhani', sans-serif;
    background: var(--dark-base);
    color: var(--epic-white);
  }

  /* ── BACKGROUND LAYERS ── */
  .bg-wrap {
    position: fixed; inset: 0; z-index: 0;
  }

  /* Gradient nebula */
  .bg-nebula {
    position: absolute; inset: 0;
    background:
      radial-gradient(ellipse 80% 60% at 20% 10%, rgba(191,90,242,0.18) 0%, transparent 60%),
      radial-gradient(ellipse 60% 80% at 80% 90%, rgba(0,212,255,0.14) 0%, transparent 55%),
      radial-gradient(ellipse 50% 50% at 50% 50%, rgba(255,45,120,0.07) 0%, transparent 70%),
      #050510;
  }

  /* Grid overlay */
  .bg-grid {
    position: absolute; inset: 0;
    background-image:
      linear-gradient(var(--grid-color) 1px, transparent 1px),
      linear-gradient(90deg, var(--grid-color) 1px, transparent 1px);
    background-size: 48px 48px;
    animation: gridDrift 30s linear infinite;
  }

  @keyframes gridDrift {
    from { background-position: 0 0; }
    to   { background-position: 0 96px; }
  }

  /* Scan-lines */
  .bg-scan {
    position: absolute; inset: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 3px,
      rgba(0,0,0,0.08) 3px,
      rgba(0,0,0,0.08) 4px
    );
    pointer-events: none;
  }

  /* Floating particles */
  .particles { position: absolute; inset: 0; overflow: hidden; }
  .particle {
    position: absolute;
    border-radius: 50%;
    animation: floatUp linear infinite;
    opacity: 0;
  }
  .particle:nth-child(odd)  { background: var(--neon-blue);   box-shadow: 0 0 6px var(--neon-blue); }
  .particle:nth-child(even) { background: var(--neon-purple); box-shadow: 0 0 6px var(--neon-purple); }
  .particle:nth-child(3n)   { background: var(--neon-pink);   box-shadow: 0 0 6px var(--neon-pink); }

  @keyframes floatUp {
    0%   { transform: translateY(110vh) scale(0); opacity: 0; }
    10%  { opacity: 1; }
    90%  { opacity: 0.6; }
    100% { transform: translateY(-10vh) scale(1); opacity: 0; }
  }

  /* ── MAIN LAYOUT ── */
  .stage {
    position: relative; z-index: 1;
    width: 100vw;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    gap: 0;
    padding: 14px 20px 16px;
  }

  /* ── TOP CORNER DECO ── */
  .corner { position: fixed; width: 80px; height: 80px; }
  .corner--tl { top: 0; left: 0; border-top: 2px solid var(--neon-blue); border-left: 2px solid var(--neon-blue); }
  .corner--tr { top: 0; right: 0; border-top: 2px solid var(--neon-purple); border-right: 2px solid var(--neon-purple); }
  .corner--bl { bottom: 0; left: 0; border-bottom: 2px solid var(--neon-purple); border-left: 2px solid var(--neon-purple); }
  .corner--br { bottom: 0; right: 0; border-bottom: 2px solid var(--neon-blue); border-right: 2px solid var(--neon-blue); }

  /* ── LIVE BADGE ── */
  .live-badge {
    display: flex; align-items: center; gap: 8px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    color: var(--neon-pink);
    text-transform: uppercase;
    margin-bottom: 12px;
    animation: fadeSlide 0.8s ease 0.2s both;
  }
  .live-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--neon-pink);
    box-shadow: 0 0 10px var(--neon-pink);
    animation: pulse 1.4s ease-in-out infinite;
  }
  @keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 1; }
    50%       { transform: scale(1.5); opacity: 0.5; }
  }

  /* ── EPIC LOGO BLOCK ── */
  .logo-block {
    display: flex; flex-direction: column; align-items: center;
    margin-bottom: 16px;
    animation: fadeSlide 0.9s ease 0.4s both;
  }

  .epic-logo-svg {
    width: 74px; height: 74px;
    filter: drop-shadow(0 0 18px rgba(255,255,255,0.5)) drop-shadow(0 0 40px rgba(0,212,255,0.4));
    animation: logoPulse 4s ease-in-out infinite;
  }
  @keyframes logoPulse {
    0%, 100% { filter: drop-shadow(0 0 18px rgba(255,255,255,0.5)) drop-shadow(0 0 40px rgba(0,212,255,0.4)); }
    50%       { filter: drop-shadow(0 0 28px rgba(255,255,255,0.8)) drop-shadow(0 0 70px rgba(0,212,255,0.7)); }
  }

  .epic-wordmark {
    font-family: 'Orbitron', monospace;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 6px;
    color: rgba(255,255,255,0.55);
    margin-top: 6px;
    text-transform: uppercase;
  }

  /* ── HEADLINE ── */
  .headline-wrap {
    text-align: center;
    margin-bottom: 16px;
    animation: fadeSlide 0.9s ease 0.6s both;
  }

  .headline-eyebrow {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 4px;
    color: var(--neon-blue);
    text-transform: uppercase;
    margin-bottom: 6px;
    text-shadow: 0 0 10px var(--neon-blue);
  }

  .headline-main {
    font-family: 'Orbitron', monospace;
    font-size: clamp(24px, 4.3vw, 48px);
    font-weight: 900;
    line-height: 1.05;
    text-transform: uppercase;
    letter-spacing: -1px;
    background: linear-gradient(135deg, #fff 0%, var(--neon-blue) 45%, var(--neon-purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 30px rgba(0,212,255,0.4));
  }

  .headline-sub {
    font-family: 'Rajdhani', sans-serif;
    font-size: clamp(12px, 1.8vw, 16px);
    font-weight: 600;
    color: rgba(255,255,255,0.5);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 4px;
  }

  /* ── DIVIDER ── */
  .divider {
    width: 220px; height: 1px;
    margin: 0 auto 14px;
    background: linear-gradient(90deg, transparent, var(--neon-blue), var(--neon-purple), transparent);
    box-shadow: 0 0 12px rgba(0,212,255,0.4);
    animation: fadeSlide 0.9s ease 0.75s both;
  }

  /* ── LOOT CARDS ── */
  .loot-grid {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 10px;
    animation: fadeSlide 1s ease 0.9s both;
  }

  .loot-card {
    width: 132px;
    background: var(--card-bg);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 8px;
    padding: 14px 10px;
    text-align: center;
    position: relative;
    overflow: hidden;
    cursor: default;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
  }
  .loot-card::before {
    content: '';
    position: absolute; top: 0; left: -100%;
    width: 60%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.05), transparent);
    transition: left 0.5s ease;
  }
  .loot-card:hover::before { left: 150%; }
  .loot-card:hover {
    transform: translateY(-6px);
    border-color: var(--neon-blue);
    box-shadow: var(--glow-blue), inset 0 0 20px rgba(0,212,255,0.04);
  }

  .loot-card--purple:hover { border-color: var(--neon-purple); box-shadow: var(--glow-purple), inset 0 0 20px rgba(191,90,242,0.04); }
  .loot-card--pink:hover   { border-color: var(--neon-pink);   box-shadow: var(--glow-pink), inset 0 0 20px rgba(255,45,120,0.04); }

  .loot-icon { font-size: 32px; margin-bottom: 10px; display: block; }
  .loot-label {
    font-family: 'Rajdhani', sans-serif;
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--neon-blue);
    margin-bottom: 4px;
  }
  .loot-card--purple .loot-label { color: var(--neon-purple); }
  .loot-card--pink   .loot-label { color: var(--neon-pink); }
  .loot-name {
    font-family: 'Orbitron', monospace;
    font-size: 10px;
    font-weight: 700;
    color: rgba(255,255,255,0.85);
    line-height: 1.3;
  }

  /* ── TIMER STRIP ── */
  .timer-strip {
    display: flex; align-items: center; gap: 20px;
    background: rgba(0,0,0,0.4);
    border: 1px solid rgba(0,212,255,0.12);
    border-radius: 6px;
    padding: 12px 28px;
    margin-bottom: 32px;
    animation: fadeSlide 1s ease 1.1s both;
  }
  .timer-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: rgba(255,255,255,0.35);
    text-transform: uppercase;
  }
  .timer-seg {
    text-align: center;
  }
  .timer-num {
    font-family: 'Orbitron', monospace;
    font-size: 22px;
    font-weight: 900;
    color: var(--neon-blue);
    text-shadow: 0 0 14px var(--neon-blue);
    line-height: 1;
  }
  .timer-unit {
    font-family: 'Share Tech Mono', monospace;
    font-size: 9px;
    letter-spacing: 2px;
    color: rgba(255,255,255,0.3);
    text-transform: uppercase;
    margin-top: 2px;
  }
  .timer-colon {
    font-family: 'Orbitron', monospace;
    font-size: 20px;
    color: rgba(0,212,255,0.4);
    animation: blink 1s step-end infinite;
    margin-bottom: 10px;
  }
  @keyframes blink { 50% { opacity: 0; } }

  /* ── CTA BUTTON ── */
  .cta-wrap {
    animation: fadeSlide 1s ease 1.25s both;
  }
  .cta-btn {
    position: relative;
    font-family: 'Orbitron', monospace;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #000;
    background: linear-gradient(135deg, var(--neon-blue) 0%, var(--neon-purple) 100%);
    border: none;
    padding: 16px 52px;
    border-radius: 4px;
    cursor: pointer;
    clip-path: polygon(12px 0%, 100% 0%, calc(100% - 12px) 100%, 0% 100%);
    box-shadow: 0 0 30px rgba(0,212,255,0.4), 0 0 80px rgba(191,90,242,0.2);
    transition: box-shadow 0.3s ease, transform 0.2s ease;
    overflow: hidden;
  }
  .cta-btn::after {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.15), transparent 50%);
    pointer-events: none;
  }
  .cta-btn:hover {
    transform: scale(1.04);
    box-shadow: 0 0 50px rgba(0,212,255,0.7), 0 0 120px rgba(191,90,242,0.4);
  }
  .cta-btn:active { transform: scale(0.98); }

  /* ── FOOTER TEXT ── */
  .footer-note {
    margin-top: 20px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    color: rgba(255,255,255,0.18);
    text-transform: uppercase;
    animation: fadeSlide 1s ease 1.4s both;
  }

  /* ── ANIMATIONS ── */
  @keyframes fadeSlide {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  /* ── GLITCH EFFECT on headline ── */
  .glitch {
    position: relative;
    display: inline-block;
  }
  .glitch::before, .glitch::after {
    content: attr(data-text);
    position: absolute; inset: 0;
    background: linear-gradient(135deg, #fff 0%, var(--neon-blue) 45%, var(--neon-purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .glitch::before {
    animation: glitch1 5s infinite;
    clip-path: polygon(0 20%, 100% 20%, 100% 40%, 0 40%);
    transform: translateX(-2px);
    opacity: 0.7;
  }
  .glitch::after {
    animation: glitch2 5s infinite;
    clip-path: polygon(0 60%, 100% 60%, 100% 80%, 0 80%);
    transform: translateX(2px);
    opacity: 0.7;
  }
  @keyframes glitch1 {
    0%, 90%, 100% { transform: translateX(0); opacity: 0; }
    91% { transform: translateX(-3px); opacity: 0.7; }
    93% { transform: translateX(3px); opacity: 0.7; }
    95% { transform: translateX(0); opacity: 0; }
  }
  @keyframes glitch2 {
    0%, 88%, 100% { transform: translateX(0); opacity: 0; }
    89% { transform: translateX(3px); opacity: 0.7; }
    91% { transform: translateX(-3px); opacity: 0.7; }
    93% { transform: translateX(0); opacity: 0; }
  }

  /* Responsive shrink for PyQt embedded views */
  @media (max-height: 600px) {
    .loot-grid { gap: 10px; }
    .loot-card { width: 120px; padding: 12px 10px; }
    .headline-main { font-size: 30px; }
    .timer-num { font-size: 18px; }
    .epic-logo-svg { width: 64px; height: 64px; }
    .logo-block { margin-bottom: 16px; }
    .headline-wrap { margin-bottom: 18px; }
    .divider { margin-bottom: 18px; }
    .loot-grid { margin-bottom: 20px; }
    .timer-strip { margin-bottom: 20px; }
  }

  @media (max-height: 820px) {
    .corner { width: 56px; height: 56px; }
    .epic-logo-svg { width: 64px; height: 64px; }
    .headline-main { font-size: 28px; }
    .loot-card { width: 118px; padding: 12px 9px; }
    .loot-grid { gap: 10px; }
  }
</style>
</head>
<body>

<!-- BACKGROUND -->
<div class="bg-wrap">
  <div class="bg-nebula"></div>
  <div class="bg-grid"></div>
  <div class="bg-scan"></div>
  <div class="particles" id="particles"></div>
</div>

<!-- CORNER DECOR -->
<div class="corner corner--tl"></div>
<div class="corner corner--tr"></div>
<div class="corner corner--bl"></div>
<div class="corner corner--br"></div>

<!-- MAIN STAGE -->
<div class="stage">

  <!-- LOGO -->
  <div class="logo-block">
    <!-- Games SVG Logo (official E mark) -->
    <img src="__LOGO__" class="epic-logo-svg" alt="Games Logo">
    <div class="epic-wordmark">__NAME__</div>
  </div>

  <!-- HEADLINE -->
  <div class="headline-wrap">
    <div class="headline-eyebrow">// Free Loot Drop</div>
    <h1 class="headline-main">
      <span class="glitch" data-text="FREE GAMES">FREE GAMES</span>
    </h1>
    <div class="headline-sub">Check Live Giveaways — No Cost. No Catch.</div>
  </div>

  <div class="divider"></div>

  <!-- LOOT CARDS -->
  <div class="loot-grid">
    <div class="loot-card">
      <span class="loot-icon">🎮</span>
      <div class="loot-label">Free Title</div>
      <div class="loot-name">Full Game Unlock</div>
    </div>
    <div class="loot-card loot-card--purple">
      <span class="loot-icon">⚔️</span>
      <div class="loot-label">Rare Loot</div>
      <div class="loot-name">Legendary Skin Bundle</div>
    </div>
    <div class="loot-card loot-card--pink">
      <span class="loot-icon">💎</span>
      <div class="loot-label">Epic Drop</div>
      <div class="loot-name">In-Game Currency Pack</div>
    </div>
  </div>

</div>

<script>
  // ── Spawn particles ──
  (function() {
    const container = document.getElementById('particles');
    const count = 28;
    for (let i = 0; i < count; i++) {
      const p = document.createElement('div');
      p.className = 'particle';
      const size = Math.random() * 4 + 1.5;
      p.style.cssText = `
        width:${size}px; height:${size}px;
        left:${Math.random()*100}%;
        animation-duration:${Math.random()*14+8}s;
        animation-delay:${Math.random()*12}s;
      `;
      container.appendChild(p);
    }
  })();
</script>
</body>
</html>

""".replace("__LOGO__", logo).replace("__NAME__", name)
