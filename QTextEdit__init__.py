from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os

class TextEdit(QMainWindow):
    def __init__ (self):
        super().__init__()

        window = QWidget()
        self.vbox = QVBoxLayout()
        window.setLayout(self.vbox)
        self.setCentralWidget(window)

        self.bar = self.menuBar()
    
        self.setWindowTitle("myNote")
        self.setMinimumSize(500, 600)

        self.text = QTextEdit()
        self.line = QLineEdit()
        self.line.setMaximumHeight(20)
        self.line.setAlignment(Qt.AlignRight)
        
        self.vbox.addWidget(self.text)
        self.vbox.addWidget(self.line)

        self.MyMenu()
        self.WordCounter()
        

    def ClearMe(self):    
        self.content = self.text.clear() 
    
    def Quit(self):
        exit()
                

    def MyMenu(self):
        file = self.bar.addMenu("File")

        new = QAction("New", self)
        new.setShortcut("Ctrl+n")
        file.addAction(new)
        
        open_ = QAction("Open", self)
        open_.setShortcut("Ctrl+o")
        file.addAction(open_)
       
        save = QAction("Save", self)
        save.setShortcut("Ctrl+s")
        file.addAction(save)
       
        save_as = QAction("Save As", self)
        save_as.setShortcut("Ctrl+Shift+s")
        file.addAction(save_as)
       
        exit_ = QAction("Exit", self)
        exit_.setShortcut("Alt+F4")
        file.addAction(exit_)

        view = self.bar.addMenu("View")
        # themes = view.addMenu("Themes")
        black = QAction("White on Black", self)
        view.addAction(black)
        
        red = QAction("Red on White", self)
        view.addAction(red)

        green = QAction("Green on Black", self)
        view.addAction(green)
  
        about = self.bar.addMenu("About") 
        author = QAction("Author", self)
        about.addAction(author)
        
        version = QAction("Version", self)
        about.addAction(version)

        file.triggered[QAction].connect(self.Events)
        view.triggered[QAction].connect(self.Themes)
        about.triggered[QAction].connect(self.Events)


    def Themes(self, event):
        e = event.text()
        
        whiteOnBlack = "QTextEdit {font: 14px; background-color: black; color: white}"
        redOnWhite = "QTextEdit {font: 14px; color: red}"
        greenOnBlack = "QTextEdit {font: 14px; background-color: black; color: green}"
        
        if e == "White on Black":
            self.text.setStyleSheet(whiteOnBlack)
            self.line.setStyleSheet(whiteOnBlack)
        
        elif e == "Red on White":
            self.text.setStyleSheet(redOnWhite)
            self.line.setStyleSheet(redOnWhite)

        else:
            self.text.setStyleSheet(greenOnBlack)
            self.line.setStyleSheet(greenOnBlack)


    def Events(self, event):
        e = event.text()
        self.WordCounter()

        f = QFileDialog()
        
        if e == "Open": 
            file = f.getOpenFileName()[0]  
            self.fileName = file.split(r'/')[-1]
            f.setFileMode(QFileDialog.ExistingFiles)
            f.setNameFilter("TXT files (*.txt)")
            f.setAcceptMode(QFileDialog.AcceptOpen)

            file = open(self.fileName)
            self.text.setText(file.read())
            self.content = self.text.toPlainText()
            self.WordCounter()

        elif e == "Save":

            self.fileName = 'untitled'
            self.CreatingFile()
            self.WordCounter()

        elif e == "Save As":
            
            self.fileName = f.getSaveFileName()[0] 
            f.setAcceptMode(QFileDialog.AcceptSave)
            self.setWindowTitle(self.fileName.split(r'/')[-1])
            f.setDefaultSuffix("txt")            
            
            self.CreatingFile()
            self.WordCounter()

        elif e == "Author":
            print("""
            Author Name: Minux_Dev
            Company: Minux Inc.
            Profission: Software Engeneer""")

        elif e == "Version":
            print("""
            Name: myNote
            Version: 0.1
            Reliese Date: 01.06.2021
            Programing Language: Python3.8.5
            Official Language: English""")
    
    def WordCounter(self):

        if self.text.toPlainText() == "":
            total = "Chars: 0 \t \t Lines: 0"
        else:
            lines = len(self.text.toPlainText().splitlines())
            chars = len(self.text.toPlainText().split(' '))

            if lines > 1:
                chars += 1
        
            total = f"Chars: {chars} \t \t Lines: {lines}"

        self.line.setText(total)

    def CreatingFile(self):
        self.content = self.text.toPlainText()
        if '.txt' in self.fileName:
            currentFile = self.fileName

        else:
            currentFile = self.fileName+".txt" 

        with open(currentFile, "w") as file:
            file.write(self.content)

if __name__ == "__main__":
    app = QApplication([])
    text = TextEdit()
    text.show()
    sys.exit(app.exec_())

'''
Consequat nisi officia id exercitation magna anim anim irure consectetur.
Consequat nisi officia id exercitation magna anim anim irure consectetur.
Consequat nisi officia id exercitation magna anim anim irure consectetur.
'''
