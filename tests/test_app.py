from dash.testing.application_runners import import_app
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # runs without opening browser
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)


def test_header_present(dash_duo):
    dash_duo.driver = create_driver()
    app = import_app("app")
    dash_duo.start_server(app)

    assert "Pink Morsels Sales Dashboard" in dash_duo.find_element("h1").text


def test_visualisation_present(dash_duo):
    dash_duo.driver = create_driver()
    app = import_app("app")
    dash_duo.start_server(app)

    assert dash_duo.find_element("#sales-line-chart") is not None


def test_region_picker_present(dash_duo):
    dash_duo.driver = create_driver()
    app = import_app("app")
    dash_duo.start_server(app)

    assert dash_duo.find_element("#region-filter") is not None