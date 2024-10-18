from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QHBoxLayout
from PyQt6.QtGui import QPixmap, QPainter, QBrush, QPainterPath
from PyQt6.QtCore import Qt, QRectF


class CategoryItem(QWidget):
    def __init__(self, photo: str, label: str):
        super().__init__()

        self.label = QLabel(label)
        self.category_photo_label = QLabel()

        self.category_photo = QPixmap(photo)
        self.category_photo_label.setPixmap(self.category_photo.scaled(130, 130))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.category_photo_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.layout)
        self.setStyleSheet("padding: 0; margin: 0;")


class CategoryItemBig(QWidget):
    def __init__(self, photo: str, label: str):
        super().__init__()

        self.label = QLabel(label)
        self.category_photo_label = QLabel()

        self.category_photo = QPixmap(photo)
        self.category_photo_label.setPixmap(self.category_photo.scaled(293, 122))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(self.category_photo_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.layout)
        self.setStyleSheet("padding: 0; margin: 0;")


class Categories(QWidget):
    def __init__(self):
        super().__init__()
        item0 = CategoryItemBig("assets/seafood.png", "Seafood")
        item1 = CategoryItem("assets/lunch.png", "Lunch")
        item2 = CategoryItem("assets/breakfast.png", "Breakfast")
        item3 = CategoryItem("assets/Dinner.png", "Dinner")
        item4 = CategoryItem("assets/vegan.png", "Vegan")
        item5 = CategoryItem("assets/dessert.png", "Dessert")
        item6 = CategoryItem("assets/drinks.png", "Drinks")
        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(item0, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)

        self.layout = QGridLayout()
        self.layout.addWidget(item1, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(item2, 0, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(item3, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(item4, 1, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(item5, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(item6, 2, 1, alignment=Qt.AlignmentFlag.AlignRight)
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.layout)

        self.setLayout(self.main_layout)
        self.setStyleSheet("padding: 0; margin: 0;")
