import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget, QWidget, 
                             QVBoxLayout, QLineEdit, QToolBar, QAction, QPushButton)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Панель навигации
        self.navbar = QToolBar()
        self.back_btn = QAction("←", self)
        self.forward_btn = QAction("→", self)
        self.reload_btn = QAction("↻", self)
        self.url_bar = QLineEdit()
        
        self.navbar.addAction(self.back_btn)
        self.navbar.addAction(self.forward_btn)
        self.navbar.addAction(self.reload_btn)
        self.navbar.addWidget(self.url_bar)
        
        # Веб-виджет
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        
        # Добавляем элементы в layout
        self.layout.addWidget(self.navbar)
        self.layout.addWidget(self.browser)
        
        # Подключаем сигналы
        self.back_btn.triggered.connect(self.browser.back)
        self.forward_btn.triggered.connect(self.browser.forward)
        self.reload_btn.triggered.connect(self.browser.reload)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.browser.urlChanged.connect(self.update_url)
    
    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))
    
    def update_url(self, q):
        self.url_bar.setText(q.toString())

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZenTerium Browser for InteriumOS")
        self.setGeometry(100, 100, 1024, 768)
        
        # Создаем виджет с вкладками
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        
        # Кнопка добавления новой вкладки (теперь как QPushButton)
        self.new_tab_btn = QPushButton("+")
        self.new_tab_btn.clicked.connect(self.add_new_tab)
        self.tabs.setCornerWidget(self.new_tab_btn)
        
        # Добавляем первую вкладку
        self.add_new_tab()
        
        self.setCentralWidget(self.tabs)
    
    def add_new_tab(self):
        tab = BrowserTab()
        index = self.tabs.addTab(tab, "Новая вкладка")
        self.tabs.setCurrentIndex(index)
        
        # Обновляем заголовок вкладки при изменении URL
        tab.browser.urlChanged.connect(lambda q, tab=tab: self.update_tab_title(tab))
    
    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
    
    def update_tab_title(self, tab):
        index = self.tabs.indexOf(tab)
        title = tab.browser.page().title()
        if len(title) > 15:
            title = title[:15] + "..."
        self.tabs.setTabText(index, title)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())