
import dearpygui.dearpygui as dpg
import soundControl as sc
from datetime import datetime
import time
import fontControl as fc

dpg.create_context()

fonts = fc.initFont()

dpg.create_viewport(title='TimeiT', width=600, height=200)
dpg.setup_dearpygui()



with dpg.window(label="Clock", no_title_bar=True, width=dpg.get_viewport_client_width(), height=dpg.get_viewport_client_height()):
    clock = dpg.add_text(datetime.now().strftime("%H:%M:%S"))
    dpg.bind_item_font(clock, fonts["clock"])


sc.playShortBeep()
dpg.show_viewport()
# dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()
    dpg.set_value(clock, datetime.now().strftime("%H:%M:%S"))


dpg.destroy_context()