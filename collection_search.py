import aqt
from aqt import mw
from aqt.qt import QAction

def search(selectedText: str) -> None:
    selectedText = selectedText.strip()
    searchTuple = (selectedText, ) if selectedText else None
    aqt.dialogs.open("Browser", mw, search=searchTuple)

def onCollectionSearch() -> None:
    text = mw.web.selectedText()
    search(text)

def createMenuItem() -> QAction:
    action = QAction(mw)
    action.setText("Search in collection")
    shortcut = mw.addonManager.getConfig(__name__)['collection_search_shortcut']
    action.setShortcut(shortcut)
    action.triggered.connect(onCollectionSearch)

    return action