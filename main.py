import dearpygui.dearpygui as dpg
import soundControl as sc
import fontControl
import contentInterface as ci

WINDOW_WIDTH    =   800
WINDOW_HEIGHT   =   800

dpg.create_context()

fontControl.initFont()
ci.initTheme()

dpg.create_viewport(title='TimeiT', width=WINDOW_WIDTH, height=WINDOW_HEIGHT, decorated=False)
dpg.setup_dearpygui()

ci.createContent()

dpg.show_viewport()

# dpg.start_dearpygui()
ci.renderloop()

dpg.destroy_context()