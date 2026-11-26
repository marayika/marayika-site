import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg=await b.new_page(viewport={"width":1280,"height":900})
        await pg.goto("http://localhost:8767/diary/")
        for f in ["Poetry","Essay","Gallery","all"]:
            await pg.click(f"button[data-filter={f}]")
            v=await pg.evaluate("[...document.querySelectorAll('.entry')].filter(e=>e.style.display!=='none').length")
            note=await pg.evaluate("!document.querySelector('[data-empty-note]').hidden")
            print(f, "visible", v, "empty note shown", note)
        await pg.click("button[data-filter=all]")
        await pg.screenshot(path="/home/claude/build/diary6.png", full_page=True)
        await b.close()
asyncio.run(main())
