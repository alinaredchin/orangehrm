from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


# def pytest_addoption(parser):
#    parser.addoption("--headless", action="store_true",
#                      help="Run browser in headless mode")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today = datetime.now()
    report_dir = Path("reports", today.strftime("%Y-%m-%d"))
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y-%m-%d_%H-%M-%S')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


def pytest_html_report_title(report):
    report.title = "Test Report"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
