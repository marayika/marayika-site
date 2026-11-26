# One featured piece on the Diary shelf. Used for the canvas (literal values)
# and for the live site (Nunjucks values).
ARROW = ('<svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="ACC" stroke-width="1.6" '
         'stroke-linecap="round" aria-hidden="true" style="flex: none; margin-top: 6px">'
         '<path d="M6 18c3.8-4 7.6-8 11.6-11.8M9 6.4c2.9-.2 5.8-.3 8.6-.2.2 2.8.2 5.6 0 8.4"/></svg>')

def card(link, cat, direction, rotate, number, image_html, date, title, subtitle_html, acc):
    return f'''<a href="{link}" data-category="{cat}" class="entry" style="display: flex; flex-direction: {direction}; flex-wrap: wrap; align-items: center; gap: 28px 56px; padding: 48px 0; border-bottom: 1px dashed #9A958C; text-decoration: none; color: #141414">
<div class="lift" style="flex: 1 1 340px; max-width: 540px; min-width: 0; position: relative; background: #FFFFFF; padding: 12px 12px 14px; border: 1.5px solid #141414; box-shadow: 5px 5px 0 #141414; transform: rotate({rotate}deg)">
<div aria-hidden="true" style="position: absolute; top: -13px; left: 50%; margin-left: -48px; width: 96px; height: 26px; background: rgba(226, 214, 186, 0.85); transform: rotate(-3deg)"></div>
{image_html}
</div>
<div style="flex: 1 1 320px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
<p style="margin: 0; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px"><span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 18px; color: {acc}">{number}</span><span style="font-family: Caveat, cursive; font-weight: 700; font-size: 26px; line-height: 1; color: {acc}">{date}</span><span style="font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; color: #5A564F">{cat}</span></p>
<h2 style="margin: 0; display: flex; gap: 14px; justify-content: space-between; align-items: flex-start; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 600; font-size: clamp(26px, 3vw, 36px); line-height: 1.1; letter-spacing: -0.02em">{title}{ARROW.replace("ACC", acc)}</h2>
{subtitle_html}
</div>
</a>'''

def subtitle(text):
    return f'<p style="margin: 0; max-width: 520px; font-family: Newsreader, Georgia, serif; font-style: italic; font-size: 19px; line-height: 1.45; color: #3D3A35">{text}</p>'

def image(src, alt):
    return f'<img loading="lazy" decoding="async" src="{src}" alt="{alt}" style="display: block; width: 100%; height: auto">'

SLOT = '''<div aria-hidden="true" style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px 20px; padding: 40px 0; border-bottom: 1px dashed #9A958C; color: #8A857C">
<span style="font-family: Caveat, cursive; font-weight: 700; font-size: 32px; line-height: 1">next page…</span>
<span style="font-family: Newsreader, Georgia, serif; font-style: italic; font-size: 18px">More pieces will join the shelf.</span>
</div>'''

def strip(srcs, alts):
    imgs = "".join(f'<img loading="lazy" decoding="async" src="{s}" alt="{a}" style="display: block; width: 100%; height: auto">' for s, a in zip(srcs, alts))
    return f'<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{imgs}</div>'

def gallery_card(cat, direction, rotate, number, images_html, title, subtitle_html, note, acc):
    return f'''<div data-category="{cat}" class="entry" style="display: flex; flex-direction: {direction}; flex-wrap: wrap; align-items: center; gap: 28px 56px; padding: 48px 0; border-bottom: 1px dashed #9A958C; color: #141414">
<figure class="lift" style="margin: 0; flex: 1 1 340px; max-width: 540px; min-width: 0; position: relative; background: #FFFFFF; padding: 12px 12px 14px; border: 1.5px solid #141414; box-shadow: 5px 5px 0 #141414; transform: rotate({rotate}deg)">
<div aria-hidden="true" style="position: absolute; top: -13px; left: 50%; margin-left: -48px; width: 96px; height: 26px; background: rgba(226, 214, 186, 0.85); transform: rotate(-3deg)"></div>
{images_html}
<figcaption style="padding-top: 10px; font-family: Caveat, cursive; font-weight: 500; font-size: 22px; text-align: center">{note}</figcaption>
</figure>
<div style="flex: 1 1 320px; min-width: 0; display: flex; flex-direction: column; gap: 10px">
<p style="margin: 0; display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px"><span style="font-family: 'Bricolage Grotesque', sans-serif; font-weight: 800; font-size: 18px; color: {acc}">{number}</span><span style="font-size: 12px; letter-spacing: 0.16em; text-transform: uppercase; color: #5A564F">{cat}</span></p>
<h2 style="margin: 0; font-family: 'Bricolage Grotesque', sans-serif; font-weight: 600; font-size: clamp(26px, 3vw, 36px); line-height: 1.1; letter-spacing: -0.02em">{title}</h2>
{subtitle_html}
</div>
</div>'''
