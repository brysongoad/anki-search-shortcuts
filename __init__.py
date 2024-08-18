from . import collection_search, url_search
from aqt import mw
from aqt.qt import QMenu

menu = QMenu()
menu.setTitle("Search Shortcuts")
mw.form.menuTools.addAction(menu.menuAction())
mw.form.searchShortcuts = menu

menu.addAction(collection_search.createMenuItem())
menu.addSeparator()
menu.addActions(url_search.createMenuItems())