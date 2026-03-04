import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Fix header img alt and src
text = text.replace('<img src="https://raw.githubusercontent.com/yboulaamane/CoumarinDB/main/header.png">', '<img src="./header.png" alt="CoumarinDB Logo">')

# Fix fav.ico
text = text.replace('href="https://raw.githubusercontent.com/yboulaamane/CoumarinDB/main/fav.ico"', 'href="./fav.ico"')

# Fix download buttons and invalid HTML nesting
old_buttons = """ <!-- Download buttons with updated style -->
<button style="background-color:#008a19; padding: 12px 24px; font-size: 16px; border: none; color: white; cursor: pointer;">
    <a href="https://github.com/yboulaamane/CoumarinDB/blob/main/coumarinDB-2D.sdf" target="_blank" style="text-decoration: none; color: white;">2D-SDF</a>
</button>
<button style="background-color:#008a19; padding: 12px 24px; font-size: 16px; border: none; color: white; cursor: pointer;">
    <a href="https://github.com/yboulaamane/CoumarinDB/blob/main/coumarinDB-3D.sdf" target="_blank" style="text-decoration: none; color: white;">3D-SDF</a>
</button>
<button style="background-color:#008a19; padding: 12px 24px; font-size: 16px; border: none; color: white; cursor: pointer;">
    <a href="https://github.com/yboulaamane/CoumarinDB/blob/main/coumarinDB-SMILES.smi" target="_blank" style="text-decoration: none; color: white;">SMILES</a>
</button>"""

new_buttons = """ <!-- Download buttons with updated style -->
<a href="./coumarinDB-2D.sdf" target="_blank" rel="noopener noreferrer" class="download-btn">2D-SDF</a>
<a href="./coumarinDB-3D.sdf" target="_blank" rel="noopener noreferrer" class="download-btn">3D-SDF</a>
<a href="./coumarinDB-SMILES.smi" target="_blank" rel="noopener noreferrer" class="download-btn">SMILES</a>"""

text = text.replace(old_buttons, new_buttons)

# Add CSS for buttons
css_addition = """    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">
    <style>
        .download-btn {
            display: inline-block;
            background-color: #008a19;
            padding: 12px 24px;
            font-size: 16px;
            border: none;
            color: white;
            cursor: pointer;
            text-decoration: none;
            border-radius: 4px;
            margin-right: 8px;
            margin-bottom: 8px;
            transition: opacity 0.2s;
        }
        .download-btn:hover, .download-btn:focus-visible {
            opacity: 0.9;
            color: white;
            outline: 2px solid #008a19;
            outline-offset: 2px;
        }
    </style>"""

text = text.replace('    <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css">', css_addition)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(text)
print("done")
