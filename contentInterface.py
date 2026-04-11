import dearpygui.dearpygui as dpg
from datetime import datetime


def createContent(fonts):
    _ui = {}
    with dpg.window(label="TimeiT", no_title_bar=True, width=dpg.get_viewport_client_width(), height=dpg.get_viewport_client_height()):
        with dpg.tab_bar():
            with dpg.tab(label="Clock"):
                _ui["clock"] = dpg.add_text(datetime.now().strftime("%H:%M:%S"))
                dpg.bind_item_font(_ui["clock"], fonts["clock"])
            with dpg.tab(label="Timer"):
                # timer UI: buttons, remaining time, etc.
                dpg.add_text("00:00", tag="timer_display")
                dpg.add_button(label="Start")
    return _ui


def renderloop(_ui):
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        dpg.set_value(_ui["clock"], datetime.now().strftime("%H:%M:%S"))