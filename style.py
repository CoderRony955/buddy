class styling:
    body = """
            QMainWindow {
                background: #eceff4;
            }

            #sidebar {
                background: #030421;
                border-right: 1px solid #181b24;
                border-top-right-radius: 15px;
                border-bottom-right-radius: 15px;
            }

            #menuToggle,
            #sidebar QPushButton {
                min-height: 38px;
                border-radius: 15px;
                border: none;
                padding: 0 14px;
                color: #f3f5fb;
                text-align: left;
                font-size: 13px;
                background: #2d3342;
            }

            #menuToggle:hover,
            #sidebar QPushButton:hover {
                background: #394155;
            }

            #sidebar QPushButton:checked {
                background: #4f6bed;
            }

            #contentArea {
                background: #f8f9fd;
            }

            #screenTitle {
                color: #1f2430;
                font-size: 28px;
                font-weight: 700;
            }

            #screenSubtitle {
                color: #4d5566;
                font-size: 14px;
                line-height: 1.4em;
            }
            """

    search_btn = """
    
            QPushButton#search {
                min-height: 38px;
                border-radius: 15px;
                border: none;
                padding: 0 14px;
                color: black;
                text-align: left;
                font-size: 13px;
                background: #06695f;
            }
            
            QPushButton#search:hover {
                background: #495c5a;
            }
            
            QPushButton#search:pressed {
                background: #394155;
            }
    """
    all_free_games_section_btn = """
    
            QPushButton#all {
                min-height: 38px;
                border-radius: 15px;
                border: none;
                padding: 0 14px;
                color: black;
                text-align: left;
                font-size: 13px;
                background: #0b6906;
            }
            
            QPushButton#all:hover {
                background: #4f614e;
            }
            
            QPushButton#all:pressed {
                background: #00ff04;
            }
    """

    epic_games_section_btn = """
    QPushButton#epic_games {
                min-height: 38px;
                border-radius: 15px;
                border: none;
                text-align: left;
                padding: 0 14px;
                color: black;
                text-align: left;
                font-size: 13px;
                background: white;
            }
    
    QPushButton#epic_games:hover {
                background: #c6ccc6;
            }
            
    QPushButton#epic_games:pressed {
                background: #c6ccc6;
            }
    
    """

    steam_section_btn = """
    QPushButton#steam {
                min-height: 38px;
                border-radius: 15px;
                border: none;
                padding: 0 14px;
                color: #f3f5fb;
                text-align: left;
                font-size: 13px;
                background: #20376b;
            }
    
    QPushButton#steam:hover {
                background: #292a38;
            }
            
    QPushButton#steam:pressed {
                background: #0b1438;
            }
    
    """

    ubisoft_section_btn = """
    QPushButton#ubisoft {
                min-height: 38px;
                border-radius: 15px;
                border: none;
                padding: 0 14px;
                color: black;
                text-align: left;
                font-size: 13px;
                background: #ffffff;
            }
    
    QPushButton#ubisoft:hover {
                background: #6b6c6e;
                color: black;
            }
            
    QPushButton#ubisoft:pressed {
                background: #394155;
                color: black;
            }
    
    """

    android_section_btn = """
    QPushButton#android {
                min-height: 38px;
                border-radius: 15px;
                border: none;
                padding: 0 14px;
                color: black;
                text-align: left;
                font-size: 13px;
                background: #e1e3e1;
            }
    
    QPushButton#android:hover {
                background: #868a86;
                color: black;
            }
            
    QPushButton#android:pressed {
                background: #868a86;
                color: black;
            }
    
    """
