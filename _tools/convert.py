#!/usr/bin/env python3
"""Convert the PieTTY Google Sites pages (saved HTML) into Jekyll Markdown."""

import hashlib
import os
import re
import sys
import urllib.parse
import urllib.request
import http.cookiejar

SITE = 'https://sites.google.com/view/pietty-project/'
OPENER = urllib.request.build_opener(
    urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
OPENER.addheaders = [('User-Agent', 'Mozilla/5.0')]

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, '_raw')
IMG_DIR = os.path.join(ROOT, 'assets', 'images')

PAGES = [
    # (raw name, output file, title, permalink)
    ('home', 'index.md', 'HOME', '/'),
    ('download', 'download.md', 'DOWNLOAD', '/download.html'),
    ('faq', 'faq.md', 'FAQ', '/faq.html'),
]

INTERNAL = {
    'home': '{{ "/" | relative_url }}',
    'download': '{{ "/download.html" | relative_url }}',
    'faq': '{{ "/faq.html" | relative_url }}',
}

KEEP_COLORS = {'#ff0000': 'red', '#008000': 'green'}

image_counter = {}


def fetch_image(url, page):
  os.makedirs(IMG_DIR, exist_ok=True)
  base = re.sub(r'=[ws]\d+$', '', url)
  h = hashlib.sha1(base.encode()).hexdigest()[:8]
  image_counter[page] = image_counter.get(page, 0) + 1
  for suffix in ('=w1600', url[len(base):]):
    try:
      req = urllib.request.Request(base + suffix,
                                   headers={'Referer': SITE})
      with OPENER.open(req, timeout=30) as r:
        data = r.read()
        ctype = r.headers.get('Content-Type', '')
      break
    except Exception as e:  # pylint: disable=broad-except
      print('  retry', suffix, e, file=sys.stderr)
  else:
    raise RuntimeError('cannot fetch ' + url)
  ext = {'image/png': '.png', 'image/jpeg': '.jpg', 'image/gif': '.gif',
         'image/webp': '.webp'}.get(ctype.split(';')[0], '.png')
  name = f'{page}-{image_counter[page]}-{h}{ext}'
  with open(os.path.join(IMG_DIR, name), 'wb') as f:
    f.write(data)
  print('  image', name, len(data), ctype, file=sys.stderr)
  return name


def fix_href(href):
  if href.startswith('http://www.google.com/url?') or href.startswith(
      'https://www.google.com/url?'):
    q = urllib.parse.parse_qs(urllib.parse.urlparse(href).query)
    href = q.get('q', [href])[0]
  m = re.match(r'^(?:https://sites\.google\.com)?/view/pietty-project/(\w+)',
               href)
  if m and m.group(1) in INTERNAL:
    return INTERNAL[m.group(1)]
  return href


def style_of(tag):
  d = {}
  for part in (tag.get('style') or '').split(';'):
    if ':' in part:
      k, v = part.split(':', 1)
      d[k.strip().lower()] = v.strip().lower()
  return d


def md_escape(text):
  text = text.replace('\\', '\\\\')
  text = re.sub(r'([*_`\[\]<>])', r'\\\1', text)
  # "** text" at the beginning of a line would become a list/emphasis.
  return text


def inline(node):
  """Render inline content of node to Markdown."""
  out = []
  for c in node.children:
    if isinstance(c, NavigableString):
      out.append(md_escape(str(c).replace('\xa0', ' ')))
      continue
    if not isinstance(c, Tag):
      continue
    if c.name == 'br':
      out.append('<br>')
    elif c.name == 'a':
      text = inline(c).strip()
      href = c.get('href', '')
      if not href or href.startswith('#'):
        out.append(text)
      else:
        out.append(f'[{text}]({fix_href(href)})')
    elif c.name == 'span':
      st = style_of(c)
      text = inline(c)
      if not text.strip():
        out.append(text)
        continue
      lead = text[:len(text) - len(text.lstrip())]
      trail = text[len(text.rstrip()):]
      core = text.strip()
      fam = st.get('font-family', '')
      if 'consolas' in fam:
        core = '`' + core.replace('\\', '') + '`'
      else:
        if st.get('font-weight') in ('700', 'bold'):
          core = f'**{core}**'
        if st.get('font-style') == 'italic':
          core = f'*{core}*'
        color = st.get('color')
        if color in KEEP_COLORS:
          core = f'<span class="{KEEP_COLORS[color]}">{core}</span>'
      out.append(lead + core + trail)
    elif c.name in ('b', 'strong'):
      out.append(f'**{inline(c).strip()}**')
    elif c.name in ('i', 'em'):
      out.append(f'*{inline(c).strip()}*')
    elif c.name == 'img':
      out.append(image_md(c))
    else:
      out.append(inline(c))
  return ''.join(out)


CURRENT_PAGE = ['']


def image_md(img):
  src = img.get('src', '')
  if not src:
    return ''
  name = fetch_image(src, CURRENT_PAGE[0])
  alt = img.get('alt', '') or ''
  return f'![{alt}]({{{{ "/assets/images/{name}" | relative_url }}}})'


