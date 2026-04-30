# contentInterface.py
import dearpygui.dearpygui as dpg
from datetime import datetime

tab_state = "clock_selected"

# Layout values initialized after viewport exists
TITLE_H = 40
vw = 0
vh = 0
LEFT_W = 0
CONTENT_Y = 0
CONTENT_H = 0
RIGHT_X = 0
RIGHT_W = 0

def init_layout():
    global LEFT_W, CONTENT_Y, CONTENT_H, RIGHT_X, RIGHT_W, vw, vh
    vw = dpg.get_viewport_width()
    vh = dpg.get_viewport_height()

    LEFT_W = vw // 5
    CONTENT_Y = TITLE_H
    CONTENT_H = vh - TITLE_H
    RIGHT_X = LEFT_W
    RIGHT_W = vw - LEFT_W

def initTheme():
    with dpg.theme(tag="theme_accent_button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (45, 52, 68, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (55, 65, 88, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (80, 170, 255, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (230, 233, 242, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)

    with dpg.theme(tag="theme_tight_window"):
        with dpg.theme_component(dpg.mvWindowAppItem):
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, 0)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 0, 0)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 0, 0)
    
    with dpg.theme(tag="theme_close_button"):
        with dpg.theme_component(dpg.mvButton):
            # subtle base red
            dpg.add_theme_color(dpg.mvThemeCol_Button, (120, 58, 58, 255))
            # slightly brighter on hover
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (145, 72, 72, 255))
            # a bit stronger when pressed
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (170, 85, 85, 255))
            # soft off-white text
            dpg.add_theme_color(dpg.mvThemeCol_Text, (240, 232, 232, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)

def on_tab_change(sender, app_data, user_data):
    global tab_state
    if sender == "clock_button":
        tab_state = "clock_selected"
        dpg.configure_item("clock_window", show=True)
        dpg.configure_item("timer_window", show=False)
    elif sender == "timer_button":
        tab_state = "timer_selected"
        dpg.configure_item("clock_window", show=False)
        dpg.configure_item("timer_window", show=True)

def on_close():
    dpg.stop_dearpygui()

def createTitleContent():
    total_w = LEFT_W + RIGHT_W
    btn_w = 32
    btn_h = 30
    pad_r = 6
    y = max(0, (TITLE_H - btn_h) // 2)
    with dpg.window( label="Title", tag="title_window", no_title_bar=True, no_move=True, no_resize=True, no_collapse=True, no_scrollbar=True, no_bring_to_front_on_focus=True, pos=[0, 0], width=total_w, height=TITLE_H):
        dpg.add_button( label="X", tag="close_btn", width=btn_w, height=btn_h, pos=[total_w - btn_w - pad_r, y], callback=on_close )
        dpg.bind_item_theme("close_btn", "theme_close_button")
    dpg.bind_item_theme("title_window", "theme_tight_window")

def createClockContent():
    with dpg.window(label="Clock", tag="clock_window", no_title_bar=True, pos=[RIGHT_X, CONTENT_Y], width=RIGHT_W, height=CONTENT_H):
        dpg.add_text(datetime.now().strftime("%H:%M:%S"), tag="clock", pos=[RIGHT_X - 50, CONTENT_Y])
        dpg.bind_item_font("clock", "font_clock")
    dpg.bind_item_theme("clock_window", "theme_tight_window")

def createTimerContent():
    with dpg.window(label="Timer", tag="timer_window", no_title_bar=True, pos=[RIGHT_X, CONTENT_Y], width=RIGHT_W, height=CONTENT_H, show=False):
        dpg.add_text("00:00", tag="timer_display")
        dpg.add_button(label="Start")
    dpg.bind_item_theme("timer_window", "theme_tight_window")

def createFunctionContent():
    with dpg.window(label="Function", tag="function_window", no_title_bar=True, pos=[0, CONTENT_Y], width=LEFT_W, height=CONTENT_H):
        btn_h = CONTENT_H // 2
        dpg.add_button(label="Clock", tag="clock_button", callback=on_tab_change, width=LEFT_W, height=btn_h)
        dpg.bind_item_theme("clock_button", "theme_accent_button")
        dpg.add_button(label="Timer", tag="timer_button", callback=on_tab_change, width=LEFT_W, height=btn_h)
        dpg.bind_item_theme("timer_button", "theme_accent_button")
    dpg.bind_item_theme("function_window", "theme_tight_window")

def createContent():
    init_layout()  # important: runs after viewport is created
    createTitleContent()
    createFunctionContent()
    createClockContent()
    createTimerContent()

def renderloop():
    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()
        if tab_state == "clock_selected":
            dpg.set_value("clock", datetime.now().strftime("%H:%M:%S"))