import re, os, shutil, sys

REVEAL = """<style>
.js-reveal main > section{opacity:0;transform:translateY(14px);transition:opacity .6s ease, transform .6s ease}
.js-reveal main > section.in{opacity:1;transform:none}
</style>
<script>
(function(){
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.documentElement.classList.add('js-reveal');
  var io = new IntersectionObserver(function(es){ es.forEach(function(e){ if (e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }); }, {rootMargin: '0px 0px -8% 0px'});
  document.querySelectorAll('main > section').forEach(function(s, i){ if (i === 0) s.classList.add('in'); else io.observe(s); });
})();
</script>"""
def polish(html):
    n = [0]
    def lazy(m):
        n[0] += 1
        tag = m.group(0)
        if n[0] <= 1 or 'loading=' in tag: return tag
        return tag.replace('<img ', '<img loading="lazy" decoding="async" ', 1)
    html = re.sub(r'<img [^>]*>', lazy, html)
    return html.replace('</body>', REVEAL + '\n</body>', 1)

SRC, OUT, ASSETS = sys.argv[1], sys.argv[2], sys.argv[3]
ACCENT = "#BA2924"
pages = {
 "Main.dc.html": ("index.html", "Marayika", "Ange Théonastine Ashimwe — a poet with a day job."),
 "Portfolio.dc.html": ("portfolio/index.html", "Portfolio — Marayika", "Development work across policy, strategy, research and grants in Rwanda and across Africa."),
 "Diary.dc.html": ("diary/index.html", "Diary — Marayika", "Poetry, essays and a gallery by Marayika."),
 "SoftEpilogue.dc.html": ("soft-epilogue/index.html", "Soft Epilogue — Marayika", "An independent bookshop in Rwanda. New and second-hand books that give back."),
 "Contact.dc.html": ("contact/index.html", "Contact — Marayika", "Write to Marayika."),
}
links = {"Main.dc.html": "/", "Portfolio.dc.html": "/portfolio/", "Diary.dc.html": "/diary/", "SoftEpilogue.dc.html": "/soft-epilogue/", "Contact.dc.html": "/contact/"}
blobs = {"ca3b1b3a9e43c1cbd7242cf6c4dcc3b2": "ange.jpg", "fc43a0d41a19d5ef543292fc46c81868": "basket.jpg",
 "88a4e90b13a05ebcaa0d6490b817be41": "table.jpg", "c4fe567203b51ced80c7a694b28b8506": "soft-epilogue-logo.jpg",
 "173a404fc4a21a803e78b905e61b0a90": "witness.jpg", "87dace042d1f1f8ace658b454e923634": "pan-african.jpg", "97a49a8981f65d5c44ada826143edfe9": "fall-in-love.jpg",
 "6b300253d86713e38fee5e43a3534cac": "inyambo-1.jpg", "dfc07c65af28139ca8122a37cf943248": "inyambo-2.jpg", "f3e19f5f560a20939882e1426a9a0e07": "inyambo-3.jpg", "2a3e4c2dcbd99e741154e7b3fbaba235": "diary-logo.jpg"}
