# Anki Search Shortcuts
This is an add-on for [Anki](https://apps.ankiweb.net/) that provides handy search functionality for selected text. There are currently two types of search shortcuts included:
1. Search selected text in your Anki collection.
2. Search selected text on the web using a customizable url. For example, if you use Anki for learning Japanese you could set up a shortcut to search text on a Japanese dictionary site such as [Jisho](https://jisho.org/search/anki) that can search based on the url.
## Installation
Clone this repo into the Anki add-on folder and restart Anki. You can find the anki add-on folder by opening Anki and navigating to `Tools -> Add-ons -> View Files`.
## Usage
Select some text while reviewing cards and hit one of the shortcut keys to search the selected text. You can also access the shortcuts through the `Tools` menu under `Search Shortcuts`.
### Customize shortcuts
The search shortcuts can be customized through Anki's add-on menu. Select this add-on from the list, then click config. You will need to restart Anki after modifying the config for the changes to take effect.

The default config looks like this:
```json
{
    "collection_search_shortcut": "Ctrl+B",
    "url_search_list": [
        {
            "name": "Jisho",
            "shortcut": "Ctrl+w",
            "url": "http://jisho.org/search/"
        }
    ]
}
```
You can change the shortcut for searching in your Anki collection by changing the value for `collection_search_shortcut`. You can customize the url search by modifying `url_search_list`. You can add more than one url shortcut if you like by adding to the list:
```json
"url_search_list": [
    {
        "name": "Jisho",
        "shortcut": "Ctrl+w",
        "url": "http://jisho.org/search/"
    },
    {
        "name": "Jisho Kanji",
        "shortcut": "Ctrl+Shift+w",
        "url": "https://jisho.org/search/%23kanji"
    }
]
```
Or remove them all:
```json
"url_search_list": []
```