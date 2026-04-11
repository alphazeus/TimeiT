
import dearpygui.dearpygui as dpg

def initFont():
    fontdict = {}
    with dpg.font_registry():
        fontdict["clock"] = dpg.add_font("C:/Windows/Fonts/segoeui.ttf", size=150)
        fontdict["default"] = dpg.add_font("C:/Windows/Fonts/times.ttf", size=100)
    return fontdict
