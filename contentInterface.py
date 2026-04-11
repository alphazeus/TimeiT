
import dearpygui.dearpygui as dpg
from datetime import datetime

tab_state = "clock_selected"

def on_tab_change(sender, app_data, user_data):
    if app_data == "tab_clock":
        tab_state = "clock_selected"
    elif app_data == "tab_timer":
        tab_state = "timer_selected"

# def createClockContent():

def createContent():
    with dpg.window(label="TimeiT", tag="main_window", no_title_bar=True, width=dpg.get_viewport_client_width(), height=dpg.get_viewport_client_height()):
        with dpg.tab_bar(callback = on_tab_change):
            with dpg.tab(label="Clock", tag = "tab_clock"):
                dpg.add_text(datetime.now().strftime("%H:%M:%S"), tag="clock")
                dpg.bind_item_font("clock", "font_clock")
            with dpg.tab(label="Timer", tag = "tab_timer"):
                dpg.add_text("00:00", tag="timer_display")
                dpg.add_button(label="Start")


def renderloop():
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        if tab_state == "clock_selected":
            dpg.set_value("clock", datetime.now().strftime("%H:%M:%S"))
        