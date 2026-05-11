import dearpygui.dearpygui as dpg
import time

TIMER_RUNNING = False
TIMER_REMAINING = 5
TIMER_TARGET_SECONDS = 5
TIMER_DEADLINE = 0

def initTimerTheme():
    with dpg.theme(tag="theme_timer_start_button"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, (120, 58, 58, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (145, 72, 72, 255))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (170, 85, 85, 255))
            dpg.add_theme_color(dpg.mvThemeCol_Text, (240, 232, 232, 255))
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)

def initTimerContent(TIMER_POS_X, TIMER_POS_Y, TIMER_W, TIMER_H):
    initTimerTheme()
    with dpg.window(label="Timer", tag="timer_window", no_title_bar=True, pos=[TIMER_POS_X, TIMER_POS_Y], width=TIMER_W, height=TIMER_H, show=False):
        dpg.add_text("00:00", tag="timer_display", pos=[(TIMER_W / 2) - 100, (TIMER_H / 3) - 80])
        dpg.bind_item_font("timer_display", "font_timer")
        dpg.add_button(label="Start", tag="timer_start_btn", callback=on_timer_start, pos=[(TIMER_W / 2) - 20, (TIMER_H / 2)], width=80, height=40)
        dpg.bind_item_theme("timer_start_btn", "theme_timer_start_button")
    dpg.bind_item_theme("timer_window", "theme_tight_window")

def on_timer_start(sender, app_data, user_data):
    global TIMER_RUNNING, TIMER_DEADLINE, TIMER_TARGET_SECONDS
    TIMER_DEADLINE = time.time() + TIMER_TARGET_SECONDS
    TIMER_RUNNING = True

def format_mm_ss(total_secs:float) -> str:
    m = int(total_secs // 60)
    s = int(total_secs % 60)
    return f"{m:02d}:{s:02d}"

def update_timer_counter():
    global TIMER_RUNNING, TIMER_DEADLINE, TIMER_REMAINING
    TIMER_REMAINING = TIMER_DEADLINE - time.time()
    if TIMER_REMAINING <= 0:
        TIMER_REMAINING = 0
        TIMER_RUNNING = False

def updateTimerContent():
    global TIMER_REMAINING
    if(TIMER_RUNNING == True):
        update_timer_counter()
    dpg.set_value("timer_display", format_mm_ss(TIMER_REMAINING))