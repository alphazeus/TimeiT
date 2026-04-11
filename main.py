
import dearpygui.dearpygui as dpg
import soundControl as sc
from datetime import datetime
import time

dpg.create_context()
dpg.create_viewport(title='TimeiT', width=600, height=200)
dpg.setup_dearpygui()

with dpg.window(label="Clock", no_title_bar=True):
    dpg.add_text(datetime.now().strftime("%H:%M:%S"), tag="clock")
    dpg.add_button(label="Click Me")
    dpg.add_input_text(label="Input Text")


sc.playShortBeep()
dpg.show_viewport()
# dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    dpg.set_value("clock", datetime.now().strftime("%H:%M:%S"))


dpg.destroy_context()