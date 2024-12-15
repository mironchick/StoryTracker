from PyQt5.QtGui import QFontDatabase

# Загрузка шрифта Krona One
font_id = QFontDatabase.addApplicationFont(r"\fonts\KronaOne-Regular.ttf")
font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
