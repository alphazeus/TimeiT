
import dearpygui.dearpygui as dpg

def initFont():
    with dpg.font_registry():
        clock_font = dpg.add_font("C:/Windows/Fonts/segoeui.ttf", size=150)
        default_font = dpg.add_font("C:/Windows/Fonts/times.ttf", size=100)
    return {
        "clock": clock_font,
        "default": default_font
    }
