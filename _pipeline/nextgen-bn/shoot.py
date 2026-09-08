import glob, os, asyncio, base64
from playwright.async_api import async_playwright

HTML = '<html><body style="margin:0;background:#fff">%s</body></html>'

async def main():
    files = sorted(glob.glob("figs/*.svg"))
    os.makedirs("figs/png", exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1500, "height": 1200})
        for f in files:
            svg = open(f, encoding="utf-8").read()
            await pg.set_content(HTML % svg)
            el = await pg.query_selector("svg")
            out = "figs/png/" + os.path.basename(f).replace(".svg", ".png")
            await el.screenshot(path=out, timeout=15000)
        await b.close()
    print("shot", len(files))

asyncio.run(main())
