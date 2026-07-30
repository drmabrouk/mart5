# -*- coding: utf-8 -*-
from html.parser import HTMLParser

class TagBalanceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        # We only track critical layout tags
        self.tracked_tags = {'div', 'table', 'tr', 'td', 'p', 'svg', 'h1', 'h2', 'span'}
        self.page_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            # Check if page-container
            for attr, val in attrs:
                if attr == 'class' and val == 'page-container':
                    self.page_count += 1

        if tag in self.tracked_tags:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.tracked_tags:
            if not self.stack:
                self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
                return

            last_tag, pos = self.stack.pop()
            if last_tag != tag:
                # We have a mismatch, search the stack
                self.errors.append(f"Mismatched tag: opened <{last_tag}> at line {pos[0]}, col {pos[1]} but closed with </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
                # Put last_tag back or let's clean up
                self.stack.append((last_tag, pos))

    def check_unclosed(self):
        while self.stack:
            tag, pos = self.stack.pop()
            self.errors.append(f"Unclosed tag <{tag}> opened at line {pos[0]}, col {pos[1]}")

def main():
    print("Parsing MART.html for HTML balance...")
    with open("MART.html", "r", encoding="utf-8") as f:
        content = f.read()

    parser = TagBalanceParser()
    try:
        parser.feed(content)
        parser.check_unclosed()
    except Exception as e:
        print(f"Parser error: {e}")
        return False

    print(f"Total page-containers found: {parser.page_count}")

    if parser.errors:
        print(f"Found {len(parser.errors)} validation issues:")
        for err in parser.errors[:20]:
            print("  -", err)
        if len(parser.errors) > 20:
            print("  - ... and more issues ...")
        return False
    else:
        print("HTML validation passed! No mismatched or unclosed tags found.")
        return True

if __name__ == "__main__":
    import sys
    if not main():
        sys.exit(1)
