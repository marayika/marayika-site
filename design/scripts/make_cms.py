import os, re, shutil, html, sys
EXP = "/home/claude/build/marayika-site"
OUT = "/home/claude/build/marayika-cms"
if os.path.exists(OUT): shutil.rmtree(OUT)
SRC = os.path.join(OUT, "src")
os.makedirs(SRC)
# static passthrough
for d in ["portfolio", "soft-epilogue", "contact", "images"]:
    shutil.copytree(os.path.join(EXP, d), os.path.join(SRC, d))
for f in ["index.html", "404.html", "favicon.svg"]:
    shutil.copy(os.path.join(EXP, f), os.path.join(SRC, f))
os.makedirs(os.path.join(SRC, "media"))
shutil.copy(os.path.join(EXP, "images/table.jpg"), os.path.join(SRC, "media/table.jpg"))
shutil.copy(os.path.join(EXP, "images/basket.jpg"), os.path.join(SRC, "media/basket.jpg"))

post_css = """.post p{margin:0}
.post h2,.post h3{margin:12px 0 0;font-family:'Bricolage Grotesque',sans-serif;font-weight:600;line-height:1.2;color:#141414}
.post h2{font-size:28px}.post h3{font-size:23px}
.post img{display:block;width:100%;height:auto;margin:12px 0}
.post blockquote{margin:12px 0;padding:8px 0 8px 24px;border-left:3px solid #BA2924;display:flex;flex-direction:column;gap:2px}
.post blockquote p:first-child{font-family:'Bricolage Grotesque',sans-serif;font-weight:600;font-size:30px;line-height:1.2;letter-spacing:-0.01em}
.post blockquote p+p{font-family:Caveat,cursive;font-weight:700;font-size:30px;color:#BA2924}
.post hr{border:0;text-align:center;margin:8px 0}.post hr::after{content:'~';font-family:Caveat,cursive;font-size:30px;color:#BA2924}
.post a{color:#BA2924}
.post ul,.post ol{margin:0;padding-left:1.2em}"""

# ---------- featured pieces (link out) ----------
pieces = [
 ("2026-11-23-now-you-are-a-witness", "Now, you are a witness. I place this bird in your hands.", "It is beautiful that I get to see you across the mountains and the oceans. Now, what do I do with all that seeing?", "2026-11-23", "Essay", "witness.jpg", "Illustration of a small bird resting on two open hands", "https://marayika.substack.com/p/now-you-are-a-witness-i-place-this"),
 ("2026-10-27-lets-eat-so-we-can-eat-again", "Let’s eat so we can eat again", "On being hungry for life, and a lesson from my five-year-old niece.", "2026-10-27", "Essay", "basket.jpg", "Illustration of a woven basket and a bowl of potato wedges on a striped cloth", "https://marayika.substack.com/p/lets-eat-so-we-can-eat-again"),
 ("2026-09-25-your-pan-african-boyfriend", "Your pan-African boyfriend wants to decolonize the continent in a missionary position.", "I would argue that the “pan-African man” is probably the most misogynistic man you will ever meet.", "2026-09-25", "Essay", "pan-african.jpg", "Title card reading: Your pan-African boyfriend wants to decolonize the continent in a missionary position.", "https://marayika.substack.com/p/your-pan-african-boyfriend-wants"),
 ("2026-09-13-we-might-as-well-fall-in-love", "We might as well fall in love", "Twenty poems on love and the stubborn argument for staying alive.", "2026-09-13", "Poetry", "fall-in-love.jpg", "Title card reading: We might as well fall in love", "https://marayika.substack.com/p/we-might-as-well-fall-in-love"),
]
import json as _j
gal = """---
title: "Imbyino y’urukundo"
subtitle: "I imagine love through lovers’ body movements inspired by inyambo."
date: 2026-11-25
category: Gallery
note: "three frames, one dance"
images:
  - /media/inyambo-1.jpg
  - /media/inyambo-2.jpg
  - /media/inyambo-3.jpg
cover_alt: "Illustrations of two dancers in draped cloth on a green and yellow checkerboard, arms raised toward each other"
---
"""
for i in (1, 2, 3): shutil.copy(os.path.join(EXP, "images", f"inyambo-{i}.jpg"), os.path.join(SRC, "media", f"inyambo-{i}.jpg"))
os.makedirs(os.path.join(SRC, "diary/posts"), exist_ok=True)
open(os.path.join(SRC, "diary/posts/2026-11-25-imbyino-yurukundo.md"), "w", encoding="utf-8").write(gal)
for slug, title, sub, date, cat, img, alt, link in pieces:
    shutil.copy(os.path.join(EXP, "images", img), os.path.join(SRC, "media", img))
    fm = "---\n" + "\n".join([f"title: {_j.dumps(title, ensure_ascii=False)}", f"subtitle: {_j.dumps(sub, ensure_ascii=False)}", f"date: {date}", f"category: {cat}", f"cover: /media/{img}", f"cover_alt: {_j.dumps(alt, ensure_ascii=False)}", f"link: {_j.dumps(link)}"]) + "\n---\n"
    open(os.path.join(SRC, f"diary/posts/{slug}.md"), "w", encoding="utf-8").write(fm)
