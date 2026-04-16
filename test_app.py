from dash.testing.application_runners import import_app

def test_header_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    header = dash_duo.find_element("h1")
    assert header.text == "Soul Foods, Pink Morsel Sales Visualiser"

def test_visualisation_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    assert dash_duo.find_element("#sales-chart") is not None

def test_region_picker_present(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    assert dash_duo.find_element("#region-filter") is not None