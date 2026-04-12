
import dearpygui.dearpygui as dpg
from datetime import datetime

tab_state = "clock_selected"

def on_tab_change(sender, app_data, user_data):
    if sender == "clock_button":
        tab_state = "clock_selected"
        dpg.configure_item("clock_window", show=True)
        dpg.configure_item("timer_window", show=False)
    elif sender == "timer_button":
        tab_state = "timer_selected"
        dpg.configure_item("clock_window", show=False)
        dpg.configure_item("timer_window", show=True)

def createClockContent():
    with dpg.window(label="Clock", tag="clock_window", no_title_bar=True, pos= [dpg.get_viewport_width()/5,0], width=(dpg.get_viewport_width()*4)/5, height=dpg.get_viewport_height()):
        dpg.add_text(datetime.now().strftime("%H:%M:%S"), tag="clock")
        dpg.bind_item_font("clock", "font_clock")

def createTimerContent():
    with dpg.window(label="Timer", tag="timer_window", no_title_bar=True, pos= [dpg.get_viewport_width()/5,0], width=(dpg.get_viewport_width()*4)/5, height=dpg.get_viewport_height(), show=False):
        dpg.add_text("00:00", tag="timer_display")
        dpg.add_button(label="Start")

def createFunctionContent():
    with dpg.window(label="Function", tag="function_window", no_title_bar=True, width=dpg.get_viewport_width()/5, height=dpg.get_viewport_height()):
        dpg.add_button(label="Clock", tag="clock_button", callback=on_tab_change)
        dpg.add_button(label="Timer", tag="timer_button", callback=on_tab_change)

def createContent():
    createFunctionContent()
    createClockContent()
    createTimerContent()


def renderloop():
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        if tab_state == "clock_selected":
            dpg.set_value("clock", datetime.now().strftime("%H:%M:%S"))
        