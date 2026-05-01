import os
import dearpygui.dearpygui as dpg

def initFont():
    with dpg.font_registry():
        # Clock font (large, stable digits)
        if os.path.exists("C:/Windows/Fonts/consola.ttf"):
            dpg.add_font("C:/Windows/Fonts/consola.ttf", size=120, tag="font_clock")
        else:
            dpg.add_font("C:/Windows/Fonts/segoeui.ttf", size=120, tag="font_clock")

        # Title font (Segoe UI Semibold)
        if os.path.exists("C:/Windows/Fonts/seguisb.ttf"):
            dpg.add_font("C:/Windows/Fonts/seguisb.ttf", size=30, tag="font_title")
        else:
            dpg.add_font("C:/Windows/Fonts/segoeui.ttf", size=30, tag="font_title")

        # General UI font
        dpg.add_font("C:/Windows/Fonts/segoeui.ttf", size=16, tag="font_ui")