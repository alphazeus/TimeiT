import dearpygui.dearpygui as dpg
import time

TIMER_RUNNING = False
TIMER_SECONDS = 0
TIMER_TARGET_SECONDS = 5
TIMER_DEADLINE = 0

def initTimerContent(TIMER_POS_X, TIMER_POS_Y, TIMER_W, TIMER_H):
    with dpg.window(label="Timer", tag="timer_window", no_title_bar=True, pos=[TIMER_POS_X, TIMER_POS_Y], width=TIMER_W, height=TIMER_H, show=False):
        dpg.add_text("00:00", tag="timer_display")
        dpg.add_button(label="Start", callback=on_timer_start)
    dpg.bind_item_theme("timer_window", "theme_tight_window")

def on_timer_start(sender, app_data, user_data):
    global TIMER_RUNNING, TIMER_DEADLINE
    TIMER_DEADLINE = time.perf_counter + TIMER_TARGET_SECONDS
    TIMER_RUNNING = True

def format_mm_ss(total_secs:float) -> str:
    m = int(total_secs // 60)
    s = int(total_secs % 60)
    return f"{m:02d}:{s:02d}"

def updateTimerContent():
    dpg.set_value("timer_display", format_mm_ss(5))