def blocks(node):
  """Render block-level content to a list of Markdown blocks."""
  out = []
  for c in node.children:
    if not isinstance(c, Tag):
      if isinstance(c, NavigableString) and str(c).strip():
        out.append(md_escape(str(c).strip()))
      continue
    if 'PPhIP' in (c.get('class') or []):
      continue
    if re.fullmatch(r'h[1-6]', c.name):
      for junk in c.select('div.PPhIP'):
        junk.decompose()
      level = int(c.name[1])
      text = inline(c).strip()
      if text:
        out.append('#' * level + ' ' + text)
    elif c.name == 'p':
      text = inline(c).strip()
      # Move line breaks out of link text and emphasis.
      for _ in range(3):
        text = re.sub(r'\[([^\]]*?)((?:<br>)+)\]\(([^)]*)\)', r'[\1](\3)\2',
                      text)
        text = re.sub(r'(\*\*|`)([^*`]*?)((?:<br>)+)\1', r'\1\2\1\3', text)
      text = re.sub(r'(<br>)+$', '', text)
      if text:
        out.append(text)
    elif c.name in ('ul', 'ol'):
      items = []
      for i, li in enumerate(c.find_all('li', recursive=False), 1):
        bullet = '-' if c.name == 'ul' else f'{i}.'
        text = ' '.join(b for b in blocks(li))
        items.append(f'{bullet} {text}')
      out.append('\n'.join(items))
    elif c.name == 'img':
      out.append(image_md(c))
    elif c.name in ('iframe',):
      out.append(str(c))
    else:
      out.extend(blocks(c))
  return out


def tile_md(tile):
  parts = []
  # Text boxes and images in document order.
  for e in tile.find_all(['div', 'img']):
    if e.name == 'div' and 'tyJCtd' in (e.get('class') or []):
      parts.extend(blocks(e))
    elif e.name == 'img' and not e.find_parent('div', class_='tyJCtd'):
      parts.append(image_md(e))
  return '\n\n'.join(p for p in parts if p.strip())


# Google Sites section styles -> our CSS classes.
SECTION_STYLES = [
    ('O13XJf', 'hero'),     # Title with background image.
    ('gk8rDe', 'title'),    # Title only.
    ('lQAHbd', 'emph1'),    # Emphasis 1: dark blue background.
    ('qeLZfd', 'emph2'),    # Emphasis 2: light grey background.
]


def section_class(sec):
  classes = sec.get('class') or []
  for gs, ours in SECTION_STYLES:
    if gs in classes:
      return ours
  return 'plain'


def convert(raw, out_name, title, permalink):
  CURRENT_PAGE[0] = raw
  # Image URLs are only valid together with the session cookie of the page
  # fetch, so always re-fetch the page before converting.
  with OPENER.open(SITE + raw, timeout=30) as r:
    with open(os.path.join(RAW, raw + '.html'), 'wb') as f:
      f.write(r.read())
  soup = BeautifulSoup(open(os.path.join(RAW, raw + '.html'),
                            encoding='utf-8'), 'html.parser')
  sections = soup.select('div.UtePc section.yaqOZd')
  chunks = []
  for sec in sections:
    cols = [c for c in sec.select('div.JNdkSc')
            if not c.find_parent('div', class_='JNdkSc')]
    rendered = []
    for col in cols:
      tiles = [t for t in col.select('div.oKdM2c')
               if not t.find_parent('div', class_='oKdM2c')]
      md = '\n\n'.join(x for x in (tile_md(t) for t in tiles) if x.strip())
      if md.strip():
        rendered.append(md)
    if not rendered:
      continue
    text = '\n\n'.join(rendered)
    if 'Canonical URL' in text and 'Copyright' in text:
      continue  # Footer: moved into the layout.
    if len(rendered) == 1:
      inner = rendered[0]
    else:
      cols_html = '\n\n'.join(
          f'<div class="col" markdown="1">\n\n{r}\n\n</div>' for r in rendered)
      inner = f'<div class="row" markdown="1">\n\n{cols_html}\n\n</div>'
    chunks.append(f'<section class="{section_class(sec)}" markdown="1">\n\n'
                  f'{inner}\n\n</section>')

  body = '\n\n'.join(chunks)
  # The page-level header on home is shown by the layout instead.
  front = f'---\nlayout: default\ntitle: {title}\npermalink: {permalink}\n---\n\n'
  with open(os.path.join(ROOT, out_name), 'w', encoding='utf-8') as f:
    f.write(front + body + '\n')
  print('wrote', out_name, file=sys.stderr)


def fetch_header_image():
  with OPENER.open(SITE + 'home', timeout=30) as r:
    html = r.read().decode('utf-8')
  m = re.search(r'background-image: url\((https://sites\.google\.com/'
                r'sitesv-images-rt/[^)]+)\)', html)
  if m:
    name = fetch_image(m.group(1), 'header')
    os.replace(os.path.join(IMG_DIR, name),
               os.path.join(IMG_DIR, 'header' + os.path.splitext(name)[1]))


def main():
  if os.path.isdir(IMG_DIR):
    for f in os.listdir(IMG_DIR):
      os.remove(os.path.join(IMG_DIR, f))
  fetch_header_image()
  for p in PAGES:
    convert(*p)


if __name__ == '__main__':
  main()
