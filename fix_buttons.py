import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add styles before </head>
styles = """
    <style>
        .download-btn {
            background-color: #008a19;
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            color: white;
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            margin-right: 8px;
        }
        .download-btn:hover {
            background-color: #006b13;
        }
        .download-btn:focus-visible {
            outline: 2px solid #008a19;
            outline-offset: 2px;
        }
    </style>
"""
if '<style>' not in content:
    content = content.replace('</head>', styles + '</head>')

# Replace nested buttons with styled links
old_buttons = """<button style="background-color:#008a19; padding: 12px 24px; font-size: 16px; border: none; color: white; cursor: pointer;">
    <a href="https://github.com/yboulaamane/CoumarinDB/blob/main/coumarinDB-2D.sdf" target="_blank" style="text-decoration: none; color: white;">2D-SDF</a>
</button>
<button style="background-color:#008a19; padding: 12px 24px; font-size: 16px; border: none; color: white; cursor: pointer;">
    <a href="https://github.com/yboulaamane/CoumarinDB/blob/main/coumarinDB-3D.sdf" target="_blank" style="text-decoration: none; color: white;">3D-SDF</a>
</button>
<button style="background-color:#008a19; padding: 12px 24px; font-size: 16px; border: none; color: white; cursor: pointer;">
    <a href="https://github.com/yboulaamane/CoumarinDB/blob/main/coumarinDB-SMILES.smi" target="_blank" style="text-decoration: none; color: white;">SMILES</a>
</button>"""

new_buttons = """<a href="coumarinDB-2D.sdf" class="download-btn" download>2D-SDF</a>
<a href="coumarinDB-3D.sdf" class="download-btn" download>3D-SDF</a>
<a href="coumarinDB-SMILES.smi" class="download-btn" download>SMILES</a>"""

if old_buttons in content:
    content = content.replace(old_buttons, new_buttons)
else:
    print("Old buttons not found exactly as expected. Trying regex...")
    # More robust regex replacement if whitespace varies
    pattern = re.compile(
        r'<button.*?><\s*a[^>]*href="[^"]*coumarinDB-2D\.sdf"[^>]*>2D-SDF</a>\s*</button>\s*'
        r'<button.*?><\s*a[^>]*href="[^"]*coumarinDB-3D\.sdf"[^>]*>3D-SDF</a>\s*</button>\s*'
        r'<button.*?><\s*a[^>]*href="[^"]*coumarinDB-SMILES\.smi"[^>]*>SMILES</a>\s*</button>',
        re.DOTALL
    )
    if pattern.search(content):
        content = pattern.sub(new_buttons, content)
        print("Regex replacement successful.")
    else:
        print("Regex replacement failed too.")


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
