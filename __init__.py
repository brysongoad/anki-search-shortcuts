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

def createMenuItem() -> None:
    a = QAction(mw)
    a.setText("Search selection in collection")
    shortcut = mw.addonManager.getConfig(__name__)['shortcut']
    a.setShortcut(shortcut)
    mw.form.menuTools.addAction(a)
    a.triggered.connect(onCollectionSearch)

createMenuItem()