
import dearpygui.dearpygui as dpg

def initFont():
    with dpg.font_registry():
        dpg.add_font("C:/Windows/Fonts/segoeui.ttf", size=150, tag="font_clock")
        dpg.add_font("C:/Windows/Fonts/times.ttf", size=100, tag="font_default")
