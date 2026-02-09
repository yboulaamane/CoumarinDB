from html.parser import HTMLParser
import json
import re
import sys

class CoumarinParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_thead = False
        self.in_tbody = False
        self.in_th = False
        self.in_tr = False
        self.in_td = False

        self.headers = []
        self.data = []
        self.current_row = {}
        self.current_cell_data = []
        self.current_col_index = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'thead':
            self.in_thead = True
        elif tag == 'tbody':
            self.in_tbody = True
        elif tag == 'tr':
            self.in_tr = True
            if self.in_tbody:
                self.current_row = {}
                self.current_col_index = 0
        elif tag == 'th':
            self.in_th = True
            self.current_cell_data = []
        elif tag == 'td':
            self.in_td = True
            self.current_cell_data = []
        elif tag == 'nl':
            if self.in_td:
                self.current_cell_data.append(", ")

    def handle_endtag(self, tag):
        if tag == 'thead':
            self.in_thead = False
        elif tag == 'tbody':
            self.in_tbody = False
        elif tag == 'tr':
            self.in_tr = False
            if self.in_tbody:
                if self.current_row:
                    self.data.append(self.current_row)
        elif tag == 'th':
            self.in_th = False
            if self.in_thead:
                header_text = "".join(self.current_cell_data).strip()
                # Clean up header text
                header_text = header_text.replace('\xa0', ' ').replace('&nbsp', ' ')
                # Convert to snake_case key
                key = re.sub(r'[^a-zA-Z0-9]', '_', header_text).lower()
                key = re.sub(r'_+', '_', key).strip('_')
                if key: # avoid empty headers
                    self.headers.append(key)
        elif tag == 'td':
            self.in_td = False
            if self.in_tbody:
                cell_text = "".join(self.current_cell_data).strip()
                # Use headers to map to keys
                if self.current_col_index < len(self.headers):
                    key = self.headers[self.current_col_index]
                    self.current_row[key] = cell_text
                    self.current_col_index += 1

    def handle_data(self, data):
        if self.in_th or self.in_td:
            self.current_cell_data.append(data)

def extract_data(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)

    parser = CoumarinParser()
    parser.feed(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(parser.data, f, indent=4)

    print(f"Extracted {len(parser.data)} rows.")
    print(f"Headers: {parser.headers}")

if __name__ == "__main__":
    extract_data('index.html', 'coumarins.json')
