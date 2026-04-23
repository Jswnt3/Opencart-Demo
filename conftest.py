import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL, HEADLESS, SLOW_MO


@pytest.fixture(scope="session")
def browser_context_args():
    return {"viewport": {"width": 1280, "height": 720}}


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=HEADLESS, slow_mo=SLOW_MO)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        pg = context.new_page()
        pg.goto(BASE_URL)
        yield pg
        # Save trace on failure
        trace_path = f"reports/trace-{pg.title()}.zip"
        context.tracing.stop(path=trace_path)
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def firefox_page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=HEADLESS)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        pg = context.new_page()
        pg.goto(BASE_URL)
        yield pg
        context.close()
        browser.close()
