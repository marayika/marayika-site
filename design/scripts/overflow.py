import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        for w in (360,390,1280):
            pg=await b.new_page(viewport={"width":w,"height":800})
            for u in ["/","/portfolio/","/diary/","/soft-epilogue/","/contact/"]:
                await pg.goto("http://localhost:8777"+u)
                bad=await pg.evaluate("""(()=>{const W=document.documentElement.clientWidth;return [...document.querySelectorAll('h1,h2,h3,p,a,span')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>W+1}).map(e=>e.tagName+':'+e.textContent.trim().slice(0,30)).slice(0,5)})()""")
                print(w,u,bad)
        await b.close()
asyncio.run(main())
