
import dearpygui.dearpygui as dpg
import soundControl as sc
import time
import fontControl as fc
import contentInterface as ci

dpg.create_context()

fc.initFont()

dpg.create_viewport(title='TimeiT', width=600, height=200)
dpg.setup_dearpygui()

ci.createContent()


sc.playShortBeep()
dpg.show_viewport()

# dpg.start_dearpygui()
ci.renderloop()


dpg.destroy_context()