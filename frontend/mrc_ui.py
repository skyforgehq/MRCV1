import sys
import os
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton # type: ignore
from PyQt6.QtSvgWidgets import QSvgWidget # type: ignore
from PyQt6.QtCore import Qt, QPoint # type: ignore

class MRC_UI(QWidget):
    def __init__(self):
        super().__init__()

        # **Window Configuration**
        self.setWindowTitle("MRC Radar UI")
        self.setGeometry(100, 100, 615, 570)  # Window size
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove title bar
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # Ensure no borders

        # **Enable Dragging Variables**
        self.old_pos = QPoint()

        # **Check if SVG File Exists**
        svg_path = "assets/ui_design.svg"
        if not os.path.exists(svg_path):
            print(f"⚠️ Error: SVG file '{svg_path}' not found!")
            sys.exit(1)  # Exit if file is missing

        # **Load Figma SVG UI**
        self.svg_widget = QSvgWidget(svg_path)
        self.svg_widget.setFixedSize(615, 570)  # Match Figma UI dimensions
        self.svg_widget.setParent(self)

        # **Create Clickable Buttons (Square with Rounded Corners)**
        self.create_buttons()

    def create_buttons(self):
        """Creates clickable square buttons with rounded corners."""
        button_positions = {
            # **Left Buttons**
            "MENU": (3, 63, 60, 60),
            "A-A": (3, 154, 60, 60),
            "A-G": (3, 245, 60, 60),
            "SNSR": (3, 336, 60, 60),
            "WPN": (3, 427, 60, 60),

            # **Right Buttons**
            "R1": (525, 63, 60, 60),
            "R2": (525, 154, 60, 60),
            "R3": (525, 245, 60, 60),
            "R4": (525, 336, 60, 60),
            "R5": (525, 427, 60, 60),

            # **Bottom Buttons**
            "B1": (150, 510, 60, 60),
            "B2": (250, 510, 60, 60),
            "B3": (340, 510, 60, 60),
            "B4": (430, 510, 60, 60),
        }

        for text, (x, y, width, height) in button_positions.items():
            btn = QPushButton("", self)
            btn.setGeometry(x, y, width, height)
            btn.setStyleSheet("background-color: rgba(0,0,0,0); border:none") #transparent buttons
            btn.clicked.connect(lambda _, b=text: self.button_click(b))

    def button_click(self, button_text):
        """Handles button clicks."""
        print(f"Clicked: {button_text}")

    # **Enable Window Dragging**
    def mousePressEvent(self, event):
        """Stores the initial position when clicking."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Moves the window when dragging."""
        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

# **Run the Application**
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MRC_UI()
    window.show()
    sys.exit(app.exec())
