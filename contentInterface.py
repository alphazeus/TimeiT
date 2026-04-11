
import dearpygui.dearpygui as dpg
from datetime import datetime

tab_state = "clock_selected"

def on_tab_change(sender, app_data, user_data):
    if app_data == "tab_clock":
        tab_state = "clock_selected"
    elif app_data == "tab_timer":
        tab_state = "timer_selected"

def createClockContent():
    dpg.add_text(datetime.now().strftime("%H:%M:%S"), tag="clock")
    dpg.bind_item_font("clock", "font_clock")

def createTimerContent():
    dpg.add_text("00:00", tag="timer_display")
    dpg.add_button(label="Start")

def createFunctionContent():
    dpg.add_button(label="Clock", tag="clock_button")
    dpg.add_button(label="Timer", tag="timer_button")

def createContent():
    with dpg.window(label="Function", tag="function_window", no_title_bar=True, width=dpg.get_viewport_client_width()/5, height=dpg.get_viewport_client_height()):
        createFunctionContent()
    with dpg.window(label="Clock", tag="clock_window", no_title_bar=True, pos= [dpg.get_viewport_client_width()/5,0], width=dpg.get_viewport_client_width(), height=dpg.get_viewport_client_height()):
        createClockContent()
    with dpg.window(label="Timer", tag="timer_window", no_title_bar=True, width=dpg.get_viewport_client_width(), height=dpg.get_viewport_client_height(), show=False):
        createTimerContent()


def renderloop():
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        if tab_state == "clock_selected":
            dpg.set_value("clock", datetime.now().strftime("%H:%M:%S"))
        