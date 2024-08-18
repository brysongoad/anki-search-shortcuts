from urllib.parse import quote
from aqt import mw
from aqt.qt import QAction, QUrl, QDesktopServices, QMenu

def onSearch(baseUrl: str) -> None:
    text = mw.web.selectedText()
    text = text.strip()
    url = baseUrl + quote(text.encode("utf-8"))
    qurl = QUrl()
    qurl.setUrl(url)
    QDesktopServices.openUrl(qurl)

def createMenuItems() -> list[QAction]:
    menuItems = []

    configList = mw.addonManager.getConfig(__name__)['url_search_list']
    for config in configList:
        action = QAction(mw)
        action.setText(config['name'])
        action.setShortcut(config['shortcut'])
        action.triggered.connect(lambda: onSearch(config['url']))
        menuItems.append(action)
    
    return menuItems