open(os.path.join(SRC, "diary/posts/posts.11tydata.js"), "w").write('export default {\n  tags: "diary",\n  permalink: false,\n};\n')

# ---------- diary index ----------
import sys; sys.path.insert(0, "/home/claude/scripts")
from diary_card import card, subtitle, image, SLOT, gallery_card
d = open(os.path.join(EXP, "diary/index.html"), encoding="utf-8").read()
sa = d.index('<section aria-label="Featured pieces"'); sb = d.index("</section>", sa) + len("</section>")
img = ("{% if post.data.cover %}" + image("{{ post.data.cover }}", "{{ post.data.cover_alt }}") +
       '{% else %}<div style="aspect-ratio: 16 / 9; background: #F4CFC9; display: flex; align-items: flex-end; padding: 20px; box-sizing: border-box">'
       '<span style="font-family: Caveat, cursive; font-weight: 700; font-size: 34px; line-height: 1.05; color: #141414">{{ post.data.title }}</span></div>{% endif %}')
tpl = card("{{ post.data.link }}", "{{ post.data.category }}",
           "{{ 'row' if loop.index is odd else 'row-reverse' }}", "{{ '-1.2' if loop.index is odd else '1.4' }}",
           "{{ '0' if loop.index < 10 }}{{ loop.index }}", img, "{{ post.date | dayMonthYear }}", "{{ post.data.title }}",
           "{% if post.data.subtitle %}" + subtitle("{{ post.data.subtitle }}") + "{% endif %}", "#BA2924")
gimgs = ('<div style="display: grid; grid-template-columns: repeat({{ post.data.images | length if post.data.images | length < 3 else 3 }}, minmax(0, 1fr)); gap: 8px">'
         '{% for im in post.data.images %}<img src="{{ im }}" alt="{{ post.data.cover_alt }}" style="display: block; width: 100%; height: auto">{% endfor %}</div>')
gtpl = gallery_card("{{ post.data.category }}", "{{ 'row' if loop.index is odd else 'row-reverse' }}", "{{ '-1.2' if loop.index is odd else '1.4' }}",
           "{{ '0' if loop.index < 10 }}{{ loop.index }}", gimgs, "{{ post.data.title }}",
           "{% if post.data.subtitle %}" + subtitle("{{ post.data.subtitle }}") + "{% endif %}", "{{ post.data.note }}", "#BA2924")
tpl = "{% if post.data.images and post.data.images.length %}" + gtpl + "{% else %}" + tpl + "{% endif %}"
sec = ('<section aria-label="Featured pieces" style="display: flex; flex-direction: column; border-top: 2px solid #141414">\n'
       "{% for post in collections.diary | reverse %}\n" + tpl + "\n{% endfor %}\n</section>")
d = d[:sa] + sec + d[sb:]
# working filter chips
chips_old = re.search(r'<div style="display: flex; flex-wrap: wrap; gap: 10px; padding-top: 6px">.*?</div>', d, re.S).group(0)
def chip(label, val, on):
    bg, fg = ("#141414", "#FBFAF6") if on else ("#FFFFFF", "#141414")
    return f'<button type="button" class="chip" data-filter="{val}" aria-pressed="{"true" if on else "false"}" style="border: 1.5px solid #141414; border-radius: 999px; padding: 8px 18px; font: inherit; font-size: 14px; cursor: pointer; background: {bg}; color: {fg}">{label}</button>'
