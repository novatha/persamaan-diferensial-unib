import asyncio
from playwright.async_api import async_playwright
import re

async def main():
    async with async_playwright() as p:
        # Launch browser. Might need to install browsers if not present.
        try:
            browser = await p.chromium.launch(headless=True)
        except Exception as e:
            import os
            os.system("playwright install chromium")
            browser = await p.chromium.launch(headless=True)
            
        page = await browser.new_page()
        
        for i in range(1, 16):
            url = f"http://127.0.0.1:8001/{i:02d}_modul_{i}/"
            print(f"Checking {url}...")
            
            try:
                response = await page.goto(url, wait_until="networkidle")
            except Exception as e:
                print(f"Error loading {url}: {e}")
                continue
            
            if response and response.status != 200:
                print(f"Failed to load {url}, status: {response.status}")
                continue
                
            await page.wait_for_timeout(2000)
            
            try:
                # get text from the markdown article
                text = await page.inner_text("article")
            except:
                text = await page.inner_text("body")
            
            # Look for unrendered MathJax syntax.
            unrendered = re.findall(r'(\$\$.*?\$\$|\$[^\s][^\$]*[^\s]\$|\\frac|\\begin|\\end|\\int|\\partial|\\nabla)', text)
            
            # Check for MathJax errors in the DOM
            error_elements = await page.query_selector_all('.mjx-math[data-semantic-type="error"], .mjx-chtml[data-semantic-type="error"]')
            if error_elements:
                print(f"Found {len(error_elements)} MathJax rendering errors in Modul {i}!")
                
            if unrendered:
                # deduplicate and filter
                unique_unrendered = list(set(unrendered))
                if unique_unrendered:
                    print(f"Found unrendered LaTeX in Modul {i}:")
                    for match in unique_unrendered:
                        # only print first 50 chars of match
                        print("  -", match[:50])
            else:
                print(f"Modul {i} looks clean.")
                
        await browser.close()

asyncio.run(main())
