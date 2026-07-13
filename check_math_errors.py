import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        errors = []
        page.on("pageerror", lambda err: errors.append(err))
        page.on("console", lambda msg: errors.append(msg) if msg.type == "error" else None)

        for i in range(1, 16):
            url = f"http://127.0.0.1:8001/{i:02d}_modul_{i}/"
            
            try:
                response = await page.goto(url, wait_until="networkidle")
            except Exception as e:
                continue
                
            if response and response.status == 200:
                await page.wait_for_timeout(2000)
                if errors:
                    print(f"--- Modul {i} JS Errors ---")
                    for err in errors:
                        print(err)
                    errors.clear()
                else:
                    print(f"Modul {i} has NO JS errors.")
                    
        await browser.close()

asyncio.run(main())
