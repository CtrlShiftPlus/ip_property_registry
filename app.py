def _page(content_html, title="IP Registry"):
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;600&family=Rajdhani:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        *,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
        :root{{
            --bg:#0a0c10;--surface:#111318;--surface2:#161a22;
            --border:#1e2330;--accent:#c8a96e;--accent2:#7eb8c9;
            --text:#e8e4dc;--muted:#6b7080;--error:#e07070;--ok:#6ec8a9;
        }}
        body{{
            background:var(--bg);color:var(--text);
            font-family:'Rajdhani',sans-serif;
            min-height:100vh;display:flex;align-items:center;
            justify-content:center;padding:40px 20px;position:relative;
        }}
        body::before{{
            content:'';position:fixed;inset:0;pointer-events:none;
            background:
                radial-gradient(ellipse 60% 50% at 20% 30%,rgba(126,184,201,.06) 0%,transparent 60%),
                radial-gradient(ellipse 55% 55% at 80% 75%,rgba(200,169,110,.07) 0%,transparent 60%);
        }}
        body::after{{
            content:'';position:fixed;inset:0;pointer-events:none;
            background-image:
                linear-gradient(rgba(200,169,110,.02) 1px,transparent 1px),
                linear-gradient(90deg,rgba(200,169,110,.02) 1px,transparent 1px);
            background-size:60px 60px;
        }}
        .card{{
            position:relative;z-index:10;
            background:var(--surface);border:1px solid var(--border);
            width:100%;max-width:560px;padding:48px 52px;
            animation:fadeIn .6s ease forwards;
        }}
        .card::before{{
            content:'';position:absolute;top:0;left:0;right:0;height:2px;
            background:linear-gradient(90deg,transparent,var(--accent),transparent);
        }}
        .card.error::before{{background:linear-gradient(90deg,transparent,var(--error),transparent)}}
        .card.success::before{{background:linear-gradient(90deg,transparent,var(--ok),transparent)}}
        @keyframes fadeIn{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
        .badge{{
            display:inline-flex;align-items:center;gap:8px;
            font-size:10px;letter-spacing:.3em;text-transform:uppercase;
            margin-bottom:16px;padding:6px 14px;border:1px solid;
        }}
        .badge.gold{{color:var(--accent);border-color:rgba(200,169,110,.25);background:rgba(200,169,110,.05)}}
        .badge.red{{color:var(--error);border-color:rgba(224,112,112,.25);background:rgba(224,112,112,.05)}}
        .badge.green{{color:var(--ok);border-color:rgba(110,200,169,.25);background:rgba(110,200,169,.05)}}
        .badge-dot{{width:5px;height:5px;border-radius:50%;background:currentColor;animation:blink 2s infinite}}
        @keyframes blink{{0%,100%{{opacity:1}}50%{{opacity:.2}}}}
        h2{{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:36px;line-height:1.1;margin-bottom:28px}}
        h2 .hi{{color:var(--accent)}}
        h2 .err{{color:var(--error)}}
        h2 .ok{{color:var(--ok)}}
        .divider{{height:1px;background:linear-gradient(90deg,transparent,var(--border),transparent);margin:28px 0}}
        .row{{display:flex;gap:12px;align-items:baseline;margin-bottom:14px}}
        .row-label{{
            font-size:10px;letter-spacing:.25em;text-transform:uppercase;
            color:var(--muted);font-weight:600;white-space:nowrap;min-width:100px;
        }}
        .row-value{{font-size:15px;letter-spacing:.03em;word-break:break-all}}
        .row-value.mono{{font-family:'Courier New',monospace;font-size:12px;color:var(--accent2)}}
        .row-value.id{{font-size:26px;font-weight:600;color:var(--accent)}}
        pre.error-trace{{
            background:var(--surface2);border:1px solid rgba(224,112,112,.2);
            padding:16px;font-size:12px;line-height:1.6;color:var(--error);
            white-space:pre-wrap;word-break:break-word;margin-bottom:24px;
        }}
        p.desc{{font-size:14px;color:var(--muted);margin-bottom:24px;line-height:1.6;letter-spacing:.03em}}
        .actions{{display:flex;gap:14px;margin-top:8px;flex-wrap:wrap}}
        a.btn{{
            display:inline-flex;align-items:center;gap:8px;text-decoration:none;
            font-size:12px;font-weight:600;letter-spacing:.15em;text-transform:uppercase;
            padding:12px 22px;border:1px solid;position:relative;overflow:hidden;
            transition:all .3s ease;
        }}
        a.btn::before{{
            content:'';position:absolute;inset:0;
            transform:scaleX(0);transform-origin:left;transition:transform .3s ease;
        }}
        a.btn:hover::before{{transform:scaleX(1)}}
        a.btn:hover{{color:var(--bg)}}
        a.btn.gold{{color:var(--accent);border-color:var(--accent)}}
        a.btn.gold::before{{background:var(--accent)}}
        a.btn.gold:hover{{box-shadow:0 0 24px rgba(200,169,110,.2)}}
        a.btn.muted{{color:var(--muted);border-color:var(--border)}}
        a.btn.muted::before{{background:var(--muted)}}
        .corner{{position:fixed;width:36px;height:36px}}
        .corner--tl{{top:20px;left:20px;border-top:1px solid var(--border);border-left:1px solid var(--border)}}
        .corner--tr{{top:20px;right:20px;border-top:1px solid var(--border);border-right:1px solid var(--border)}}
        .corner--bl{{bottom:20px;left:20px;border-bottom:1px solid var(--border);border-left:1px solid var(--border)}}
        .corner--br{{bottom:20px;right:20px;border-bottom:1px solid var(--border);border-right:1px solid var(--border)}}
    </style>
</head>
<body>
<div class="corner corner--tl"></div>
<div class="corner corner--tr"></div>
<div class="corner corner--bl"></div>
<div class="corner corner--br"></div>
{content_html}
</body>
</html>"""





from flask import Flask, render_template, request
import subprocess
import json
import re

app = Flask(__name__)

# Your deployed Stellar contract ID
CONTRACT_ID = "CC7LJ7NVULQ5S43MCA664GMB7LFRT6EVDIOIGP5AQ7B4SA3252K4MZ2X"

# Local funded signer key name from stellar keys ls
SOURCE_KEY = "alices"


# -------------------------------------------------
# Utility Functions
# -------------------------------------------------

def run_stellar_command(cmd):
    """
    Runs Stellar CLI command safely with UTF-8 handling.
    Returns output string.
    """
    return subprocess.check_output(
        cmd,
        text=True,
        encoding="utf-8",
        errors="ignore",
        stderr=subprocess.STDOUT
    ).strip()


def normalize_title(title):
    """
    Normalize title for duplicate checking.
    """
    title = title.lower().strip()
    title = re.sub(r'[^a-z0-9\s]', '', title)
    title = re.sub(r'\s+', ' ', title)
    return title


def valid_wallet(wallet):
    """
    Validate Stellar public key format.
    """
    return re.fullmatch(r"G[A-Z2-7]{55}", wallet) is not None


def get_record(record_id):
    """
    Fetch record from deployed contract by ID.
    Returns dict or None.
    """
    cmd = [
        "stellar", "contract", "invoke",
        "--id", CONTRACT_ID,
        "--source", SOURCE_KEY,
        "--network", "testnet",
        "--",
        "get",
        "--id", str(record_id)
    ]

    try:
        output = run_stellar_command(cmd)

        # Extract JSON only
        start = output.find("{")
        end = output.rfind("}")

        if start != -1 and end != -1:
            clean_json = output[start:end+1]
            return json.loads(clean_json)

        return None

    except Exception:
        return None


def is_duplicate_title(new_title):
    new_norm = normalize_title(new_title)

    misses = 0

    for i in range(1, 50):   # max 49 checks
        record = get_record(i)

        if record:
            misses = 0
            existing_title = record.get("title", "")

            old_norm = normalize_title(existing_title)

            if old_norm == new_norm or old_norm in new_norm or new_norm in old_norm:
                return True
        else:
            misses += 1

        # stop after 3 missing IDs in a row
        if misses >= 3:
            break

    return False


# -------------------------------------------------
# Routes
# -------------------------------------------------

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/register_ip', methods=['POST'])
def register_ip():
    title = request.form['title'].strip()
    description = request.form['description'].strip()
    wallet = request.form['wallet'].strip()
 
    # Wallet validation
    if not valid_wallet(wallet):
        return _page("""
        <div class="card error">
            <div class="badge red"><span class="badge-dot"></span>Validation Failed</div>
            <h2>Invalid <span class="err">Wallet</span><br>Address</h2>
            <p class="desc">The Freighter public wallet address provided is not valid.<br>
            Please double-check and try again.</p>
            <div class="actions">
                <a href="/register" class="btn gold">← Try Again</a>
                <a href="/" class="btn muted">Home</a>
            </div>
        </div>
        """, title="Invalid Wallet")
 
    # Duplicate check
    if is_duplicate_title(title):
        return _page(f"""
        <div class="card error">
            <div class="badge red"><span class="badge-dot"></span>Duplicate Detected</div>
            <h2>Property <span class="err">Already</span><br>Registered</h2>
            <div class="divider"></div>
            <div class="row">
                <span class="row-label">Title</span>
                <span class="row-value">{title}</span>
            </div>
            <div class="divider"></div>
            <p class="desc">A similar intellectual property title already exists on the ledger.</p>
            <div class="actions">
                <a href="/register" class="btn gold">← Register New</a>
                <a href="/" class="btn muted">Home</a>
            </div>
        </div>
        """, title="Duplicate Property")
 
    # Create new blockchain record
    cmd = [
        "stellar", "contract", "invoke",
        "--id", CONTRACT_ID,
        "--source", SOURCE_KEY,
        "--network", "testnet",
        "--",
        "create",
        "--title", title,
        "--description", description,
        "--owner", wallet
    ]
 
    try:
        output = run_stellar_command(cmd)
 
        match = re.search(r'(\d+)\s*$', output)
        registry_id = match.group(1) if match else output
 
        return _page(f"""
        <div class="card success">
            <div class="badge green"><span class="badge-dot"></span>On-Chain · Confirmed</div>
            <h2>Property <span class="ok">Registered</span><br>Successfully</h2>
            <div class="divider"></div>
            <div class="row">
                <span class="row-label">Registry ID</span>
                <span class="row-value id">#{registry_id}</span>
            </div>
            <div class="row">
                <span class="row-label">Title</span>
                <span class="row-value">{title}</span>
            </div>
            <div class="row">
                <span class="row-label">Owner</span>
                <span class="row-value mono">{wallet}</span>
            </div>
            <div class="divider"></div>
            <div class="actions">
                <a href="/" class="btn gold">Go Home →</a>
                <a href="/register" class="btn muted">Register Another</a>
            </div>
        </div>
        """, title="Registered Successfully")
 
    except Exception as e:
        return _page(f"""
        <div class="card error">
            <div class="badge red"><span class="badge-dot"></span>Transaction Failed</div>
            <h2>Error <span class="err">Registering</span><br>Property</h2>
            <div class="divider"></div>
            <pre class="error-trace">{str(e)}</pre>
            <div class="actions">
                <a href="/register" class="btn gold">← Try Again</a>
                <a href="/" class="btn muted">Home</a>
            </div>
        </div>
        """, title="Registration Error")
 


@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None

    if request.method == 'POST':
        ip_id = request.form['ip_id']

        record = get_record(ip_id)

        if record:
            result = f"""
Registry ID : {record['id']}
Title       : {record['title']}
Description : {record['description']}
Owner       : {record['owner']}
"""
        else:
            result = "No property found with this ID."

    return render_template("search.html", result=result)


# -------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)