def update_shortcuts(custom_keys):
        # Configure actions.
        action = QtWidgets.QAction('Print', None)
        action.setEnabled(True)
        printkey = QtGui.QKeySequence(QtGui.QKeySequence.Print)
        if 'print' in custom_keys.keys():
            printkey = custom_keys['print'] 
        elif printkey.matches("Ctrl+P") and sys.platform != 'darwin':
            # Only override the default if there is a collision.
            # Qt ctrl = cmd on OSX, so the match gets a false positive on OSX.
            printkey = "Ctrl+Shift+P"

        action.setShortcut(printkey)
        action.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        action.triggered.connect(self.print_)
        self.addAction(action)
        self.print_action = action

        action = QtWidgets.QAction('Save as HTML/XML', None)
        action.setShortcut(QtGui.QKeySequence.Save)
        action.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        action.triggered.connect(self.export_html)
        self.addAction(action)
        self.export_action = action

        action = QtWidgets.QAction('Select All', None)
        action.setEnabled(True)
        selectall = QtGui.QKeySequence(QtGui.QKeySequence.SelectAll)
        if selectall.matches("Ctrl+A") and sys.platform != 'darwin':
            # Only override the default if there is a collision.
            # Qt ctrl = cmd on OSX, so the match gets a false positive on OSX.
            selectall = "Ctrl+Shift+A"
        action.setShortcut(selectall)
        action.setShortcutContext(QtCore.Qt.WidgetWithChildrenShortcut)
        action.triggered.connect(self.select_all_smart)
        self.addAction(action)
        self.select_all_action = action

        self.increase_font_size = QtWidgets.QAction("Bigger Font",
                self,
                shortcut=QtGui.QKeySequence.ZoomIn,
                shortcutContext=QtCore.Qt.WidgetWithChildrenShortcut,
                statusTip="Increase the font size by one point",
                triggered=self._increase_font_size)
        self.addAction(self.increase_font_size)

        self.decrease_font_size = QtWidgets.QAction("Smaller Font",
                self,
                shortcut=QtGui.QKeySequence.ZoomOut,
                shortcutContext=QtCore.Qt.WidgetWithChildrenShortcut,
                statusTip="Decrease the font size by one point",
                triggered=self._decrease_font_size)
        self.addAction(self.decrease_font_size)

        self.reset_font_size = QtWidgets.QAction("Normal Font",
                self,
                shortcut="Ctrl+0",
                shortcutContext=QtCore.Qt.WidgetWithChildrenShortcut,
                statusTip="Restore the Normal font size",
                triggered=self.reset_font)
        self.addAction(self.reset_font_size)