favicon = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#FBFAF6"/><text x="10" y="46" font-family="Arial Black, Arial, sans-serif" font-weight="900" font-size="40" fill="#141414">m</text><circle cx="52" cy="42" r="5" fill="#BA2924"/></svg>'
phone_css = "@media (max-width: 640px){header,main,footer{padding-left:44px !important;padding-right:20px !important}}"
since_js = """<script>
document.querySelectorAll('[data-since]').forEach(function(el){
var p=el.getAttribute('data-since').split('-'),n=new Date();
var m=(n.getFullYear()-+p[0])*12+(n.getMonth()+1-+p[1])+1;if(m<1)m=1;
var y=Math.floor(m/12),r=m%12,o=[];if(y)o.push(y+(y===1?' yr':' yrs'));if(r)o.push(r+(r===1?' mo':' mos'));
el.textContent=o.join(' ');});
</script>"""
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, "images"))
for f in blobs.values(): shutil.copy(os.path.join(ASSETS, f), os.path.join(OUT, "images", f))
open(os.path.join(OUT, "favicon.svg"), "w").write(favicon)
for src, (dst, title, desc) in pages.items():
    s = open(os.path.join(SRC, src), encoding="utf-8").read()
    helmet = re.search(r"<helmet>(.*?)</helmet>", s, re.S).group(1)
    body = re.search(r"</helmet>(.*?)</x-dc>", s, re.S).group(1)
    body = body.replace("{{accent}}", ACCENT)
    body = body.replace("{{vgTotal}}", '<span data-since="2025-03">1 yr 9 mos</span>').replace("{{analystDur}}", '<span data-since="2026-01">11 mos</span>')
    body = body.replace('onClick="{{ copy }}"', 'id="copy-email"').replace("{{ copyLabel }}", "Copy address")
    if 'id="copy-email"' in body:
        body += """<script>
document.getElementById('copy-email').addEventListener('click',function(){var b=this;
try{navigator.clipboard.writeText('hello@marayika.com');}catch(e){}
b.querySelector('span').textContent='Copied';});
</script>"""
    # canvas-only logic -> static HTML
    body = re.sub(r"<sc-if[^>]*>|</sc-if>", "", body)
    base = "border: 1.5px solid #141414; border-radius: 999px; padding: 8px 18px; font: inherit; font-size: 14px; cursor: pointer; "
    for k in ["All", "Poetry", "Essay", "Gallery"]:
        on = k == "All"
        body = body.replace('onClick="{{ f%s }}" ' % k, 'data-filter="%s" class="chip" ' % ("all" if on else k))
        body = body.replace('aria-pressed="{{ on%s }}"' % k, 'aria-pressed="%s"' % ("true" if on else "false"))
        body = body.replace('style="{{ s%s }}"' % k, 'style="%s"' % (base + ("background: #141414; color: #FBFAF6" if on else "background: #FFFFFF; color: #141414")))
    body = body.replace("<p data-empty-note ", "<p data-empty-note hidden ")
    body = re.sub(r"<form data-substack-embed.*?</form>",
        '<iframe src="https://marayika.substack.com/embed" title="Subscribe to Marayika’s Diary on Substack" width="100%" height="320" style="display: block; border: 0; background: #FFFFFF" frameborder="0" scrolling="no"></iframe>',
        body, flags=re.S)
    # poem block: drop it entirely until the poem is typed in
    body = re.sub(r'<figure data-poem.*?\[Type the poem here\].*?</figure>\s*', '', body, flags=re.S)
    # poem placeholder: hide until the line is added; credit stays
    body = re.sub(r'<p[^>]*>\[Paste the line from the poem here\]</p>\s*', '', body)
    body = body.replace("<p style=\"margin: 12px 0 0; font-family: Caveat, cursive; font-size: 24px; color: " + ACCENT + "\">— nikka ursula",
                        "<p style=\"margin: 0; font-family: Caveat, cursive; font-size: 26px; color: " + ACCENT + "\">from a poem by nikka ursula")
    for k, v in links.items(): body = body.replace('href="%s' % k, 'href="%s' % v)
    for k, v in blobs.items(): body = body.replace("/_blob/" + k, "/images/" + v)
    helmet = helmet.replace("{{accent}}", ACCENT).replace("</style>", phone_css + "\n</style>")
    leftover = re.findall(r"\{\{[^}]*\}\}|\.dc\.html|/_blob/|\[[A-Z][^\]]*\]", body + helmet)
    assert not leftover, (src, leftover)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://marayika.com/images/ange.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
{helmet.strip()}
</head>
<body>
{body.strip()}
{since_js if 'data-since' in body else ''}
</body>
</html>
"""
    html = polish(html)
    p = os.path.join(OUT, dst); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)
    print("wrote", dst)
# 404
idx = open(os.path.join(OUT, "index.html"), encoding="utf-8").read()
nf = re.sub(r"<main.*?</main>", '<main style="max-width: 1180px; margin: 0 auto; padding: 96px 40px 96px 56px; display: flex; flex-direction: column; gap: 18px"><p style="margin: 0; font-family: Caveat, cursive; font-weight: 700; font-size: 34px; color: #BA2924">wrong page —</p><h1 style="margin: 0; font-family: \'Bricolage Grotesque\', sans-serif; font-weight: 800; font-size: clamp(64px, 10vw, 128px); line-height: 0.9; letter-spacing: -0.05em">404<span style="color: #BA2924">.</span></h1><p style="margin: 0">This page is not in the notebook.</p><a href="/" style="font-weight: 500">← Back to home</a></main>', idx, flags=re.S)
open(os.path.join(OUT, "404.html"), "w", encoding="utf-8").write(nf.replace("<title>Marayika</title>", "<title>Page not found — Marayika</title>"))
print("wrote 404.html")
