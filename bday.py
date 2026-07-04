import streamlit as st
import time
import base64

st.set_page_config(
    page_title="Happy Birthday Hansika 🎂",
    page_icon="🎂",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,600;0,700;0,900;1,400&display=swap');

* { font-family: 'Poppins', sans-serif !important; box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
    background: linear-gradient(160deg, #0f0024 0%, #0d1a3e 40%, #1a0035 80%, #0a0015 100%) !important;
    min-height: 100vh;
}
[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"] {
    background: transparent !important; display: none !important;
}
.main .block-container { padding-top: 2rem; padding-bottom: 4rem; max-width: 780px; }

.hero-name {
    text-align: center;
    font-size: clamp(2.4rem, 7vw, 4rem);
    font-weight: 900;
    background: linear-gradient(90deg, #ff6eb4, #c084fc, #60a5fa, #ff6eb4);
    background-size: 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient-shift 4s ease infinite;
    line-height: 1.15;
    margin: 0.2rem 0;
}
.hero-sub {
    text-align: center;
    color: #c4b5fd;
    font-size: 1.05rem;
    letter-spacing: 0.05em;
    margin-bottom: 0.5rem;
}
.section-label {
    color: #a78bfa;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    text-align: center;
    margin: 2.8rem 0 0.8rem;
}
.glass-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(192,132,252,0.25);
    border-radius: 24px;
    padding: 2rem 2.2rem;
    margin: 0.8rem 0;
    color: #e8d5ff;
    line-height: 2;
    font-size: 1.04rem;
}
.highlight-card {
    background: linear-gradient(135deg, rgba(255,110,180,0.09), rgba(168,85,247,0.11));
    border: 1px solid rgba(255,110,180,0.32);
    border-radius: 24px;
    padding: 2rem 2.2rem;
    margin: 0.8rem 0;
    color: #fce7ff;
    font-size: 1.06rem;
    line-height: 2;
    text-align: center;
}
.pink-card {
    background: linear-gradient(135deg, rgba(255,110,180,0.06), rgba(192,132,252,0.06));
    border: 1px solid rgba(255,110,180,0.2);
    border-radius: 24px;
    padding: 2rem 2.2rem;
    margin: 0.8rem 0;
    color: #fce7ff;
    font-size: 1.04rem;
    line-height: 2;
}
.quote-card {
    border-left: 4px solid #a855f7;
    background: rgba(168,85,247,0.08);
    border-radius: 0 20px 20px 0;
    padding: 1.4rem 1.8rem;
    color: #d8b4fe;
    font-style: italic;
    font-size: 1.12rem;
    margin: 1.2rem 0;
    line-height: 1.85;
}
.soft-card {
    background: rgba(96,165,250,0.05);
    border: 1px solid rgba(96,165,250,0.18);
    border-radius: 20px;
    padding: 1.8rem 2.2rem;
    color: #bae6fd;
    margin: 0.8rem 0;
    font-size: 1.03rem;
    line-height: 2;
}
.wish-item {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 1rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    color: #e8d5ff;
    font-size: 1.02rem;
    line-height: 1.8;
}
.wish-icon { font-size: 1.5rem; margin-top: 2px; flex-shrink: 0; }
.closing-card {
    background: linear-gradient(135deg, rgba(168,85,247,0.13), rgba(255,110,180,0.09));
    border: 1px solid rgba(192,132,252,0.38);
    border-radius: 28px;
    padding: 2.5rem 2.2rem;
    text-align: center;
    color: #fce7ff;
    font-size: 1.08rem;
    line-height: 2.1;
    margin: 1rem 0;
}
.letter-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,200,230,0.15);
    border-radius: 24px;
    padding: 2.2rem 2.4rem;
    color: #f0d9ff;
    font-size: 1.05rem;
    line-height: 2.1;
    margin: 0.8rem 0;
    position: relative;
}
.photo-card {
    border-radius: 20px;
    overflow: hidden;
    border: 2px solid rgba(255,110,180,0.45);
    box-shadow: 0 0 28px rgba(168,85,247,0.35), 0 0 60px rgba(255,110,180,0.1);
    animation: pop-in 0.7s ease both;
    margin-bottom: 0.5rem;
}
.photo-caption {
    text-align: center;
    color: #c4b5fd;
    font-size: 0.85rem;
    margin-top: 0.3rem;
    font-style: italic;
    margin-bottom: 1rem;
}
.cake-wrap { text-align: center; }
.cake-big { font-size: 5.5rem; display: inline-block; animation: float 2.2s ease-in-out infinite; }
.balloon-row { text-align: center; margin: 1.5rem 0; }
.balloon-row span { display: inline-block; margin: 0 6px; }
.star-divider { text-align: center; color: #7c3aed; font-size: 1.1rem; margin: 1.2rem 0; letter-spacing: 0.5em; }
.lock-screen { text-align: center; padding: 3rem 1rem; }
.lock-emoji { font-size: 4rem; display: inline-block; animation: float 2s ease-in-out infinite; }
.lock-title { color: #c4b5fd; font-size: 1.5rem; font-weight: 700; margin: 1rem 0 0.3rem; }
.lock-sub { color: #7c6aad; font-size: 0.95rem; }
.stButton > button {
    background: linear-gradient(90deg, #ff6eb4, #a855f7, #60a5fa) !important;
    background-size: 200% !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.85rem 3rem !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    width: 100% !important;
    box-shadow: 0 4px 24px rgba(168,85,247,0.5) !important;
    transition: transform 0.2s, box-shadow 0.2s !important;
}
.stButton > button:hover {
    transform: scale(1.03) !important;
    box-shadow: 0 8px 36px rgba(255,110,180,0.6) !important;
}
[data-testid="stFileUploaderDropzone"] {
    background: rgba(255,255,255,0.03) !important;
    border: 2px dashed rgba(168,85,247,0.45) !important;
    border-radius: 18px !important;
    color: #a78bfa !important;
}
.stFileUploader label p { color: #c4b5fd !important; font-weight: 600; }

@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-14px)} }
@keyframes gradient-shift { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }
@keyframes pop-in { 0%{transform:scale(0.5) rotate(-4deg);opacity:0} 60%{transform:scale(1.05) rotate(1deg)} 100%{transform:scale(1) rotate(0);opacity:1} }
@keyframes fade-up { from{transform:translateY(30px);opacity:0} to{transform:translateY(0);opacity:1} }
.fade-up { animation: fade-up 0.7s ease both; }
</style>
""", unsafe_allow_html=True)

CONFETTI_JS = """<script>
(function(){
    const canvas=document.createElement('canvas');
    canvas.style.cssText='position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;';
    document.body.appendChild(canvas);
    const ctx=canvas.getContext('2d');
    canvas.width=window.innerWidth; canvas.height=window.innerHeight;
    const colors=['#ff6eb4','#a855f7','#60a5fa','#fbbf24','#34d399','#f87171','#fff','#c084fc','#fb7185'];
    const pieces=[];
    for(let i=0;i<240;i++){
        pieces.push({
            x:Math.random()*canvas.width,y:Math.random()*canvas.height-canvas.height,
            w:Math.random()*12+5,h:Math.random()*7+3,
            color:colors[Math.floor(Math.random()*colors.length)],
            speed:Math.random()*4+2,angle:Math.random()*Math.PI*2,
            spin:(Math.random()-0.5)*0.18,opacity:1,
            shape:Math.random()>0.6?'circle':'rect'
        });
    }
    let frame=0;
    function draw(){
        ctx.clearRect(0,0,canvas.width,canvas.height); frame++;
        pieces.forEach(p=>{
            p.y+=p.speed; p.angle+=p.spin; p.x+=Math.sin(p.angle)*2;
            if(frame>160) p.opacity-=0.005;
            ctx.save(); ctx.globalAlpha=Math.max(0,p.opacity);
            ctx.translate(p.x+p.w/2,p.y+p.h/2); ctx.rotate(p.angle);
            ctx.fillStyle=p.color;
            if(p.shape==='circle'){ctx.beginPath();ctx.arc(0,0,p.w/2,0,Math.PI*2);ctx.fill();}
            else ctx.fillRect(-p.w/2,-p.h/2,p.w,p.h);
            ctx.restore();
            if(p.y>canvas.height) p.y=-10;
        });
        if(frame<320) requestAnimationFrame(draw); else canvas.remove();
    }
    draw();
})();
</script>"""

MUSIC_JS = """<script>
(function(){
    try{
        const ac=new(window.AudioContext||window.webkitAudioContext)();
        const notes=[523,523,587,523,698,659,523,523,587,523,784,698,523,523,1047,880,698,659,587,880,880,784,698,784];
        const durs=[0.4,0.4,0.8,0.8,0.8,1.6,0.4,0.4,0.8,0.8,0.9,1.6,0.4,0.4,0.8,0.8,0.8,0.8,1.6,0.4,0.4,0.8,0.8,1.8];
        let t=ac.currentTime+0.2;
        notes.forEach((freq,i)=>{
            const osc=ac.createOscillator(),gain=ac.createGain();
            osc.connect(gain); gain.connect(ac.destination);
            osc.frequency.value=freq; osc.type='sine';
            gain.gain.setValueAtTime(0,t);
            gain.gain.linearRampToValueAtTime(0.15,t+0.06);
            gain.gain.linearRampToValueAtTime(0,t+durs[i]-0.05);
            osc.start(t); osc.stop(t+durs[i]); t+=durs[i];
        });
    }catch(e){}
})();
</script>"""

if "revealed" not in st.session_state:
    st.session_state.revealed = False
if "photos" not in st.session_state:
    st.session_state.photos = []

# ══════════════════════════════════════════════════
#  PRE-REVEAL SCREEN
# ══════════════════════════════════════════════════
if not st.session_state.revealed:
    st.markdown("""
    <div class="lock-screen">
        <span class="lock-emoji">🌙</span>
        <div class="lock-title">Something special is waiting for you...</div>
        <div class="lock-sub">Upload her photos & unlock the surprise at midnight 💜</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-label">📸 Add her photos</div>', unsafe_allow_html=True)
    uploaded = st.file_uploader(
        "Choose photos of Hansika",
        type=["jpg","jpeg","png","webp"],
        accept_multiple_files=True,
        label_visibility="collapsed"
    )
    if uploaded:
        st.session_state.photos = [f.read() for f in uploaded]
        st.markdown(f'<p style="text-align:center;color:#a78bfa;font-size:0.95rem;margin-top:0.8rem;">✅ {len(uploaded)} photo(s) ready ✨</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">🎁 when she\'s ready — press it</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🎉 Open Her Surprise!"):
        if not st.session_state.photos:
            st.warning("⚠️ Upload at least one photo first bro!")
        else:
            with st.spinner("Making it perfect..."):
                time.sleep(1.5)
            st.session_state.revealed = True
            st.rerun()

# ══════════════════════════════════════════════════
#  REVEALED
# ══════════════════════════════════════════════════
else:
    st.markdown(CONFETTI_JS, unsafe_allow_html=True)
    st.markdown(MUSIC_JS, unsafe_allow_html=True)

    # ── HERO ──
    st.markdown('<div class="cake-wrap"><span class="cake-big">🎂</span></div>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub">✨ on this very special night ✨</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-name">Happy Birthday,<br>Hansika 💜</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-sub" style="margin-top:0.6rem;font-size:0.95rem;color:#9b7fd4;">so glad you exist, Hansika 🥺</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="balloon-row">
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0s">🎈</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0.2s">🎀</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0.4s">🎊</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0.6s">💜</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0.8s">🌟</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 1s">🎈</span>
    </div>""", unsafe_allow_html=True)

    # ── PHOTOS ──
    st.markdown('<div class="section-label">📸 look at her though</div>', unsafe_allow_html=True)
    photos = st.session_state.photos
    captions = ["always her 🌸", "this one hits different 💜", "radiant as always ✨", "iconic, no debate 🎊", "she doesn't even try 🥺", "forever this girl 💫", "the room changes when she walks in 🌟", "proof that she's everything 💜"]
    if len(photos) == 1:
        b64 = base64.b64encode(photos[0]).decode()
        st.markdown(f'<div class="photo-card"><img src="data:image/jpeg;base64,{b64}" style="width:100%;display:block;"/></div><p class="photo-caption">always her 🌸</p>', unsafe_allow_html=True)
    else:
        for i in range(0, len(photos), 2):
            c1, c2 = st.columns(2)
            for j, col in enumerate([c1, c2]):
                idx = i + j
                if idx < len(photos):
                    b64 = base64.b64encode(photos[idx]).decode()
                    cap = captions[idx % len(captions)]
                    with col:
                        st.markdown(f'<div class="photo-card" style="animation-delay:{idx*0.12}s"><img src="data:image/jpeg;base64,{b64}" style="width:100%;display:block;border-radius:18px;"/></div><p class="photo-caption">{cap}</p>', unsafe_allow_html=True)

    # ── OPENING LETTER ──
    st.markdown('<div class="star-divider">· · · ✦ · · ·</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">💌 a letter. just for you.</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="letter-card fade-up">
        Hey Hansika. 🌸<br><br>
        It's midnight. Which means it's officially your day.<br>
        And before the chaos of calls and messages and celebrations begins —
        I just wanted to get here first. To say something that needed to be said.<br><br>
        I've been watching you show up for everyone around you —
        sometimes when you were tired, sometimes when you were hurting,
        sometimes when you had every reason <em>not</em> to.<br><br>
        But you always did. You always do.<br><br>
        And I don't think you realize how rare that is. 💜
    </div>""", unsafe_allow_html=True)

    # ── THE TRUTH ABOUT HER ──
    st.markdown('<div class="section-label">🌸 the thing nobody tells you enough</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card fade-up">
        Here's what I've noticed about you —<br><br>
        You have this incredible, almost instinctive way of making people feel
        like they matter. Like <em>truly</em> matter. You remember the small things.
        You check in when you sense something's off. You laugh at the right moments
        and go quiet at the right ones. You carry people's heaviness like it's nothing,
        like it's just part of who you are.<br><br>
        And it <em>is</em> part of who you are. That's the beautiful thing.<br><br>
        But here's the part that gets me, Hansika —<br>
        while you're busy being a safe place for the whole world,
        who's being a safe place for <em>you?</em><br><br>
        Who's asking <em>you</em> how you're really doing?<br>
        Who's remembering what <em>you're</em> going through?<br>
        Who's showing up for <em>you</em> the way you show up for everyone else? 🥺
    </div>""", unsafe_allow_html=True)



    st.markdown("""
    <div class="pink-card fade-up">
        Today is the one day where that changes.<br><br>
        Today is <em>yours.</em> Not theirs. Not everyone else's. Yours.<br><br>
        Today, you don't have to hold anything up. You don't have to be strong for anyone.
        You don't have to check in, follow up, or make sure everyone else is okay first.<br><br>
        You just get to <strong style="color:#ff9de2;">exist.</strong>
        Fully. Warmly. Without guilt. Without rushing.<br><br>
        Just you — and all the love you so freely give others,
        finally coming back around to you. 🌙
    </div>""", unsafe_allow_html=True)

    # ── NOTICED ──
    st.markdown('<div class="section-label">🌙 what I noticed about you</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card fade-up">
        You know what's funny? The more you pay attention to someone,
        the more you realize how much they've been hiding in plain sight.<br><br>
        And with you, Hansika — the more I see, the more I realize
        how much you underestimate yourself. Every single time.<br><br>
        Someone who gives without keeping score.<br>
        Someone who listens like it's the most important thing in the world.<br>
        Someone who makes ordinary moments feel like they actually meant something.<br>
        Someone who doesn't even realize the impact she leaves behind
        in every room she walks through. 🌟<br><br>
        You think you're just being normal.<br>
        But Hansika — what you are is <em>extraordinary.</em><br>
        And honestly? I don't think I'll ever fully get used to it.
    </div>""", unsafe_allow_html=True)

    # ── SOFT FUNNY ──
    st.markdown('<div class="section-label">😭 okay but also</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="soft-card fade-up">
        Can we talk about the fact that you spend so much time being everyone's
        person — and you still somehow act surprised when people care about you back? 😭<br><br>
        Like bestie. The audacity of being that kind, that warm, that effortlessly
        wonderful — and then going "wait, people actually like me?" 🤦<br><br>
        We do. We really, really do.<br><br>
        More than you know. More than you let yourself believe.<br><br>
        And one day — hopefully soon — I hope you look in the mirror and see
        exactly what the rest of us have been seeing this whole time. 💜<br><br>
        Because it's a lot, Hansika. It's genuinely a lot.
    </div>""", unsafe_allow_html=True)

    # ── DEEP EMOTIONAL ──
    st.markdown('<div class="section-label">💜 what I really want you to know</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="letter-card fade-up">
        I want you to know that the world is genuinely, measurably better
        because you're in it.<br><br>
        Not in a grand, abstract way. In the most specific, real way —<br><br>
        The conversations that went deeper because you were in them.<br>
        The people who felt less alone because you thought to check in.<br>
        The moments that became memories because you were there, being you.<br><br>
        That's not small. That's not nothing. That's <em>everything.</em><br><br>
        And I know you'll probably read this and think "oh they're just being nice."<br>
        But I need you to hear it differently this time:<br><br>
        <strong style="color:#ff9de2; font-size:1.1rem;">
        This is not kindness. This is the truth. And you deserve to finally receive it.
        </strong><br><br>
        You've spent so long pouring into others. Tonight, let this pour into you. 🌙
    </div>""", unsafe_allow_html=True)

    # ── WISHES ──
    st.markdown('<div class="section-label">🌟 everything I wish for you this year</div>', unsafe_allow_html=True)

    wishes = [
        ("🌸", "That you finally, <em>finally</em> start treating yourself with the same softness you give everyone else."),
        ("💜", "People who show up for you the way you show up for the whole world — without being asked."),
        ("🌙", "Quiet nights that feel like rest, not guilt. You are allowed to do nothing and still be enough."),
        ("✨", "That one thing you've been quietly hoping for — I hope it finds you this year, exactly when you need it."),
        ("😂", "At least one moment so good that you laugh until it hurts and forget everything else for a little while."),
        ("🔥", "A year that finally matches the energy you bring to everyone else's lives — big, warm, and full."),
        ("🧠", "The slow, growing realization of how capable you actually are. Because you are. Deeply."),
        ("🎯", "For things to stop being hard in the ways that have been quietly wearing you down."),
        ("💫", "Random, unplanned moments of joy — the kind that catch you off guard and remind you life is still good."),
        ("🌟", "The confidence to take up space. To ask for things. To need things. You're allowed to."),
        ("🎊", "Celebrations that actually feel like celebrations — not just days you get through."),
        ("💌", "To feel, at least once this year, as loved as you make everyone around you feel. Because you deserve that so much."),
    ]

    for icon, text in wishes:
        st.markdown(f'<div class="wish-item"><span class="wish-icon">{icon}</span><span>{text}</span></div>', unsafe_allow_html=True)

    # ── CLOSING ──
    st.markdown('<div class="star-divider">· · · ✦ · · ·</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-label">🎂 and finally</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="closing-card fade-up">
        <span style="font-size:2.5rem">💜</span><br><br>
        <strong style="font-size:1.25rem; color:#ff9de2;">Happy Birthday, Hansika.</strong><br><br>
        Thank you for being the kind of person who makes the people around you
        feel like they matter.<br><br>
        Now it's your turn to feel that. Starting tonight.<br><br>
        You don't have to earn love today. You don't have to do anything.
        Just exist — and know that simply <em>being you</em>
        is more than enough. It always has been. 🌙<br><br>
        Go eat your cake. Hug the people who love you.
        Stay up too late laughing. Be present. Be soft with yourself.<br><br>
        <em>And for once — let yourself be the one who's taken care of.</em><br><br>
        <span style="color:#a78bfa; font-size:0.95rem;">
            With so much warmth and genuine admiration 🌸<br>
            — someone who sees you, exactly as you are ✨
        </span>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="balloon-row" style="margin-top:2rem;">
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0s;display:inline-block">🎈</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0.25s;display:inline-block">🎀</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0.5s;display:inline-block">🎊</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 0.75s;display:inline-block">💜</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 1s;display:inline-block">🌟</span>
        <span style="font-size:2rem;animation:float 1.8s ease-in-out infinite 1.25s;display:inline-block">🎂</span>
    </div>""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🔄 Replay the Surprise"):
        st.session_state.revealed = False
        st.rerun()