chips = '<div style="display: flex; flex-wrap: wrap; gap: 10px; padding-top: 6px">' + chip("All", "all", True) + chip("Poetry", "Poetry", False) + chip("Essays", "Essay", False) + chip("Gallery", "Gallery", False) + "</div>"
d = d.replace(chips_old, chips)
script = """<script>
document.querySelectorAll('.chip').forEach(function(c){c.addEventListener('click',function(){
var f=c.getAttribute('data-filter');
document.querySelectorAll('.chip').forEach(function(o){var on=o===c;o.setAttribute('aria-pressed',on);o.style.background=on?'#141414':'#FFFFFF';o.style.color=on?'#FBFAF6':'#141414';});
var n=0;document.querySelectorAll('.entry').forEach(function(e){var on=(f==='all'||e.getAttribute('data-category')===f);e.style.display=on?'':'none';if(on)n++;});var note=document.querySelector('[data-empty-note]');if(note)note.hidden=n>0;
});});
</script>
</body>"""
d = d.replace("</body>", script, 1)
open(os.path.join(SRC, "diary/index.njk"), "w", encoding="utf-8").write("---\npermalink: /diary/\n---\n" + d)

# ---------- config ----------
open(os.path.join(OUT, "eleventy.config.js"), "w").write("""export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({ "src/images": "images" });
  eleventyConfig.addPassthroughCopy({ "src/media": "media" });
  eleventyConfig.addPassthroughCopy({ "src/portfolio": "portfolio" });
  eleventyConfig.addPassthroughCopy({ "src/soft-epilogue": "soft-epilogue" });
  eleventyConfig.addPassthroughCopy({ "src/contact": "contact" });
  eleventyConfig.addPassthroughCopy({ "src/index.html": "index.html" });
  eleventyConfig.addPassthroughCopy({ "src/404.html": "404.html" });
  eleventyConfig.addPassthroughCopy({ "src/favicon.svg": "favicon.svg" });

  // Keep line breaks as written, so poems keep their shape
  eleventyConfig.amendLibrary("md", (md) => md.set({ breaks: true, html: true, typographer: false }));

  const fmt = (d, opts) => new Intl.DateTimeFormat("en-GB", { timeZone: "UTC", ...opts }).format(new Date(d));
  eleventyConfig.addFilter("shortDate", (d) =>
    new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "short", day: "numeric", year: "numeric" }).format(new Date(d)));
  eleventyConfig.addFilter("dayMonthYear", (d) =>
    new Intl.DateTimeFormat("en-GB", { timeZone: "UTC", day: "numeric", month: "long", year: "numeric" }).format(new Date(d)));
  eleventyConfig.addFilter("longDate", (d) =>
    new Intl.DateTimeFormat("en-US", { timeZone: "UTC", month: "long", day: "numeric", year: "numeric" }).format(new Date(d)));

  return {
    dir: { input: "src", output: "_site", includes: "_includes" },
    templateFormats: ["md", "njk"],
    markdownTemplateEngine: false,
  };
}
""")
open(os.path.join(OUT, "package.json"), "w").write("""{
  "name": "marayika-site",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "eleventy"
  },
  "devDependencies": {
    "@11ty/eleventy": "^3.1.2"
  }
}
""")
open(os.path.join(OUT, "netlify.toml"), "w").write("""[build]
  command = "npm run build"
  publish = "_site"

[build.environment]
  NODE_VERSION = "22"
""")
pages_yml = """media:
  input: src/media
  output: /media
  categories: [image]

content:
  - name: diary
    label: Diary
    type: collection
    path: src/diary/posts
    filename: "{year}-{month}-{day}-{title}.md"
    exclude: [posts.11tydata.js]
    view:
      fields: [title, category, date]
      sort: [date]
      default:
        sort: date
        order: desc
    fields:
      - name: title
        label: Title
        type: string
        required: true
      - name: link
        label: Link to the piece (Substack or anywhere else; leave empty for Gallery work)
        type: string
      - name: subtitle
        label: Subtitle (one line under the title)
        type: string
      - name: date
        label: Date
        type: date
        options:
          format: yyyy-MM-dd
      - name: category
        label: Type
        type: select
        default: Essay
        options:
          values: [Poetry, Essay, Gallery]
      - name: cover
        label: Cover image (optional)
        type: image
      - name: cover_alt
        label: Describe the image(s) (for screen readers)
        type: string
      - name: images
        label: Gallery images (for Gallery pieces; up to 3 show side by side)
        type: image
        list: true
      - name: note
        label: Handwritten caption under the images (optional)
        type: string
"""
open(os.path.join(OUT, ".pages.yml"), "w").write(pages_yml)
open(os.path.join(OUT, "pages-cms-settings-copy.txt"), "w").write("Only needed if the file called .pages.yml did not upload to GitHub.\nCreate a new file in your repository named exactly:  .pages.yml\nand paste everything below this line into it.\n----------------------------------------\n" + pages_yml)
open(os.path.join(OUT, ".gitignore"), "w").write("node_modules\n_site\n")
print("generated")
