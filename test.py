LuaMaker_NahBro3.pyc (Python 3.13)
[Code]
    File Name: LuaMaker_NahBro3.py
    Object Name: <module>
    Qualified Name: <module>
    Arg Count: 0
    Pos Only Arg Count: 0
    KW Only Arg Count: 0
    Stack Size: 6
    Flags: 0x00000000
    [Names]
        'sys'
        're'
        'json'
        'shutil'
        'requests'
        'ctypes'
        'logging'
        'os'
        'zipfile'
        'time'
        'subprocess'
        'sourcedefender'
        'pathlib'
        'Path'
        'PyQt6.QtWidgets'
        'QApplication'
        'QMainWindow'
        'QWidget'
        'QVBoxLayout'
        'QHBoxLayout'
        'QGridLayout'
        'QLabel'
        'QLineEdit'
        'QPushButton'
        'QTextEdit'
        'QFileDialog'
        'QMessageBox'
        'QComboBox'
        'QTabWidget'
        'PyQt6.QtGui'
        'QIntValidator'
        'QFont'
        'PyQt6.QtCore'
        'Qt'
        'QThread'
        'basicConfig'
        'WARNING'
        'str'
        'parse_acf_file'
        'dict'
        'parse_appmanifest'
        'get_manifest_from_acf'
        'SteamAPI'
        'LuaScriptMaker'
        'main'
        '__name__'
    [Locals+Names]
    [Constants]
        0
        None
        (
            'Path'
        )
        (
            'QApplication'
            'QMainWindow'
            'QWidget'
            'QVBoxLayout'
            'QHBoxLayout'
            'QGridLayout'
            'QLabel'
            'QLineEdit'
            'QPushButton'
            'QTextEdit'
            'QFileDialog'
            'QMessageBox'
            'QComboBox'
            'QTabWidget'
        )
        (
            'QIntValidator'
            'QFont'
        )
        (
            'Qt'
            'QThread'
        )
        'error_log.txt'
        '%(asctime)s - %(levelname)s - %(message)s'
        (
            'filename'
            'level'
            'format'
        )
        'acf_path'
        'return'
        [Code]
            File Name: LuaMaker_NahBro3.py
            Object Name: parse_acf_file
            Qualified Name: parse_acf_file
            Arg Count: 1
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 6
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'open'
                'read'
                're'
                'search'
                'group'
                'Exception'
                'logging'
                'exception'
            [Locals+Names]
                'acf_path'
                'f'
                'content'
                'm'
                'e'
            [Constants]
                None
                'r'
                'utf-8'
                (
                    'encoding'
                )
                '"installdir"\\s*"([^"]+)"'
                1
                'Error parsing ACF file: %s'
            [Disassembly]
                0       RESUME                          0
                2       NOP
                4       LOAD_FAST                       0: acf_path
                6       LOAD_ATTR                       1: open
                26      LOAD_CONST                      1: 'r'
                28      LOAD_CONST                      2: 'utf-8'
                30      LOAD_CONST                      3: ('encoding',)
                32      CALL_KW                         2
                34      BEFORE_WITH
                36      STORE_FAST                      1: f
                38      LOAD_FAST                       1: f
                40      LOAD_ATTR                       3: read
                60      CALL                            0
                68      STORE_FAST                      2: content
                70      LOAD_CONST                      0: None
                72      LOAD_CONST                      0: None
                74      LOAD_CONST                      0: None
                76      CALL                            2
                84      POP_TOP
                86      LOAD_GLOBAL                     4: re
                96      LOAD_ATTR                       6: search
                116     PUSH_NULL
                118     LOAD_CONST                      4: '"installdir"\\s*"([^"]+)"'
                120     LOAD_FAST_CHECK                 2: content
                122     CALL                            2
                130     STORE_FAST                      3: m
                132     LOAD_FAST                       3: m
                134     TO_BOOL
                142     POP_JUMP_IF_FALSE               17 (to 178)
                146     LOAD_FAST                       3: m
                148     LOAD_ATTR                       9: group
                168     LOAD_CONST                      5: 1
                170     CALL                            1
                178     RETURN_VALUE
                180     NOP
                182     RETURN_CONST                    0: None
                184     PUSH_EXC_INFO
                186     WITH_EXCEPT_START
                188     TO_BOOL
                196     POP_JUMP_IF_TRUE                1 (to 200)
                200     RERAISE                         2
                202     POP_TOP
                204     POP_EXCEPT
                206     POP_TOP
                208     POP_TOP
                210     JUMP_BACKWARD_NO_INTERRUPT      63 (to 86)
                212     COPY                            3
                214     POP_EXCEPT
                216     RERAISE                         1
                218     PUSH_EXC_INFO
                220     LOAD_GLOBAL                     10: Exception
                230     CHECK_EXC_MATCH
                232     POP_JUMP_IF_FALSE               33 (to 300)
                236     STORE_FAST                      4: e
                238     LOAD_GLOBAL                     12: logging
                248     LOAD_ATTR                       14: exception
                268     PUSH_NULL
                270     LOAD_CONST                      6: 'Error parsing ACF file: %s'
                272     LOAD_FAST                       0: acf_path
                274     CALL                            2
                282     POP_TOP
                284     POP_EXCEPT
                286     LOAD_CONST                      0: None
                288     STORE_FAST                      4: e
                290     DELETE_FAST                     4: e
                292     RETURN_CONST                    0: None
                294     LOAD_CONST                      0: None
                296     STORE_FAST                      4: e
                298     DELETE_FAST                     4: e
                300     RERAISE                         1
                302     RERAISE                         0
                304     COPY                            3
                306     POP_EXCEPT
                308     RERAISE                         1
        [Code]
            File Name: LuaMaker_NahBro3.py
            Object Name: parse_appmanifest
            Qualified Name: parse_appmanifest
            Arg Count: 1
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 6
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'open'
                'read'
                're'
                'search'
                'group'
                'Exception'
                'logging'
                'exception'
            [Locals+Names]
                'acf_path'
                'data'
                'f'
                'content'
                'm_appid'
                'm_name'
                'e'
            [Constants]
                None
                'r'
                'utf-8'
                (
                    'encoding'
                )
                '"appid"\\s*"(\\d+)"'
                '"name"\\s*"([^"]+)"'
                1
                'appid'
                'name'
                'Error parsing appmanifest file: %s'
            [Disassembly]
                0       RESUME                          0
                2       BUILD_MAP                       0
                4       STORE_FAST                      1: data
                6       NOP
                8       LOAD_FAST                       0: acf_path
                10      LOAD_ATTR                       1: open
                30      LOAD_CONST                      1: 'r'
                32      LOAD_CONST                      2: 'utf-8'
                34      LOAD_CONST                      3: ('encoding',)
                36      CALL_KW                         2
                38      BEFORE_WITH
                40      STORE_FAST                      2: f
                42      LOAD_FAST                       2: f
                44      LOAD_ATTR                       3: read
                64      CALL                            0
                72      STORE_FAST                      3: content
                74      LOAD_CONST                      0: None
                76      LOAD_CONST                      0: None
                78      LOAD_CONST                      0: None
                80      CALL                            2
                88      POP_TOP
                90      LOAD_GLOBAL                     4: re
                100     LOAD_ATTR                       6: search
                120     PUSH_NULL
                122     LOAD_CONST                      4: '"appid"\\s*"(\\d+)"'
                124     LOAD_FAST_CHECK                 3: content
                126     CALL                            2
                134     STORE_FAST                      4: m_appid
                136     LOAD_GLOBAL                     4: re
                146     LOAD_ATTR                       6: search
                166     PUSH_NULL
                168     LOAD_CONST                      5: '"name"\\s*"([^"]+)"'
                170     LOAD_FAST                       3: content
                172     CALL                            2
                180     STORE_FAST                      5: m_name
                182     LOAD_FAST                       4: m_appid
                184     TO_BOOL
                192     POP_JUMP_IF_FALSE               20 (to 234)
                196     LOAD_FAST                       4: m_appid
                198     LOAD_ATTR                       9: group
                218     LOAD_CONST                      6: 1
                220     CALL                            1
                228     LOAD_FAST                       1: data
                230     LOAD_CONST                      7: 'appid'
                232     STORE_SUBSCR
                236     LOAD_FAST                       5: m_name
                238     TO_BOOL
                246     POP_JUMP_IF_FALSE               20 (to 288)
                250     LOAD_FAST                       5: m_name
                252     LOAD_ATTR                       9: group
                272     LOAD_CONST                      6: 1
                274     CALL                            1
                282     LOAD_FAST                       1: data
                284     LOAD_CONST                      8: 'name'
                286     STORE_SUBSCR
                290     LOAD_FAST                       1: data
                292     RETURN_VALUE
                294     PUSH_EXC_INFO
                296     WITH_EXCEPT_START
                298     TO_BOOL
                306     POP_JUMP_IF_TRUE                1 (to 310)
                310     RERAISE                         2
                312     POP_TOP
                314     POP_EXCEPT
                316     POP_TOP
                318     POP_TOP
                320     JUMP_BACKWARD_NO_INTERRUPT      116 (to 90)
                322     COPY                            3
                324     POP_EXCEPT
                326     RERAISE                         1
                328     PUSH_EXC_INFO
                330     LOAD_GLOBAL                     10: Exception
                340     CHECK_EXC_MATCH
                342     POP_JUMP_IF_FALSE               34 (to 412)
                346     STORE_FAST                      6: e
                348     LOAD_GLOBAL                     12: logging
                358     LOAD_ATTR                       14: exception
                378     PUSH_NULL
                380     LOAD_CONST                      9: 'Error parsing appmanifest file: %s'
                382     LOAD_FAST                       0: acf_path
                384     CALL                            2
                392     POP_TOP
                394     POP_EXCEPT
                396     LOAD_CONST                      0: None
                398     STORE_FAST                      6: e
                400     DELETE_FAST                     6: e
                402     LOAD_FAST                       1: data
                404     RETURN_VALUE
                406     LOAD_CONST                      0: None
                408     STORE_FAST                      6: e
                410     DELETE_FAST                     6: e
                412     RERAISE                         1
                414     RERAISE                         0
                416     COPY                            3
                418     POP_EXCEPT
                420     RERAISE                         1
        [Code]
            File Name: LuaMaker_NahBro3.py
            Object Name: get_manifest_from_acf
            Qualified Name: get_manifest_from_acf
            Arg Count: 1
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 6
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'open'
                'read'
                're'
                'search'
                'group'
                'Exception'
                'logging'
                'exception'
            [Locals+Names]
                'acf_path'
                'f'
                'content'
                'm'
                'e'
            [Constants]
                None
                'r'
                'utf-8'
                (
                    'encoding'
                )
                '"buildid"\\s*"(\\d+)"'
                1
                'Unknown'
                'Error retrieving buildid from %s'
            [Disassembly]
                0       RESUME                          0
                2       NOP
                4       LOAD_FAST                       0: acf_path
                6       LOAD_ATTR                       1: open
                26      LOAD_CONST                      1: 'r'
                28      LOAD_CONST                      2: 'utf-8'
                30      LOAD_CONST                      3: ('encoding',)
                32      CALL_KW                         2
                34      BEFORE_WITH
                36      STORE_FAST                      1: f
                38      LOAD_FAST                       1: f
                40      LOAD_ATTR                       3: read
                60      CALL                            0
                68      STORE_FAST                      2: content
                70      LOAD_CONST                      0: None
                72      LOAD_CONST                      0: None
                74      LOAD_CONST                      0: None
                76      CALL                            2
                84      POP_TOP
                86      LOAD_GLOBAL                     4: re
                96      LOAD_ATTR                       6: search
                116     PUSH_NULL
                118     LOAD_CONST                      4: '"buildid"\\s*"(\\d+)"'
                120     LOAD_FAST_CHECK                 2: content
                122     CALL                            2
                130     STORE_FAST                      3: m
                132     LOAD_FAST                       3: m
                134     TO_BOOL
                142     POP_JUMP_IF_FALSE               17 (to 178)
                146     LOAD_FAST                       3: m
                148     LOAD_ATTR                       9: group
                168     LOAD_CONST                      5: 1
                170     CALL                            1
                178     RETURN_VALUE
                180     LOAD_CONST                      6: 'Unknown'
                182     RETURN_VALUE
                184     PUSH_EXC_INFO
                186     WITH_EXCEPT_START
                188     TO_BOOL
                196     POP_JUMP_IF_TRUE                1 (to 200)
                200     RERAISE                         2
                202     POP_TOP
                204     POP_EXCEPT
                206     POP_TOP
                208     POP_TOP
                210     JUMP_BACKWARD_NO_INTERRUPT      63 (to 86)
                212     COPY                            3
                214     POP_EXCEPT
                216     RERAISE                         1
                218     PUSH_EXC_INFO
                220     LOAD_GLOBAL                     10: Exception
                230     CHECK_EXC_MATCH
                232     POP_JUMP_IF_FALSE               33 (to 300)
                236     STORE_FAST                      4: e
                238     LOAD_GLOBAL                     12: logging
                248     LOAD_ATTR                       14: exception
                268     PUSH_NULL
                270     LOAD_CONST                      7: 'Error retrieving buildid from %s'
                272     LOAD_FAST                       0: acf_path
                274     CALL                            2
                282     POP_TOP
                284     POP_EXCEPT
                286     LOAD_CONST                      0: None
                288     STORE_FAST                      4: e
                290     DELETE_FAST                     4: e
                292     RETURN_CONST                    6: 'Unknown'
                294     LOAD_CONST                      0: None
                296     STORE_FAST                      4: e
                298     DELETE_FAST                     4: e
                300     RERAISE                         1
                302     RERAISE                         0
                304     COPY                            3
                306     POP_EXCEPT
                308     RERAISE                         1
        [Code]
            File Name: LuaMaker_NahBro3.py
            Object Name: SteamAPI
            Qualified Name: SteamAPI
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 5
            Flags: 0x00000000
            [Names]
                '__name__'
                '__module__'
                '__qualname__'
                '__firstlineno__'
                'staticmethod'
                'str'
                'list'
                'list_dlcs'
                '__static_attributes__'
            [Locals+Names]
            [Constants]
                'SteamAPI'
                61
                'primary'
                'return'
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: list_dlcs
                    Qualified Name: SteamAPI.list_dlcs
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 6
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'requests'
                        'get'
                        'json'
                        'str'
                        'text'
                        'set'
                        're'
                        'findall'
                        'discard'
                        'list'
                        'Exception'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'primary'
                        'url'
                        'response'
                        'data'
                        'dlcs'
                        'url2'
                        'r2'
                        'html'
                        'found'
                        'e'
                    [Constants]
                        None
                        'https://store.steampowered.com/api/appdetails?appids='
                        '&cc=us&l=en'
                        'data'
                        'dlc'
                        'https://steamdb.info/app/'
                        '/'
                        '/app/(\\d+)/'
                        'SteamAPI.list_dlcs error'
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_CONST                      1: 'https://store.steampowered.com/api/appdetails?appids='
                        6       LOAD_FAST                       0: primary
                        8       FORMAT_SIMPLE
                        10      LOAD_CONST                      2: '&cc=us&l=en'
                        12      BUILD_STRING                    3
                        14      STORE_FAST                      1: url
                        16      LOAD_GLOBAL                     0: requests
                        26      LOAD_ATTR                       2: get
                        46      PUSH_NULL
                        48      LOAD_FAST                       1: url
                        50      CALL                            1
                        58      STORE_FAST                      2: response
                        60      LOAD_FAST                       2: response
                        62      LOAD_ATTR                       5: json
                        82      CALL                            0
                        90      STORE_FAST                      3: data
                        92      LOAD_FAST                       3: data
                        94      LOAD_ATTR                       3: get
                        114     LOAD_GLOBAL                     7: NULL + str
                        124     LOAD_FAST                       0: primary
                        126     CALL                            1
                        134     BUILD_MAP                       0
                        136     CALL                            2
                        144     LOAD_ATTR                       3: get
                        164     LOAD_CONST                      3: 'data'
                        166     BUILD_MAP                       0
                        168     CALL                            2
                        176     LOAD_ATTR                       3: get
                        196     LOAD_CONST                      4: 'dlc'
                        198     BUILD_LIST                      0
                        200     CALL                            2
                        208     STORE_FAST                      4: dlcs
                        210     LOAD_FAST                       4: dlcs
                        212     TO_BOOL
                        220     POP_JUMP_IF_TRUE                109 (to 440)
                        224     LOAD_CONST                      5: 'https://steamdb.info/app/'
                        226     LOAD_FAST                       0: primary
                        228     FORMAT_SIMPLE
                        230     LOAD_CONST                      6: '/'
                        232     BUILD_STRING                    3
                        234     STORE_FAST                      5: url2
                        236     LOAD_GLOBAL                     0: requests
                        246     LOAD_ATTR                       2: get
                        266     PUSH_NULL
                        268     LOAD_FAST                       5: url2
                        270     CALL                            1
                        278     STORE_FAST                      6: r2
                        280     LOAD_FAST                       6: r2
                        282     LOAD_ATTR                       8: text
                        302     STORE_FAST                      7: html
                        304     LOAD_GLOBAL                     11: NULL + set
                        314     LOAD_GLOBAL                     12: re
                        324     LOAD_ATTR                       14: findall
                        344     PUSH_NULL
                        346     LOAD_CONST                      7: '/app/(\\d+)/'
                        348     LOAD_FAST                       7: html
                        350     CALL                            2
                        358     CALL                            1
                        366     STORE_FAST                      8: found
                        368     LOAD_FAST                       8: found
                        370     LOAD_ATTR                       17: discard
                        390     LOAD_GLOBAL                     7: NULL + str
                        400     LOAD_FAST                       0: primary
                        402     CALL                            1
                        410     CALL                            1
                        418     POP_TOP
                        420     LOAD_GLOBAL                     19: NULL + list
                        430     LOAD_FAST                       8: found
                        432     CALL                            1
                        440     STORE_FAST                      4: dlcs
                        442     LOAD_FAST                       4: dlcs
                        444     RETURN_VALUE
                        446     PUSH_EXC_INFO
                        448     LOAD_GLOBAL                     20: Exception
                        458     CHECK_EXC_MATCH
                        460     POP_JUMP_IF_FALSE               34 (to 530)
                        464     STORE_FAST                      9: e
                        466     LOAD_GLOBAL                     22: logging
                        476     LOAD_ATTR                       24: exception
                        496     PUSH_NULL
                        498     LOAD_CONST                      8: 'SteamAPI.list_dlcs error'
                        500     CALL                            1
                        508     POP_TOP
                        510     BUILD_LIST                      0
                        512     SWAP                            2
                        514     POP_EXCEPT
                        516     LOAD_CONST                      0: None
                        518     STORE_FAST                      9: e
                        520     DELETE_FAST                     9: e
                        522     RETURN_VALUE
                        524     LOAD_CONST                      0: None
                        526     STORE_FAST                      9: e
                        528     DELETE_FAST                     9: e
                        530     RERAISE                         1
                        532     RERAISE                         0
                        534     COPY                            3
                        536     POP_EXCEPT
                        538     RERAISE                         1
                (
                )
                None
            [Disassembly]
                0       RESUME                          0
                2       LOAD_NAME                       0: __name__
                4       STORE_NAME                      1: __module__
                6       LOAD_CONST                      0: 'SteamAPI'
                8       STORE_NAME                      2: __qualname__
                10      LOAD_CONST                      1: 61
                12      STORE_NAME                      3: __firstlineno__
                14      LOAD_NAME                       4: staticmethod
                16      LOAD_CONST                      2: 'primary'
                18      LOAD_NAME                       5: str
                20      LOAD_CONST                      3: 'return'
                22      LOAD_NAME                       6: list
                24      BUILD_TUPLE                     4
                26      LOAD_CONST                      4: <CODE> list_dlcs
                28      MAKE_FUNCTION
                30      SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                32      CALL                            0
                40      STORE_NAME                      7: list_dlcs
                42      LOAD_CONST                      5: ()
                44      STORE_NAME                      8: __static_attributes__
                46      RETURN_CONST                    6: None
        'SteamAPI'
        [Code]
            File Name: LuaMaker_NahBro3.py
            Object Name: LuaScriptMaker
            Qualified Name: LuaScriptMaker
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 7
            Flags: 0x00000000
            [Names]
                '__name__'
                '__module__'
                '__qualname__'
                '__firstlineno__'
                'getattr'
                'sys'
                'Path'
                'executable'
                'parent'
                'BASE_PATH'
                '__file__'
                'resolve'
                'CONFIG_PATH'
                '__init__'
                'load_config'
                'save_config'
                'build_ui'
                'log_console'
                'log_removal'
                'clear_draft'
                'toggle_export_pause'
                'update_theme'
                'auto_detect_steam_dir'
                'change_steam_directory'
                'select_save_directory'
                'select_game_directory'
                'set'
                'get_library_folders'
                'auto_fill_fields'
                'update_preview'
                'str'
                'get_game_name_from_primary'
                'get_dkey'
                'get_manifest_for_appid'
                'get_manifest'
                'copy_manifest_files'
                'copy_fallback_manifest'
                'copy_bin_files'
                'copy_achievement_bin_files'
                'create_zip_archive'
                'process_dlc_ids'
                'fetch_dlc_ids'
                'list'
                'fetch_depot_ids_from_steamdb'
                'process_primary_appid'
                'export_game'
                'export_all_installed_games'
                'handle_preview'
                'handle_save'
                'save_lua_script'
                'remove_game_handler'
                'remove_game'
                'restart_steam'
                '__static_attributes__'
                '__classcell__'
            [Locals+Names]
                '__class__'
            [Constants]
                'LuaScriptMaker'
                84
                'frozen'
                False
                'config.json'
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: __init__
                    Qualified Name: LuaScriptMaker.__init__
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 3
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'super'
                        '__init__'
                        'steam_dir'
                        'game_dir'
                        'save_dir'
                        'script_lines'
                        'dlc_ids'
                        'set'
                        'added_ids'
                        'export_paused'
                        'load_config'
                        'build_ui'
                        'auto_detect_steam_dir'
                    [Locals+Names]
                        'self'
                        '__class__'
                    [Constants]
                        None
                        False
                    [Disassembly]
                        0       COPY_FREE_VARS                  1
                        2       RESUME                          0
                        4       LOAD_GLOBAL                     0: super
                        14      LOAD_DEREF                      1: __class__
                        16      LOAD_FAST                       0: self
                        18      LOAD_SUPER_ATTR                 5: __init__
                        22      CALL                            0
                        30      POP_TOP
                        32      LOAD_CONST                      0: None
                        34      LOAD_FAST                       0: self
                        36      STORE_ATTR                      2: steam_dir
                        46      LOAD_CONST                      0: None
                        48      LOAD_FAST                       0: self
                        50      STORE_ATTR                      3: game_dir
                        60      LOAD_CONST                      0: None
                        62      LOAD_FAST                       0: self
                        64      STORE_ATTR                      4: save_dir
                        74      BUILD_LIST                      0
                        76      LOAD_FAST                       0: self
                        78      STORE_ATTR                      5: script_lines
                        88      BUILD_LIST                      0
                        90      LOAD_FAST                       0: self
                        92      STORE_ATTR                      6: dlc_ids
                        102     LOAD_GLOBAL                     15: NULL + set
                        112     CALL                            0
                        120     LOAD_FAST                       0: self
                        122     STORE_ATTR                      8: added_ids
                        132     LOAD_CONST                      1: False
                        134     LOAD_FAST                       0: self
                        136     STORE_ATTR                      9: export_paused
                        146     LOAD_FAST                       0: self
                        148     LOAD_ATTR                       21: load_config
                        168     CALL                            0
                        176     POP_TOP
                        178     LOAD_FAST                       0: self
                        180     LOAD_ATTR                       23: build_ui
                        200     CALL                            0
                        208     POP_TOP
                        210     LOAD_FAST                       0: self
                        212     LOAD_ATTR                       25: auto_detect_steam_dir
                        232     CALL                            0
                        240     POP_TOP
                        242     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: load_config
                    Qualified Name: LuaScriptMaker.load_config
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'CONFIG_PATH'
                        'exists'
                        'open'
                        'json'
                        'load'
                        'get'
                        'steam_dir'
                        'game_dir'
                        'save_dir'
                        'dump'
                        'Exception'
                        'QMessageBox'
                        'warning'
                        'str'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'f'
                        'conf'
                        'default_conf'
                        'e'
                    [Constants]
                        None
                        'r'
                        'utf-8'
                        (
                            'encoding'
                        )
                        'steam_directory'
                        'game_directory'
                        'save_directory'
                        ''
                        (
                            'steam_directory'
                            'game_directory'
                            'save_directory'
                        )
                        'w'
                        4
                        (
                            'indent'
                        )
                        'Config Error'
                        'Failed to load configuration: '
                        'Configuration load error:'
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       0: CONFIG_PATH
                        26      LOAD_ATTR                       3: exists
                        46      CALL                            0
                        54      TO_BOOL
                        62      POP_JUMP_IF_FALSE               124 (to 312)
                        66      LOAD_FAST                       0: self
                        68      LOAD_ATTR                       0: CONFIG_PATH
                        88      LOAD_ATTR                       5: open
                        108     LOAD_CONST                      1: 'r'
                        110     LOAD_CONST                      2: 'utf-8'
                        112     LOAD_CONST                      3: ('encoding',)
                        114     CALL_KW                         2
                        116     BEFORE_WITH
                        118     STORE_FAST                      1: f
                        120     LOAD_GLOBAL                     6: json
                        130     LOAD_ATTR                       8: load
                        150     PUSH_NULL
                        152     LOAD_FAST                       1: f
                        154     CALL                            1
                        162     STORE_FAST                      2: conf
                        164     LOAD_FAST                       2: conf
                        166     LOAD_ATTR                       11: get
                        186     LOAD_CONST                      4: 'steam_directory'
                        188     CALL                            1
                        196     LOAD_FAST                       0: self
                        198     STORE_ATTR                      6: steam_dir
                        208     LOAD_FAST                       2: conf
                        210     LOAD_ATTR                       11: get
                        230     LOAD_CONST                      5: 'game_directory'
                        232     CALL                            1
                        240     LOAD_FAST                       0: self
                        242     STORE_ATTR                      7: game_dir
                        252     LOAD_FAST                       2: conf
                        254     LOAD_ATTR                       11: get
                        274     LOAD_CONST                      6: 'save_directory'
                        276     CALL                            1
                        284     LOAD_FAST                       0: self
                        286     STORE_ATTR                      8: save_dir
                        296     LOAD_CONST                      0: None
                        298     LOAD_CONST                      0: None
                        300     LOAD_CONST                      0: None
                        302     CALL                            2
                        310     POP_TOP
                        312     RETURN_CONST                    0: None
                        314     LOAD_CONST                      7: ''
                        316     LOAD_CONST                      7: ''
                        318     LOAD_CONST                      7: ''
                        320     LOAD_CONST                      8: ('steam_directory', 'game_directory', 'save_directory')
                        322     BUILD_CONST_KEY_MAP             3
                        324     STORE_FAST                      3: default_conf
                        326     LOAD_FAST                       0: self
                        328     LOAD_ATTR                       0: CONFIG_PATH
                        348     LOAD_ATTR                       5: open
                        368     LOAD_CONST                      9: 'w'
                        370     LOAD_CONST                      2: 'utf-8'
                        372     LOAD_CONST                      3: ('encoding',)
                        374     CALL_KW                         2
                        376     BEFORE_WITH
                        378     STORE_FAST                      1: f
                        380     LOAD_GLOBAL                     6: json
                        390     LOAD_ATTR                       18: dump
                        410     PUSH_NULL
                        412     LOAD_FAST_LOAD_FAST             49: default_conf, f
                        414     LOAD_CONST                      10: 4
                        416     LOAD_CONST                      11: ('indent',)
                        418     CALL_KW                         3
                        420     POP_TOP
                        422     LOAD_CONST                      0: None
                        424     LOAD_CONST                      0: None
                        426     LOAD_CONST                      0: None
                        428     CALL                            2
                        436     POP_TOP
                        438     LOAD_CONST                      7: ''
                        440     LOAD_FAST                       0: self
                        442     STORE_ATTR                      6: steam_dir
                        452     LOAD_CONST                      7: ''
                        454     LOAD_FAST                       0: self
                        456     STORE_ATTR                      7: game_dir
                        466     LOAD_CONST                      7: ''
                        468     LOAD_FAST                       0: self
                        470     STORE_ATTR                      8: save_dir
                        480     RETURN_CONST                    0: None
                        482     PUSH_EXC_INFO
                        484     WITH_EXCEPT_START
                        486     TO_BOOL
                        494     POP_JUMP_IF_TRUE                1 (to 498)
                        498     RERAISE                         2
                        500     POP_TOP
                        502     POP_EXCEPT
                        504     POP_TOP
                        506     POP_TOP
                        508     RETURN_CONST                    0: None
                        510     COPY                            3
                        512     POP_EXCEPT
                        514     RERAISE                         1
                        516     PUSH_EXC_INFO
                        518     WITH_EXCEPT_START
                        520     TO_BOOL
                        528     POP_JUMP_IF_TRUE                1 (to 532)
                        532     RERAISE                         2
                        534     POP_TOP
                        536     POP_EXCEPT
                        538     POP_TOP
                        540     POP_TOP
                        542     JUMP_BACKWARD_NO_INTERRUPT      53 (to 438)
                        544     COPY                            3
                        546     POP_EXCEPT
                        548     RERAISE                         1
                        550     PUSH_EXC_INFO
                        552     LOAD_GLOBAL                     20: Exception
                        562     CHECK_EXC_MATCH
                        564     POP_JUMP_IF_FALSE               68 (to 702)
                        568     STORE_FAST                      4: e
                        570     LOAD_GLOBAL                     22: QMessageBox
                        580     LOAD_ATTR                       24: warning
                        600     PUSH_NULL
                        602     LOAD_FAST                       0: self
                        604     LOAD_CONST                      12: 'Config Error'
                        606     LOAD_CONST                      13: 'Failed to load configuration: '
                        608     LOAD_GLOBAL                     27: NULL + str
                        618     LOAD_FAST                       4: e
                        620     CALL                            1
                        628     FORMAT_SIMPLE
                        630     BUILD_STRING                    2
                        632     CALL                            3
                        640     POP_TOP
                        642     LOAD_GLOBAL                     28: logging
                        652     LOAD_ATTR                       30: exception
                        672     PUSH_NULL
                        674     LOAD_CONST                      14: 'Configuration load error:'
                        676     CALL                            1
                        684     POP_TOP
                        686     POP_EXCEPT
                        688     LOAD_CONST                      0: None
                        690     STORE_FAST                      4: e
                        692     DELETE_FAST                     4: e
                        694     RETURN_CONST                    0: None
                        696     LOAD_CONST                      0: None
                        698     STORE_FAST                      4: e
                        700     DELETE_FAST                     4: e
                        702     RERAISE                         1
                        704     RERAISE                         0
                        706     COPY                            3
                        708     POP_EXCEPT
                        710     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: save_config
                    Qualified Name: LuaScriptMaker.save_config
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'CONFIG_PATH'
                        'parent'
                        'mkdir'
                        'steam_dir'
                        'game_dir'
                        'save_dir'
                        'open'
                        'json'
                        'dump'
                        'Exception'
                        'QMessageBox'
                        'warning'
                        'str'
                    [Locals+Names]
                        'self'
                        'conf'
                        'f'
                        'e'
                    [Constants]
                        None
                        True
                        (
                            'parents'
                            'exist_ok'
                        )
                        (
                            'steam_directory'
                            'game_directory'
                            'save_directory'
                        )
                        'w'
                        'utf-8'
                        (
                            'encoding'
                        )
                        4
                        (
                            'indent'
                        )
                        'Save Error'
                        'Failed to save configuration: '
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       0: CONFIG_PATH
                        26      LOAD_ATTR                       2: parent
                        46      LOAD_ATTR                       5: mkdir
                        66      LOAD_CONST                      1: True
                        68      LOAD_CONST                      1: True
                        70      LOAD_CONST                      2: ('parents', 'exist_ok')
                        72      CALL_KW                         2
                        74      POP_TOP
                        76      LOAD_FAST                       0: self
                        78      LOAD_ATTR                       6: steam_dir
                        98      LOAD_FAST                       0: self
                        100     LOAD_ATTR                       8: game_dir
                        120     LOAD_FAST                       0: self
                        122     LOAD_ATTR                       10: save_dir
                        142     LOAD_CONST                      3: ('steam_directory', 'game_directory', 'save_directory')
                        144     BUILD_CONST_KEY_MAP             3
                        146     STORE_FAST                      1: conf
                        148     LOAD_FAST                       0: self
                        150     LOAD_ATTR                       0: CONFIG_PATH
                        170     LOAD_ATTR                       13: open
                        190     LOAD_CONST                      4: 'w'
                        192     LOAD_CONST                      5: 'utf-8'
                        194     LOAD_CONST                      6: ('encoding',)
                        196     CALL_KW                         2
                        198     BEFORE_WITH
                        200     STORE_FAST                      2: f
                        202     LOAD_GLOBAL                     14: json
                        212     LOAD_ATTR                       16: dump
                        232     PUSH_NULL
                        234     LOAD_FAST_LOAD_FAST             18: conf, f
                        236     LOAD_CONST                      7: 4
                        238     LOAD_CONST                      8: ('indent',)
                        240     CALL_KW                         3
                        242     POP_TOP
                        244     LOAD_CONST                      0: None
                        246     LOAD_CONST                      0: None
                        248     LOAD_CONST                      0: None
                        250     CALL                            2
                        258     POP_TOP
                        260     RETURN_CONST                    0: None
                        262     PUSH_EXC_INFO
                        264     WITH_EXCEPT_START
                        266     TO_BOOL
                        274     POP_JUMP_IF_TRUE                1 (to 278)
                        278     RERAISE                         2
                        280     POP_TOP
                        282     POP_EXCEPT
                        284     POP_TOP
                        286     POP_TOP
                        288     RETURN_CONST                    0: None
                        290     COPY                            3
                        292     POP_EXCEPT
                        294     RERAISE                         1
                        296     PUSH_EXC_INFO
                        298     LOAD_GLOBAL                     18: Exception
                        308     CHECK_EXC_MATCH
                        310     POP_JUMP_IF_FALSE               46 (to 404)
                        314     STORE_FAST                      3: e
                        316     LOAD_GLOBAL                     20: QMessageBox
                        326     LOAD_ATTR                       22: warning
                        346     PUSH_NULL
                        348     LOAD_FAST                       0: self
                        350     LOAD_CONST                      9: 'Save Error'
                        352     LOAD_CONST                      10: 'Failed to save configuration: '
                        354     LOAD_GLOBAL                     25: NULL + str
                        364     LOAD_FAST                       3: e
                        366     CALL                            1
                        374     FORMAT_SIMPLE
                        376     BUILD_STRING                    2
                        378     CALL                            3
                        386     POP_TOP
                        388     POP_EXCEPT
                        390     LOAD_CONST                      0: None
                        392     STORE_FAST                      3: e
                        394     DELETE_FAST                     3: e
                        396     RETURN_CONST                    0: None
                        398     LOAD_CONST                      0: None
                        400     STORE_FAST                      3: e
                        402     DELETE_FAST                     3: e
                        404     RERAISE                         1
                        406     RERAISE                         0
                        408     COPY                            3
                        410     POP_EXCEPT
                        412     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: build_ui
                    Qualified Name: LuaScriptMaker.build_ui
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 7
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'setWindowTitle'
                        'setGeometry'
                        'QWidget'
                        'setCentralWidget'
                        'QVBoxLayout'
                        'setContentsMargins'
                        'setSpacing'
                        'QTabWidget'
                        'tabs'
                        'addWidget'
                        'exporter_tab'
                        'QGridLayout'
                        'QLabel'
                        'label_primary'
                        'setFont'
                        'QFont'
                        'Weight'
                        'Bold'
                        'QLineEdit'
                        'input_primary'
                        'setPlaceholderText'
                        'setValidator'
                        'QIntValidator'
                        'editingFinished'
                        'connect'
                        'process_primary_appid'
                        'label_secondary'
                        'input_secondary'
                        'label_dkey'
                        'input_dkey'
                        'label_manifest'
                        'input_manifest'
                        'label_dlc'
                        'input_dlc'
                        'addLayout'
                        'QHBoxLayout'
                        'QComboBox'
                        'combo_theme'
                        'addItems'
                        'currentTextChanged'
                        'update_theme'
                        'addStretch'
                        'QPushButton'
                        'btn_select_save'
                        'clicked'
                        'select_save_directory'
                        'label_save_dir'
                        'setWordWrap'
                        'btn_change_steam'
                        'change_steam_directory'
                        'label_steam'
                        'btn_set_game'
                        'select_game_directory'
                        'label_game'
                        'btn_preview'
                        'handle_preview'
                        'btn_save'
                        'handle_save'
                        'btn_clear'
                        'clear_draft'
                        'btn_export_all'
                        'export_all_installed_games'
                        'btn_pause'
                        'toggle_export_pause'
                        'label_preview'
                        'QTextEdit'
                        'text_preview'
                        'setReadOnly'
                        'label_console'
                        'text_console'
                        'setFixedHeight'
                        'addTab'
                        'remover_tab'
                        'label_remove'
                        'input_remove'
                        'btn_remove'
                        'remove_game_handler'
                        'btn_restart'
                        'restart_steam'
                        'text_remove_console'
                        'steam_dir'
                        'setText'
                        'save_dir'
                    [Locals+Names]
                        'self'
                        'central'
                        'main_layout'
                        'exporter_layout'
                        'form'
                        'theme_layout'
                        'dir_layout'
                        'action_layout'
                        'preview_layout'
                        'remover_layout'
                        'form_rem'
                        'btn_layout'
                    [Constants]
                        None
                        'LUA Script Maker'
                        100
                        900
                        700
                        10
                        'Primary AppID:'
                        'Arial'
                        'Enter first AppID (e.g., 678950)'
                        0
                        1
                        'Secondary AppID:'
                        'Autofilled Secondary AppID'
                        'DKey:'
                        'Autofilled DKey'
                        2
                        'Manifest ID:'
                        'Autofilled Manifest ID'
                        3
                        'DLC AppID:'
                        'Enter DLC AppID if any'
                        4
                        (
                            'Sapphire'
                            'Midnight'
                            'Obsidian'
                        )
                        'Select Theme:'
                        'Select Save Directory'
                        'Save Directory: None'
                        True
                        'Change Steam Directory'
                        'Steam Directory: None'
                        'Set Game Directory'
                        'Game Directory: None'
                        'Preview Script'
                        'Save LUA (Manual)'
                        'Clear Draft'
                        'Export Installed Games (Automatic)'
                        'Pause Export'
                        'Script Preview:'
                        'Console:'
                        'Courier'
                        9
                        150
                        'Exporter'
                        'Enter Game Name or AppID:'
                        'Game Name or AppID'
                        'Remove Game'
                        'Restart Steam'
                        'Removal Log:'
                        'Game Remover'
                        'Steam Directory: (set)'
                        'Save Directory: (set)'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       1: setWindowTitle
                        24      LOAD_CONST                      1: 'LUA Script Maker'
                        26      CALL                            1
                        34      POP_TOP
                        36      LOAD_FAST                       0: self
                        38      LOAD_ATTR                       3: setGeometry
                        58      LOAD_CONST                      2: 100
                        60      LOAD_CONST                      2: 100
                        62      LOAD_CONST                      3: 900
                        64      LOAD_CONST                      4: 700
                        66      CALL                            4
                        74      POP_TOP
                        76      LOAD_GLOBAL                     5: NULL + QWidget
                        86      LOAD_FAST                       0: self
                        88      CALL                            1
                        96      STORE_FAST                      1: central
                        98      LOAD_FAST                       0: self
                        100     LOAD_ATTR                       7: setCentralWidget
                        120     LOAD_FAST                       1: central
                        122     CALL                            1
                        130     POP_TOP
                        132     LOAD_GLOBAL                     9: NULL + QVBoxLayout
                        142     LOAD_FAST                       1: central
                        144     CALL                            1
                        152     STORE_FAST                      2: main_layout
                        154     LOAD_FAST                       2: main_layout
                        156     LOAD_ATTR                       11: setContentsMargins
                        176     LOAD_CONST                      5: 10
                        178     LOAD_CONST                      5: 10
                        180     LOAD_CONST                      5: 10
                        182     LOAD_CONST                      5: 10
                        184     CALL                            4
                        192     POP_TOP
                        194     LOAD_FAST                       2: main_layout
                        196     LOAD_ATTR                       13: setSpacing
                        216     LOAD_CONST                      5: 10
                        218     CALL                            1
                        226     POP_TOP
                        228     LOAD_GLOBAL                     15: NULL + QTabWidget
                        238     CALL                            0
                        246     LOAD_FAST                       0: self
                        248     STORE_ATTR                      8: tabs
                        258     LOAD_FAST                       2: main_layout
                        260     LOAD_ATTR                       19: addWidget
                        280     LOAD_FAST                       0: self
                        282     LOAD_ATTR                       16: tabs
                        302     CALL                            1
                        310     POP_TOP
                        312     LOAD_GLOBAL                     5: NULL + QWidget
                        322     CALL                            0
                        330     LOAD_FAST                       0: self
                        332     STORE_ATTR                      10: exporter_tab
                        342     LOAD_GLOBAL                     9: NULL + QVBoxLayout
                        352     LOAD_FAST                       0: self
                        354     LOAD_ATTR                       20: exporter_tab
                        374     CALL                            1
                        382     STORE_FAST                      3: exporter_layout
                        384     LOAD_FAST                       3: exporter_layout
                        386     LOAD_ATTR                       13: setSpacing
                        406     LOAD_CONST                      5: 10
                        408     CALL                            1
                        416     POP_TOP
                        418     LOAD_GLOBAL                     23: NULL + QGridLayout
                        428     CALL                            0
                        436     STORE_FAST                      4: form
                        438     LOAD_FAST                       4: form
                        440     LOAD_ATTR                       13: setSpacing
                        460     LOAD_CONST                      5: 10
                        462     CALL                            1
                        470     POP_TOP
                        472     LOAD_GLOBAL                     25: NULL + QLabel
                        482     LOAD_CONST                      6: 'Primary AppID:'
                        484     CALL                            1
                        492     LOAD_FAST                       0: self
                        494     STORE_ATTR                      13: label_primary
                        504     LOAD_FAST                       0: self
                        506     LOAD_ATTR                       26: label_primary
                        526     LOAD_ATTR                       29: setFont
                        546     LOAD_GLOBAL                     31: NULL + QFont
                        556     LOAD_CONST                      7: 'Arial'
                        558     LOAD_CONST                      5: 10
                        560     LOAD_GLOBAL                     30: QFont
                        570     LOAD_ATTR                       32: Weight
                        590     LOAD_ATTR                       34: Bold
                        610     CALL                            3
                        618     CALL                            1
                        626     POP_TOP
                        628     LOAD_GLOBAL                     37: NULL + QLineEdit
                        638     CALL                            0
                        646     LOAD_FAST                       0: self
                        648     STORE_ATTR                      19: input_primary
                        658     LOAD_FAST                       0: self
                        660     LOAD_ATTR                       38: input_primary
                        680     LOAD_ATTR                       41: setPlaceholderText
                        700     LOAD_CONST                      8: 'Enter first AppID (e.g., 678950)'
                        702     CALL                            1
                        710     POP_TOP
                        712     LOAD_FAST                       0: self
                        714     LOAD_ATTR                       38: input_primary
                        734     LOAD_ATTR                       43: setValidator
                        754     LOAD_GLOBAL                     45: NULL + QIntValidator
                        764     CALL                            0
                        772     CALL                            1
                        780     POP_TOP
                        782     LOAD_FAST                       4: form
                        784     LOAD_ATTR                       19: addWidget
                        804     LOAD_FAST                       0: self
                        806     LOAD_ATTR                       26: label_primary
                        826     LOAD_CONST                      9: 0
                        828     LOAD_CONST                      9: 0
                        830     CALL                            3
                        838     POP_TOP
                        840     LOAD_FAST                       4: form
                        842     LOAD_ATTR                       19: addWidget
                        862     LOAD_FAST                       0: self
                        864     LOAD_ATTR                       38: input_primary
                        884     LOAD_CONST                      9: 0
                        886     LOAD_CONST                      10: 1
                        888     CALL                            3
                        896     POP_TOP
                        898     LOAD_FAST                       0: self
                        900     LOAD_ATTR                       38: input_primary
                        920     LOAD_ATTR                       46: editingFinished
                        940     LOAD_ATTR                       49: connect
                        960     LOAD_FAST                       0: self
                        962     LOAD_ATTR                       50: process_primary_appid
                        982     CALL                            1
                        990     POP_TOP
                        992     LOAD_GLOBAL                     25: NULL + QLabel
                        1002    LOAD_CONST                      11: 'Secondary AppID:'
                        1004    CALL                            1
                        1012    LOAD_FAST                       0: self
                        1014    STORE_ATTR                      26: label_secondary
                        1024    LOAD_FAST                       0: self
                        1026    LOAD_ATTR                       52: label_secondary
                        1046    LOAD_ATTR                       29: setFont
                        1066    LOAD_GLOBAL                     31: NULL + QFont
                        1076    LOAD_CONST                      7: 'Arial'
                        1078    LOAD_CONST                      5: 10
                        1080    LOAD_GLOBAL                     30: QFont
                        1090    LOAD_ATTR                       32: Weight
                        1110    LOAD_ATTR                       34: Bold
                        1130    CALL                            3
                        1138    CALL                            1
                        1146    POP_TOP
                        1148    LOAD_GLOBAL                     37: NULL + QLineEdit
                        1158    CALL                            0
                        1166    LOAD_FAST                       0: self
                        1168    STORE_ATTR                      27: input_secondary
                        1178    LOAD_FAST                       0: self
                        1180    LOAD_ATTR                       54: input_secondary
                        1200    LOAD_ATTR                       41: setPlaceholderText
                        1220    LOAD_CONST                      12: 'Autofilled Secondary AppID'
                        1222    CALL                            1
                        1230    POP_TOP
                        1232    LOAD_FAST                       4: form
                        1234    LOAD_ATTR                       19: addWidget
                        1254    LOAD_FAST                       0: self
                        1256    LOAD_ATTR                       52: label_secondary
                        1276    LOAD_CONST                      10: 1
                        1278    LOAD_CONST                      9: 0
                        1280    CALL                            3
                        1288    POP_TOP
                        1290    LOAD_FAST                       4: form
                        1292    LOAD_ATTR                       19: addWidget
                        1312    LOAD_FAST                       0: self
                        1314    LOAD_ATTR                       54: input_secondary
                        1334    LOAD_CONST                      10: 1
                        1336    LOAD_CONST                      10: 1
                        1338    CALL                            3
                        1346    POP_TOP
                        1348    LOAD_GLOBAL                     25: NULL + QLabel
                        1358    LOAD_CONST                      13: 'DKey:'
                        1360    CALL                            1
                        1368    LOAD_FAST                       0: self
                        1370    STORE_ATTR                      28: label_dkey
                        1380    LOAD_FAST                       0: self
                        1382    LOAD_ATTR                       56: label_dkey
                        1402    LOAD_ATTR                       29: setFont
                        1422    LOAD_GLOBAL                     31: NULL + QFont
                        1432    LOAD_CONST                      7: 'Arial'
                        1434    LOAD_CONST                      5: 10
                        1436    LOAD_GLOBAL                     30: QFont
                        1446    LOAD_ATTR                       32: Weight
                        1466    LOAD_ATTR                       34: Bold
                        1486    CALL                            3
                        1494    CALL                            1
                        1502    POP_TOP
                        1504    LOAD_GLOBAL                     37: NULL + QLineEdit
                        1514    CALL                            0
                        1522    LOAD_FAST                       0: self
                        1524    STORE_ATTR                      29: input_dkey
                        1534    LOAD_FAST                       0: self
                        1536    LOAD_ATTR                       58: input_dkey
                        1556    LOAD_ATTR                       41: setPlaceholderText
                        1576    LOAD_CONST                      14: 'Autofilled DKey'
                        1578    CALL                            1
                        1586    POP_TOP
                        1588    LOAD_FAST                       4: form
                        1590    LOAD_ATTR                       19: addWidget
                        1610    LOAD_FAST                       0: self
                        1612    LOAD_ATTR                       56: label_dkey
                        1632    LOAD_CONST                      15: 2
                        1634    LOAD_CONST                      9: 0
                        1636    CALL                            3
                        1644    POP_TOP
                        1646    LOAD_FAST                       4: form
                        1648    LOAD_ATTR                       19: addWidget
                        1668    LOAD_FAST                       0: self
                        1670    LOAD_ATTR                       58: input_dkey
                        1690    LOAD_CONST                      15: 2
                        1692    LOAD_CONST                      10: 1
                        1694    CALL                            3
                        1702    POP_TOP
                        1704    LOAD_GLOBAL                     25: NULL + QLabel
                        1714    LOAD_CONST                      16: 'Manifest ID:'
                        1716    CALL                            1
                        1724    LOAD_FAST                       0: self
                        1726    STORE_ATTR                      30: label_manifest
                        1736    LOAD_FAST                       0: self
                        1738    LOAD_ATTR                       60: label_manifest
                        1758    LOAD_ATTR                       29: setFont
                        1778    LOAD_GLOBAL                     31: NULL + QFont
                        1788    LOAD_CONST                      7: 'Arial'
                        1790    LOAD_CONST                      5: 10
                        1792    LOAD_GLOBAL                     30: QFont
                        1802    LOAD_ATTR                       32: Weight
                        1822    LOAD_ATTR                       34: Bold
                        1842    CALL                            3
                        1850    CALL                            1
                        1858    POP_TOP
                        1860    LOAD_GLOBAL                     37: NULL + QLineEdit
                        1870    CALL                            0
                        1878    LOAD_FAST                       0: self
                        1880    STORE_ATTR                      31: input_manifest
                        1890    LOAD_FAST                       0: self
                        1892    LOAD_ATTR                       62: input_manifest
                        1912    LOAD_ATTR                       41: setPlaceholderText
                        1932    LOAD_CONST                      17: 'Autofilled Manifest ID'
                        1934    CALL                            1
                        1942    POP_TOP
                        1944    LOAD_FAST                       4: form
                        1946    LOAD_ATTR                       19: addWidget
                        1966    LOAD_FAST                       0: self
                        1968    LOAD_ATTR                       60: label_manifest
                        1988    LOAD_CONST                      18: 3
                        1990    LOAD_CONST                      9: 0
                        1992    CALL                            3
                        2000    POP_TOP
                        2002    LOAD_FAST                       4: form
                        2004    LOAD_ATTR                       19: addWidget
                        2024    LOAD_FAST                       0: self
                        2026    LOAD_ATTR                       62: input_manifest
                        2046    LOAD_CONST                      18: 3
                        2048    LOAD_CONST                      10: 1
                        2050    CALL                            3
                        2058    POP_TOP
                        2060    LOAD_GLOBAL                     25: NULL + QLabel
                        2070    LOAD_CONST                      19: 'DLC AppID:'
                        2072    CALL                            1
                        2080    LOAD_FAST                       0: self
                        2082    STORE_ATTR                      32: label_dlc
                        2092    LOAD_FAST                       0: self
                        2094    LOAD_ATTR                       64: label_dlc
                        2114    LOAD_ATTR                       29: setFont
                        2134    LOAD_GLOBAL                     31: NULL + QFont
                        2144    LOAD_CONST                      7: 'Arial'
                        2146    LOAD_CONST                      5: 10
                        2148    LOAD_GLOBAL                     30: QFont
                        2158    LOAD_ATTR                       32: Weight
                        2178    LOAD_ATTR                       34: Bold
                        2198    CALL                            3
                        2206    CALL                            1
                        2214    POP_TOP
                        2216    LOAD_GLOBAL                     37: NULL + QLineEdit
                        2226    CALL                            0
                        2234    LOAD_FAST                       0: self
                        2236    STORE_ATTR                      33: input_dlc
                        2246    LOAD_FAST                       0: self
                        2248    LOAD_ATTR                       66: input_dlc
                        2268    LOAD_ATTR                       41: setPlaceholderText
                        2288    LOAD_CONST                      20: 'Enter DLC AppID if any'
                        2290    CALL                            1
                        2298    POP_TOP
                        2300    LOAD_FAST                       4: form
                        2302    LOAD_ATTR                       19: addWidget
                        2322    LOAD_FAST                       0: self
                        2324    LOAD_ATTR                       64: label_dlc
                        2344    LOAD_CONST                      21: 4
                        2346    LOAD_CONST                      9: 0
                        2348    CALL                            3
                        2356    POP_TOP
                        2358    LOAD_FAST                       4: form
                        2360    LOAD_ATTR                       19: addWidget
                        2380    LOAD_FAST                       0: self
                        2382    LOAD_ATTR                       66: input_dlc
                        2402    LOAD_CONST                      21: 4
                        2404    LOAD_CONST                      10: 1
                        2406    CALL                            3
                        2414    POP_TOP
                        2416    LOAD_FAST                       3: exporter_layout
                        2418    LOAD_ATTR                       69: addLayout
                        2438    LOAD_FAST                       4: form
                        2440    CALL                            1
                        2448    POP_TOP
                        2450    LOAD_GLOBAL                     71: NULL + QHBoxLayout
                        2460    CALL                            0
                        2468    STORE_FAST                      5: theme_layout
                        2470    LOAD_GLOBAL                     73: NULL + QComboBox
                        2480    CALL                            0
                        2488    LOAD_FAST                       0: self
                        2490    STORE_ATTR                      37: combo_theme
                        2500    LOAD_FAST                       0: self
                        2502    LOAD_ATTR                       74: combo_theme
                        2522    LOAD_ATTR                       77: addItems
                        2542    BUILD_LIST                      0
                        2544    LOAD_CONST                      22: ('Sapphire', 'Midnight', 'Obsidian')
                        2546    LIST_EXTEND                     1
                        2548    CALL                            1
                        2556    POP_TOP
                        2558    LOAD_FAST                       0: self
                        2560    LOAD_ATTR                       74: combo_theme
                        2580    LOAD_ATTR                       78: currentTextChanged
                        2600    LOAD_ATTR                       49: connect
                        2620    LOAD_FAST                       0: self
                        2622    LOAD_ATTR                       80: update_theme
                        2642    CALL                            1
                        2650    POP_TOP
                        2652    LOAD_FAST                       5: theme_layout
                        2654    LOAD_ATTR                       19: addWidget
                        2674    LOAD_GLOBAL                     25: NULL + QLabel
                        2684    LOAD_CONST                      23: 'Select Theme:'
                        2686    CALL                            1
                        2694    CALL                            1
                        2702    POP_TOP
                        2704    LOAD_FAST                       5: theme_layout
                        2706    LOAD_ATTR                       19: addWidget
                        2726    LOAD_FAST                       0: self
                        2728    LOAD_ATTR                       74: combo_theme
                        2748    CALL                            1
                        2756    POP_TOP
                        2758    LOAD_FAST                       5: theme_layout
                        2760    LOAD_ATTR                       83: addStretch
                        2780    CALL                            0
                        2788    POP_TOP
                        2790    LOAD_FAST                       3: exporter_layout
                        2792    LOAD_ATTR                       69: addLayout
                        2812    LOAD_FAST                       5: theme_layout
                        2814    CALL                            1
                        2822    POP_TOP
                        2824    LOAD_GLOBAL                     71: NULL + QHBoxLayout
                        2834    CALL                            0
                        2842    STORE_FAST                      6: dir_layout
                        2844    LOAD_GLOBAL                     85: NULL + QPushButton
                        2854    LOAD_CONST                      24: 'Select Save Directory'
                        2856    CALL                            1
                        2864    LOAD_FAST                       0: self
                        2866    STORE_ATTR                      43: btn_select_save
                        2876    LOAD_FAST                       0: self
                        2878    LOAD_ATTR                       86: btn_select_save
                        2898    LOAD_ATTR                       88: clicked
                        2918    LOAD_ATTR                       49: connect
                        2938    LOAD_FAST                       0: self
                        2940    LOAD_ATTR                       90: select_save_directory
                        2960    CALL                            1
                        2968    POP_TOP
                        2970    LOAD_FAST                       6: dir_layout
                        2972    LOAD_ATTR                       19: addWidget
                        2992    LOAD_FAST                       0: self
                        2994    LOAD_ATTR                       86: btn_select_save
                        3014    CALL                            1
                        3022    POP_TOP
                        3024    LOAD_GLOBAL                     25: NULL + QLabel
                        3034    LOAD_CONST                      25: 'Save Directory: None'
                        3036    CALL                            1
                        3044    LOAD_FAST                       0: self
                        3046    STORE_ATTR                      46: label_save_dir
                        3056    LOAD_FAST                       0: self
                        3058    LOAD_ATTR                       92: label_save_dir
                        3078    LOAD_ATTR                       95: setWordWrap
                        3098    LOAD_CONST                      26: True
                        3100    CALL                            1
                        3108    POP_TOP
                        3110    LOAD_FAST                       6: dir_layout
                        3112    LOAD_ATTR                       19: addWidget
                        3132    LOAD_FAST                       0: self
                        3134    LOAD_ATTR                       92: label_save_dir
                        3154    CALL                            1
                        3162    POP_TOP
                        3164    LOAD_GLOBAL                     85: NULL + QPushButton
                        3174    LOAD_CONST                      27: 'Change Steam Directory'
                        3176    CALL                            1
                        3184    LOAD_FAST                       0: self
                        3186    STORE_ATTR                      48: btn_change_steam
                        3196    LOAD_FAST                       0: self
                        3198    LOAD_ATTR                       96: btn_change_steam
                        3218    LOAD_ATTR                       88: clicked
                        3238    LOAD_ATTR                       49: connect
                        3258    LOAD_FAST                       0: self
                        3260    LOAD_ATTR                       98: change_steam_directory
                        3280    CALL                            1
                        3288    POP_TOP
                        3290    LOAD_FAST                       6: dir_layout
                        3292    LOAD_ATTR                       19: addWidget
                        3312    LOAD_FAST                       0: self
                        3314    LOAD_ATTR                       96: btn_change_steam
                        3334    CALL                            1
                        3342    POP_TOP
                        3344    LOAD_GLOBAL                     25: NULL + QLabel
                        3354    LOAD_CONST                      28: 'Steam Directory: None'
                        3356    CALL                            1
                        3364    LOAD_FAST                       0: self
                        3366    STORE_ATTR                      50: label_steam
                        3376    LOAD_FAST                       0: self
                        3378    LOAD_ATTR                       100: label_steam
                        3398    LOAD_ATTR                       95: setWordWrap
                        3418    LOAD_CONST                      26: True
                        3420    CALL                            1
                        3428    POP_TOP
                        3430    LOAD_FAST                       6: dir_layout
                        3432    LOAD_ATTR                       19: addWidget
                        3452    LOAD_FAST                       0: self
                        3454    LOAD_ATTR                       100: label_steam
                        3474    CALL                            1
                        3482    POP_TOP
                        3484    LOAD_GLOBAL                     85: NULL + QPushButton
                        3494    LOAD_CONST                      29: 'Set Game Directory'
                        3496    CALL                            1
                        3504    LOAD_FAST                       0: self
                        3506    STORE_ATTR                      51: btn_set_game
                        3516    LOAD_FAST                       0: self
                        3518    LOAD_ATTR                       102: btn_set_game
                        3538    LOAD_ATTR                       88: clicked
                        3558    LOAD_ATTR                       49: connect
                        3578    LOAD_FAST                       0: self
                        3580    LOAD_ATTR                       104: select_game_directory
                        3600    CALL                            1
                        3608    POP_TOP
                        3610    LOAD_FAST                       6: dir_layout
                        3612    LOAD_ATTR                       19: addWidget
                        3632    LOAD_FAST                       0: self
                        3634    LOAD_ATTR                       102: btn_set_game
                        3654    CALL                            1
                        3662    POP_TOP
                        3664    LOAD_GLOBAL                     25: NULL + QLabel
                        3674    LOAD_CONST                      30: 'Game Directory: None'
                        3676    CALL                            1
                        3684    LOAD_FAST                       0: self
                        3686    STORE_ATTR                      53: label_game
                        3696    LOAD_FAST                       0: self
                        3698    LOAD_ATTR                       106: label_game
                        3718    LOAD_ATTR                       95: setWordWrap
                        3738    LOAD_CONST                      26: True
                        3740    CALL                            1
                        3748    POP_TOP
                        3750    LOAD_FAST                       6: dir_layout
                        3752    LOAD_ATTR                       19: addWidget
                        3772    LOAD_FAST                       0: self
                        3774    LOAD_ATTR                       106: label_game
                        3794    CALL                            1
                        3802    POP_TOP
                        3804    LOAD_FAST                       3: exporter_layout
                        3806    LOAD_ATTR                       69: addLayout
                        3826    LOAD_FAST                       6: dir_layout
                        3828    CALL                            1
                        3836    POP_TOP
                        3838    LOAD_GLOBAL                     71: NULL + QHBoxLayout
                        3848    CALL                            0
                        3856    STORE_FAST                      7: action_layout
                        3858    LOAD_GLOBAL                     85: NULL + QPushButton
                        3868    LOAD_CONST                      31: 'Preview Script'
                        3870    CALL                            1
                        3878    LOAD_FAST                       0: self
                        3880    STORE_ATTR                      54: btn_preview
                        3890    LOAD_FAST                       0: self
                        3892    LOAD_ATTR                       108: btn_preview
                        3912    LOAD_ATTR                       88: clicked
                        3932    LOAD_ATTR                       49: connect
                        3952    LOAD_FAST                       0: self
                        3954    LOAD_ATTR                       110: handle_preview
                        3974    CALL                            1
                        3982    POP_TOP
                        3984    LOAD_FAST                       7: action_layout
                        3986    LOAD_ATTR                       19: addWidget
                        4006    LOAD_FAST                       0: self
                        4008    LOAD_ATTR                       108: btn_preview
                        4028    CALL                            1
                        4036    POP_TOP
                        4038    LOAD_GLOBAL                     85: NULL + QPushButton
                        4048    LOAD_CONST                      32: 'Save LUA (Manual)'
                        4050    CALL                            1
                        4058    LOAD_FAST                       0: self
                        4060    STORE_ATTR                      56: btn_save
                        4070    LOAD_FAST                       0: self
                        4072    LOAD_ATTR                       112: btn_save
                        4092    LOAD_ATTR                       88: clicked
                        4112    LOAD_ATTR                       49: connect
                        4132    LOAD_FAST                       0: self
                        4134    LOAD_ATTR                       114: handle_save
                        4154    CALL                            1
                        4162    POP_TOP
                        4164    LOAD_FAST                       7: action_layout
                        4166    LOAD_ATTR                       19: addWidget
                        4186    LOAD_FAST                       0: self
                        4188    LOAD_ATTR                       112: btn_save
                        4208    CALL                            1
                        4216    POP_TOP
                        4218    LOAD_GLOBAL                     85: NULL + QPushButton
                        4228    LOAD_CONST                      33: 'Clear Draft'
                        4230    CALL                            1
                        4238    LOAD_FAST                       0: self
                        4240    STORE_ATTR                      58: btn_clear
                        4250    LOAD_FAST                       0: self
                        4252    LOAD_ATTR                       116: btn_clear
                        4272    LOAD_ATTR                       88: clicked
                        4292    LOAD_ATTR                       49: connect
                        4312    LOAD_FAST                       0: self
                        4314    LOAD_ATTR                       118: clear_draft
                        4334    CALL                            1
                        4342    POP_TOP
                        4344    LOAD_FAST                       7: action_layout
                        4346    LOAD_ATTR                       19: addWidget
                        4366    LOAD_FAST                       0: self
                        4368    LOAD_ATTR                       116: btn_clear
                        4388    CALL                            1
                        4396    POP_TOP
                        4398    LOAD_GLOBAL                     85: NULL + QPushButton
                        4408    LOAD_CONST                      34: 'Export Installed Games (Automatic)'
                        4410    CALL                            1
                        4418    LOAD_FAST                       0: self
                        4420    STORE_ATTR                      60: btn_export_all
                        4430    LOAD_FAST                       0: self
                        4432    LOAD_ATTR                       120: btn_export_all
                        4452    LOAD_ATTR                       88: clicked
                        4472    LOAD_ATTR                       49: connect
                        4492    LOAD_FAST                       0: self
                        4494    LOAD_ATTR                       122: export_all_installed_games
                        4514    CALL                            1
                        4522    POP_TOP
                        4524    LOAD_FAST                       7: action_layout
                        4526    LOAD_ATTR                       19: addWidget
                        4546    LOAD_FAST                       0: self
                        4548    LOAD_ATTR                       120: btn_export_all
                        4568    CALL                            1
                        4576    POP_TOP
                        4578    LOAD_GLOBAL                     85: NULL + QPushButton
                        4588    LOAD_CONST                      35: 'Pause Export'
                        4590    CALL                            1
                        4598    LOAD_FAST                       0: self
                        4600    STORE_ATTR                      62: btn_pause
                        4610    LOAD_FAST                       0: self
                        4612    LOAD_ATTR                       124: btn_pause
                        4632    LOAD_ATTR                       88: clicked
                        4652    LOAD_ATTR                       49: connect
                        4672    LOAD_FAST                       0: self
                        4674    LOAD_ATTR                       126: toggle_export_pause
                        4694    CALL                            1
                        4702    POP_TOP
                        4704    LOAD_FAST                       7: action_layout
                        4706    LOAD_ATTR                       19: addWidget
                        4726    LOAD_FAST                       0: self
                        4728    LOAD_ATTR                       124: btn_pause
                        4748    CALL                            1
                        4756    POP_TOP
                        4758    LOAD_FAST                       7: action_layout
                        4760    LOAD_ATTR                       83: addStretch
                        4780    CALL                            0
                        4788    POP_TOP
                        4790    LOAD_FAST                       3: exporter_layout
                        4792    LOAD_ATTR                       69: addLayout
                        4812    LOAD_FAST                       7: action_layout
                        4814    CALL                            1
                        4822    POP_TOP
                        4824    LOAD_GLOBAL                     9: NULL + QVBoxLayout
                        4834    CALL                            0
                        4842    STORE_FAST                      8: preview_layout
                        4844    LOAD_GLOBAL                     25: NULL + QLabel
                        4854    LOAD_CONST                      36: 'Script Preview:'
                        4856    CALL                            1
                        4864    LOAD_FAST                       0: self
                        4866    STORE_ATTR                      64: label_preview
                        4876    LOAD_FAST                       0: self
                        4878    LOAD_ATTR                       128: label_preview
                        4898    LOAD_ATTR                       29: setFont
                        4918    LOAD_GLOBAL                     31: NULL + QFont
                        4928    LOAD_CONST                      7: 'Arial'
                        4930    LOAD_CONST                      5: 10
                        4932    LOAD_GLOBAL                     30: QFont
                        4942    LOAD_ATTR                       32: Weight
                        4962    LOAD_ATTR                       34: Bold
                        4982    CALL                            3
                        4990    CALL                            1
                        4998    POP_TOP
                        5000    LOAD_FAST                       8: preview_layout
                        5002    LOAD_ATTR                       19: addWidget
                        5022    LOAD_FAST                       0: self
                        5024    LOAD_ATTR                       128: label_preview
                        5044    CALL                            1
                        5052    POP_TOP
                        5054    LOAD_GLOBAL                     131: NULL + QTextEdit
                        5064    CALL                            0
                        5072    LOAD_FAST                       0: self
                        5074    STORE_ATTR                      66: text_preview
                        5084    LOAD_FAST                       0: self
                        5086    LOAD_ATTR                       132: text_preview
                        5106    LOAD_ATTR                       135: setReadOnly
                        5126    LOAD_CONST                      26: True
                        5128    CALL                            1
                        5136    POP_TOP
                        5138    LOAD_FAST                       8: preview_layout
                        5140    LOAD_ATTR                       19: addWidget
                        5160    LOAD_FAST                       0: self
                        5162    LOAD_ATTR                       132: text_preview
                        5182    CALL                            1
                        5190    POP_TOP
                        5192    LOAD_GLOBAL                     25: NULL + QLabel
                        5202    LOAD_CONST                      37: 'Console:'
                        5204    CALL                            1
                        5212    LOAD_FAST                       0: self
                        5214    STORE_ATTR                      68: label_console
                        5224    LOAD_FAST                       0: self
                        5226    LOAD_ATTR                       136: label_console
                        5246    LOAD_ATTR                       29: setFont
                        5266    LOAD_GLOBAL                     31: NULL + QFont
                        5276    LOAD_CONST                      7: 'Arial'
                        5278    LOAD_CONST                      5: 10
                        5280    LOAD_GLOBAL                     30: QFont
                        5290    LOAD_ATTR                       32: Weight
                        5310    LOAD_ATTR                       34: Bold
                        5330    CALL                            3
                        5338    CALL                            1
                        5346    POP_TOP
                        5348    LOAD_FAST                       8: preview_layout
                        5350    LOAD_ATTR                       19: addWidget
                        5370    LOAD_FAST                       0: self
                        5372    LOAD_ATTR                       136: label_console
                        5392    CALL                            1
                        5400    POP_TOP
                        5402    LOAD_GLOBAL                     131: NULL + QTextEdit
                        5412    CALL                            0
                        5420    LOAD_FAST                       0: self
                        5422    STORE_ATTR                      69: text_console
                        5432    LOAD_FAST                       0: self
                        5434    LOAD_ATTR                       138: text_console
                        5454    LOAD_ATTR                       135: setReadOnly
                        5474    LOAD_CONST                      26: True
                        5476    CALL                            1
                        5484    POP_TOP
                        5486    LOAD_FAST                       0: self
                        5488    LOAD_ATTR                       138: text_console
                        5508    LOAD_ATTR                       29: setFont
                        5528    LOAD_GLOBAL                     31: NULL + QFont
                        5538    LOAD_CONST                      38: 'Courier'
                        5540    LOAD_CONST                      39: 9
                        5542    CALL                            2
                        5550    CALL                            1
                        5558    POP_TOP
                        5560    LOAD_FAST                       0: self
                        5562    LOAD_ATTR                       138: text_console
                        5582    LOAD_ATTR                       141: setFixedHeight
                        5602    LOAD_CONST                      40: 150
                        5604    CALL                            1
                        5612    POP_TOP
                        5614    LOAD_FAST                       8: preview_layout
                        5616    LOAD_ATTR                       19: addWidget
                        5636    LOAD_FAST                       0: self
                        5638    LOAD_ATTR                       138: text_console
                        5658    CALL                            1
                        5666    POP_TOP
                        5668    LOAD_FAST                       3: exporter_layout
                        5670    LOAD_ATTR                       69: addLayout
                        5690    LOAD_FAST                       8: preview_layout
                        5692    CALL                            1
                        5700    POP_TOP
                        5702    LOAD_FAST                       0: self
                        5704    LOAD_ATTR                       16: tabs
                        5724    LOAD_ATTR                       143: addTab
                        5744    LOAD_FAST                       0: self
                        5746    LOAD_ATTR                       20: exporter_tab
                        5766    LOAD_CONST                      41: 'Exporter'
                        5768    CALL                            2
                        5776    POP_TOP
                        5778    LOAD_GLOBAL                     5: NULL + QWidget
                        5788    CALL                            0
                        5796    LOAD_FAST                       0: self
                        5798    STORE_ATTR                      72: remover_tab
                        5808    LOAD_GLOBAL                     9: NULL + QVBoxLayout
                        5818    LOAD_FAST                       0: self
                        5820    LOAD_ATTR                       144: remover_tab
                        5840    CALL                            1
                        5848    STORE_FAST                      9: remover_layout
                        5850    LOAD_FAST                       9: remover_layout
                        5852    LOAD_ATTR                       13: setSpacing
                        5872    LOAD_CONST                      5: 10
                        5874    CALL                            1
                        5882    POP_TOP
                        5884    LOAD_GLOBAL                     23: NULL + QGridLayout
                        5894    CALL                            0
                        5902    STORE_FAST                      10: form_rem
                        5904    LOAD_GLOBAL                     25: NULL + QLabel
                        5914    LOAD_CONST                      42: 'Enter Game Name or AppID:'
                        5916    CALL                            1
                        5924    LOAD_FAST                       0: self
                        5926    STORE_ATTR                      73: label_remove
                        5936    LOAD_FAST                       0: self
                        5938    LOAD_ATTR                       146: label_remove
                        5958    LOAD_ATTR                       29: setFont
                        5978    LOAD_GLOBAL                     31: NULL + QFont
                        5988    LOAD_CONST                      7: 'Arial'
                        5990    LOAD_CONST                      5: 10
                        5992    LOAD_GLOBAL                     30: QFont
                        6002    LOAD_ATTR                       32: Weight
                        6022    LOAD_ATTR                       34: Bold
                        6042    CALL                            3
                        6050    CALL                            1
                        6058    POP_TOP
                        6060    LOAD_GLOBAL                     37: NULL + QLineEdit
                        6070    CALL                            0
                        6078    LOAD_FAST                       0: self
                        6080    STORE_ATTR                      74: input_remove
                        6090    LOAD_FAST                       0: self
                        6092    LOAD_ATTR                       148: input_remove
                        6112    LOAD_ATTR                       41: setPlaceholderText
                        6132    LOAD_CONST                      43: 'Game Name or AppID'
                        6134    CALL                            1
                        6142    POP_TOP
                        6144    LOAD_FAST                       10: form_rem
                        6146    LOAD_ATTR                       19: addWidget
                        6166    LOAD_FAST                       0: self
                        6168    LOAD_ATTR                       146: label_remove
                        6188    LOAD_CONST                      9: 0
                        6190    LOAD_CONST                      9: 0
                        6192    CALL                            3
                        6200    POP_TOP
                        6202    LOAD_FAST                       10: form_rem
                        6204    LOAD_ATTR                       19: addWidget
                        6224    LOAD_FAST                       0: self
                        6226    LOAD_ATTR                       148: input_remove
                        6246    LOAD_CONST                      9: 0
                        6248    LOAD_CONST                      10: 1
                        6250    CALL                            3
                        6258    POP_TOP
                        6260    LOAD_FAST                       9: remover_layout
                        6262    LOAD_ATTR                       69: addLayout
                        6282    LOAD_FAST                       10: form_rem
                        6284    CALL                            1
                        6292    POP_TOP
                        6294    LOAD_GLOBAL                     71: NULL + QHBoxLayout
                        6304    CALL                            0
                        6312    STORE_FAST                      11: btn_layout
                        6314    LOAD_GLOBAL                     85: NULL + QPushButton
                        6324    LOAD_CONST                      44: 'Remove Game'
                        6326    CALL                            1
                        6334    LOAD_FAST                       0: self
                        6336    STORE_ATTR                      75: btn_remove
                        6346    LOAD_FAST                       0: self
                        6348    LOAD_ATTR                       150: btn_remove
                        6368    LOAD_ATTR                       88: clicked
                        6388    LOAD_ATTR                       49: connect
                        6408    LOAD_FAST                       0: self
                        6410    LOAD_ATTR                       152: remove_game_handler
                        6430    CALL                            1
                        6438    POP_TOP
                        6440    LOAD_FAST                       11: btn_layout
                        6442    LOAD_ATTR                       19: addWidget
                        6462    LOAD_FAST                       0: self
                        6464    LOAD_ATTR                       150: btn_remove
                        6484    CALL                            1
                        6492    POP_TOP
                        6494    LOAD_GLOBAL                     85: NULL + QPushButton
                        6504    LOAD_CONST                      45: 'Restart Steam'
                        6506    CALL                            1
                        6514    LOAD_FAST                       0: self
                        6516    STORE_ATTR                      77: btn_restart
                        6526    LOAD_FAST                       0: self
                        6528    LOAD_ATTR                       154: btn_restart
                        6548    LOAD_ATTR                       88: clicked
                        6568    LOAD_ATTR                       49: connect
                        6588    LOAD_FAST                       0: self
                        6590    LOAD_ATTR                       156: restart_steam
                        6610    CALL                            1
                        6618    POP_TOP
                        6620    LOAD_FAST                       11: btn_layout
                        6622    LOAD_ATTR                       19: addWidget
                        6642    LOAD_FAST                       0: self
                        6644    LOAD_ATTR                       154: btn_restart
                        6664    CALL                            1
                        6672    POP_TOP
                        6674    LOAD_FAST                       11: btn_layout
                        6676    LOAD_ATTR                       83: addStretch
                        6696    CALL                            0
                        6704    POP_TOP
                        6706    LOAD_FAST                       9: remover_layout
                        6708    LOAD_ATTR                       69: addLayout
                        6728    LOAD_FAST                       11: btn_layout
                        6730    CALL                            1
                        6738    POP_TOP
                        6740    LOAD_GLOBAL                     131: NULL + QTextEdit
                        6750    CALL                            0
                        6758    LOAD_FAST                       0: self
                        6760    STORE_ATTR                      79: text_remove_console
                        6770    LOAD_FAST                       0: self
                        6772    LOAD_ATTR                       158: text_remove_console
                        6792    LOAD_ATTR                       135: setReadOnly
                        6812    LOAD_CONST                      26: True
                        6814    CALL                            1
                        6822    POP_TOP
                        6824    LOAD_FAST                       0: self
                        6826    LOAD_ATTR                       158: text_remove_console
                        6846    LOAD_ATTR                       29: setFont
                        6866    LOAD_GLOBAL                     31: NULL + QFont
                        6876    LOAD_CONST                      38: 'Courier'
                        6878    LOAD_CONST                      39: 9
                        6880    CALL                            2
                        6888    CALL                            1
                        6896    POP_TOP
                        6898    LOAD_FAST                       9: remover_layout
                        6900    LOAD_ATTR                       19: addWidget
                        6920    LOAD_GLOBAL                     25: NULL + QLabel
                        6930    LOAD_CONST                      46: 'Removal Log:'
                        6932    CALL                            1
                        6940    CALL                            1
                        6948    POP_TOP
                        6950    LOAD_FAST                       9: remover_layout
                        6952    LOAD_ATTR                       19: addWidget
                        6972    LOAD_FAST                       0: self
                        6974    LOAD_ATTR                       158: text_remove_console
                        6994    CALL                            1
                        7002    POP_TOP
                        7004    LOAD_FAST                       0: self
                        7006    LOAD_ATTR                       16: tabs
                        7026    LOAD_ATTR                       143: addTab
                        7046    LOAD_FAST                       0: self
                        7048    LOAD_ATTR                       144: remover_tab
                        7068    LOAD_CONST                      47: 'Game Remover'
                        7070    CALL                            2
                        7078    POP_TOP
                        7080    LOAD_FAST                       0: self
                        7082    LOAD_ATTR                       160: steam_dir
                        7102    TO_BOOL
                        7110    POP_JUMP_IF_FALSE               27 (to 7166)
                        7114    LOAD_FAST                       0: self
                        7116    LOAD_ATTR                       100: label_steam
                        7136    LOAD_ATTR                       163: setText
                        7156    LOAD_CONST                      48: 'Steam Directory: (set)'
                        7158    CALL                            1
                        7166    POP_TOP
                        7168    LOAD_FAST                       0: self
                        7170    LOAD_ATTR                       164: save_dir
                        7190    TO_BOOL
                        7198    POP_JUMP_IF_FALSE               28 (to 7256)
                        7202    LOAD_FAST                       0: self
                        7204    LOAD_ATTR                       92: label_save_dir
                        7224    LOAD_ATTR                       163: setText
                        7244    LOAD_CONST                      49: 'Save Directory: (set)'
                        7246    CALL                            1
                        7254    POP_TOP
                        7256    RETURN_CONST                    0: None
                        7258    RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: log_console
                    Qualified Name: LuaScriptMaker.log_console
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 3
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'text_console'
                        'append'
                        'logging'
                        'info'
                    [Locals+Names]
                        'self'
                        'msg'
                    [Constants]
                        None
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: text_console
                        24      LOAD_ATTR                       3: append
                        44      LOAD_FAST                       1: msg
                        46      CALL                            1
                        54      POP_TOP
                        56      LOAD_GLOBAL                     4: logging
                        66      LOAD_ATTR                       6: info
                        86      PUSH_NULL
                        88      LOAD_FAST                       1: msg
                        90      CALL                            1
                        98      POP_TOP
                        100     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: log_removal
                    Qualified Name: LuaScriptMaker.log_removal
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 3
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'text_remove_console'
                        'append'
                        'logging'
                        'info'
                    [Locals+Names]
                        'self'
                        'msg'
                    [Constants]
                        None
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: text_remove_console
                        24      LOAD_ATTR                       3: append
                        44      LOAD_FAST                       1: msg
                        46      CALL                            1
                        54      POP_TOP
                        56      LOAD_GLOBAL                     4: logging
                        66      LOAD_ATTR                       6: info
                        86      PUSH_NULL
                        88      LOAD_FAST                       1: msg
                        90      CALL                            1
                        98      POP_TOP
                        100     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: clear_draft
                    Qualified Name: LuaScriptMaker.clear_draft
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'script_lines'
                        'clear'
                        'added_ids'
                        'text_preview'
                        'text_console'
                        'QMessageBox'
                        'information'
                    [Locals+Names]
                        'self'
                    [Constants]
                        None
                        'Cleared'
                        'Draft cleared.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: script_lines
                        24      LOAD_ATTR                       3: clear
                        44      CALL                            0
                        52      POP_TOP
                        54      LOAD_FAST                       0: self
                        56      LOAD_ATTR                       4: added_ids
                        76      LOAD_ATTR                       3: clear
                        96      CALL                            0
                        104     POP_TOP
                        106     LOAD_FAST                       0: self
                        108     LOAD_ATTR                       6: text_preview
                        128     LOAD_ATTR                       3: clear
                        148     CALL                            0
                        156     POP_TOP
                        158     LOAD_FAST                       0: self
                        160     LOAD_ATTR                       8: text_console
                        180     LOAD_ATTR                       3: clear
                        200     CALL                            0
                        208     POP_TOP
                        210     LOAD_GLOBAL                     10: QMessageBox
                        220     LOAD_ATTR                       12: information
                        240     PUSH_NULL
                        242     LOAD_FAST                       0: self
                        244     LOAD_CONST                      1: 'Cleared'
                        246     LOAD_CONST                      2: 'Draft cleared.'
                        248     CALL                            3
                        256     POP_TOP
                        258     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: toggle_export_pause
                    Qualified Name: LuaScriptMaker.toggle_export_pause
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 3
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'export_paused'
                        'btn_pause'
                        'setText'
                        'log_console'
                    [Locals+Names]
                        'self'
                    [Constants]
                        None
                        'Resume Export'
                        'Export paused.'
                        'Pause Export'
                        'Export resumed.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: export_paused
                        24      TO_BOOL
                        32      UNARY_NOT
                        34      LOAD_FAST                       0: self
                        36      STORE_ATTR                      0: export_paused
                        46      LOAD_FAST                       0: self
                        48      LOAD_ATTR                       0: export_paused
                        68      TO_BOOL
                        76      POP_JUMP_IF_FALSE               45 (to 168)
                        80      LOAD_FAST                       0: self
                        82      LOAD_ATTR                       2: btn_pause
                        102     LOAD_ATTR                       5: setText
                        122     LOAD_CONST                      1: 'Resume Export'
                        124     CALL                            1
                        132     POP_TOP
                        134     LOAD_FAST                       0: self
                        136     LOAD_ATTR                       7: log_console
                        156     LOAD_CONST                      2: 'Export paused.'
                        158     CALL                            1
                        166     POP_TOP
                        168     RETURN_CONST                    0: None
                        170     LOAD_FAST                       0: self
                        172     LOAD_ATTR                       2: btn_pause
                        192     LOAD_ATTR                       5: setText
                        212     LOAD_CONST                      3: 'Pause Export'
                        214     CALL                            1
                        222     POP_TOP
                        224     LOAD_FAST                       0: self
                        226     LOAD_ATTR                       7: log_console
                        246     LOAD_CONST                      4: 'Export resumed.'
                        248     CALL                            1
                        256     POP_TOP
                        258     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: update_theme
                    Qualified Name: LuaScriptMaker.update_theme
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'get'
                        'QApplication'
                        'instance'
                        'setStyleSheet'
                    [Locals+Names]
                        'self'
                        'theme_name'
                        'themes'
                        'style'
                    [Constants]
                        None
                        "\n                QWidget { background-color: #2c3e50; color: #ecf0f1; font-family: 'gg sans', Helvetica Neue, Helvetica, Arial, sans-serif; }\n                QLineEdit, QTextEdit { background-color: #34495e; color: #ecf0f1; border: 1px solid #7f8c8d; }\n                QPushButton { background-color: #2980b9; color: #ecf0f1; padding: 5px; border: none; }\n                QPushButton:hover { background-color: #3498db; }\n                QPushButton:pressed { background-color: #1abc9c; }\n                QLabel { color: #ecf0f1; }\n            "
                        "\n                QWidget { background-color: #36393f; color: #b9bbbe; font-family: 'gg sans', Helvetica Neue, Helvetica, Arial, sans-serif; }\n                QLineEdit, QTextEdit { background-color: #40444b; color: #dcddde; border: 1px solid #72767d; }\n                QPushButton { background-color: #7289da; color: #ffffff; padding: 5px; border: none; }\n                QPushButton:hover { background-color: #5b6eae; }\n                QPushButton:pressed { background-color: #4e5d94; }\n                QLabel { color: #b9bbbe; }\n            "
                        "\n                QWidget { background-color: #000000; color: #f1f1f1; font-family: 'gg sans', Helvetica Neue, Helvetica, Arial, sans-serif; }\n                QLineEdit, QTextEdit { background-color: #111111; color: #f1f1f1; border: 1px solid #333333; }\n                QPushButton { background-color: #222222; color: #f1f1f1; padding: 5px; border: none; }\n                QPushButton:hover { background-color: #333333; }\n                QPushButton:pressed { background-color: #444444; }\n                QLabel { color: #f1f1f1; }\n            "
                        (
                            'Sapphire'
                            'Midnight'
                            'Obsidian'
                        )
                        'Sapphire'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_CONST                      1: "\n                QWidget { background-color: #2c3e50; color: #ecf0f1; font-family: 'gg sans', Helvetica Neue, Helvetica, Arial, sans-serif; }\n                QLineEdit, QTextEdit { background-color: #34495e; color: #ecf0f1; border: 1px solid #7f8c8d; }\n                QPushButton { background-color: #2980b9; color: #ecf0f1; padding: 5px; border: none; }\n                QPushButton:hover { background-color: #3498db; }\n                QPushButton:pressed { background-color: #1abc9c; }\n                QLabel { color: #ecf0f1; }\n            "
                        4       LOAD_CONST                      2: "\n                QWidget { background-color: #36393f; color: #b9bbbe; font-family: 'gg sans', Helvetica Neue, Helvetica, Arial, sans-serif; }\n                QLineEdit, QTextEdit { background-color: #40444b; color: #dcddde; border: 1px solid #72767d; }\n                QPushButton { background-color: #7289da; color: #ffffff; padding: 5px; border: none; }\n                QPushButton:hover { background-color: #5b6eae; }\n                QPushButton:pressed { background-color: #4e5d94; }\n                QLabel { color: #b9bbbe; }\n            "
                        6       LOAD_CONST                      3: "\n                QWidget { background-color: #000000; color: #f1f1f1; font-family: 'gg sans', Helvetica Neue, Helvetica, Arial, sans-serif; }\n                QLineEdit, QTextEdit { background-color: #111111; color: #f1f1f1; border: 1px solid #333333; }\n                QPushButton { background-color: #222222; color: #f1f1f1; padding: 5px; border: none; }\n                QPushButton:hover { background-color: #333333; }\n                QPushButton:pressed { background-color: #444444; }\n                QLabel { color: #f1f1f1; }\n            "
                        8       LOAD_CONST                      4: ('Sapphire', 'Midnight', 'Obsidian')
                        10      BUILD_CONST_KEY_MAP             3
                        12      STORE_FAST                      2: themes
                        14      LOAD_FAST                       2: themes
                        16      LOAD_ATTR                       1: get
                        36      LOAD_FAST_LOAD_FAST             18: theme_name, themes
                        38      LOAD_CONST                      5: 'Sapphire'
                        40      BINARY_SUBSCR
                        44      CALL                            2
                        52      STORE_FAST                      3: style
                        54      LOAD_GLOBAL                     2: QApplication
                        64      LOAD_ATTR                       4: instance
                        84      PUSH_NULL
                        86      CALL                            0
                        94      LOAD_ATTR                       7: setStyleSheet
                        114     LOAD_FAST                       3: style
                        116     CALL                            1
                        124     POP_TOP
                        126     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: auto_detect_steam_dir
                    Qualified Name: LuaScriptMaker.auto_detect_steam_dir
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'Path'
                        'exists'
                        'str'
                        'steam_dir'
                        'label_steam'
                        'setText'
                        'save_config'
                        'QMessageBox'
                        'warning'
                    [Locals+Names]
                        'self'
                        'all_drives'
                        'candidates'
                        'detected'
                        'drive'
                        'sub'
                        'candidate'
                    [Constants]
                        None
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: all_drives
                            Qualified Name: LuaScriptMaker.auto_detect_steam_dir.<locals>.all_drives
                            Arg Count: 0
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 9
                            Flags: 0x00000013 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED)
                            [Names]
                                'ctypes'
                                'windll'
                                'kernel32'
                                'GetLogicalDrives'
                                'range'
                                'append'
                                'Path'
                                'chr'
                            [Locals+Names]
                                'drives'
                                'bitmask'
                                'i'
                            [Constants]
                                None
                                26
                                1
                                65
                                ':\\'
                            [Disassembly]
                                0       RESUME                          0
                                2       BUILD_LIST                      0
                                4       STORE_FAST                      0: drives
                                6       LOAD_GLOBAL                     0: ctypes
                                16      LOAD_ATTR                       2: windll
                                36      LOAD_ATTR                       4: kernel32
                                56      LOAD_ATTR                       7: GetLogicalDrives
                                76      CALL                            0
                                84      STORE_FAST                      1: bitmask
                                86      LOAD_GLOBAL                     9: NULL + range
                                96      LOAD_CONST                      1: 26
                                98      CALL                            1
                                106     GET_ITER
                                108     FOR_ITER                        59 (to 228)
                                112     STORE_FAST                      2: i
                                114     LOAD_FAST                       1: bitmask
                                116     LOAD_CONST                      2: 1
                                118     LOAD_FAST                       2: i
                                120     BINARY_OP                       3 (<<)
                                124     BINARY_OP                       1 (&)
                                128     TO_BOOL
                                136     POP_JUMP_IF_TRUE                2 (to 142)
                                140     JUMP_BACKWARD                   18 (to 106)
                                144     LOAD_FAST                       0: drives
                                146     LOAD_ATTR                       11: append
                                166     LOAD_GLOBAL                     13: NULL + Path
                                176     LOAD_GLOBAL                     15: NULL + chr
                                186     LOAD_CONST                      3: 65
                                188     LOAD_FAST                       2: i
                                190     BINARY_OP                       0 (+)
                                194     CALL                            1
                                202     FORMAT_SIMPLE
                                204     LOAD_CONST                      4: ':\\'
                                206     BUILD_STRING                    2
                                208     CALL                            1
                                216     CALL                            1
                                224     POP_TOP
                                226     JUMP_BACKWARD                   61 (to 106)
                                230     END_FOR
                                232     POP_TOP
                                234     LOAD_FAST                       0: drives
                                236     RETURN_VALUE
                        'Program Files (x86)\\Steam'
                        'Program Files\\Steam'
                        'Steam'
                        'steam.exe'
                        'Steam Directory: (set)'
                        'Directory Not Found'
                        'Steam directory not detected. Please set it manually.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_CONST                      1: <CODE> all_drives
                        4       MAKE_FUNCTION
                        6       STORE_FAST                      1: all_drives
                        8       LOAD_GLOBAL                     1: NULL + Path
                        18      LOAD_CONST                      2: 'Program Files (x86)\\Steam'
                        20      CALL                            1
                        28      LOAD_GLOBAL                     1: NULL + Path
                        38      LOAD_CONST                      3: 'Program Files\\Steam'
                        40      CALL                            1
                        48      LOAD_GLOBAL                     1: NULL + Path
                        58      LOAD_CONST                      4: 'Steam'
                        60      CALL                            1
                        68      BUILD_LIST                      3
                        70      STORE_FAST                      2: candidates
                        72      LOAD_CONST                      0: None
                        74      STORE_FAST                      3: detected
                        76      LOAD_FAST                       1: all_drives
                        78      PUSH_NULL
                        80      CALL                            0
                        88      GET_ITER
                        90      FOR_ITER                        62 (to 216)
                        94      STORE_FAST                      4: drive
                        96      LOAD_FAST                       2: candidates
                        98      GET_ITER
                        100     FOR_ITER                        44 (to 190)
                        104     STORE_FAST                      5: sub
                        106     LOAD_FAST_LOAD_FAST             69: drive, sub
                        108     BINARY_OP                       11 (/)
                        112     STORE_FAST                      6: candidate
                        114     LOAD_FAST                       6: candidate
                        116     LOAD_CONST                      5: 'steam.exe'
                        118     BINARY_OP                       11 (/)
                        122     LOAD_ATTR                       3: exists
                        142     CALL                            0
                        150     TO_BOOL
                        158     POP_JUMP_IF_TRUE                2 (to 164)
                        162     JUMP_BACKWARD                   33 (to 98)
                        166     LOAD_GLOBAL                     5: NULL + str
                        176     LOAD_FAST                       6: candidate
                        178     CALL                            1
                        186     STORE_FAST                      3: detected
                        188     POP_TOP
                        190     JUMP_FORWARD                    2 (to 196)
                        192     END_FOR
                        194     POP_TOP
                        196     LOAD_FAST                       3: detected
                        198     TO_BOOL
                        206     POP_JUMP_IF_TRUE                2 (to 212)
                        210     JUMP_BACKWARD                   62 (to 88)
                        214     POP_TOP
                        216     JUMP_FORWARD                    2 (to 222)
                        218     END_FOR
                        220     POP_TOP
                        222     LOAD_FAST                       3: detected
                        224     TO_BOOL
                        232     POP_JUMP_IF_FALSE               50 (to 334)
                        236     LOAD_FAST_LOAD_FAST             48: detected, self
                        238     STORE_ATTR                      3: steam_dir
                        248     LOAD_FAST                       0: self
                        250     LOAD_ATTR                       8: label_steam
                        270     LOAD_ATTR                       11: setText
                        290     LOAD_CONST                      6: 'Steam Directory: (set)'
                        292     CALL                            1
                        300     POP_TOP
                        302     LOAD_FAST                       0: self
                        304     LOAD_ATTR                       13: save_config
                        324     CALL                            0
                        332     POP_TOP
                        334     RETURN_CONST                    0: None
                        336     LOAD_GLOBAL                     14: QMessageBox
                        346     LOAD_ATTR                       16: warning
                        366     PUSH_NULL
                        368     LOAD_FAST                       0: self
                        370     LOAD_CONST                      7: 'Directory Not Found'
                        372     LOAD_CONST                      8: 'Steam directory not detected. Please set it manually.'
                        374     CALL                            3
                        382     POP_TOP
                        384     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: change_steam_directory
                    Qualified Name: LuaScriptMaker.change_steam_directory
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'QFileDialog'
                        'getExistingDirectory'
                        'steam_dir'
                        'label_steam'
                        'setText'
                        'QMessageBox'
                        'information'
                        'save_config'
                        'warning'
                    [Locals+Names]
                        'self'
                        'chosen'
                    [Constants]
                        None
                        'Select Steam Directory'
                        'Steam Directory: (set)'
                        'Directory Set'
                        'Steam directory updated.'
                        'Directory Error'
                        'No directory selected.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     0: QFileDialog
                        12      LOAD_ATTR                       2: getExistingDirectory
                        32      PUSH_NULL
                        34      LOAD_FAST                       0: self
                        36      LOAD_CONST                      1: 'Select Steam Directory'
                        38      CALL                            2
                        46      STORE_FAST                      1: chosen
                        48      LOAD_FAST                       1: chosen
                        50      TO_BOOL
                        58      POP_JUMP_IF_FALSE               74 (to 208)
                        62      LOAD_FAST_LOAD_FAST             16: chosen, self
                        64      STORE_ATTR                      2: steam_dir
                        74      LOAD_FAST                       0: self
                        76      LOAD_ATTR                       6: label_steam
                        96      LOAD_ATTR                       9: setText
                        116     LOAD_CONST                      2: 'Steam Directory: (set)'
                        118     CALL                            1
                        126     POP_TOP
                        128     LOAD_GLOBAL                     10: QMessageBox
                        138     LOAD_ATTR                       12: information
                        158     PUSH_NULL
                        160     LOAD_FAST                       0: self
                        162     LOAD_CONST                      3: 'Directory Set'
                        164     LOAD_CONST                      4: 'Steam directory updated.'
                        166     CALL                            3
                        174     POP_TOP
                        176     LOAD_FAST                       0: self
                        178     LOAD_ATTR                       15: save_config
                        198     CALL                            0
                        206     POP_TOP
                        208     RETURN_CONST                    0: None
                        210     LOAD_GLOBAL                     10: QMessageBox
                        220     LOAD_ATTR                       16: warning
                        240     PUSH_NULL
                        242     LOAD_FAST                       0: self
                        244     LOAD_CONST                      5: 'Directory Error'
                        246     LOAD_CONST                      6: 'No directory selected.'
                        248     CALL                            3
                        256     POP_TOP
                        258     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: select_save_directory
                    Qualified Name: LuaScriptMaker.select_save_directory
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'QFileDialog'
                        'getExistingDirectory'
                        'save_dir'
                        'label_save_dir'
                        'setText'
                        'QMessageBox'
                        'information'
                        'save_config'
                        'warning'
                    [Locals+Names]
                        'self'
                        'chosen'
                    [Constants]
                        None
                        'Select Save Directory'
                        'Save Directory: (set)'
                        'Directory Set'
                        'Save directory updated.'
                        'Directory Error'
                        'No directory selected.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     0: QFileDialog
                        12      LOAD_ATTR                       2: getExistingDirectory
                        32      PUSH_NULL
                        34      LOAD_FAST                       0: self
                        36      LOAD_CONST                      1: 'Select Save Directory'
                        38      CALL                            2
                        46      STORE_FAST                      1: chosen
                        48      LOAD_FAST                       1: chosen
                        50      TO_BOOL
                        58      POP_JUMP_IF_FALSE               74 (to 208)
                        62      LOAD_FAST_LOAD_FAST             16: chosen, self
                        64      STORE_ATTR                      2: save_dir
                        74      LOAD_FAST                       0: self
                        76      LOAD_ATTR                       6: label_save_dir
                        96      LOAD_ATTR                       9: setText
                        116     LOAD_CONST                      2: 'Save Directory: (set)'
                        118     CALL                            1
                        126     POP_TOP
                        128     LOAD_GLOBAL                     10: QMessageBox
                        138     LOAD_ATTR                       12: information
                        158     PUSH_NULL
                        160     LOAD_FAST                       0: self
                        162     LOAD_CONST                      3: 'Directory Set'
                        164     LOAD_CONST                      4: 'Save directory updated.'
                        166     CALL                            3
                        174     POP_TOP
                        176     LOAD_FAST                       0: self
                        178     LOAD_ATTR                       15: save_config
                        198     CALL                            0
                        206     POP_TOP
                        208     RETURN_CONST                    0: None
                        210     LOAD_GLOBAL                     10: QMessageBox
                        220     LOAD_ATTR                       16: warning
                        240     PUSH_NULL
                        242     LOAD_FAST                       0: self
                        244     LOAD_CONST                      5: 'Directory Error'
                        246     LOAD_CONST                      6: 'No directory selected.'
                        248     CALL                            3
                        256     POP_TOP
                        258     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: select_game_directory
                    Qualified Name: LuaScriptMaker.select_game_directory
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'QFileDialog'
                        'getExistingDirectory'
                        'game_dir'
                        'label_game'
                        'setText'
                        'QMessageBox'
                        'information'
                        'save_config'
                        'warning'
                    [Locals+Names]
                        'self'
                        'chosen'
                    [Constants]
                        None
                        'Select Game Directory'
                        'Game Directory: (set)'
                        'Directory Set'
                        'Game directory updated.'
                        'Directory Error'
                        'No directory selected.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     0: QFileDialog
                        12      LOAD_ATTR                       2: getExistingDirectory
                        32      PUSH_NULL
                        34      LOAD_FAST                       0: self
                        36      LOAD_CONST                      1: 'Select Game Directory'
                        38      CALL                            2
                        46      STORE_FAST                      1: chosen
                        48      LOAD_FAST                       1: chosen
                        50      TO_BOOL
                        58      POP_JUMP_IF_FALSE               74 (to 208)
                        62      LOAD_FAST_LOAD_FAST             16: chosen, self
                        64      STORE_ATTR                      2: game_dir
                        74      LOAD_FAST                       0: self
                        76      LOAD_ATTR                       6: label_game
                        96      LOAD_ATTR                       9: setText
                        116     LOAD_CONST                      2: 'Game Directory: (set)'
                        118     CALL                            1
                        126     POP_TOP
                        128     LOAD_GLOBAL                     10: QMessageBox
                        138     LOAD_ATTR                       12: information
                        158     PUSH_NULL
                        160     LOAD_FAST                       0: self
                        162     LOAD_CONST                      3: 'Directory Set'
                        164     LOAD_CONST                      4: 'Game directory updated.'
                        166     CALL                            3
                        174     POP_TOP
                        176     LOAD_FAST                       0: self
                        178     LOAD_ATTR                       15: save_config
                        198     CALL                            0
                        206     POP_TOP
                        208     RETURN_CONST                    0: None
                        210     LOAD_GLOBAL                     10: QMessageBox
                        220     LOAD_ATTR                       16: warning
                        240     PUSH_NULL
                        242     LOAD_FAST                       0: self
                        244     LOAD_CONST                      5: 'Directory Error'
                        246     LOAD_CONST                      6: 'No directory selected.'
                        248     CALL                            3
                        256     POP_TOP
                        258     RETURN_CONST                    0: None
                'return'
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: get_library_folders
                    Qualified Name: LuaScriptMaker.get_library_folders
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 8
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'set'
                        'Path'
                        'steam_dir'
                        'exists'
                        'open'
                        'read'
                        're'
                        'findall'
                        'DOTALL'
                        'search'
                        'add'
                        'group'
                        'Exception'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'library_folders'
                        'main_lib_path'
                        'f'
                        'content'
                        'blocks'
                        'block'
                        'm'
                        'e'
                        'config_lib_path'
                    [Constants]
                        None
                        'steamapps'
                        'libraryfolders.vdf'
                        'r'
                        'utf-8'
                        (
                            'encoding'
                        )
                        '"\\d+"\\s*{(.*?)}'
                        '"path"\\s*"([^"]+)"'
                        1
                        'Error reading main libraryfolders.vdf:'
                        'config'
                        'Error reading config libraryfolders.vdf:'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     1: NULL + set
                        12      CALL                            0
                        20      STORE_FAST                      1: library_folders
                        22      LOAD_GLOBAL                     3: NULL + Path
                        32      LOAD_FAST                       0: self
                        34      LOAD_ATTR                       4: steam_dir
                        54      CALL                            1
                        62      LOAD_CONST                      1: 'steamapps'
                        64      BINARY_OP                       11 (/)
                        68      LOAD_CONST                      2: 'libraryfolders.vdf'
                        70      BINARY_OP                       11 (/)
                        74      STORE_FAST                      2: main_lib_path
                        76      LOAD_FAST                       2: main_lib_path
                        78      LOAD_ATTR                       7: exists
                        98      CALL                            0
                        106     TO_BOOL
                        114     POP_JUMP_IF_FALSE               165 (to 446)
                        118     NOP
                        120     LOAD_FAST                       2: main_lib_path
                        122     LOAD_ATTR                       9: open
                        142     LOAD_CONST                      3: 'r'
                        144     LOAD_CONST                      4: 'utf-8'
                        146     LOAD_CONST                      5: ('encoding',)
                        148     CALL_KW                         2
                        150     BEFORE_WITH
                        152     STORE_FAST                      3: f
                        154     LOAD_FAST                       3: f
                        156     LOAD_ATTR                       11: read
                        176     CALL                            0
                        184     STORE_FAST                      4: content
                        186     LOAD_CONST                      0: None
                        188     LOAD_CONST                      0: None
                        190     LOAD_CONST                      0: None
                        192     CALL                            2
                        200     POP_TOP
                        202     LOAD_GLOBAL                     12: re
                        212     LOAD_ATTR                       14: findall
                        232     PUSH_NULL
                        234     LOAD_CONST                      6: '"\\d+"\\s*{(.*?)}'
                        236     LOAD_FAST_CHECK                 4: content
                        238     LOAD_GLOBAL                     12: re
                        248     LOAD_ATTR                       16: DOTALL
                        268     CALL                            3
                        276     STORE_FAST                      5: blocks
                        278     LOAD_FAST                       5: blocks
                        280     GET_ITER
                        282     FOR_ITER                        79 (to 442)
                        286     STORE_FAST                      6: block
                        288     LOAD_GLOBAL                     12: re
                        298     LOAD_ATTR                       18: search
                        318     PUSH_NULL
                        320     LOAD_CONST                      7: '"path"\\s*"([^"]+)"'
                        322     LOAD_FAST                       6: block
                        324     CALL                            2
                        332     STORE_FAST                      7: m
                        334     LOAD_FAST                       7: m
                        336     TO_BOOL
                        344     POP_JUMP_IF_TRUE                2 (to 350)
                        348     JUMP_BACKWARD                   35 (to 280)
                        352     LOAD_FAST                       1: library_folders
                        354     LOAD_ATTR                       21: add
                        374     LOAD_GLOBAL                     3: NULL + Path
                        384     LOAD_FAST                       7: m
                        386     LOAD_ATTR                       23: group
                        406     LOAD_CONST                      8: 1
                        408     CALL                            1
                        416     CALL                            1
                        424     LOAD_CONST                      1: 'steamapps'
                        426     BINARY_OP                       11 (/)
                        430     CALL                            1
                        438     POP_TOP
                        440     JUMP_BACKWARD                   81 (to 280)
                        444     END_FOR
                        446     POP_TOP
                        448     LOAD_GLOBAL                     3: NULL + Path
                        458     LOAD_FAST                       0: self
                        460     LOAD_ATTR                       4: steam_dir
                        480     CALL                            1
                        488     LOAD_CONST                      10: 'config'
                        490     BINARY_OP                       11 (/)
                        494     LOAD_CONST                      2: 'libraryfolders.vdf'
                        496     BINARY_OP                       11 (/)
                        500     STORE_FAST                      9: config_lib_path
                        502     LOAD_FAST                       9: config_lib_path
                        504     LOAD_ATTR                       7: exists
                        524     CALL                            0
                        532     TO_BOOL
                        540     POP_JUMP_IF_FALSE               165 (to 872)
                        544     NOP
                        546     LOAD_FAST                       9: config_lib_path
                        548     LOAD_ATTR                       9: open
                        568     LOAD_CONST                      3: 'r'
                        570     LOAD_CONST                      4: 'utf-8'
                        572     LOAD_CONST                      5: ('encoding',)
                        574     CALL_KW                         2
                        576     BEFORE_WITH
                        578     STORE_FAST                      3: f
                        580     LOAD_FAST                       3: f
                        582     LOAD_ATTR                       11: read
                        602     CALL                            0
                        610     STORE_FAST                      4: content
                        612     LOAD_CONST                      0: None
                        614     LOAD_CONST                      0: None
                        616     LOAD_CONST                      0: None
                        618     CALL                            2
                        626     POP_TOP
                        628     LOAD_GLOBAL                     12: re
                        638     LOAD_ATTR                       14: findall
                        658     PUSH_NULL
                        660     LOAD_CONST                      6: '"\\d+"\\s*{(.*?)}'
                        662     LOAD_FAST_CHECK                 4: content
                        664     LOAD_GLOBAL                     12: re
                        674     LOAD_ATTR                       16: DOTALL
                        694     CALL                            3
                        702     STORE_FAST                      5: blocks
                        704     LOAD_FAST                       5: blocks
                        706     GET_ITER
                        708     FOR_ITER                        79 (to 868)
                        712     STORE_FAST                      6: block
                        714     LOAD_GLOBAL                     12: re
                        724     LOAD_ATTR                       18: search
                        744     PUSH_NULL
                        746     LOAD_CONST                      7: '"path"\\s*"([^"]+)"'
                        748     LOAD_FAST                       6: block
                        750     CALL                            2
                        758     STORE_FAST                      7: m
                        760     LOAD_FAST                       7: m
                        762     TO_BOOL
                        770     POP_JUMP_IF_TRUE                2 (to 776)
                        774     JUMP_BACKWARD                   35 (to 706)
                        778     LOAD_FAST                       1: library_folders
                        780     LOAD_ATTR                       21: add
                        800     LOAD_GLOBAL                     3: NULL + Path
                        810     LOAD_FAST                       7: m
                        812     LOAD_ATTR                       23: group
                        832     LOAD_CONST                      8: 1
                        834     CALL                            1
                        842     CALL                            1
                        850     LOAD_CONST                      1: 'steamapps'
                        852     BINARY_OP                       11 (/)
                        856     CALL                            1
                        864     POP_TOP
                        866     JUMP_BACKWARD                   81 (to 706)
                        870     END_FOR
                        872     POP_TOP
                        874     LOAD_FAST                       1: library_folders
                        876     LOAD_ATTR                       21: add
                        896     LOAD_GLOBAL                     3: NULL + Path
                        906     LOAD_FAST                       0: self
                        908     LOAD_ATTR                       4: steam_dir
                        928     CALL                            1
                        936     LOAD_CONST                      1: 'steamapps'
                        938     BINARY_OP                       11 (/)
                        942     CALL                            1
                        950     POP_TOP
                        952     LOAD_FAST                       1: library_folders
                        954     RETURN_VALUE
                        956     PUSH_EXC_INFO
                        958     WITH_EXCEPT_START
                        960     TO_BOOL
                        968     POP_JUMP_IF_TRUE                1 (to 972)
                        972     RERAISE                         2
                        974     POP_TOP
                        976     POP_EXCEPT
                        978     POP_TOP
                        980     POP_TOP
                        982     JUMP_BACKWARD_NO_INTERRUPT      392 (to 202)
                        986     COPY                            3
                        988     POP_EXCEPT
                        990     RERAISE                         1
                        992     PUSH_EXC_INFO
                        994     LOAD_GLOBAL                     24: Exception
                        1004    CHECK_EXC_MATCH
                        1006    POP_JUMP_IF_FALSE               33 (to 1074)
                        1010    STORE_FAST                      8: e
                        1012    LOAD_GLOBAL                     26: logging
                        1022    LOAD_ATTR                       28: exception
                        1042    PUSH_NULL
                        1044    LOAD_CONST                      9: 'Error reading main libraryfolders.vdf:'
                        1046    CALL                            1
                        1054    POP_TOP
                        1056    POP_EXCEPT
                        1058    LOAD_CONST                      0: None
                        1060    STORE_FAST                      8: e
                        1062    DELETE_FAST                     8: e
                        1064    JUMP_BACKWARD_NO_INTERRUPT      310 (to 448)
                        1068    LOAD_CONST                      0: None
                        1070    STORE_FAST                      8: e
                        1072    DELETE_FAST                     8: e
                        1074    RERAISE                         1
                        1076    RERAISE                         0
                        1078    COPY                            3
                        1080    POP_EXCEPT
                        1082    RERAISE                         1
                        1084    PUSH_EXC_INFO
                        1086    WITH_EXCEPT_START
                        1088    TO_BOOL
                        1096    POP_JUMP_IF_TRUE                1 (to 1100)
                        1100    RERAISE                         2
                        1102    POP_TOP
                        1104    POP_EXCEPT
                        1106    POP_TOP
                        1108    POP_TOP
                        1110    JUMP_BACKWARD_NO_INTERRUPT      242 (to 628)
                        1112    COPY                            3
                        1114    POP_EXCEPT
                        1116    RERAISE                         1
                        1118    PUSH_EXC_INFO
                        1120    LOAD_GLOBAL                     24: Exception
                        1130    CHECK_EXC_MATCH
                        1132    POP_JUMP_IF_FALSE               32 (to 1198)
                        1136    STORE_FAST                      8: e
                        1138    LOAD_GLOBAL                     26: logging
                        1148    LOAD_ATTR                       28: exception
                        1168    PUSH_NULL
                        1170    LOAD_CONST                      11: 'Error reading config libraryfolders.vdf:'
                        1172    CALL                            1
                        1180    POP_TOP
                        1182    POP_EXCEPT
                        1184    LOAD_CONST                      0: None
                        1186    STORE_FAST                      8: e
                        1188    DELETE_FAST                     8: e
                        1190    JUMP_BACKWARD_NO_INTERRUPT      159 (to 874)
                        1192    LOAD_CONST                      0: None
                        1194    STORE_FAST                      8: e
                        1196    DELETE_FAST                     8: e
                        1198    RERAISE                         1
                        1200    RERAISE                         0
                        1202    COPY                            3
                        1204    POP_EXCEPT
                        1206    RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: auto_fill_fields
                    Qualified Name: LuaScriptMaker.auto_fill_fields
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'input_primary'
                        'text'
                        'strip'
                        'input_dlc'
                        'clear'
                        'steam_dir'
                        'QMessageBox'
                        'warning'
                        'isdigit'
                        'str'
                        'int'
                        'input_secondary'
                        'setText'
                        'Path'
                        'get_dkey'
                        'input_dkey'
                        'get_manifest_for_appid'
                        'input_manifest'
                        'log_console'
                    [Locals+Names]
                        'self'
                        'primary'
                        'secondary'
                        'config_path'
                        'dkey_val'
                        'manifest_val'
                    [Constants]
                        None
                        'Directory Error'
                        'Please set the Steam directory first.'
                        1
                        'config'
                        'config.vdf'
                        'DummyDKey_for_'
                        'Unknown'
                        'DummyManifest_for_'
                        'Fields autofilled for secondary AppID '
                        '.'
                        'Input Error'
                        'Primary AppID must be numeric.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: input_primary
                        24      LOAD_ATTR                       3: text
                        44      CALL                            0
                        52      LOAD_ATTR                       5: strip
                        72      CALL                            0
                        80      STORE_FAST                      1: primary
                        82      LOAD_FAST                       0: self
                        84      LOAD_ATTR                       6: input_dlc
                        104     LOAD_ATTR                       9: clear
                        124     CALL                            0
                        132     POP_TOP
                        134     LOAD_FAST                       0: self
                        136     LOAD_ATTR                       10: steam_dir
                        156     TO_BOOL
                        164     POP_JUMP_IF_TRUE                25 (to 216)
                        168     LOAD_GLOBAL                     12: QMessageBox
                        178     LOAD_ATTR                       14: warning
                        198     PUSH_NULL
                        200     LOAD_FAST                       0: self
                        202     LOAD_CONST                      1: 'Directory Error'
                        204     LOAD_CONST                      2: 'Please set the Steam directory first.'
                        206     CALL                            3
                        214     POP_TOP
                        216     RETURN_CONST                    0: None
                        218     LOAD_FAST                       1: primary
                        220     LOAD_ATTR                       17: isdigit
                        240     CALL                            0
                        248     TO_BOOL
                        256     POP_JUMP_IF_FALSE               227 (to 712)
                        260     LOAD_GLOBAL                     19: NULL + str
                        270     LOAD_GLOBAL                     21: NULL + int
                        280     LOAD_FAST                       1: primary
                        282     CALL                            1
                        290     LOAD_CONST                      3: 1
                        292     BINARY_OP                       0 (+)
                        296     CALL                            1
                        304     STORE_FAST                      2: secondary
                        306     LOAD_FAST                       0: self
                        308     LOAD_ATTR                       22: input_secondary
                        328     LOAD_ATTR                       25: setText
                        348     LOAD_FAST                       2: secondary
                        350     CALL                            1
                        358     POP_TOP
                        360     LOAD_GLOBAL                     27: NULL + Path
                        370     LOAD_FAST                       0: self
                        372     LOAD_ATTR                       10: steam_dir
                        392     CALL                            1
                        400     LOAD_CONST                      4: 'config'
                        402     BINARY_OP                       11 (/)
                        406     LOAD_CONST                      5: 'config.vdf'
                        408     BINARY_OP                       11 (/)
                        412     STORE_FAST                      3: config_path
                        414     LOAD_FAST                       0: self
                        416     LOAD_ATTR                       29: get_dkey
                        436     LOAD_GLOBAL                     19: NULL + str
                        446     LOAD_FAST                       3: config_path
                        448     CALL                            1
                        456     LOAD_FAST                       2: secondary
                        458     CALL                            2
                        466     STORE_FAST                      4: dkey_val
                        468     LOAD_FAST                       4: dkey_val
                        470     TO_BOOL
                        478     POP_JUMP_IF_TRUE                5 (to 490)
                        482     LOAD_CONST                      6: 'DummyDKey_for_'
                        484     LOAD_FAST                       2: secondary
                        486     FORMAT_SIMPLE
                        488     BUILD_STRING                    2
                        490     STORE_FAST                      4: dkey_val
                        492     LOAD_FAST                       0: self
                        494     LOAD_ATTR                       30: input_dkey
                        514     LOAD_ATTR                       25: setText
                        534     LOAD_FAST                       4: dkey_val
                        536     CALL                            1
                        544     POP_TOP
                        546     LOAD_FAST                       0: self
                        548     LOAD_ATTR                       33: get_manifest_for_appid
                        568     LOAD_FAST                       2: secondary
                        570     CALL                            1
                        578     STORE_FAST                      5: manifest_val
                        580     LOAD_FAST                       5: manifest_val
                        582     TO_BOOL
                        590     POP_JUMP_IF_FALSE               6 (to 604)
                        594     LOAD_FAST                       5: manifest_val
                        596     LOAD_CONST                      7: 'Unknown'
                        598     COMPARE_OP                      88 (==)
                        602     POP_JUMP_IF_FALSE               5 (to 614)
                        606     LOAD_CONST                      8: 'DummyManifest_for_'
                        608     LOAD_FAST                       2: secondary
                        610     FORMAT_SIMPLE
                        612     BUILD_STRING                    2
                        614     STORE_FAST                      5: manifest_val
                        616     LOAD_FAST                       0: self
                        618     LOAD_ATTR                       34: input_manifest
                        638     LOAD_ATTR                       25: setText
                        658     LOAD_FAST                       5: manifest_val
                        660     CALL                            1
                        668     POP_TOP
                        670     LOAD_FAST                       0: self
                        672     LOAD_ATTR                       37: log_console
                        692     LOAD_CONST                      9: 'Fields autofilled for secondary AppID '
                        694     LOAD_FAST                       2: secondary
                        696     FORMAT_SIMPLE
                        698     LOAD_CONST                      10: '.'
                        700     BUILD_STRING                    3
                        702     CALL                            1
                        710     POP_TOP
                        712     RETURN_CONST                    0: None
                        714     LOAD_GLOBAL                     12: QMessageBox
                        724     LOAD_ATTR                       14: warning
                        744     PUSH_NULL
                        746     LOAD_FAST                       0: self
                        748     LOAD_CONST                      11: 'Input Error'
                        750     LOAD_CONST                      12: 'Primary AppID must be numeric.'
                        752     CALL                            3
                        760     POP_TOP
                        762     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: update_preview
                    Qualified Name: LuaScriptMaker.update_preview
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 4
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'text_preview'
                        'clear'
                        'script_lines'
                        'append'
                    [Locals+Names]
                        'self'
                        'line'
                    [Constants]
                        None
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: text_preview
                        24      LOAD_ATTR                       3: clear
                        44      CALL                            0
                        52      POP_TOP
                        54      LOAD_FAST                       0: self
                        56      LOAD_ATTR                       4: script_lines
                        76      GET_ITER
                        78      FOR_ITER                        30 (to 140)
                        82      STORE_FAST                      1: line
                        84      LOAD_FAST                       0: self
                        86      LOAD_ATTR                       0: text_preview
                        106     LOAD_ATTR                       7: append
                        126     LOAD_FAST                       1: line
                        128     CALL                            1
                        136     POP_TOP
                        138     JUMP_BACKWARD                   32 (to 76)
                        142     END_FOR
                        144     POP_TOP
                        146     RETURN_CONST                    0: None
                'primary'
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: get_game_name_from_primary
                    Qualified Name: LuaScriptMaker.get_game_name_from_primary
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'get_library_folders'
                        'exists'
                        'parse_appmanifest'
                        'get'
                    [Locals+Names]
                        'self'
                        'primary'
                        'libraries'
                        'lib'
                        'acf_path'
                        'app_data'
                    [Constants]
                        None
                        'appmanifest_'
                        '.acf'
                        'name'
                        'unknown'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       1: get_library_folders
                        24      CALL                            0
                        32      STORE_FAST                      2: libraries
                        34      LOAD_FAST                       2: libraries
                        36      GET_ITER
                        38      FOR_ITER                        75 (to 190)
                        42      STORE_FAST                      3: lib
                        44      LOAD_FAST                       3: lib
                        46      LOAD_CONST                      1: 'appmanifest_'
                        48      LOAD_FAST                       1: primary
                        50      FORMAT_SIMPLE
                        52      LOAD_CONST                      2: '.acf'
                        54      BUILD_STRING                    3
                        56      BINARY_OP                       11 (/)
                        60      STORE_FAST                      4: acf_path
                        62      LOAD_FAST                       4: acf_path
                        64      LOAD_ATTR                       3: exists
                        84      CALL                            0
                        92      TO_BOOL
                        100     POP_JUMP_IF_TRUE                2 (to 106)
                        104     JUMP_BACKWARD                   35 (to 36)
                        108     LOAD_GLOBAL                     5: NULL + parse_appmanifest
                        118     LOAD_FAST                       4: acf_path
                        120     CALL                            1
                        128     STORE_FAST                      5: app_data
                        130     LOAD_FAST                       5: app_data
                        132     LOAD_ATTR                       7: get
                        152     LOAD_CONST                      3: 'name'
                        154     CALL                            1
                        162     TO_BOOL
                        170     POP_JUMP_IF_TRUE                2 (to 176)
                        174     JUMP_BACKWARD                   70 (to 36)
                        178     LOAD_FAST                       5: app_data
                        180     LOAD_CONST                      3: 'name'
                        182     BINARY_SUBSCR
                        186     SWAP                            2
                        188     POP_TOP
                        190     RETURN_VALUE
                        192     END_FOR
                        194     POP_TOP
                        196     RETURN_CONST                    4: 'unknown'
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: get_dkey
                    Qualified Name: LuaScriptMaker.get_dkey
                    Arg Count: 3
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 6
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'Path'
                        'exists'
                        'open'
                        'read'
                        're'
                        'search'
                        'DOTALL'
                        'group'
                        'Exception'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'config_filename'
                        'appid'
                        'path_obj'
                        'f'
                        'content'
                        'pattern'
                        'match'
                        'block'
                        'dkey_match'
                        'e'
                    [Constants]
                        None
                        'r'
                        'utf-8'
                        (
                            'encoding'
                        )
                        '"'
                        '"\\s*{([^}]*)}'
                        1
                        '"DecryptionKey"\\s+"([a-fA-F0-9]+)"'
                        'Error extracting DKey for AppID %s:'
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_GLOBAL                     1: NULL + Path
                        14      LOAD_FAST                       1: config_filename
                        16      CALL                            1
                        24      STORE_FAST                      3: path_obj
                        26      LOAD_FAST                       3: path_obj
                        28      LOAD_ATTR                       3: exists
                        48      CALL                            0
                        56      TO_BOOL
                        64      POP_JUMP_IF_TRUE                1 (to 68)
                        68      RETURN_CONST                    0: None
                        70      LOAD_FAST                       3: path_obj
                        72      LOAD_ATTR                       5: open
                        92      LOAD_CONST                      1: 'r'
                        94      LOAD_CONST                      2: 'utf-8'
                        96      LOAD_CONST                      3: ('encoding',)
                        98      CALL_KW                         2
                        100     BEFORE_WITH
                        102     STORE_FAST                      4: f
                        104     LOAD_FAST                       4: f
                        106     LOAD_ATTR                       7: read
                        126     CALL                            0
                        134     STORE_FAST                      5: content
                        136     LOAD_CONST                      0: None
                        138     LOAD_CONST                      0: None
                        140     LOAD_CONST                      0: None
                        142     CALL                            2
                        150     POP_TOP
                        152     LOAD_CONST                      4: '"'
                        154     LOAD_FAST                       2: appid
                        156     FORMAT_SIMPLE
                        158     LOAD_CONST                      5: '"\\s*{([^}]*)}'
                        160     BUILD_STRING                    3
                        162     STORE_FAST                      6: pattern
                        164     LOAD_GLOBAL                     8: re
                        174     LOAD_ATTR                       10: search
                        194     PUSH_NULL
                        196     LOAD_FAST                       6: pattern
                        198     LOAD_FAST_CHECK                 5: content
                        200     LOAD_GLOBAL                     8: re
                        210     LOAD_ATTR                       12: DOTALL
                        230     CALL                            3
                        238     STORE_FAST                      7: match
                        240     LOAD_FAST                       7: match
                        242     TO_BOOL
                        250     POP_JUMP_IF_FALSE               64 (to 380)
                        254     LOAD_FAST                       7: match
                        256     LOAD_ATTR                       15: group
                        276     LOAD_CONST                      6: 1
                        278     CALL                            1
                        286     STORE_FAST                      8: block
                        288     LOAD_GLOBAL                     8: re
                        298     LOAD_ATTR                       10: search
                        318     PUSH_NULL
                        320     LOAD_CONST                      7: '"DecryptionKey"\\s+"([a-fA-F0-9]+)"'
                        322     LOAD_FAST                       8: block
                        324     CALL                            2
                        332     STORE_FAST                      9: dkey_match
                        334     LOAD_FAST                       9: dkey_match
                        336     TO_BOOL
                        344     POP_JUMP_IF_FALSE               17 (to 380)
                        348     LOAD_FAST                       9: dkey_match
                        350     LOAD_ATTR                       15: group
                        370     LOAD_CONST                      6: 1
                        372     CALL                            1
                        380     RETURN_VALUE
                        382     RETURN_CONST                    0: None
                        384     PUSH_EXC_INFO
                        386     WITH_EXCEPT_START
                        388     TO_BOOL
                        396     POP_JUMP_IF_TRUE                1 (to 400)
                        400     RERAISE                         2
                        402     POP_TOP
                        404     POP_EXCEPT
                        406     POP_TOP
                        408     POP_TOP
                        410     JUMP_BACKWARD_NO_INTERRUPT      130 (to 152)
                        412     COPY                            3
                        414     POP_EXCEPT
                        416     RERAISE                         1
                        418     PUSH_EXC_INFO
                        420     LOAD_GLOBAL                     16: Exception
                        430     CHECK_EXC_MATCH
                        432     POP_JUMP_IF_FALSE               33 (to 500)
                        436     STORE_FAST                      10: e
                        438     LOAD_GLOBAL                     18: logging
                        448     LOAD_ATTR                       20: exception
                        468     PUSH_NULL
                        470     LOAD_CONST                      8: 'Error extracting DKey for AppID %s:'
                        472     LOAD_FAST                       2: appid
                        474     CALL                            2
                        482     POP_TOP
                        484     POP_EXCEPT
                        486     LOAD_CONST                      0: None
                        488     STORE_FAST                      10: e
                        490     DELETE_FAST                     10: e
                        492     RETURN_CONST                    0: None
                        494     LOAD_CONST                      0: None
                        496     STORE_FAST                      10: e
                        498     DELETE_FAST                     10: e
                        500     RERAISE                         1
                        502     RERAISE                         0
                        504     COPY                            3
                        506     POP_EXCEPT
                        508     RERAISE                         1
                'appid'
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: get_manifest_for_appid
                    Qualified Name: LuaScriptMaker.get_manifest_for_appid
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'get_manifest'
                        'get_library_folders'
                        'exists'
                        'get_manifest_from_acf'
                    [Locals+Names]
                        'self'
                        'appid'
                        'm'
                        'libraries'
                        'lib'
                        'acf_path'
                        'fallback'
                    [Constants]
                        None
                        'Unknown'
                        'appmanifest_'
                        '.acf'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       1: get_manifest
                        24      LOAD_FAST                       1: appid
                        26      CALL                            1
                        34      STORE_FAST                      2: m
                        36      LOAD_FAST                       2: m
                        38      LOAD_CONST                      1: 'Unknown'
                        40      COMPARE_OP                      88 (==)
                        44      POP_JUMP_IF_FALSE               79 (to 204)
                        48      LOAD_FAST                       0: self
                        50      LOAD_ATTR                       3: get_library_folders
                        70      CALL                            0
                        78      STORE_FAST                      3: libraries
                        80      LOAD_FAST                       3: libraries
                        82      GET_ITER
                        84      FOR_ITER                        56 (to 198)
                        88      STORE_FAST                      4: lib
                        90      LOAD_FAST                       4: lib
                        92      LOAD_CONST                      2: 'appmanifest_'
                        94      LOAD_FAST                       1: appid
                        96      FORMAT_SIMPLE
                        98      LOAD_CONST                      3: '.acf'
                        100     BUILD_STRING                    3
                        102     BINARY_OP                       11 (/)
                        106     STORE_FAST                      5: acf_path
                        108     LOAD_FAST                       5: acf_path
                        110     LOAD_ATTR                       5: exists
                        130     CALL                            0
                        138     TO_BOOL
                        146     POP_JUMP_IF_TRUE                2 (to 152)
                        150     JUMP_BACKWARD                   35 (to 82)
                        154     LOAD_GLOBAL                     7: NULL + get_manifest_from_acf
                        164     LOAD_FAST                       5: acf_path
                        166     CALL                            1
                        174     STORE_FAST                      6: fallback
                        176     LOAD_FAST                       6: fallback
                        178     LOAD_CONST                      1: 'Unknown'
                        180     COMPARE_OP                      119 (!=)
                        184     POP_JUMP_IF_TRUE                2 (to 190)
                        188     JUMP_BACKWARD                   54 (to 82)
                        192     LOAD_FAST                       6: fallback
                        194     SWAP                            2
                        196     POP_TOP
                        198     RETURN_VALUE
                        200     END_FOR
                        202     POP_TOP
                        204     RETURN_CONST                    1: 'Unknown'
                        206     LOAD_FAST                       2: m
                        208     RETURN_VALUE
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: get_manifest
                    Qualified Name: LuaScriptMaker.get_manifest
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 7
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'steam_dir'
                        'Path'
                        'exists'
                        'list'
                        'iterdir'
                        'name'
                        'startswith'
                        'endswith'
                        'sort'
                        're'
                        'match'
                        'group'
                        'Exception'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'appid'
                        'files'
                        'f'
                        'manifests'
                        'latest'
                        'match'
                        'e'
                        'depotcache'
                    [Constants]
                        None
                        'Unknown'
                        'depotcache'
                        '_'
                        '.manifest'
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: <lambda>
                            Qualified Name: LuaScriptMaker.get_manifest.<locals>.<lambda>
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 2
                            Flags: 0x00000013 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED)
                            [Names]
                                'stat'
                                'st_mtime'
                            [Locals+Names]
                                'x'
                                'depotcache'
                            [Constants]
                                None
                            [Disassembly]
                                0       COPY_FREE_VARS                  1
                                2       RESUME                          0
                                4       LOAD_DEREF                      1: depotcache
                                6       LOAD_FAST                       0: x
                                8       BINARY_OP                       11 (/)
                                12      LOAD_ATTR                       1: stat
                                32      CALL                            0
                                40      LOAD_ATTR                       2: st_mtime
                                60      RETURN_VALUE
                        True
                        (
                            'key'
                            'reverse'
                        )
                        0
                        '_(\\d+)\\.manifest'
                        1
                        'Error retrieving Manifest for AppID %s:'
                    [Disassembly]
                        0       MAKE_CELL                       8: depotcache
                        2       RESUME                          0
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       0: steam_dir
                        26      TO_BOOL
                        34      POP_JUMP_IF_TRUE                1 (to 38)
                        38      RETURN_CONST                    1: 'Unknown'
                        40      LOAD_GLOBAL                     3: NULL + Path
                        50      LOAD_FAST                       0: self
                        52      LOAD_ATTR                       0: steam_dir
                        72      CALL                            1
                        80      LOAD_CONST                      2: 'depotcache'
                        82      BINARY_OP                       11 (/)
                        86      STORE_DEREF                     8: depotcache
                        88      NOP
                        90      LOAD_DEREF                      8: depotcache
                        92      LOAD_ATTR                       5: exists
                        112     CALL                            0
                        120     TO_BOOL
                        128     POP_JUMP_IF_TRUE                1 (to 132)
                        132     RETURN_CONST                    1: 'Unknown'
                        134     LOAD_GLOBAL                     7: NULL + list
                        144     LOAD_DEREF                      8: depotcache
                        146     LOAD_ATTR                       9: iterdir
                        166     CALL                            0
                        174     CALL                            1
                        182     STORE_FAST                      2: files
                        184     LOAD_FAST                       2: files
                        186     GET_ITER
                        188     LOAD_FAST_AND_CLEAR             3: f
                        190     SWAP                            2
                        192     BUILD_LIST                      0
                        194     SWAP                            2
                        196     GET_ITER
                        198     FOR_ITER                        85 (to 370)
                        202     STORE_FAST_LOAD_FAST            51: f, f
                        204     LOAD_ATTR                       10: name
                        224     LOAD_ATTR                       13: startswith
                        244     LOAD_FAST                       1: appid
                        246     FORMAT_SIMPLE
                        248     LOAD_CONST                      3: '_'
                        250     BUILD_STRING                    2
                        252     CALL                            1
                        260     TO_BOOL
                        268     POP_JUMP_IF_TRUE                2 (to 274)
                        272     JUMP_BACKWARD                   39 (to 196)
                        276     LOAD_FAST                       3: f
                        278     LOAD_ATTR                       10: name
                        298     LOAD_ATTR                       15: endswith
                        318     LOAD_CONST                      4: '.manifest'
                        320     CALL                            1
                        328     TO_BOOL
                        336     POP_JUMP_IF_TRUE                2 (to 342)
                        340     JUMP_BACKWARD                   73 (to 196)
                        344     LOAD_FAST                       3: f
                        346     LOAD_ATTR                       10: name
                        366     LIST_APPEND                     2
                        368     JUMP_BACKWARD                   87 (to 196)
                        372     END_FOR
                        374     POP_TOP
                        376     STORE_FAST                      4: manifests
                        378     STORE_FAST                      3: f
                        380     LOAD_FAST                       4: manifests
                        382     TO_BOOL
                        390     POP_JUMP_IF_FALSE               76 (to 544)
                        394     LOAD_FAST                       4: manifests
                        396     LOAD_ATTR                       17: sort
                        416     LOAD_FAST                       8: depotcache
                        418     BUILD_TUPLE                     1
                        420     LOAD_CONST                      5: <CODE> <lambda>
                        422     MAKE_FUNCTION
                        424     SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        426     LOAD_CONST                      6: True
                        428     LOAD_CONST                      7: ('key', 'reverse')
                        430     CALL_KW                         2
                        432     POP_TOP
                        434     LOAD_FAST                       4: manifests
                        436     LOAD_CONST                      8: 0
                        438     BINARY_SUBSCR
                        442     STORE_FAST                      5: latest
                        444     LOAD_GLOBAL                     18: re
                        454     LOAD_ATTR                       20: match
                        474     PUSH_NULL
                        476     LOAD_FAST                       1: appid
                        478     FORMAT_SIMPLE
                        480     LOAD_CONST                      9: '_(\\d+)\\.manifest'
                        482     BUILD_STRING                    2
                        484     LOAD_FAST                       5: latest
                        486     CALL                            2
                        494     STORE_FAST                      6: match
                        496     LOAD_FAST                       6: match
                        498     TO_BOOL
                        506     POP_JUMP_IF_FALSE               17 (to 542)
                        510     LOAD_FAST                       6: match
                        512     LOAD_ATTR                       23: group
                        532     LOAD_CONST                      10: 1
                        534     CALL                            1
                        542     RETURN_VALUE
                        544     RETURN_CONST                    1: 'Unknown'
                        546     RETURN_CONST                    1: 'Unknown'
                        548     SWAP                            2
                        550     POP_TOP
                        552     SWAP                            2
                        554     STORE_FAST                      3: f
                        556     RERAISE                         0
                        558     PUSH_EXC_INFO
                        560     LOAD_GLOBAL                     24: Exception
                        570     CHECK_EXC_MATCH
                        572     POP_JUMP_IF_FALSE               33 (to 640)
                        576     STORE_FAST                      7: e
                        578     LOAD_GLOBAL                     26: logging
                        588     LOAD_ATTR                       28: exception
                        608     PUSH_NULL
                        610     LOAD_CONST                      11: 'Error retrieving Manifest for AppID %s:'
                        612     LOAD_FAST                       1: appid
                        614     CALL                            2
                        622     POP_TOP
                        624     POP_EXCEPT
                        626     LOAD_CONST                      0: None
                        628     STORE_FAST                      7: e
                        630     DELETE_FAST                     7: e
                        632     RETURN_CONST                    1: 'Unknown'
                        634     LOAD_CONST                      0: None
                        636     STORE_FAST                      7: e
                        638     DELETE_FAST                     7: e
                        640     RERAISE                         1
                        642     RERAISE                         0
                        644     COPY                            3
                        646     POP_EXCEPT
                        648     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: copy_manifest_files
                    Qualified Name: LuaScriptMaker.copy_manifest_files
                    Arg Count: 3
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'Path'
                        'steam_dir'
                        'exists'
                        'glob'
                        'shutil'
                        'copy'
                        'name'
                        'log_console'
                        'Exception'
                        'logging'
                        'warning'
                        'str'
                    [Locals+Names]
                        'self'
                        'target_folder'
                        'appid'
                        'depotcache'
                        'file'
                        'e'
                    [Constants]
                        None
                        'depotcache'
                        '_*.manifest'
                        'Copied manifest '
                        'Could not copy manifest %s: %s'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     1: NULL + Path
                        12      LOAD_FAST                       0: self
                        14      LOAD_ATTR                       2: steam_dir
                        34      CALL                            1
                        42      LOAD_CONST                      1: 'depotcache'
                        44      BINARY_OP                       11 (/)
                        48      STORE_FAST                      3: depotcache
                        50      LOAD_FAST                       3: depotcache
                        52      LOAD_ATTR                       5: exists
                        72      CALL                            0
                        80      TO_BOOL
                        88      POP_JUMP_IF_TRUE                1 (to 92)
                        92      RETURN_CONST                    0: None
                        94      LOAD_FAST                       3: depotcache
                        96      LOAD_ATTR                       7: glob
                        116     LOAD_FAST                       2: appid
                        118     FORMAT_SIMPLE
                        120     LOAD_CONST                      2: '_*.manifest'
                        122     BUILD_STRING                    2
                        124     CALL                            1
                        132     GET_ITER
                        134     FOR_ITER                        69 (to 274)
                        138     STORE_FAST                      4: file
                        140     NOP
                        142     LOAD_GLOBAL                     8: shutil
                        152     LOAD_ATTR                       10: copy
                        172     PUSH_NULL
                        174     LOAD_FAST_LOAD_FAST             65: file, target_folder
                        176     LOAD_FAST                       4: file
                        178     LOAD_ATTR                       12: name
                        198     BINARY_OP                       11 (/)
                        202     CALL                            2
                        210     POP_TOP
                        212     LOAD_FAST                       0: self
                        214     LOAD_ATTR                       15: log_console
                        234     LOAD_CONST                      3: 'Copied manifest '
                        236     LOAD_FAST                       4: file
                        238     LOAD_ATTR                       12: name
                        258     FORMAT_SIMPLE
                        260     BUILD_STRING                    2
                        262     CALL                            1
                        270     POP_TOP
                        272     JUMP_BACKWARD                   71 (to 132)
                        276     END_FOR
                        278     POP_TOP
                        280     RETURN_CONST                    0: None
                        282     PUSH_EXC_INFO
                        284     LOAD_GLOBAL                     16: Exception
                        294     CHECK_EXC_MATCH
                        296     POP_JUMP_IF_FALSE               54 (to 406)
                        300     STORE_FAST                      5: e
                        302     LOAD_GLOBAL                     18: logging
                        312     LOAD_ATTR                       20: warning
                        332     PUSH_NULL
                        334     LOAD_CONST                      4: 'Could not copy manifest %s: %s'
                        336     LOAD_FAST                       4: file
                        338     LOAD_ATTR                       12: name
                        358     LOAD_GLOBAL                     23: NULL + str
                        368     LOAD_FAST                       5: e
                        370     CALL                            1
                        378     CALL                            3
                        386     POP_TOP
                        388     POP_EXCEPT
                        390     LOAD_CONST                      0: None
                        392     STORE_FAST                      5: e
                        394     DELETE_FAST                     5: e
                        396     JUMP_BACKWARD                   133 (to 132)
                        400     LOAD_CONST                      0: None
                        402     STORE_FAST                      5: e
                        404     DELETE_FAST                     5: e
                        406     RERAISE                         1
                        408     RERAISE                         0
                        410     COPY                            3
                        412     POP_EXCEPT
                        414     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: copy_fallback_manifest
                    Qualified Name: LuaScriptMaker.copy_fallback_manifest
                    Arg Count: 3
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 10
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'get_library_folders'
                        'exists'
                        'get_manifest_from_acf'
                        'shutil'
                        'copy'
                        'log_console'
                        'Exception'
                        'str'
                    [Locals+Names]
                        'self'
                        'target_folder'
                        'appid'
                        'libraries'
                        'lib'
                        'acf_path'
                        'fallback_manifest_id'
                        'fallback_filename'
                        'e'
                    [Constants]
                        None
                        'appmanifest_'
                        '.acf'
                        'Unknown'
                        '_'
                        '.manifest'
                        'Copied fallback ACF as manifest '
                        ' for AppID '
                        'Fallback manifest copy failed for AppID '
                        ': '
                        'No fallback manifest available for AppID '
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       1: get_library_folders
                        24      CALL                            0
                        32      STORE_FAST                      3: libraries
                        34      LOAD_FAST                       3: libraries
                        36      GET_ITER
                        38      FOR_ITER                        111 (to 262)
                        42      STORE_FAST                      4: lib
                        44      LOAD_FAST                       4: lib
                        46      LOAD_CONST                      1: 'appmanifest_'
                        48      LOAD_FAST                       2: appid
                        50      FORMAT_SIMPLE
                        52      LOAD_CONST                      2: '.acf'
                        54      BUILD_STRING                    3
                        56      BINARY_OP                       11 (/)
                        60      STORE_FAST                      5: acf_path
                        62      LOAD_FAST                       5: acf_path
                        64      LOAD_ATTR                       3: exists
                        84      CALL                            0
                        92      TO_BOOL
                        100     POP_JUMP_IF_TRUE                2 (to 106)
                        104     JUMP_BACKWARD                   35 (to 36)
                        108     LOAD_GLOBAL                     5: NULL + get_manifest_from_acf
                        118     LOAD_FAST                       5: acf_path
                        120     CALL                            1
                        128     STORE_FAST                      6: fallback_manifest_id
                        130     LOAD_FAST                       6: fallback_manifest_id
                        132     LOAD_CONST                      3: 'Unknown'
                        134     COMPARE_OP                      119 (!=)
                        138     POP_JUMP_IF_TRUE                2 (to 144)
                        142     JUMP_BACKWARD                   54 (to 36)
                        146     LOAD_FAST                       2: appid
                        148     FORMAT_SIMPLE
                        150     LOAD_CONST                      4: '_'
                        152     LOAD_FAST                       6: fallback_manifest_id
                        154     FORMAT_SIMPLE
                        156     LOAD_CONST                      5: '.manifest'
                        158     BUILD_STRING                    4
                        160     STORE_FAST                      7: fallback_filename
                        162     NOP
                        164     LOAD_GLOBAL                     6: shutil
                        174     LOAD_ATTR                       8: copy
                        194     PUSH_NULL
                        196     LOAD_FAST_LOAD_FAST             81: acf_path, target_folder
                        198     LOAD_FAST                       7: fallback_filename
                        200     BINARY_OP                       11 (/)
                        204     CALL                            2
                        212     POP_TOP
                        214     LOAD_FAST                       0: self
                        216     LOAD_ATTR                       11: log_console
                        236     LOAD_CONST                      6: 'Copied fallback ACF as manifest '
                        238     LOAD_FAST                       7: fallback_filename
                        240     FORMAT_SIMPLE
                        242     LOAD_CONST                      7: ' for AppID '
                        244     LOAD_FAST                       2: appid
                        246     FORMAT_SIMPLE
                        248     BUILD_STRING                    4
                        250     CALL                            1
                        258     POP_TOP
                        260     POP_TOP
                        262     RETURN_CONST                    0: None
                        264     END_FOR
                        266     POP_TOP
                        268     LOAD_FAST                       0: self
                        270     LOAD_ATTR                       11: log_console
                        290     LOAD_CONST                      10: 'No fallback manifest available for AppID '
                        292     LOAD_FAST                       2: appid
                        294     FORMAT_SIMPLE
                        296     BUILD_STRING                    2
                        298     CALL                            1
                        306     POP_TOP
                        308     RETURN_CONST                    0: None
                        310     PUSH_EXC_INFO
                        312     LOAD_GLOBAL                     12: Exception
                        322     CHECK_EXC_MATCH
                        324     POP_JUMP_IF_FALSE               43 (to 412)
                        328     STORE_FAST                      8: e
                        330     LOAD_FAST                       0: self
                        332     LOAD_ATTR                       11: log_console
                        352     LOAD_CONST                      8: 'Fallback manifest copy failed for AppID '
                        354     LOAD_FAST                       2: appid
                        356     FORMAT_SIMPLE
                        358     LOAD_CONST                      9: ': '
                        360     LOAD_GLOBAL                     15: NULL + str
                        370     LOAD_FAST                       8: e
                        372     CALL                            1
                        380     FORMAT_SIMPLE
                        382     BUILD_STRING                    4
                        384     CALL                            1
                        392     POP_TOP
                        394     POP_EXCEPT
                        396     LOAD_CONST                      0: None
                        398     STORE_FAST                      8: e
                        400     DELETE_FAST                     8: e
                        402     JUMP_BACKWARD                   184 (to 36)
                        406     LOAD_CONST                      0: None
                        408     STORE_FAST                      8: e
                        410     DELETE_FAST                     8: e
                        412     RERAISE                         1
                        414     RERAISE                         0
                        416     COPY                            3
                        418     POP_EXCEPT
                        420     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: copy_bin_files
                    Qualified Name: LuaScriptMaker.copy_bin_files
                    Arg Count: 3
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'Path'
                        'steam_dir'
                        'exists'
                        'logging'
                        'warning'
                        'os'
                        'listdir'
                        'endswith'
                        're'
                        'match'
                        'shutil'
                        'copy'
                        'Exception'
                        'str'
                    [Locals+Names]
                        'self'
                        'target_folder'
                        'appid'
                        'stats'
                        'f'
                        'all_bins'
                        'pattern'
                        'bins'
                        'file'
                        'src'
                        'dest'
                        'e'
                    [Constants]
                        None
                        'appcache'
                        'stats'
                        'Stats folder not found.'
                        '.bin'
                        '.*_'
                        '(?:_\\d+)?\\.bin$'
                        'Could not copy %s: %s'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     1: NULL + Path
                        12      LOAD_FAST                       0: self
                        14      LOAD_ATTR                       2: steam_dir
                        34      CALL                            1
                        42      LOAD_CONST                      1: 'appcache'
                        44      BINARY_OP                       11 (/)
                        48      LOAD_CONST                      2: 'stats'
                        50      BINARY_OP                       11 (/)
                        54      STORE_FAST                      3: stats
                        56      LOAD_FAST                       3: stats
                        58      LOAD_ATTR                       5: exists
                        78      CALL                            0
                        86      TO_BOOL
                        94      POP_JUMP_IF_TRUE                23 (to 142)
                        98      LOAD_GLOBAL                     6: logging
                        108     LOAD_ATTR                       8: warning
                        128     PUSH_NULL
                        130     LOAD_CONST                      3: 'Stats folder not found.'
                        132     CALL                            1
                        140     POP_TOP
                        142     RETURN_CONST                    0: None
                        144     LOAD_GLOBAL                     10: os
                        154     LOAD_ATTR                       12: listdir
                        174     PUSH_NULL
                        176     LOAD_FAST                       3: stats
                        178     CALL                            1
                        186     GET_ITER
                        188     LOAD_FAST_AND_CLEAR             4: f
                        190     SWAP                            2
                        192     BUILD_LIST                      0
                        194     SWAP                            2
                        196     GET_ITER
                        198     FOR_ITER                        28 (to 256)
                        202     STORE_FAST_LOAD_FAST            68: f, f
                        204     LOAD_ATTR                       15: endswith
                        224     LOAD_CONST                      4: '.bin'
                        226     CALL                            1
                        234     TO_BOOL
                        242     POP_JUMP_IF_TRUE                2 (to 248)
                        246     JUMP_BACKWARD                   26 (to 196)
                        250     LOAD_FAST                       4: f
                        252     LIST_APPEND                     2
                        254     JUMP_BACKWARD                   30 (to 196)
                        258     END_FOR
                        260     POP_TOP
                        262     STORE_FAST                      5: all_bins
                        264     STORE_FAST                      4: f
                        266     LOAD_CONST                      5: '.*_'
                        268     LOAD_FAST                       2: appid
                        270     FORMAT_SIMPLE
                        272     LOAD_CONST                      6: '(?:_\\d+)?\\.bin$'
                        274     BUILD_STRING                    3
                        276     STORE_FAST                      6: pattern
                        278     LOAD_FAST                       5: all_bins
                        280     GET_ITER
                        282     LOAD_FAST_AND_CLEAR             4: f
                        284     SWAP                            2
                        286     BUILD_LIST                      0
                        288     SWAP                            2
                        290     GET_ITER
                        292     FOR_ITER                        34 (to 362)
                        296     STORE_FAST                      4: f
                        298     LOAD_GLOBAL                     16: re
                        308     LOAD_ATTR                       18: match
                        328     PUSH_NULL
                        330     LOAD_FAST_LOAD_FAST             100: pattern, f
                        332     CALL                            2
                        340     TO_BOOL
                        348     POP_JUMP_IF_TRUE                2 (to 354)
                        352     JUMP_BACKWARD                   32 (to 290)
                        356     LOAD_FAST                       4: f
                        358     LIST_APPEND                     2
                        360     JUMP_BACKWARD                   36 (to 290)
                        364     END_FOR
                        366     POP_TOP
                        368     STORE_FAST                      7: bins
                        370     STORE_FAST                      4: f
                        372     LOAD_FAST                       7: bins
                        374     GET_ITER
                        376     FOR_ITER                        67 (to 512)
                        380     STORE_FAST                      8: file
                        382     LOAD_GLOBAL                     1: NULL + Path
                        392     LOAD_FAST                       3: stats
                        394     CALL                            1
                        402     LOAD_FAST                       8: file
                        404     BINARY_OP                       11 (/)
                        408     STORE_FAST                      9: src
                        410     LOAD_FAST_LOAD_FAST             24: target_folder, file
                        412     BINARY_OP                       11 (/)
                        416     STORE_FAST                      10: dest
                        418     LOAD_FAST                       9: src
                        420     LOAD_ATTR                       5: exists
                        440     CALL                            0
                        448     TO_BOOL
                        456     POP_JUMP_IF_TRUE                2 (to 462)
                        460     JUMP_BACKWARD                   44 (to 374)
                        464     NOP
                        466     LOAD_GLOBAL                     20: shutil
                        476     LOAD_ATTR                       22: copy
                        496     PUSH_NULL
                        498     LOAD_FAST_LOAD_FAST             154: src, dest
                        500     CALL                            2
                        508     POP_TOP
                        510     JUMP_BACKWARD                   69 (to 374)
                        514     END_FOR
                        516     POP_TOP
                        518     RETURN_CONST                    0: None
                        520     SWAP                            2
                        522     POP_TOP
                        524     SWAP                            2
                        526     STORE_FAST                      4: f
                        528     RERAISE                         0
                        530     SWAP                            2
                        532     POP_TOP
                        534     SWAP                            2
                        536     STORE_FAST                      4: f
                        538     RERAISE                         0
                        540     PUSH_EXC_INFO
                        542     LOAD_GLOBAL                     24: Exception
                        552     CHECK_EXC_MATCH
                        554     POP_JUMP_IF_FALSE               44 (to 644)
                        558     STORE_FAST                      11: e
                        560     LOAD_GLOBAL                     6: logging
                        570     LOAD_ATTR                       8: warning
                        590     PUSH_NULL
                        592     LOAD_CONST                      7: 'Could not copy %s: %s'
                        594     LOAD_FAST                       8: file
                        596     LOAD_GLOBAL                     27: NULL + str
                        606     LOAD_FAST                       11: e
                        608     CALL                            1
                        616     CALL                            3
                        624     POP_TOP
                        626     POP_EXCEPT
                        628     LOAD_CONST                      0: None
                        630     STORE_FAST                      11: e
                        632     DELETE_FAST                     11: e
                        634     JUMP_BACKWARD                   131 (to 374)
                        638     LOAD_CONST                      0: None
                        640     STORE_FAST                      11: e
                        642     DELETE_FAST                     11: e
                        644     RERAISE                         1
                        646     RERAISE                         0
                        648     COPY                            3
                        650     POP_EXCEPT
                        652     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: copy_achievement_bin_files
                    Qualified Name: LuaScriptMaker.copy_achievement_bin_files
                    Arg Count: 3
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'Path'
                        'steam_dir'
                        'exists'
                        'logging'
                        'warning'
                        'os'
                        'listdir'
                        'endswith'
                        're'
                        'match'
                        'shutil'
                        'copy'
                        'log_console'
                        'Exception'
                        'str'
                    [Locals+Names]
                        'self'
                        'target_folder'
                        'appid'
                        'ach_folder'
                        'f'
                        'all_bins'
                        'pattern'
                        'bins'
                        'file'
                        'src'
                        'dest'
                        'e'
                    [Constants]
                        None
                        'appcache'
                        'achievements'
                        'Achievements folder not found.'
                        '.bin'
                        '.*_'
                        '(?:_\\d+)?\\.bin$'
                        'Copied achievement BIN file '
                        'Could not copy achievement BIN file %s: %s'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_GLOBAL                     1: NULL + Path
                        12      LOAD_FAST                       0: self
                        14      LOAD_ATTR                       2: steam_dir
                        34      CALL                            1
                        42      LOAD_CONST                      1: 'appcache'
                        44      BINARY_OP                       11 (/)
                        48      LOAD_CONST                      2: 'achievements'
                        50      BINARY_OP                       11 (/)
                        54      STORE_FAST                      3: ach_folder
                        56      LOAD_FAST                       3: ach_folder
                        58      LOAD_ATTR                       5: exists
                        78      CALL                            0
                        86      TO_BOOL
                        94      POP_JUMP_IF_TRUE                23 (to 142)
                        98      LOAD_GLOBAL                     6: logging
                        108     LOAD_ATTR                       8: warning
                        128     PUSH_NULL
                        130     LOAD_CONST                      3: 'Achievements folder not found.'
                        132     CALL                            1
                        140     POP_TOP
                        142     RETURN_CONST                    0: None
                        144     LOAD_GLOBAL                     10: os
                        154     LOAD_ATTR                       12: listdir
                        174     PUSH_NULL
                        176     LOAD_FAST                       3: ach_folder
                        178     CALL                            1
                        186     GET_ITER
                        188     LOAD_FAST_AND_CLEAR             4: f
                        190     SWAP                            2
                        192     BUILD_LIST                      0
                        194     SWAP                            2
                        196     GET_ITER
                        198     FOR_ITER                        28 (to 256)
                        202     STORE_FAST_LOAD_FAST            68: f, f
                        204     LOAD_ATTR                       15: endswith
                        224     LOAD_CONST                      4: '.bin'
                        226     CALL                            1
                        234     TO_BOOL
                        242     POP_JUMP_IF_TRUE                2 (to 248)
                        246     JUMP_BACKWARD                   26 (to 196)
                        250     LOAD_FAST                       4: f
                        252     LIST_APPEND                     2
                        254     JUMP_BACKWARD                   30 (to 196)
                        258     END_FOR
                        260     POP_TOP
                        262     STORE_FAST                      5: all_bins
                        264     STORE_FAST                      4: f
                        266     LOAD_CONST                      5: '.*_'
                        268     LOAD_FAST                       2: appid
                        270     FORMAT_SIMPLE
                        272     LOAD_CONST                      6: '(?:_\\d+)?\\.bin$'
                        274     BUILD_STRING                    3
                        276     STORE_FAST                      6: pattern
                        278     LOAD_FAST                       5: all_bins
                        280     GET_ITER
                        282     LOAD_FAST_AND_CLEAR             4: f
                        284     SWAP                            2
                        286     BUILD_LIST                      0
                        288     SWAP                            2
                        290     GET_ITER
                        292     FOR_ITER                        34 (to 362)
                        296     STORE_FAST                      4: f
                        298     LOAD_GLOBAL                     16: re
                        308     LOAD_ATTR                       18: match
                        328     PUSH_NULL
                        330     LOAD_FAST_LOAD_FAST             100: pattern, f
                        332     CALL                            2
                        340     TO_BOOL
                        348     POP_JUMP_IF_TRUE                2 (to 354)
                        352     JUMP_BACKWARD                   32 (to 290)
                        356     LOAD_FAST                       4: f
                        358     LIST_APPEND                     2
                        360     JUMP_BACKWARD                   36 (to 290)
                        364     END_FOR
                        366     POP_TOP
                        368     STORE_FAST                      7: bins
                        370     STORE_FAST                      4: f
                        372     LOAD_FAST                       7: bins
                        374     GET_ITER
                        376     FOR_ITER                        77 (to 532)
                        380     STORE_FAST                      8: file
                        382     LOAD_FAST_LOAD_FAST             56: ach_folder, file
                        384     BINARY_OP                       11 (/)
                        388     STORE_FAST                      9: src
                        390     LOAD_FAST_LOAD_FAST             24: target_folder, file
                        392     BINARY_OP                       11 (/)
                        396     STORE_FAST                      10: dest
                        398     LOAD_FAST                       9: src
                        400     LOAD_ATTR                       5: exists
                        420     CALL                            0
                        428     TO_BOOL
                        436     POP_JUMP_IF_TRUE                2 (to 442)
                        440     JUMP_BACKWARD                   34 (to 374)
                        444     NOP
                        446     LOAD_GLOBAL                     20: shutil
                        456     LOAD_ATTR                       22: copy
                        476     PUSH_NULL
                        478     LOAD_FAST_LOAD_FAST             154: src, dest
                        480     CALL                            2
                        488     POP_TOP
                        490     LOAD_FAST                       0: self
                        492     LOAD_ATTR                       25: log_console
                        512     LOAD_CONST                      7: 'Copied achievement BIN file '
                        514     LOAD_FAST                       8: file
                        516     FORMAT_SIMPLE
                        518     BUILD_STRING                    2
                        520     CALL                            1
                        528     POP_TOP
                        530     JUMP_BACKWARD                   79 (to 374)
                        534     END_FOR
                        536     POP_TOP
                        538     RETURN_CONST                    0: None
                        540     SWAP                            2
                        542     POP_TOP
                        544     SWAP                            2
                        546     STORE_FAST                      4: f
                        548     RERAISE                         0
                        550     SWAP                            2
                        552     POP_TOP
                        554     SWAP                            2
                        556     STORE_FAST                      4: f
                        558     RERAISE                         0
                        560     PUSH_EXC_INFO
                        562     LOAD_GLOBAL                     26: Exception
                        572     CHECK_EXC_MATCH
                        574     POP_JUMP_IF_FALSE               44 (to 664)
                        578     STORE_FAST                      11: e
                        580     LOAD_GLOBAL                     6: logging
                        590     LOAD_ATTR                       8: warning
                        610     PUSH_NULL
                        612     LOAD_CONST                      8: 'Could not copy achievement BIN file %s: %s'
                        614     LOAD_FAST                       8: file
                        616     LOAD_GLOBAL                     29: NULL + str
                        626     LOAD_FAST                       11: e
                        628     CALL                            1
                        636     CALL                            3
                        644     POP_TOP
                        646     POP_EXCEPT
                        648     LOAD_CONST                      0: None
                        650     STORE_FAST                      11: e
                        652     DELETE_FAST                     11: e
                        654     JUMP_BACKWARD                   141 (to 374)
                        658     LOAD_CONST                      0: None
                        660     STORE_FAST                      11: e
                        662     DELETE_FAST                     11: e
                        664     RERAISE                         1
                        666     RERAISE                         0
                        668     COPY                            3
                        670     POP_EXCEPT
                        672     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: create_zip_archive
                    Qualified Name: LuaScriptMaker.create_zip_archive
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'with_suffix'
                        'zipfile'
                        'ZipFile'
                        'ZIP_DEFLATED'
                        'os'
                        'walk'
                        'path'
                        'join'
                        'relpath'
                        'write'
                        'Exception'
                        'QMessageBox'
                        'warning'
                        'str'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'folder'
                        'zip_filename'
                        'zipf'
                        'root'
                        'dirs'
                        'files'
                        'file'
                        'file_path'
                        'arcname'
                        'e'
                    [Constants]
                        None
                        '.zip'
                        'w'
                        (
                            'start'
                        )
                        'Zip Error'
                        'Error creating zip archive: '
                        'Zip archive error:'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       1: folder
                        4       LOAD_ATTR                       1: with_suffix
                        24      LOAD_CONST                      1: '.zip'
                        26      CALL                            1
                        34      STORE_FAST                      2: zip_filename
                        36      NOP
                        38      LOAD_GLOBAL                     2: zipfile
                        48      LOAD_ATTR                       4: ZipFile
                        68      PUSH_NULL
                        70      LOAD_FAST                       2: zip_filename
                        72      LOAD_CONST                      2: 'w'
                        74      LOAD_GLOBAL                     2: zipfile
                        84      LOAD_ATTR                       6: ZIP_DEFLATED
                        104     CALL                            3
                        112     BEFORE_WITH
                        114     STORE_FAST                      3: zipf
                        116     LOAD_GLOBAL                     8: os
                        126     LOAD_ATTR                       10: walk
                        146     PUSH_NULL
                        148     LOAD_FAST                       1: folder
                        150     CALL                            1
                        158     GET_ITER
                        160     FOR_ITER                        92 (to 346)
                        164     UNPACK_SEQUENCE                 3
                        168     STORE_FAST_STORE_FAST           69: root, dirs
                        170     STORE_FAST                      6: files
                        172     LOAD_FAST                       6: files
                        174     GET_ITER
                        176     FOR_ITER                        80 (to 338)
                        180     STORE_FAST                      7: file
                        182     LOAD_GLOBAL                     8: os
                        192     LOAD_ATTR                       12: path
                        212     LOAD_ATTR                       15: join
                        232     LOAD_FAST_LOAD_FAST             71: root, file
                        234     CALL                            2
                        242     STORE_FAST                      8: file_path
                        244     LOAD_GLOBAL                     8: os
                        254     LOAD_ATTR                       12: path
                        274     LOAD_ATTR                       17: relpath
                        294     LOAD_FAST_LOAD_FAST             129: file_path, folder
                        296     LOAD_CONST                      3: ('start',)
                        298     CALL_KW                         2
                        300     STORE_FAST                      9: arcname
                        302     LOAD_FAST                       3: zipf
                        304     LOAD_ATTR                       19: write
                        324     LOAD_FAST_LOAD_FAST             137: file_path, arcname
                        326     CALL                            2
                        334     POP_TOP
                        336     JUMP_BACKWARD                   82 (to 174)
                        340     END_FOR
                        342     POP_TOP
                        344     JUMP_BACKWARD                   94 (to 158)
                        348     END_FOR
                        350     POP_TOP
                        352     LOAD_CONST                      0: None
                        354     LOAD_CONST                      0: None
                        356     LOAD_CONST                      0: None
                        358     CALL                            2
                        366     POP_TOP
                        368     LOAD_FAST                       2: zip_filename
                        370     RETURN_VALUE
                        372     PUSH_EXC_INFO
                        374     WITH_EXCEPT_START
                        376     TO_BOOL
                        384     POP_JUMP_IF_TRUE                1 (to 388)
                        388     RERAISE                         2
                        390     POP_TOP
                        392     POP_EXCEPT
                        394     POP_TOP
                        396     POP_TOP
                        398     LOAD_FAST                       2: zip_filename
                        400     RETURN_VALUE
                        402     COPY                            3
                        404     POP_EXCEPT
                        406     RERAISE                         1
                        408     PUSH_EXC_INFO
                        410     LOAD_GLOBAL                     20: Exception
                        420     CHECK_EXC_MATCH
                        422     POP_JUMP_IF_FALSE               68 (to 560)
                        426     STORE_FAST                      10: e
                        428     LOAD_GLOBAL                     22: QMessageBox
                        438     LOAD_ATTR                       24: warning
                        458     PUSH_NULL
                        460     LOAD_FAST                       0: self
                        462     LOAD_CONST                      4: 'Zip Error'
                        464     LOAD_CONST                      5: 'Error creating zip archive: '
                        466     LOAD_GLOBAL                     27: NULL + str
                        476     LOAD_FAST                       10: e
                        478     CALL                            1
                        486     FORMAT_SIMPLE
                        488     BUILD_STRING                    2
                        490     CALL                            3
                        498     POP_TOP
                        500     LOAD_GLOBAL                     28: logging
                        510     LOAD_ATTR                       30: exception
                        530     PUSH_NULL
                        532     LOAD_CONST                      6: 'Zip archive error:'
                        534     CALL                            1
                        542     POP_TOP
                        544     POP_EXCEPT
                        546     LOAD_CONST                      0: None
                        548     STORE_FAST                      10: e
                        550     DELETE_FAST                     10: e
                        552     RETURN_CONST                    0: None
                        554     LOAD_CONST                      0: None
                        556     STORE_FAST                      10: e
                        558     DELETE_FAST                     10: e
                        560     RERAISE                         1
                        562     RERAISE                         0
                        564     COPY                            3
                        566     POP_EXCEPT
                        568     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: process_dlc_ids
                    Qualified Name: LuaScriptMaker.process_dlc_ids
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 8
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'steam_dir'
                        'dlc_ids'
                        'Path'
                        'str'
                        'added_ids'
                        'get_dkey'
                        'get_manifest_for_appid'
                        'script_lines'
                        'append'
                        'add'
                        'input_dlc'
                        'setText'
                        'join'
                    [Locals+Names]
                        'self'
                        'config_path'
                        'dlc'
                        'depot_id'
                        'dkey_val'
                        'manifest_val'
                    [Constants]
                        None
                        'config'
                        'config.vdf'
                        'Unknown'
                        'addappid('
                        ', 1, "'
                        '")'
                        'setManifestid('
                        ', "'
                        '", 0)'
                        ')'
                        ', '
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: <genexpr>
                            Qualified Name: LuaScriptMaker.process_dlc_ids.<locals>.<genexpr>
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 4
                            Flags: 0x00000033 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED | CO_GENERATOR)
                            [Names]
                                'str'
                            [Locals+Names]
                                '.0'
                                'x'
                            [Constants]
                                None
                            [Disassembly]
                                0       RETURN_GENERATOR
                                2       POP_TOP
                                4       RESUME                          0
                                6       LOAD_FAST                       0: .0
                                8       GET_ITER
                                10      FOR_ITER                        16 (to 44)
                                14      STORE_FAST                      1: x
                                16      LOAD_GLOBAL                     1: NULL + str
                                26      LOAD_FAST                       1: x
                                28      CALL                            1
                                36      YIELD_VALUE                     0
                                38      RESUME                          5
                                40      POP_TOP
                                42      JUMP_BACKWARD                   18 (to 8)
                                46      END_FOR
                                48      POP_TOP
                                50      RETURN_CONST                    0: None
                                52      CALL_INTRINSIC_1                3 (INTRINSIC_STOPITERATION_ERROR)
                                54      RERAISE                         1
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: steam_dir
                        24      TO_BOOL
                        32      POP_JUMP_IF_FALSE               17 (to 68)
                        36      LOAD_FAST                       0: self
                        38      LOAD_ATTR                       2: dlc_ids
                        58      TO_BOOL
                        66      POP_JUMP_IF_TRUE                1 (to 70)
                        70      RETURN_CONST                    0: None
                        72      LOAD_GLOBAL                     5: NULL + Path
                        82      LOAD_FAST                       0: self
                        84      LOAD_ATTR                       0: steam_dir
                        104     CALL                            1
                        112     LOAD_CONST                      1: 'config'
                        114     BINARY_OP                       11 (/)
                        118     LOAD_CONST                      2: 'config.vdf'
                        120     BINARY_OP                       11 (/)
                        124     STORE_FAST                      1: config_path
                        126     LOAD_FAST                       0: self
                        128     LOAD_ATTR                       2: dlc_ids
                        148     GET_ITER
                        150     FOR_ITER                        222 (to 596)
                        154     STORE_FAST                      2: dlc
                        156     LOAD_GLOBAL                     7: NULL + str
                        166     LOAD_FAST                       2: dlc
                        168     CALL                            1
                        176     STORE_FAST                      3: depot_id
                        178     LOAD_FAST_LOAD_FAST             48: depot_id, self
                        180     LOAD_ATTR                       8: added_ids
                        200     CONTAINS_OP                     0 (in)
                        204     POP_JUMP_IF_FALSE               2 (to 210)
                        208     JUMP_BACKWARD                   31 (to 148)
                        212     LOAD_FAST                       0: self
                        214     LOAD_ATTR                       11: get_dkey
                        234     LOAD_GLOBAL                     7: NULL + str
                        244     LOAD_FAST                       1: config_path
                        246     CALL                            1
                        254     LOAD_FAST                       3: depot_id
                        256     CALL                            2
                        264     STORE_FAST                      4: dkey_val
                        266     LOAD_FAST                       0: self
                        268     LOAD_ATTR                       13: get_manifest_for_appid
                        288     LOAD_FAST                       3: depot_id
                        290     CALL                            1
                        298     STORE_FAST                      5: manifest_val
                        300     LOAD_FAST                       4: dkey_val
                        302     TO_BOOL
                        310     POP_JUMP_IF_FALSE               82 (to 476)
                        314     LOAD_FAST                       5: manifest_val
                        316     TO_BOOL
                        324     POP_JUMP_IF_FALSE               75 (to 476)
                        328     LOAD_FAST                       5: manifest_val
                        330     LOAD_CONST                      3: 'Unknown'
                        332     COMPARE_OP                      119 (!=)
                        336     POP_JUMP_IF_FALSE               69 (to 476)
                        340     LOAD_FAST                       0: self
                        342     LOAD_ATTR                       14: script_lines
                        362     LOAD_ATTR                       17: append
                        382     LOAD_CONST                      4: 'addappid('
                        384     LOAD_FAST                       3: depot_id
                        386     FORMAT_SIMPLE
                        388     LOAD_CONST                      5: ', 1, "'
                        390     LOAD_FAST                       4: dkey_val
                        392     FORMAT_SIMPLE
                        394     LOAD_CONST                      6: '")'
                        396     BUILD_STRING                    5
                        398     CALL                            1
                        406     POP_TOP
                        408     LOAD_FAST                       0: self
                        410     LOAD_ATTR                       14: script_lines
                        430     LOAD_ATTR                       17: append
                        450     LOAD_CONST                      7: 'setManifestid('
                        452     LOAD_FAST                       3: depot_id
                        454     FORMAT_SIMPLE
                        456     LOAD_CONST                      8: ', "'
                        458     LOAD_FAST                       5: manifest_val
                        460     FORMAT_SIMPLE
                        462     LOAD_CONST                      9: '", 0)'
                        464     BUILD_STRING                    5
                        466     CALL                            1
                        474     POP_TOP
                        476     JUMP_FORWARD                    31 (to 540)
                        478     LOAD_FAST                       0: self
                        480     LOAD_ATTR                       14: script_lines
                        500     LOAD_ATTR                       17: append
                        520     LOAD_CONST                      4: 'addappid('
                        522     LOAD_FAST                       3: depot_id
                        524     FORMAT_SIMPLE
                        526     LOAD_CONST                      10: ')'
                        528     BUILD_STRING                    3
                        530     CALL                            1
                        538     POP_TOP
                        540     LOAD_FAST                       0: self
                        542     LOAD_ATTR                       8: added_ids
                        562     LOAD_ATTR                       19: add
                        582     LOAD_FAST                       3: depot_id
                        584     CALL                            1
                        592     POP_TOP
                        594     JUMP_BACKWARD                   224 (to 148)
                        598     END_FOR
                        600     POP_TOP
                        602     LOAD_FAST                       0: self
                        604     LOAD_ATTR                       20: input_dlc
                        624     LOAD_ATTR                       23: setText
                        644     LOAD_CONST                      11: ', '
                        646     LOAD_ATTR                       25: join
                        666     LOAD_CONST                      12: <CODE> <genexpr>
                        668     MAKE_FUNCTION
                        670     LOAD_FAST                       0: self
                        672     LOAD_ATTR                       2: dlc_ids
                        692     GET_ITER
                        694     CALL                            0
                        702     CALL                            1
                        710     CALL                            1
                        718     POP_TOP
                        720     RETURN_CONST                    0: None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: fetch_dlc_ids
                    Qualified Name: LuaScriptMaker.fetch_dlc_ids
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'requests'
                        'get'
                        'json'
                        'str'
                        'dlc_ids'
                        'Exception'
                        'QMessageBox'
                        'warning'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'primary'
                        'url'
                        'response'
                        'data'
                        'app_data'
                        'e'
                    [Constants]
                        None
                        'https://store.steampowered.com/api/appdetails?appids='
                        '&cc=us&l=en'
                        'success'
                        'data'
                        'dlc'
                        'DLC Error'
                        'Error fetching DLC IDs: '
                        'Error fetching DLC IDs:'
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_CONST                      1: 'https://store.steampowered.com/api/appdetails?appids='
                        6       LOAD_FAST                       1: primary
                        8       FORMAT_SIMPLE
                        10      LOAD_CONST                      2: '&cc=us&l=en'
                        12      BUILD_STRING                    3
                        14      STORE_FAST                      2: url
                        16      LOAD_GLOBAL                     0: requests
                        26      LOAD_ATTR                       2: get
                        46      PUSH_NULL
                        48      LOAD_FAST                       2: url
                        50      CALL                            1
                        58      STORE_FAST                      3: response
                        60      LOAD_FAST                       3: response
                        62      LOAD_ATTR                       5: json
                        82      CALL                            0
                        90      STORE_FAST                      4: data
                        92      LOAD_GLOBAL                     7: NULL + str
                        102     LOAD_FAST                       1: primary
                        104     CALL                            1
                        112     LOAD_FAST                       4: data
                        114     CONTAINS_OP                     0 (in)
                        118     POP_JUMP_IF_FALSE               63 (to 246)
                        122     LOAD_FAST                       4: data
                        124     LOAD_GLOBAL                     7: NULL + str
                        134     LOAD_FAST                       1: primary
                        136     CALL                            1
                        144     BINARY_SUBSCR
                        148     LOAD_CONST                      3: 'success'
                        150     BINARY_SUBSCR
                        154     TO_BOOL
                        162     POP_JUMP_IF_FALSE               41 (to 246)
                        166     LOAD_FAST                       4: data
                        168     LOAD_GLOBAL                     7: NULL + str
                        178     LOAD_FAST                       1: primary
                        180     CALL                            1
                        188     BINARY_SUBSCR
                        192     LOAD_CONST                      4: 'data'
                        194     BINARY_SUBSCR
                        198     STORE_FAST                      5: app_data
                        200     LOAD_FAST                       5: app_data
                        202     LOAD_ATTR                       3: get
                        222     LOAD_CONST                      5: 'dlc'
                        224     BUILD_LIST                      0
                        226     CALL                            2
                        234     LOAD_FAST                       0: self
                        236     STORE_ATTR                      4: dlc_ids
                        246     RETURN_CONST                    0: None
                        248     BUILD_LIST                      0
                        250     LOAD_FAST                       0: self
                        252     STORE_ATTR                      4: dlc_ids
                        262     RETURN_CONST                    0: None
                        264     PUSH_EXC_INFO
                        266     LOAD_GLOBAL                     10: Exception
                        276     CHECK_EXC_MATCH
                        278     POP_JUMP_IF_FALSE               75 (to 430)
                        282     STORE_FAST                      6: e
                        284     LOAD_GLOBAL                     12: QMessageBox
                        294     LOAD_ATTR                       14: warning
                        314     PUSH_NULL
                        316     LOAD_FAST                       0: self
                        318     LOAD_CONST                      6: 'DLC Error'
                        320     LOAD_CONST                      7: 'Error fetching DLC IDs: '
                        322     LOAD_GLOBAL                     7: NULL + str
                        332     LOAD_FAST                       6: e
                        334     CALL                            1
                        342     FORMAT_SIMPLE
                        344     BUILD_STRING                    2
                        346     CALL                            3
                        354     POP_TOP
                        356     LOAD_GLOBAL                     16: logging
                        366     LOAD_ATTR                       18: exception
                        386     PUSH_NULL
                        388     LOAD_CONST                      8: 'Error fetching DLC IDs:'
                        390     CALL                            1
                        398     POP_TOP
                        400     BUILD_LIST                      0
                        402     LOAD_FAST                       0: self
                        404     STORE_ATTR                      4: dlc_ids
                        414     POP_EXCEPT
                        416     LOAD_CONST                      0: None
                        418     STORE_FAST                      6: e
                        420     DELETE_FAST                     6: e
                        422     RETURN_CONST                    0: None
                        424     LOAD_CONST                      0: None
                        426     STORE_FAST                      6: e
                        428     DELETE_FAST                     6: e
                        430     RERAISE                         1
                        432     RERAISE                         0
                        434     COPY                            3
                        436     POP_EXCEPT
                        438     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: fetch_depot_ids_from_steamdb
                    Qualified Name: LuaScriptMaker.fetch_depot_ids_from_steamdb
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 5
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'requests'
                        'get'
                        'text'
                        're'
                        'findall'
                        'list'
                        'set'
                        'remove'
                        'Exception'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'appid'
                        'url'
                        'response'
                        'html'
                        'depot_ids'
                        'e'
                    [Constants]
                        None
                        'https://steamdb.info/app/'
                        '/'
                        '/depot/(\\d+)'
                        'Error fetching depot IDs from SteamDB for AppID %s:'
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_CONST                      1: 'https://steamdb.info/app/'
                        6       LOAD_FAST                       1: appid
                        8       FORMAT_SIMPLE
                        10      LOAD_CONST                      2: '/'
                        12      BUILD_STRING                    3
                        14      STORE_FAST                      2: url
                        16      LOAD_GLOBAL                     0: requests
                        26      LOAD_ATTR                       2: get
                        46      PUSH_NULL
                        48      LOAD_FAST                       2: url
                        50      CALL                            1
                        58      STORE_FAST                      3: response
                        60      LOAD_FAST                       3: response
                        62      LOAD_ATTR                       4: text
                        82      STORE_FAST                      4: html
                        84      LOAD_GLOBAL                     6: re
                        94      LOAD_ATTR                       8: findall
                        114     PUSH_NULL
                        116     LOAD_CONST                      3: '/depot/(\\d+)'
                        118     LOAD_FAST                       4: html
                        120     CALL                            2
                        128     STORE_FAST                      5: depot_ids
                        130     LOAD_GLOBAL                     11: NULL + list
                        140     LOAD_GLOBAL                     13: NULL + set
                        150     LOAD_FAST                       5: depot_ids
                        152     CALL                            1
                        160     CALL                            1
                        168     STORE_FAST                      5: depot_ids
                        170     LOAD_FAST_LOAD_FAST             21: appid, depot_ids
                        172     CONTAINS_OP                     0 (in)
                        176     POP_JUMP_IF_FALSE               17 (to 212)
                        180     LOAD_FAST                       5: depot_ids
                        182     LOAD_ATTR                       15: remove
                        202     LOAD_FAST                       1: appid
                        204     CALL                            1
                        212     POP_TOP
                        214     LOAD_FAST                       5: depot_ids
                        216     RETURN_VALUE
                        218     PUSH_EXC_INFO
                        220     LOAD_GLOBAL                     16: Exception
                        230     CHECK_EXC_MATCH
                        232     POP_JUMP_IF_FALSE               35 (to 304)
                        236     STORE_FAST                      6: e
                        238     LOAD_GLOBAL                     18: logging
                        248     LOAD_ATTR                       20: exception
                        268     PUSH_NULL
                        270     LOAD_CONST                      4: 'Error fetching depot IDs from SteamDB for AppID %s:'
                        272     LOAD_FAST                       1: appid
                        274     CALL                            2
                        282     POP_TOP
                        284     BUILD_LIST                      0
                        286     SWAP                            2
                        288     POP_EXCEPT
                        290     LOAD_CONST                      0: None
                        292     STORE_FAST                      6: e
                        294     DELETE_FAST                     6: e
                        296     RETURN_VALUE
                        298     LOAD_CONST                      0: None
                        300     STORE_FAST                      6: e
                        302     DELETE_FAST                     6: e
                        304     RERAISE                         1
                        306     RERAISE                         0
                        308     COPY                            3
                        310     POP_EXCEPT
                        312     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: process_primary_appid
                    Qualified Name: LuaScriptMaker.process_primary_appid
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 8
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'script_lines'
                        'clear'
                        'added_ids'
                        'text_preview'
                        'input_primary'
                        'text'
                        'strip'
                        'append'
                        'add'
                        'isdigit'
                        'int'
                        'Path'
                        'steam_dir'
                        'range'
                        'str'
                        'get_dkey'
                        'get_manifest_for_appid'
                        'fetch_dlc_ids'
                        'dlc_ids'
                        'fetch_depot_ids_from_steamdb'
                        'process_dlc_ids'
                        'QMessageBox'
                        'warning'
                    [Locals+Names]
                        'self'
                        'primary'
                        'base_val'
                        'config_path'
                        'offset'
                        'candidate'
                        'dkey_val'
                        'manifest_val'
                        'depot_ids'
                        'depot'
                    [Constants]
                        None
                        'addappid('
                        ')'
                        'config'
                        'config.vdf'
                        1
                        10
                        'Unknown'
                        ', 1, "'
                        '")'
                        'setManifestid('
                        ', "'
                        '", 0)'
                        'Input Error'
                        'Primary AppID must be numeric.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: script_lines
                        24      LOAD_ATTR                       3: clear
                        44      CALL                            0
                        52      POP_TOP
                        54      LOAD_FAST                       0: self
                        56      LOAD_ATTR                       4: added_ids
                        76      LOAD_ATTR                       3: clear
                        96      CALL                            0
                        104     POP_TOP
                        106     LOAD_FAST                       0: self
                        108     LOAD_ATTR                       6: text_preview
                        128     LOAD_ATTR                       3: clear
                        148     CALL                            0
                        156     POP_TOP
                        158     LOAD_FAST                       0: self
                        160     LOAD_ATTR                       8: input_primary
                        180     LOAD_ATTR                       11: text
                        200     CALL                            0
                        208     LOAD_ATTR                       13: strip
                        228     CALL                            0
                        236     STORE_FAST                      1: primary
                        238     LOAD_FAST                       1: primary
                        240     TO_BOOL
                        248     POP_JUMP_IF_FALSE               73 (to 396)
                        252     LOAD_FAST_LOAD_FAST             16: primary, self
                        254     LOAD_ATTR                       4: added_ids
                        274     CONTAINS_OP                     1 (not in)
                        278     POP_JUMP_IF_FALSE               58 (to 396)
                        282     LOAD_FAST                       0: self
                        284     LOAD_ATTR                       0: script_lines
                        304     LOAD_ATTR                       15: append
                        324     LOAD_CONST                      1: 'addappid('
                        326     LOAD_FAST                       1: primary
                        328     FORMAT_SIMPLE
                        330     LOAD_CONST                      2: ')'
                        332     BUILD_STRING                    3
                        334     CALL                            1
                        342     POP_TOP
                        344     LOAD_FAST                       0: self
                        346     LOAD_ATTR                       4: added_ids
                        366     LOAD_ATTR                       17: add
                        386     LOAD_FAST                       1: primary
                        388     CALL                            1
                        396     POP_TOP
                        398     LOAD_FAST                       1: primary
                        400     LOAD_ATTR                       19: isdigit
                        420     CALL                            0
                        428     TO_BOOL
                        436     POP_JUMP_IF_FALSE               538 (to 1516)
                        442     LOAD_GLOBAL                     21: NULL + int
                        452     LOAD_FAST                       1: primary
                        454     CALL                            1
                        462     STORE_FAST                      2: base_val
                        464     LOAD_GLOBAL                     23: NULL + Path
                        474     LOAD_FAST                       0: self
                        476     LOAD_ATTR                       24: steam_dir
                        496     CALL                            1
                        504     LOAD_CONST                      3: 'config'
                        506     BINARY_OP                       11 (/)
                        510     LOAD_CONST                      4: 'config.vdf'
                        512     BINARY_OP                       11 (/)
                        516     STORE_FAST                      3: config_path
                        518     LOAD_GLOBAL                     27: NULL + range
                        528     LOAD_CONST                      5: 1
                        530     LOAD_CONST                      6: 10
                        532     CALL                            2
                        540     GET_ITER
                        542     FOR_ITER                        177 (to 898)
                        546     STORE_FAST                      4: offset
                        548     LOAD_GLOBAL                     29: NULL + str
                        558     LOAD_FAST_LOAD_FAST             36: base_val, offset
                        560     BINARY_OP                       0 (+)
                        564     CALL                            1
                        572     STORE_FAST                      5: candidate
                        574     LOAD_FAST                       0: self
                        576     LOAD_ATTR                       31: get_dkey
                        596     LOAD_GLOBAL                     29: NULL + str
                        606     LOAD_FAST                       3: config_path
                        608     CALL                            1
                        616     LOAD_FAST                       5: candidate
                        618     CALL                            2
                        626     STORE_FAST                      6: dkey_val
                        628     LOAD_FAST                       0: self
                        630     LOAD_ATTR                       33: get_manifest_for_appid
                        650     LOAD_FAST                       5: candidate
                        652     CALL                            1
                        660     STORE_FAST                      7: manifest_val
                        662     LOAD_FAST                       6: dkey_val
                        664     TO_BOOL
                        672     POP_JUMP_IF_FALSE               110 (to 894)
                        676     LOAD_FAST                       7: manifest_val
                        678     TO_BOOL
                        686     POP_JUMP_IF_FALSE               103 (to 894)
                        690     LOAD_FAST                       7: manifest_val
                        692     LOAD_CONST                      7: 'Unknown'
                        694     COMPARE_OP                      119 (!=)
                        698     POP_JUMP_IF_FALSE               97 (to 894)
                        702     LOAD_FAST                       0: self
                        704     LOAD_ATTR                       0: script_lines
                        724     LOAD_ATTR                       15: append
                        744     LOAD_CONST                      1: 'addappid('
                        746     LOAD_FAST                       5: candidate
                        748     FORMAT_SIMPLE
                        750     LOAD_CONST                      8: ', 1, "'
                        752     LOAD_FAST                       6: dkey_val
                        754     FORMAT_SIMPLE
                        756     LOAD_CONST                      9: '")'
                        758     BUILD_STRING                    5
                        760     CALL                            1
                        768     POP_TOP
                        770     LOAD_FAST                       0: self
                        772     LOAD_ATTR                       0: script_lines
                        792     LOAD_ATTR                       15: append
                        812     LOAD_CONST                      10: 'setManifestid('
                        814     LOAD_FAST                       5: candidate
                        816     FORMAT_SIMPLE
                        818     LOAD_CONST                      11: ', "'
                        820     LOAD_FAST                       7: manifest_val
                        822     FORMAT_SIMPLE
                        824     LOAD_CONST                      12: '", 0)'
                        826     BUILD_STRING                    5
                        828     CALL                            1
                        836     POP_TOP
                        838     LOAD_FAST                       0: self
                        840     LOAD_ATTR                       4: added_ids
                        860     LOAD_ATTR                       17: add
                        880     LOAD_FAST                       5: candidate
                        882     CALL                            1
                        890     POP_TOP
                        892     JUMP_BACKWARD                   177 (to 540)
                        896     POP_TOP
                        898     JUMP_FORWARD                    2 (to 904)
                        900     END_FOR
                        902     POP_TOP
                        904     LOAD_FAST                       0: self
                        906     LOAD_ATTR                       35: fetch_dlc_ids
                        926     LOAD_FAST                       1: primary
                        928     CALL                            1
                        936     POP_TOP
                        938     LOAD_FAST                       0: self
                        940     LOAD_ATTR                       36: dlc_ids
                        960     TO_BOOL
                        968     POP_JUMP_IF_TRUE                22 (to 1014)
                        972     LOAD_FAST                       0: self
                        974     LOAD_ATTR                       39: fetch_depot_ids_from_steamdb
                        994     LOAD_FAST                       1: primary
                        996     CALL                            1
                        1004    LOAD_FAST                       0: self
                        1006    STORE_ATTR                      18: dlc_ids
                        1016    LOAD_FAST                       0: self
                        1018    LOAD_ATTR                       41: process_dlc_ids
                        1038    CALL                            0
                        1046    POP_TOP
                        1048    LOAD_FAST                       0: self
                        1050    LOAD_ATTR                       39: fetch_depot_ids_from_steamdb
                        1070    LOAD_FAST                       1: primary
                        1072    CALL                            1
                        1080    STORE_FAST                      8: depot_ids
                        1082    LOAD_FAST                       8: depot_ids
                        1084    GET_ITER
                        1086    FOR_ITER                        211 (to 1510)
                        1090    STORE_FAST                      9: depot
                        1092    LOAD_FAST_LOAD_FAST             144: depot, self
                        1094    LOAD_ATTR                       4: added_ids
                        1114    CONTAINS_OP                     1 (not in)
                        1118    POP_JUMP_IF_TRUE                2 (to 1124)
                        1122    JUMP_BACKWARD                   20 (to 1084)
                        1126    LOAD_FAST                       0: self
                        1128    LOAD_ATTR                       31: get_dkey
                        1148    LOAD_GLOBAL                     29: NULL + str
                        1158    LOAD_FAST                       3: config_path
                        1160    CALL                            1
                        1168    LOAD_FAST                       9: depot
                        1170    CALL                            2
                        1178    STORE_FAST                      6: dkey_val
                        1180    LOAD_FAST                       0: self
                        1182    LOAD_ATTR                       33: get_manifest_for_appid
                        1202    LOAD_FAST                       9: depot
                        1204    CALL                            1
                        1212    STORE_FAST                      7: manifest_val
                        1214    LOAD_FAST                       6: dkey_val
                        1216    TO_BOOL
                        1224    POP_JUMP_IF_FALSE               82 (to 1390)
                        1228    LOAD_FAST                       7: manifest_val
                        1230    TO_BOOL
                        1238    POP_JUMP_IF_FALSE               75 (to 1390)
                        1242    LOAD_FAST                       7: manifest_val
                        1244    LOAD_CONST                      7: 'Unknown'
                        1246    COMPARE_OP                      119 (!=)
                        1250    POP_JUMP_IF_FALSE               69 (to 1390)
                        1254    LOAD_FAST                       0: self
                        1256    LOAD_ATTR                       0: script_lines
                        1276    LOAD_ATTR                       15: append
                        1296    LOAD_CONST                      1: 'addappid('
                        1298    LOAD_FAST                       9: depot
                        1300    FORMAT_SIMPLE
                        1302    LOAD_CONST                      8: ', 1, "'
                        1304    LOAD_FAST                       6: dkey_val
                        1306    FORMAT_SIMPLE
                        1308    LOAD_CONST                      9: '")'
                        1310    BUILD_STRING                    5
                        1312    CALL                            1
                        1320    POP_TOP
                        1322    LOAD_FAST                       0: self
                        1324    LOAD_ATTR                       0: script_lines
                        1344    LOAD_ATTR                       15: append
                        1364    LOAD_CONST                      10: 'setManifestid('
                        1366    LOAD_FAST                       9: depot
                        1368    FORMAT_SIMPLE
                        1370    LOAD_CONST                      11: ', "'
                        1372    LOAD_FAST                       7: manifest_val
                        1374    FORMAT_SIMPLE
                        1376    LOAD_CONST                      12: '", 0)'
                        1378    BUILD_STRING                    5
                        1380    CALL                            1
                        1388    POP_TOP
                        1390    JUMP_FORWARD                    31 (to 1454)
                        1392    LOAD_FAST                       0: self
                        1394    LOAD_ATTR                       0: script_lines
                        1414    LOAD_ATTR                       15: append
                        1434    LOAD_CONST                      1: 'addappid('
                        1436    LOAD_FAST                       9: depot
                        1438    FORMAT_SIMPLE
                        1440    LOAD_CONST                      2: ')'
                        1442    BUILD_STRING                    3
                        1444    CALL                            1
                        1452    POP_TOP
                        1454    LOAD_FAST                       0: self
                        1456    LOAD_ATTR                       4: added_ids
                        1476    LOAD_ATTR                       17: add
                        1496    LOAD_FAST                       9: depot
                        1498    CALL                            1
                        1506    POP_TOP
                        1508    JUMP_BACKWARD                   213 (to 1084)
                        1512    END_FOR
                        1514    POP_TOP
                        1516    RETURN_CONST                    0: None
                        1518    LOAD_GLOBAL                     42: QMessageBox
                        1528    LOAD_ATTR                       44: warning
                        1548    PUSH_NULL
                        1550    LOAD_FAST                       0: self
                        1552    LOAD_CONST                      13: 'Input Error'
                        1554    LOAD_CONST                      14: 'Primary AppID must be numeric.'
                        1556    CALL                            3
                        1564    POP_TOP
                        1566    RETURN_CONST                    0: None
                'gamename'
                None
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: export_game
                    Qualified Name: LuaScriptMaker.export_game
                    Arg Count: 3
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'script_lines'
                        'clear'
                        'added_ids'
                        'Path'
                        'steam_dir'
                        'append'
                        'add'
                        'isdigit'
                        'int'
                        'range'
                        'str'
                        'get_dkey'
                        'get_manifest_for_appid'
                        'fetch_dlc_ids'
                        'dlc_ids'
                        'fetch_depot_ids_from_steamdb'
                        'process_dlc_ids'
                        'get_game_name_from_primary'
                        're'
                        'sub'
                        'save_dir'
                        'mkdir'
                        'Exception'
                        'log_console'
                        'open'
                        'write'
                        'copy_manifest_files'
                        'any'
                        'os'
                        'listdir'
                        'copy_fallback_manifest'
                        'copy_bin_files'
                        'copy_achievement_bin_files'
                        'create_zip_archive'
                        'zipfile'
                        'ZipFile'
                        'testzip'
                        'shutil'
                        'rmtree'
                    [Locals+Names]
                        'self'
                        'primary'
                        'gamename'
                        'config_path'
                        'base_val'
                        'offset'
                        'candidate'
                        'dkey_val'
                        'manifest_val'
                        'depot_ids'
                        'depot'
                        'game_name_found'
                        'game_name_sanitized'
                        'folder_name'
                        'target_folder'
                        'e'
                        'lua_file'
                        'f'
                        'line'
                        'zip_path'
                        'zipf'
                        'aid'
                    [Constants]
                        None
                        'config'
                        'config.vdf'
                        'addappid('
                        ')'
                        1
                        10
                        'Unknown'
                        ', 1, "'
                        '")'
                        'setManifestid('
                        ', "'
                        '", 0)'
                        '[\\\\/*?:"<>|]'
                        ''
                        '_'
                        True
                        (
                            'parents'
                            'exist_ok'
                        )
                        'Error creating folder for AppID '
                        ': '
                        '.lua'
                        'w'
                        'utf-8'
                        (
                            'encoding'
                        )
                        '\n'
                        'Error writing LUA file for AppID '
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: <genexpr>
                            Qualified Name: LuaScriptMaker.export_game.<locals>.<genexpr>
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 5
                            Flags: 0x00000033 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED | CO_GENERATOR)
                            [Names]
                                'startswith'
                            [Locals+Names]
                                '.0'
                                'fname'
                                'aid'
                            [Constants]
                                '_'
                                None
                            [Disassembly]
                                0       COPY_FREE_VARS                  1
                                2       RETURN_GENERATOR
                                4       POP_TOP
                                6       RESUME                          0
                                8       LOAD_FAST                       0: .0
                                10      GET_ITER
                                12      FOR_ITER                        24 (to 62)
                                16      STORE_FAST_LOAD_FAST            17: fname, fname
                                18      LOAD_ATTR                       1: startswith
                                38      LOAD_DEREF                      2: aid
                                40      FORMAT_SIMPLE
                                42      LOAD_CONST                      0: '_'
                                44      BUILD_STRING                    2
                                46      CALL                            1
                                54      YIELD_VALUE                     0
                                56      RESUME                          5
                                58      POP_TOP
                                60      JUMP_BACKWARD                   26 (to 10)
                                64      END_FOR
                                66      POP_TOP
                                68      RETURN_CONST                    1: None
                                70      CALL_INTRINSIC_1                3 (INTRINSIC_STOPITERATION_ERROR)
                                72      RERAISE                         1
                        'r'
                        'Zip archive error for AppID '
                        'Failed to delete folder '
                    [Disassembly]
                        0       MAKE_CELL                       21: aid
                        2       RESUME                          0
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       0: script_lines
                        26      LOAD_ATTR                       3: clear
                        46      CALL                            0
                        54      POP_TOP
                        56      LOAD_FAST                       0: self
                        58      LOAD_ATTR                       4: added_ids
                        78      LOAD_ATTR                       3: clear
                        98      CALL                            0
                        106     POP_TOP
                        108     LOAD_GLOBAL                     7: NULL + Path
                        118     LOAD_FAST                       0: self
                        120     LOAD_ATTR                       8: steam_dir
                        140     CALL                            1
                        148     LOAD_CONST                      1: 'config'
                        150     BINARY_OP                       11 (/)
                        154     LOAD_CONST                      2: 'config.vdf'
                        156     BINARY_OP                       11 (/)
                        160     STORE_FAST                      3: config_path
                        162     LOAD_FAST                       0: self
                        164     LOAD_ATTR                       0: script_lines
                        184     LOAD_ATTR                       11: append
                        204     LOAD_CONST                      3: 'addappid('
                        206     LOAD_FAST                       1: primary
                        208     FORMAT_SIMPLE
                        210     LOAD_CONST                      4: ')'
                        212     BUILD_STRING                    3
                        214     CALL                            1
                        222     POP_TOP
                        224     LOAD_FAST                       0: self
                        226     LOAD_ATTR                       4: added_ids
                        246     LOAD_ATTR                       13: add
                        266     LOAD_FAST                       1: primary
                        268     CALL                            1
                        276     POP_TOP
                        278     LOAD_FAST                       1: primary
                        280     LOAD_ATTR                       15: isdigit
                        300     CALL                            0
                        308     TO_BOOL
                        316     POP_JUMP_IF_FALSE               510 (to 1340)
                        322     LOAD_GLOBAL                     17: NULL + int
                        332     LOAD_FAST                       1: primary
                        334     CALL                            1
                        342     STORE_FAST                      4: base_val
                        344     LOAD_GLOBAL                     19: NULL + range
                        354     LOAD_CONST                      5: 1
                        356     LOAD_CONST                      6: 10
                        358     CALL                            2
                        366     GET_ITER
                        368     FOR_ITER                        177 (to 724)
                        372     STORE_FAST                      5: offset
                        374     LOAD_GLOBAL                     21: NULL + str
                        384     LOAD_FAST_LOAD_FAST             69: base_val, offset
                        386     BINARY_OP                       0 (+)
                        390     CALL                            1
                        398     STORE_FAST                      6: candidate
                        400     LOAD_FAST                       0: self
                        402     LOAD_ATTR                       23: get_dkey
                        422     LOAD_GLOBAL                     21: NULL + str
                        432     LOAD_FAST                       3: config_path
                        434     CALL                            1
                        442     LOAD_FAST                       6: candidate
                        444     CALL                            2
                        452     STORE_FAST                      7: dkey_val
                        454     LOAD_FAST                       0: self
                        456     LOAD_ATTR                       25: get_manifest_for_appid
                        476     LOAD_FAST                       6: candidate
                        478     CALL                            1
                        486     STORE_FAST                      8: manifest_val
                        488     LOAD_FAST                       7: dkey_val
                        490     TO_BOOL
                        498     POP_JUMP_IF_FALSE               110 (to 720)
                        502     LOAD_FAST                       8: manifest_val
                        504     TO_BOOL
                        512     POP_JUMP_IF_FALSE               103 (to 720)
                        516     LOAD_FAST                       8: manifest_val
                        518     LOAD_CONST                      7: 'Unknown'
                        520     COMPARE_OP                      119 (!=)
                        524     POP_JUMP_IF_FALSE               97 (to 720)
                        528     LOAD_FAST                       0: self
                        530     LOAD_ATTR                       0: script_lines
                        550     LOAD_ATTR                       11: append
                        570     LOAD_CONST                      3: 'addappid('
                        572     LOAD_FAST                       6: candidate
                        574     FORMAT_SIMPLE
                        576     LOAD_CONST                      8: ', 1, "'
                        578     LOAD_FAST                       7: dkey_val
                        580     FORMAT_SIMPLE
                        582     LOAD_CONST                      9: '")'
                        584     BUILD_STRING                    5
                        586     CALL                            1
                        594     POP_TOP
                        596     LOAD_FAST                       0: self
                        598     LOAD_ATTR                       0: script_lines
                        618     LOAD_ATTR                       11: append
                        638     LOAD_CONST                      10: 'setManifestid('
                        640     LOAD_FAST                       6: candidate
                        642     FORMAT_SIMPLE
                        644     LOAD_CONST                      11: ', "'
                        646     LOAD_FAST                       8: manifest_val
                        648     FORMAT_SIMPLE
                        650     LOAD_CONST                      12: '", 0)'
                        652     BUILD_STRING                    5
                        654     CALL                            1
                        662     POP_TOP
                        664     LOAD_FAST                       0: self
                        666     LOAD_ATTR                       4: added_ids
                        686     LOAD_ATTR                       13: add
                        706     LOAD_FAST                       6: candidate
                        708     CALL                            1
                        716     POP_TOP
                        718     JUMP_BACKWARD                   177 (to 366)
                        722     POP_TOP
                        724     JUMP_FORWARD                    2 (to 730)
                        726     END_FOR
                        728     POP_TOP
                        730     LOAD_FAST                       0: self
                        732     LOAD_ATTR                       27: fetch_dlc_ids
                        752     LOAD_FAST                       1: primary
                        754     CALL                            1
                        762     POP_TOP
                        764     LOAD_FAST                       0: self
                        766     LOAD_ATTR                       28: dlc_ids
                        786     TO_BOOL
                        794     POP_JUMP_IF_TRUE                22 (to 840)
                        798     LOAD_FAST                       0: self
                        800     LOAD_ATTR                       31: fetch_depot_ids_from_steamdb
                        820     LOAD_FAST                       1: primary
                        822     CALL                            1
                        830     LOAD_FAST                       0: self
                        832     STORE_ATTR                      14: dlc_ids
                        842     LOAD_FAST                       0: self
                        844     LOAD_ATTR                       33: process_dlc_ids
                        864     CALL                            0
                        872     POP_TOP
                        874     LOAD_FAST                       0: self
                        876     LOAD_ATTR                       31: fetch_depot_ids_from_steamdb
                        896     LOAD_FAST                       1: primary
                        898     CALL                            1
                        906     STORE_FAST                      9: depot_ids
                        908     LOAD_FAST                       9: depot_ids
                        910     GET_ITER
                        912     FOR_ITER                        211 (to 1336)
                        916     STORE_FAST                      10: depot
                        918     LOAD_FAST_LOAD_FAST             160: depot, self
                        920     LOAD_ATTR                       4: added_ids
                        940     CONTAINS_OP                     1 (not in)
                        944     POP_JUMP_IF_TRUE                2 (to 950)
                        948     JUMP_BACKWARD                   20 (to 910)
                        952     LOAD_FAST                       0: self
                        954     LOAD_ATTR                       23: get_dkey
                        974     LOAD_GLOBAL                     21: NULL + str
                        984     LOAD_FAST                       3: config_path
                        986     CALL                            1
                        994     LOAD_FAST                       10: depot
                        996     CALL                            2
                        1004    STORE_FAST                      7: dkey_val
                        1006    LOAD_FAST                       0: self
                        1008    LOAD_ATTR                       25: get_manifest_for_appid
                        1028    LOAD_FAST                       10: depot
                        1030    CALL                            1
                        1038    STORE_FAST                      8: manifest_val
                        1040    LOAD_FAST                       7: dkey_val
                        1042    TO_BOOL
                        1050    POP_JUMP_IF_FALSE               82 (to 1216)
                        1054    LOAD_FAST                       8: manifest_val
                        1056    TO_BOOL
                        1064    POP_JUMP_IF_FALSE               75 (to 1216)
                        1068    LOAD_FAST                       8: manifest_val
                        1070    LOAD_CONST                      7: 'Unknown'
                        1072    COMPARE_OP                      119 (!=)
                        1076    POP_JUMP_IF_FALSE               69 (to 1216)
                        1080    LOAD_FAST                       0: self
                        1082    LOAD_ATTR                       0: script_lines
                        1102    LOAD_ATTR                       11: append
                        1122    LOAD_CONST                      3: 'addappid('
                        1124    LOAD_FAST                       10: depot
                        1126    FORMAT_SIMPLE
                        1128    LOAD_CONST                      8: ', 1, "'
                        1130    LOAD_FAST                       7: dkey_val
                        1132    FORMAT_SIMPLE
                        1134    LOAD_CONST                      9: '")'
                        1136    BUILD_STRING                    5
                        1138    CALL                            1
                        1146    POP_TOP
                        1148    LOAD_FAST                       0: self
                        1150    LOAD_ATTR                       0: script_lines
                        1170    LOAD_ATTR                       11: append
                        1190    LOAD_CONST                      10: 'setManifestid('
                        1192    LOAD_FAST                       10: depot
                        1194    FORMAT_SIMPLE
                        1196    LOAD_CONST                      11: ', "'
                        1198    LOAD_FAST                       8: manifest_val
                        1200    FORMAT_SIMPLE
                        1202    LOAD_CONST                      12: '", 0)'
                        1204    BUILD_STRING                    5
                        1206    CALL                            1
                        1214    POP_TOP
                        1216    JUMP_FORWARD                    31 (to 1280)
                        1218    LOAD_FAST                       0: self
                        1220    LOAD_ATTR                       0: script_lines
                        1240    LOAD_ATTR                       11: append
                        1260    LOAD_CONST                      3: 'addappid('
                        1262    LOAD_FAST                       10: depot
                        1264    FORMAT_SIMPLE
                        1266    LOAD_CONST                      4: ')'
                        1268    BUILD_STRING                    3
                        1270    CALL                            1
                        1278    POP_TOP
                        1280    LOAD_FAST                       0: self
                        1282    LOAD_ATTR                       4: added_ids
                        1302    LOAD_ATTR                       13: add
                        1322    LOAD_FAST                       10: depot
                        1324    CALL                            1
                        1332    POP_TOP
                        1334    JUMP_BACKWARD                   213 (to 910)
                        1338    END_FOR
                        1340    POP_TOP
                        1342    LOAD_FAST                       0: self
                        1344    LOAD_ATTR                       35: get_game_name_from_primary
                        1364    LOAD_FAST                       1: primary
                        1366    CALL                            1
                        1374    STORE_FAST                      11: game_name_found
                        1376    LOAD_GLOBAL                     36: re
                        1386    LOAD_ATTR                       38: sub
                        1406    PUSH_NULL
                        1408    LOAD_CONST                      13: '[\\\\/*?:"<>|]'
                        1410    LOAD_CONST                      14: ''
                        1412    LOAD_FAST                       11: game_name_found
                        1414    CALL                            3
                        1422    STORE_FAST                      12: game_name_sanitized
                        1424    LOAD_FAST                       1: primary
                        1426    FORMAT_SIMPLE
                        1428    LOAD_CONST                      15: '_'
                        1430    LOAD_FAST                       12: game_name_sanitized
                        1432    FORMAT_SIMPLE
                        1434    BUILD_STRING                    3
                        1436    STORE_FAST                      13: folder_name
                        1438    LOAD_GLOBAL                     7: NULL + Path
                        1448    LOAD_FAST                       0: self
                        1450    LOAD_ATTR                       40: save_dir
                        1470    CALL                            1
                        1478    LOAD_FAST                       13: folder_name
                        1480    BINARY_OP                       11 (/)
                        1484    STORE_FAST                      14: target_folder
                        1486    NOP
                        1488    LOAD_FAST                       14: target_folder
                        1490    LOAD_ATTR                       43: mkdir
                        1510    LOAD_CONST                      16: True
                        1512    LOAD_CONST                      16: True
                        1514    LOAD_CONST                      17: ('parents', 'exist_ok')
                        1516    CALL_KW                         2
                        1518    POP_TOP
                        1520    LOAD_FAST_LOAD_FAST             225: target_folder, primary
                        1522    FORMAT_SIMPLE
                        1524    LOAD_CONST                      20: '.lua'
                        1526    BUILD_STRING                    2
                        1528    BINARY_OP                       11 (/)
                        1532    STORE_FAST                      16: lua_file
                        1534    NOP
                        1536    LOAD_FAST                       16: lua_file
                        1538    LOAD_ATTR                       49: open
                        1558    LOAD_CONST                      21: 'w'
                        1560    LOAD_CONST                      22: 'utf-8'
                        1562    LOAD_CONST                      23: ('encoding',)
                        1564    CALL_KW                         2
                        1566    BEFORE_WITH
                        1568    STORE_FAST                      17: f
                        1570    LOAD_FAST                       0: self
                        1572    LOAD_ATTR                       0: script_lines
                        1592    GET_ITER
                        1594    FOR_ITER                        23 (to 1642)
                        1598    STORE_FAST                      18: line
                        1600    LOAD_FAST                       17: f
                        1602    LOAD_ATTR                       51: write
                        1622    LOAD_FAST                       18: line
                        1624    LOAD_CONST                      24: '\n'
                        1626    BINARY_OP                       0 (+)
                        1630    CALL                            1
                        1638    POP_TOP
                        1640    JUMP_BACKWARD                   25 (to 1592)
                        1644    END_FOR
                        1646    POP_TOP
                        1648    LOAD_CONST                      0: None
                        1650    LOAD_CONST                      0: None
                        1652    LOAD_CONST                      0: None
                        1654    CALL                            2
                        1662    POP_TOP
                        1664    LOAD_FAST                       0: self
                        1666    LOAD_ATTR                       4: added_ids
                        1686    GET_ITER
                        1688    FOR_ITER                        121 (to 1932)
                        1692    STORE_DEREF                     21: aid
                        1694    LOAD_FAST                       0: self
                        1696    LOAD_ATTR                       53: copy_manifest_files
                        1716    LOAD_FAST                       14: target_folder
                        1718    LOAD_DEREF                      21: aid
                        1720    CALL                            2
                        1728    POP_TOP
                        1730    LOAD_GLOBAL                     55: NULL + any
                        1740    LOAD_FAST                       21: aid
                        1742    BUILD_TUPLE                     1
                        1744    LOAD_CONST                      26: <CODE> <genexpr>
                        1746    MAKE_FUNCTION
                        1748    SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        1750    LOAD_GLOBAL                     56: os
                        1760    LOAD_ATTR                       58: listdir
                        1780    PUSH_NULL
                        1782    LOAD_FAST                       14: target_folder
                        1784    CALL                            1
                        1792    GET_ITER
                        1794    CALL                            0
                        1802    CALL                            1
                        1810    TO_BOOL
                        1818    POP_JUMP_IF_TRUE                18 (to 1856)
                        1822    LOAD_FAST                       0: self
                        1824    LOAD_ATTR                       61: copy_fallback_manifest
                        1844    LOAD_FAST                       14: target_folder
                        1846    LOAD_DEREF                      21: aid
                        1848    CALL                            2
                        1856    POP_TOP
                        1858    LOAD_FAST                       0: self
                        1860    LOAD_ATTR                       63: copy_bin_files
                        1880    LOAD_FAST                       14: target_folder
                        1882    LOAD_DEREF                      21: aid
                        1884    CALL                            2
                        1892    POP_TOP
                        1894    LOAD_FAST                       0: self
                        1896    LOAD_ATTR                       65: copy_achievement_bin_files
                        1916    LOAD_FAST                       14: target_folder
                        1918    LOAD_DEREF                      21: aid
                        1920    CALL                            2
                        1928    POP_TOP
                        1930    JUMP_BACKWARD                   123 (to 1686)
                        1934    END_FOR
                        1936    POP_TOP
                        1938    LOAD_FAST                       0: self
                        1940    LOAD_ATTR                       67: create_zip_archive
                        1960    LOAD_FAST                       14: target_folder
                        1962    CALL                            1
                        1970    STORE_FAST                      19: zip_path
                        1972    LOAD_FAST                       19: zip_path
                        1974    TO_BOOL
                        1982    POP_JUMP_IF_FALSE               74 (to 2132)
                        1986    NOP
                        1988    LOAD_GLOBAL                     68: zipfile
                        1998    LOAD_ATTR                       70: ZipFile
                        2018    PUSH_NULL
                        2020    LOAD_FAST                       19: zip_path
                        2022    LOAD_CONST                      27: 'r'
                        2024    CALL                            2
                        2032    BEFORE_WITH
                        2034    STORE_FAST                      20: zipf
                        2036    LOAD_FAST                       20: zipf
                        2038    LOAD_ATTR                       73: testzip
                        2058    CALL                            0
                        2066    POP_TOP
                        2068    LOAD_CONST                      0: None
                        2070    LOAD_CONST                      0: None
                        2072    LOAD_CONST                      0: None
                        2074    CALL                            2
                        2082    POP_TOP
                        2084    NOP
                        2086    LOAD_GLOBAL                     74: shutil
                        2096    LOAD_ATTR                       76: rmtree
                        2116    PUSH_NULL
                        2118    LOAD_FAST                       14: target_folder
                        2120    CALL                            1
                        2128    POP_TOP
                        2130    LOAD_FAST                       19: zip_path
                        2132    RETURN_VALUE
                        2134    RETURN_CONST                    0: None
                        2136    PUSH_EXC_INFO
                        2138    LOAD_GLOBAL                     44: Exception
                        2148    CHECK_EXC_MATCH
                        2150    POP_JUMP_IF_FALSE               42 (to 2236)
                        2154    STORE_FAST                      15: e
                        2156    LOAD_FAST                       0: self
                        2158    LOAD_ATTR                       47: log_console
                        2178    LOAD_CONST                      18: 'Error creating folder for AppID '
                        2180    LOAD_FAST                       1: primary
                        2182    FORMAT_SIMPLE
                        2184    LOAD_CONST                      19: ': '
                        2186    LOAD_GLOBAL                     21: NULL + str
                        2196    LOAD_FAST                       15: e
                        2198    CALL                            1
                        2206    FORMAT_SIMPLE
                        2208    BUILD_STRING                    4
                        2210    CALL                            1
                        2218    POP_TOP
                        2220    POP_EXCEPT
                        2222    LOAD_CONST                      0: None
                        2224    STORE_FAST                      15: e
                        2226    DELETE_FAST                     15: e
                        2228    RETURN_CONST                    0: None
                        2230    LOAD_CONST                      0: None
                        2232    STORE_FAST                      15: e
                        2234    DELETE_FAST                     15: e
                        2236    RERAISE                         1
                        2238    RERAISE                         0
                        2240    COPY                            3
                        2242    POP_EXCEPT
                        2244    RERAISE                         1
                        2246    PUSH_EXC_INFO
                        2248    WITH_EXCEPT_START
                        2250    TO_BOOL
                        2258    POP_JUMP_IF_TRUE                1 (to 2262)
                        2262    RERAISE                         2
                        2264    POP_TOP
                        2266    POP_EXCEPT
                        2268    POP_TOP
                        2270    POP_TOP
                        2272    JUMP_BACKWARD_NO_INTERRUPT      306 (to 1664)
                        2276    COPY                            3
                        2278    POP_EXCEPT
                        2280    RERAISE                         1
                        2282    PUSH_EXC_INFO
                        2284    LOAD_GLOBAL                     44: Exception
                        2294    CHECK_EXC_MATCH
                        2296    POP_JUMP_IF_FALSE               42 (to 2382)
                        2300    STORE_FAST                      15: e
                        2302    LOAD_FAST                       0: self
                        2304    LOAD_ATTR                       47: log_console
                        2324    LOAD_CONST                      25: 'Error writing LUA file for AppID '
                        2326    LOAD_FAST                       1: primary
                        2328    FORMAT_SIMPLE
                        2330    LOAD_CONST                      19: ': '
                        2332    LOAD_GLOBAL                     21: NULL + str
                        2342    LOAD_FAST                       15: e
                        2344    CALL                            1
                        2352    FORMAT_SIMPLE
                        2354    BUILD_STRING                    4
                        2356    CALL                            1
                        2364    POP_TOP
                        2366    POP_EXCEPT
                        2368    LOAD_CONST                      0: None
                        2370    STORE_FAST                      15: e
                        2372    DELETE_FAST                     15: e
                        2374    RETURN_CONST                    0: None
                        2376    LOAD_CONST                      0: None
                        2378    STORE_FAST                      15: e
                        2380    DELETE_FAST                     15: e
                        2382    RERAISE                         1
                        2384    RERAISE                         0
                        2386    COPY                            3
                        2388    POP_EXCEPT
                        2390    RERAISE                         1
                        2392    PUSH_EXC_INFO
                        2394    WITH_EXCEPT_START
                        2396    TO_BOOL
                        2404    POP_JUMP_IF_TRUE                1 (to 2408)
                        2408    RERAISE                         2
                        2410    POP_TOP
                        2412    POP_EXCEPT
                        2414    POP_TOP
                        2416    POP_TOP
                        2418    JUMP_BACKWARD_NO_INTERRUPT      168 (to 2084)
                        2420    COPY                            3
                        2422    POP_EXCEPT
                        2424    RERAISE                         1
                        2426    PUSH_EXC_INFO
                        2428    LOAD_GLOBAL                     44: Exception
                        2438    CHECK_EXC_MATCH
                        2440    POP_JUMP_IF_FALSE               42 (to 2526)
                        2444    STORE_FAST                      15: e
                        2446    LOAD_FAST                       0: self
                        2448    LOAD_ATTR                       47: log_console
                        2468    LOAD_CONST                      28: 'Zip archive error for AppID '
                        2470    LOAD_FAST                       1: primary
                        2472    FORMAT_SIMPLE
                        2474    LOAD_CONST                      19: ': '
                        2476    LOAD_GLOBAL                     21: NULL + str
                        2486    LOAD_FAST                       15: e
                        2488    CALL                            1
                        2496    FORMAT_SIMPLE
                        2498    BUILD_STRING                    4
                        2500    CALL                            1
                        2508    POP_TOP
                        2510    POP_EXCEPT
                        2512    LOAD_CONST                      0: None
                        2514    STORE_FAST                      15: e
                        2516    DELETE_FAST                     15: e
                        2518    RETURN_CONST                    0: None
                        2520    LOAD_CONST                      0: None
                        2522    STORE_FAST                      15: e
                        2524    DELETE_FAST                     15: e
                        2526    RERAISE                         1
                        2528    RERAISE                         0
                        2530    COPY                            3
                        2532    POP_EXCEPT
                        2534    RERAISE                         1
                        2536    PUSH_EXC_INFO
                        2538    LOAD_GLOBAL                     44: Exception
                        2548    CHECK_EXC_MATCH
                        2550    POP_JUMP_IF_FALSE               43 (to 2638)
                        2554    STORE_FAST                      15: e
                        2556    LOAD_FAST                       0: self
                        2558    LOAD_ATTR                       47: log_console
                        2578    LOAD_CONST                      29: 'Failed to delete folder '
                        2580    LOAD_FAST                       14: target_folder
                        2582    FORMAT_SIMPLE
                        2584    LOAD_CONST                      19: ': '
                        2586    LOAD_GLOBAL                     21: NULL + str
                        2596    LOAD_FAST                       15: e
                        2598    CALL                            1
                        2606    FORMAT_SIMPLE
                        2608    BUILD_STRING                    4
                        2610    CALL                            1
                        2618    POP_TOP
                        2620    POP_EXCEPT
                        2622    LOAD_CONST                      0: None
                        2624    STORE_FAST                      15: e
                        2626    DELETE_FAST                     15: e
                        2628    LOAD_FAST                       19: zip_path
                        2630    RETURN_VALUE
                        2632    LOAD_CONST                      0: None
                        2634    STORE_FAST                      15: e
                        2636    DELETE_FAST                     15: e
                        2638    RERAISE                         1
                        2640    RERAISE                         0
                        2642    COPY                            3
                        2644    POP_EXCEPT
                        2646    RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: export_all_installed_games
                    Qualified Name: LuaScriptMaker.export_all_installed_games
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'steam_dir'
                        'QMessageBox'
                        'warning'
                        'save_dir'
                        'log_console'
                        'get_library_folders'
                        'str'
                        'exists'
                        'glob'
                        'parse_appmanifest'
                        'get'
                        'strip'
                        'any'
                        'export_game'
                        'export_paused'
                        'QApplication'
                        'processEvents'
                        'QThread'
                        'msleep'
                        'information'
                    [Locals+Names]
                        'self'
                        'blacklist'
                        'libraries'
                        'p'
                        'exported_count'
                        'lib'
                        'acf_file'
                        'app_data'
                        'primary'
                        'zip_path'
                        'gamename'
                    [Constants]
                        None
                        'Steam Directory Error'
                        'Please set the Steam directory first.'
                        'Save Directory Error'
                        'Please set the Save directory first.'
                        'Starting export of installed games (automatic)...'
                        'Steamworks Common Redistributables'
                        'Steamworks Common Redistributables (32-bit)'
                        'Detected library folders: '
                        0
                        'appmanifest_*.acf'
                        'appid'
                        'name'
                        'unknown'
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: <genexpr>
                            Qualified Name: LuaScriptMaker.export_all_installed_games.<locals>.<genexpr>
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 4
                            Flags: 0x00000033 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED | CO_GENERATOR)
                            [Names]
                                'lower'
                            [Locals+Names]
                                '.0'
                                'bl_word'
                                'gamename'
                            [Constants]
                                None
                            [Disassembly]
                                0       COPY_FREE_VARS                  1
                                2       RETURN_GENERATOR
                                4       POP_TOP
                                6       RESUME                          0
                                8       LOAD_FAST                       0: .0
                                10      GET_ITER
                                12      FOR_ITER                        37 (to 88)
                                16      STORE_FAST_LOAD_FAST            17: bl_word, bl_word
                                18      LOAD_ATTR                       1: lower
                                38      CALL                            0
                                46      LOAD_DEREF                      2: gamename
                                48      LOAD_ATTR                       1: lower
                                68      CALL                            0
                                76      CONTAINS_OP                     0 (in)
                                80      YIELD_VALUE                     0
                                82      RESUME                          5
                                84      POP_TOP
                                86      JUMP_BACKWARD                   39 (to 10)
                                90      END_FOR
                                92      POP_TOP
                                94      RETURN_CONST                    0: None
                                96      CALL_INTRINSIC_1                3 (INTRINSIC_STOPITERATION_ERROR)
                                98      RERAISE                         1
                        'Skipping non-game entry: '
                        ' - '
                        'Exporting game '
                        'Created zip: '
                        1
                        200
                        'Export completed. '
                        ' games exported.'
                        'Export Completed'
                    [Disassembly]
                        0       MAKE_CELL                       10: gamename
                        2       RESUME                          0
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       0: steam_dir
                        26      TO_BOOL
                        34      POP_JUMP_IF_TRUE                25 (to 86)
                        38      LOAD_GLOBAL                     2: QMessageBox
                        48      LOAD_ATTR                       4: warning
                        68      PUSH_NULL
                        70      LOAD_FAST                       0: self
                        72      LOAD_CONST                      1: 'Steam Directory Error'
                        74      LOAD_CONST                      2: 'Please set the Steam directory first.'
                        76      CALL                            3
                        84      POP_TOP
                        86      RETURN_CONST                    0: None
                        88      LOAD_FAST                       0: self
                        90      LOAD_ATTR                       6: save_dir
                        110     TO_BOOL
                        118     POP_JUMP_IF_TRUE                25 (to 170)
                        122     LOAD_GLOBAL                     2: QMessageBox
                        132     LOAD_ATTR                       4: warning
                        152     PUSH_NULL
                        154     LOAD_FAST                       0: self
                        156     LOAD_CONST                      3: 'Save Directory Error'
                        158     LOAD_CONST                      4: 'Please set the Save directory first.'
                        160     CALL                            3
                        168     POP_TOP
                        170     RETURN_CONST                    0: None
                        172     LOAD_FAST                       0: self
                        174     LOAD_ATTR                       9: log_console
                        194     LOAD_CONST                      5: 'Starting export of installed games (automatic)...'
                        196     CALL                            1
                        204     POP_TOP
                        206     LOAD_CONST                      6: 'Steamworks Common Redistributables'
                        208     LOAD_CONST                      7: 'Steamworks Common Redistributables (32-bit)'
                        210     BUILD_LIST                      2
                        212     STORE_FAST                      1: blacklist
                        214     LOAD_FAST                       0: self
                        216     LOAD_ATTR                       11: get_library_folders
                        236     CALL                            0
                        244     STORE_FAST                      2: libraries
                        246     LOAD_FAST                       0: self
                        248     LOAD_ATTR                       9: log_console
                        268     LOAD_CONST                      8: 'Detected library folders: '
                        270     LOAD_FAST                       2: libraries
                        272     GET_ITER
                        274     LOAD_FAST_AND_CLEAR             3: p
                        276     SWAP                            2
                        278     BUILD_LIST                      0
                        280     SWAP                            2
                        282     GET_ITER
                        284     FOR_ITER                        14 (to 314)
                        288     STORE_FAST                      3: p
                        290     LOAD_GLOBAL                     13: NULL + str
                        300     LOAD_FAST                       3: p
                        302     CALL                            1
                        310     LIST_APPEND                     2
                        312     JUMP_BACKWARD                   16 (to 282)
                        316     END_FOR
                        318     POP_TOP
                        320     SWAP                            2
                        322     STORE_FAST                      3: p
                        324     FORMAT_SIMPLE
                        326     BUILD_STRING                    2
                        328     CALL                            1
                        336     POP_TOP
                        338     LOAD_CONST                      9: 0
                        340     STORE_FAST                      4: exported_count
                        342     LOAD_FAST                       2: libraries
                        344     GET_ITER
                        346     FOR_ITER                        349 (to 1048)
                        352     STORE_FAST                      5: lib
                        354     LOAD_FAST                       5: lib
                        356     LOAD_ATTR                       15: exists
                        376     CALL                            0
                        384     TO_BOOL
                        392     POP_JUMP_IF_TRUE                2 (to 398)
                        396     JUMP_BACKWARD                   27 (to 344)
                        400     LOAD_FAST                       5: lib
                        402     LOAD_ATTR                       17: glob
                        422     LOAD_CONST                      10: 'appmanifest_*.acf'
                        424     CALL                            1
                        432     GET_ITER
                        434     FOR_ITER                        300 (to 1038)
                        440     STORE_FAST                      6: acf_file
                        442     LOAD_GLOBAL                     19: NULL + parse_appmanifest
                        452     LOAD_FAST                       6: acf_file
                        454     CALL                            1
                        462     STORE_FAST                      7: app_data
                        464     LOAD_FAST                       7: app_data
                        466     LOAD_ATTR                       21: get
                        486     LOAD_CONST                      11: 'appid'
                        488     CALL                            1
                        496     TO_BOOL
                        504     POP_JUMP_IF_TRUE                2 (to 510)
                        508     JUMP_BACKWARD                   39 (to 432)
                        512     LOAD_FAST                       7: app_data
                        514     LOAD_CONST                      11: 'appid'
                        516     BINARY_SUBSCR
                        520     STORE_FAST                      8: primary
                        522     LOAD_FAST                       7: app_data
                        524     LOAD_ATTR                       21: get
                        544     LOAD_CONST                      12: 'name'
                        546     LOAD_CONST                      13: 'unknown'
                        548     CALL                            2
                        556     LOAD_ATTR                       23: strip
                        576     CALL                            0
                        584     STORE_DEREF                     10: gamename
                        586     LOAD_GLOBAL                     25: NULL + any
                        596     LOAD_FAST                       10: gamename
                        598     BUILD_TUPLE                     1
                        600     LOAD_CONST                      14: <CODE> <genexpr>
                        602     MAKE_FUNCTION
                        604     SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        606     LOAD_FAST                       1: blacklist
                        608     GET_ITER
                        610     CALL                            0
                        618     CALL                            1
                        626     TO_BOOL
                        634     POP_JUMP_IF_FALSE               25 (to 686)
                        638     LOAD_FAST                       0: self
                        640     LOAD_ATTR                       9: log_console
                        660     LOAD_CONST                      15: 'Skipping non-game entry: '
                        662     LOAD_FAST                       8: primary
                        664     FORMAT_SIMPLE
                        666     LOAD_CONST                      16: ' - '
                        668     LOAD_DEREF                      10: gamename
                        670     FORMAT_SIMPLE
                        672     BUILD_STRING                    4
                        674     CALL                            1
                        682     POP_TOP
                        684     JUMP_BACKWARD                   127 (to 432)
                        688     LOAD_FAST                       0: self
                        690     LOAD_ATTR                       9: log_console
                        710     LOAD_CONST                      17: 'Exporting game '
                        712     LOAD_FAST                       8: primary
                        714     FORMAT_SIMPLE
                        716     LOAD_CONST                      16: ' - '
                        718     LOAD_DEREF                      10: gamename
                        720     FORMAT_SIMPLE
                        722     BUILD_STRING                    4
                        724     CALL                            1
                        732     POP_TOP
                        734     LOAD_FAST                       0: self
                        736     LOAD_ATTR                       27: export_game
                        756     LOAD_FAST                       8: primary
                        758     LOAD_DEREF                      10: gamename
                        760     CALL                            2
                        768     STORE_FAST                      9: zip_path
                        770     LOAD_FAST                       9: zip_path
                        772     TO_BOOL
                        780     POP_JUMP_IF_FALSE               25 (to 832)
                        784     LOAD_FAST                       0: self
                        786     LOAD_ATTR                       9: log_console
                        806     LOAD_CONST                      18: 'Created zip: '
                        808     LOAD_FAST                       9: zip_path
                        810     FORMAT_SIMPLE
                        812     BUILD_STRING                    2
                        814     CALL                            1
                        822     POP_TOP
                        824     LOAD_FAST                       4: exported_count
                        826     LOAD_CONST                      19: 1
                        828     BINARY_OP                       13 (+=)
                        832     STORE_FAST                      4: exported_count
                        834     LOAD_FAST                       0: self
                        836     LOAD_ATTR                       28: export_paused
                        856     TO_BOOL
                        864     POP_JUMP_IF_FALSE               62 (to 990)
                        868     LOAD_GLOBAL                     30: QApplication
                        878     LOAD_ATTR                       32: processEvents
                        898     PUSH_NULL
                        900     CALL                            0
                        908     POP_TOP
                        910     LOAD_GLOBAL                     34: QThread
                        920     LOAD_ATTR                       36: msleep
                        940     PUSH_NULL
                        942     LOAD_CONST                      20: 200
                        944     CALL                            1
                        952     POP_TOP
                        954     LOAD_FAST                       0: self
                        956     LOAD_ATTR                       28: export_paused
                        976     TO_BOOL
                        984     POP_JUMP_IF_FALSE               2 (to 990)
                        988     JUMP_BACKWARD                   62 (to 866)
                        992     LOAD_GLOBAL                     30: QApplication
                        1002    LOAD_ATTR                       32: processEvents
                        1022    PUSH_NULL
                        1024    CALL                            0
                        1032    POP_TOP
                        1034    JUMP_BACKWARD                   303 (to 432)
                        1040    END_FOR
                        1042    POP_TOP
                        1044    JUMP_BACKWARD                   352 (to 344)
                        1050    END_FOR
                        1052    POP_TOP
                        1054    LOAD_FAST                       0: self
                        1056    LOAD_ATTR                       9: log_console
                        1076    LOAD_CONST                      21: 'Export completed. '
                        1078    LOAD_FAST                       4: exported_count
                        1080    FORMAT_SIMPLE
                        1082    LOAD_CONST                      22: ' games exported.'
                        1084    BUILD_STRING                    3
                        1086    CALL                            1
                        1094    POP_TOP
                        1096    LOAD_GLOBAL                     2: QMessageBox
                        1106    LOAD_ATTR                       38: information
                        1126    PUSH_NULL
                        1128    LOAD_FAST                       0: self
                        1130    LOAD_CONST                      23: 'Export Completed'
                        1132    LOAD_CONST                      21: 'Export completed. '
                        1134    LOAD_FAST                       4: exported_count
                        1136    FORMAT_SIMPLE
                        1138    LOAD_CONST                      22: ' games exported.'
                        1140    BUILD_STRING                    3
                        1142    CALL                            3
                        1150    POP_TOP
                        1152    RETURN_CONST                    0: None
                        1154    SWAP                            2
                        1156    POP_TOP
                        1158    SWAP                            2
                        1160    STORE_FAST                      3: p
                        1162    RERAISE                         0
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: handle_preview
                    Qualified Name: LuaScriptMaker.handle_preview
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'auto_fill_fields'
                        'process_primary_appid'
                        'update_preview'
                        'Exception'
                        'QMessageBox'
                        'critical'
                        'str'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'ex'
                    [Constants]
                        None
                        'Preview Error'
                        'Error generating preview: '
                        'Preview error:'
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       1: auto_fill_fields
                        26      CALL                            0
                        34      POP_TOP
                        36      LOAD_FAST                       0: self
                        38      LOAD_ATTR                       3: process_primary_appid
                        58      CALL                            0
                        66      POP_TOP
                        68      LOAD_FAST                       0: self
                        70      LOAD_ATTR                       5: update_preview
                        90      CALL                            0
                        98      POP_TOP
                        100     RETURN_CONST                    0: None
                        102     PUSH_EXC_INFO
                        104     LOAD_GLOBAL                     6: Exception
                        114     CHECK_EXC_MATCH
                        116     POP_JUMP_IF_FALSE               68 (to 254)
                        120     STORE_FAST                      1: ex
                        122     LOAD_GLOBAL                     8: QMessageBox
                        132     LOAD_ATTR                       10: critical
                        152     PUSH_NULL
                        154     LOAD_FAST                       0: self
                        156     LOAD_CONST                      1: 'Preview Error'
                        158     LOAD_CONST                      2: 'Error generating preview: '
                        160     LOAD_GLOBAL                     13: NULL + str
                        170     LOAD_FAST                       1: ex
                        172     CALL                            1
                        180     FORMAT_SIMPLE
                        182     BUILD_STRING                    2
                        184     CALL                            3
                        192     POP_TOP
                        194     LOAD_GLOBAL                     14: logging
                        204     LOAD_ATTR                       16: exception
                        224     PUSH_NULL
                        226     LOAD_CONST                      3: 'Preview error:'
                        228     CALL                            1
                        236     POP_TOP
                        238     POP_EXCEPT
                        240     LOAD_CONST                      0: None
                        242     STORE_FAST                      1: ex
                        244     DELETE_FAST                     1: ex
                        246     RETURN_CONST                    0: None
                        248     LOAD_CONST                      0: None
                        250     STORE_FAST                      1: ex
                        252     DELETE_FAST                     1: ex
                        254     RERAISE                         1
                        256     RERAISE                         0
                        258     COPY                            3
                        260     POP_EXCEPT
                        262     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: handle_save
                    Qualified Name: LuaScriptMaker.handle_save
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'auto_fill_fields'
                        'process_primary_appid'
                        'save_lua_script'
                        'Exception'
                        'QMessageBox'
                        'critical'
                        'str'
                        'logging'
                        'exception'
                    [Locals+Names]
                        'self'
                        'ex'
                    [Constants]
                        None
                        'Save Error'
                        'Error saving LUA: '
                        'Save error:'
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       1: auto_fill_fields
                        26      CALL                            0
                        34      POP_TOP
                        36      LOAD_FAST                       0: self
                        38      LOAD_ATTR                       3: process_primary_appid
                        58      CALL                            0
                        66      POP_TOP
                        68      LOAD_FAST                       0: self
                        70      LOAD_ATTR                       5: save_lua_script
                        90      CALL                            0
                        98      POP_TOP
                        100     RETURN_CONST                    0: None
                        102     PUSH_EXC_INFO
                        104     LOAD_GLOBAL                     6: Exception
                        114     CHECK_EXC_MATCH
                        116     POP_JUMP_IF_FALSE               68 (to 254)
                        120     STORE_FAST                      1: ex
                        122     LOAD_GLOBAL                     8: QMessageBox
                        132     LOAD_ATTR                       10: critical
                        152     PUSH_NULL
                        154     LOAD_FAST                       0: self
                        156     LOAD_CONST                      1: 'Save Error'
                        158     LOAD_CONST                      2: 'Error saving LUA: '
                        160     LOAD_GLOBAL                     13: NULL + str
                        170     LOAD_FAST                       1: ex
                        172     CALL                            1
                        180     FORMAT_SIMPLE
                        182     BUILD_STRING                    2
                        184     CALL                            3
                        192     POP_TOP
                        194     LOAD_GLOBAL                     14: logging
                        204     LOAD_ATTR                       16: exception
                        224     PUSH_NULL
                        226     LOAD_CONST                      3: 'Save error:'
                        228     CALL                            1
                        236     POP_TOP
                        238     POP_EXCEPT
                        240     LOAD_CONST                      0: None
                        242     STORE_FAST                      1: ex
                        244     DELETE_FAST                     1: ex
                        246     RETURN_CONST                    0: None
                        248     LOAD_CONST                      0: None
                        250     STORE_FAST                      1: ex
                        252     DELETE_FAST                     1: ex
                        254     RERAISE                         1
                        256     RERAISE                         0
                        258     COPY                            3
                        260     POP_EXCEPT
                        262     RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: save_lua_script
                    Qualified Name: LuaScriptMaker.save_lua_script
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'auto_fill_fields'
                        'process_primary_appid'
                        'save_dir'
                        'QMessageBox'
                        'warning'
                        'script_lines'
                        're'
                        'search'
                        'group'
                        'get_game_name_from_primary'
                        'sub'
                        'Path'
                        'mkdir'
                        'Exception'
                        'critical'
                        'str'
                        'open'
                        'write'
                        'added_ids'
                        'copy_manifest_files'
                        'any'
                        'os'
                        'listdir'
                        'copy_fallback_manifest'
                        'copy_bin_files'
                        'copy_achievement_bin_files'
                        'create_zip_archive'
                        'zipfile'
                        'ZipFile'
                        'testzip'
                        'logging'
                        'exception'
                        'shutil'
                        'rmtree'
                        'information'
                    [Locals+Names]
                        'self'
                        'first_line'
                        'match'
                        'primary'
                        'game_name'
                        'game_name_sanitized'
                        'folder_name'
                        'target_folder'
                        'e'
                        'lua_file'
                        'f'
                        'line'
                        'zip_path'
                        'zipf'
                        'aid'
                    [Constants]
                        None
                        'Save Error'
                        'Please set the Save directory first.'
                        'Input Error'
                        'No AppID data to save.'
                        0
                        'addappid\\((\\d+)\\)'
                        'Error'
                        'Could not extract AppID from script.'
                        1
                        '[\\\\/*?:"<>|]'
                        ''
                        '_'
                        True
                        (
                            'parents'
                            'exist_ok'
                        )
                        'Folder Error'
                        'Could not create folder: '
                        '.lua'
                        'w'
                        'utf-8'
                        (
                            'encoding'
                        )
                        '\n'
                        'File Error'
                        'Error saving Lua script: '
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: <genexpr>
                            Qualified Name: LuaScriptMaker.save_lua_script.<locals>.<genexpr>
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 5
                            Flags: 0x00000033 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED | CO_GENERATOR)
                            [Names]
                                'startswith'
                            [Locals+Names]
                                '.0'
                                'fname'
                                'aid'
                            [Constants]
                                '_'
                                None
                            [Disassembly]
                                0       COPY_FREE_VARS                  1
                                2       RETURN_GENERATOR
                                4       POP_TOP
                                6       RESUME                          0
                                8       LOAD_FAST                       0: .0
                                10      GET_ITER
                                12      FOR_ITER                        24 (to 62)
                                16      STORE_FAST_LOAD_FAST            17: fname, fname
                                18      LOAD_ATTR                       1: startswith
                                38      LOAD_DEREF                      2: aid
                                40      FORMAT_SIMPLE
                                42      LOAD_CONST                      0: '_'
                                44      BUILD_STRING                    2
                                46      CALL                            1
                                54      YIELD_VALUE                     0
                                56      RESUME                          5
                                58      POP_TOP
                                60      JUMP_BACKWARD                   26 (to 10)
                                64      END_FOR
                                66      POP_TOP
                                68      RETURN_CONST                    1: None
                                70      CALL_INTRINSIC_1                3 (INTRINSIC_STOPITERATION_ERROR)
                                72      RERAISE                         1
                        'r'
                        'Zip Error'
                        'Zip archive appears corrupted: '
                        'Zip archive error:'
                        'Failed to delete folder %s: %s'
                        'Success'
                        'Files saved and zipped successfully:\n'
                        'Failed to create zip archive.'
                    [Disassembly]
                        0       MAKE_CELL                       14: aid
                        2       RESUME                          0
                        4       LOAD_FAST                       0: self
                        6       LOAD_ATTR                       1: auto_fill_fields
                        26      CALL                            0
                        34      POP_TOP
                        36      LOAD_FAST                       0: self
                        38      LOAD_ATTR                       3: process_primary_appid
                        58      CALL                            0
                        66      POP_TOP
                        68      LOAD_FAST                       0: self
                        70      LOAD_ATTR                       4: save_dir
                        90      TO_BOOL
                        98      POP_JUMP_IF_TRUE                25 (to 150)
                        102     LOAD_GLOBAL                     6: QMessageBox
                        112     LOAD_ATTR                       8: warning
                        132     PUSH_NULL
                        134     LOAD_FAST                       0: self
                        136     LOAD_CONST                      1: 'Save Error'
                        138     LOAD_CONST                      2: 'Please set the Save directory first.'
                        140     CALL                            3
                        148     POP_TOP
                        150     RETURN_CONST                    0: None
                        152     LOAD_FAST                       0: self
                        154     LOAD_ATTR                       10: script_lines
                        174     TO_BOOL
                        182     POP_JUMP_IF_TRUE                25 (to 234)
                        186     LOAD_GLOBAL                     6: QMessageBox
                        196     LOAD_ATTR                       8: warning
                        216     PUSH_NULL
                        218     LOAD_FAST                       0: self
                        220     LOAD_CONST                      3: 'Input Error'
                        222     LOAD_CONST                      4: 'No AppID data to save.'
                        224     CALL                            3
                        232     POP_TOP
                        234     RETURN_CONST                    0: None
                        236     LOAD_FAST                       0: self
                        238     LOAD_ATTR                       10: script_lines
                        258     LOAD_CONST                      5: 0
                        260     BINARY_SUBSCR
                        264     STORE_FAST                      1: first_line
                        266     LOAD_GLOBAL                     12: re
                        276     LOAD_ATTR                       14: search
                        296     PUSH_NULL
                        298     LOAD_CONST                      6: 'addappid\\((\\d+)\\)'
                        300     LOAD_FAST                       1: first_line
                        302     CALL                            2
                        310     STORE_FAST                      2: match
                        312     LOAD_FAST                       2: match
                        314     TO_BOOL
                        322     POP_JUMP_IF_TRUE                25 (to 374)
                        326     LOAD_GLOBAL                     6: QMessageBox
                        336     LOAD_ATTR                       8: warning
                        356     PUSH_NULL
                        358     LOAD_FAST                       0: self
                        360     LOAD_CONST                      7: 'Error'
                        362     LOAD_CONST                      8: 'Could not extract AppID from script.'
                        364     CALL                            3
                        372     POP_TOP
                        374     RETURN_CONST                    0: None
                        376     LOAD_FAST                       2: match
                        378     LOAD_ATTR                       17: group
                        398     LOAD_CONST                      9: 1
                        400     CALL                            1
                        408     STORE_FAST                      3: primary
                        410     LOAD_FAST                       0: self
                        412     LOAD_ATTR                       19: get_game_name_from_primary
                        432     LOAD_FAST                       3: primary
                        434     CALL                            1
                        442     STORE_FAST                      4: game_name
                        444     LOAD_GLOBAL                     12: re
                        454     LOAD_ATTR                       20: sub
                        474     PUSH_NULL
                        476     LOAD_CONST                      10: '[\\\\/*?:"<>|]'
                        478     LOAD_CONST                      11: ''
                        480     LOAD_FAST                       4: game_name
                        482     CALL                            3
                        490     STORE_FAST                      5: game_name_sanitized
                        492     LOAD_FAST                       3: primary
                        494     FORMAT_SIMPLE
                        496     LOAD_CONST                      12: '_'
                        498     LOAD_FAST                       5: game_name_sanitized
                        500     FORMAT_SIMPLE
                        502     BUILD_STRING                    3
                        504     STORE_FAST                      6: folder_name
                        506     LOAD_GLOBAL                     23: NULL + Path
                        516     LOAD_FAST                       0: self
                        518     LOAD_ATTR                       4: save_dir
                        538     CALL                            1
                        546     LOAD_FAST                       6: folder_name
                        548     BINARY_OP                       11 (/)
                        552     STORE_FAST                      7: target_folder
                        554     NOP
                        556     LOAD_FAST                       7: target_folder
                        558     LOAD_ATTR                       25: mkdir
                        578     LOAD_CONST                      13: True
                        580     LOAD_CONST                      13: True
                        582     LOAD_CONST                      14: ('parents', 'exist_ok')
                        584     CALL_KW                         2
                        586     POP_TOP
                        588     LOAD_FAST_LOAD_FAST             115: target_folder, primary
                        590     FORMAT_SIMPLE
                        592     LOAD_CONST                      17: '.lua'
                        594     BUILD_STRING                    2
                        596     BINARY_OP                       11 (/)
                        600     STORE_FAST                      9: lua_file
                        602     NOP
                        604     LOAD_FAST                       9: lua_file
                        606     LOAD_ATTR                       33: open
                        626     LOAD_CONST                      18: 'w'
                        628     LOAD_CONST                      19: 'utf-8'
                        630     LOAD_CONST                      20: ('encoding',)
                        632     CALL_KW                         2
                        634     BEFORE_WITH
                        636     STORE_FAST                      10: f
                        638     LOAD_FAST                       0: self
                        640     LOAD_ATTR                       10: script_lines
                        660     GET_ITER
                        662     FOR_ITER                        23 (to 710)
                        666     STORE_FAST                      11: line
                        668     LOAD_FAST                       10: f
                        670     LOAD_ATTR                       35: write
                        690     LOAD_FAST                       11: line
                        692     LOAD_CONST                      21: '\n'
                        694     BINARY_OP                       0 (+)
                        698     CALL                            1
                        706     POP_TOP
                        708     JUMP_BACKWARD                   25 (to 660)
                        712     END_FOR
                        714     POP_TOP
                        716     LOAD_CONST                      0: None
                        718     LOAD_CONST                      0: None
                        720     LOAD_CONST                      0: None
                        722     CALL                            2
                        730     POP_TOP
                        732     LOAD_FAST                       0: self
                        734     LOAD_ATTR                       36: added_ids
                        754     GET_ITER
                        756     FOR_ITER                        121 (to 1000)
                        760     STORE_DEREF                     14: aid
                        762     LOAD_FAST                       0: self
                        764     LOAD_ATTR                       39: copy_manifest_files
                        784     LOAD_FAST                       7: target_folder
                        786     LOAD_DEREF                      14: aid
                        788     CALL                            2
                        796     POP_TOP
                        798     LOAD_GLOBAL                     41: NULL + any
                        808     LOAD_FAST                       14: aid
                        810     BUILD_TUPLE                     1
                        812     LOAD_CONST                      24: <CODE> <genexpr>
                        814     MAKE_FUNCTION
                        816     SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        818     LOAD_GLOBAL                     42: os
                        828     LOAD_ATTR                       44: listdir
                        848     PUSH_NULL
                        850     LOAD_FAST                       7: target_folder
                        852     CALL                            1
                        860     GET_ITER
                        862     CALL                            0
                        870     CALL                            1
                        878     TO_BOOL
                        886     POP_JUMP_IF_TRUE                18 (to 924)
                        890     LOAD_FAST                       0: self
                        892     LOAD_ATTR                       47: copy_fallback_manifest
                        912     LOAD_FAST                       7: target_folder
                        914     LOAD_DEREF                      14: aid
                        916     CALL                            2
                        924     POP_TOP
                        926     LOAD_FAST                       0: self
                        928     LOAD_ATTR                       49: copy_bin_files
                        948     LOAD_FAST                       7: target_folder
                        950     LOAD_DEREF                      14: aid
                        952     CALL                            2
                        960     POP_TOP
                        962     LOAD_FAST                       0: self
                        964     LOAD_ATTR                       51: copy_achievement_bin_files
                        984     LOAD_FAST                       7: target_folder
                        986     LOAD_DEREF                      14: aid
                        988     CALL                            2
                        996     POP_TOP
                        998     JUMP_BACKWARD                   123 (to 754)
                        1002    END_FOR
                        1004    POP_TOP
                        1006    LOAD_FAST                       0: self
                        1008    LOAD_ATTR                       53: create_zip_archive
                        1028    LOAD_FAST                       7: target_folder
                        1030    CALL                            1
                        1038    STORE_FAST                      12: zip_path
                        1040    LOAD_FAST                       12: zip_path
                        1042    TO_BOOL
                        1050    POP_JUMP_IF_FALSE               100 (to 1252)
                        1054    NOP
                        1056    LOAD_GLOBAL                     54: zipfile
                        1066    LOAD_ATTR                       56: ZipFile
                        1086    PUSH_NULL
                        1088    LOAD_FAST                       12: zip_path
                        1090    LOAD_CONST                      25: 'r'
                        1092    CALL                            2
                        1100    BEFORE_WITH
                        1102    STORE_FAST                      13: zipf
                        1104    LOAD_FAST                       13: zipf
                        1106    LOAD_ATTR                       59: testzip
                        1126    CALL                            0
                        1134    POP_TOP
                        1136    LOAD_CONST                      0: None
                        1138    LOAD_CONST                      0: None
                        1140    LOAD_CONST                      0: None
                        1142    CALL                            2
                        1150    POP_TOP
                        1152    NOP
                        1154    LOAD_GLOBAL                     64: shutil
                        1164    LOAD_ATTR                       66: rmtree
                        1184    PUSH_NULL
                        1186    LOAD_FAST                       7: target_folder
                        1188    CALL                            1
                        1196    POP_TOP
                        1198    LOAD_GLOBAL                     6: QMessageBox
                        1208    LOAD_ATTR                       68: information
                        1228    PUSH_NULL
                        1230    LOAD_FAST                       0: self
                        1232    LOAD_CONST                      30: 'Success'
                        1234    LOAD_CONST                      31: 'Files saved and zipped successfully:\n'
                        1236    LOAD_FAST                       12: zip_path
                        1238    FORMAT_SIMPLE
                        1240    BUILD_STRING                    2
                        1242    CALL                            3
                        1250    POP_TOP
                        1252    RETURN_CONST                    0: None
                        1254    LOAD_GLOBAL                     6: QMessageBox
                        1264    LOAD_ATTR                       8: warning
                        1284    PUSH_NULL
                        1286    LOAD_FAST                       0: self
                        1288    LOAD_CONST                      26: 'Zip Error'
                        1290    LOAD_CONST                      32: 'Failed to create zip archive.'
                        1292    CALL                            3
                        1300    POP_TOP
                        1302    RETURN_CONST                    0: None
                        1304    PUSH_EXC_INFO
                        1306    LOAD_GLOBAL                     26: Exception
                        1316    CHECK_EXC_MATCH
                        1318    POP_JUMP_IF_FALSE               46 (to 1412)
                        1322    STORE_FAST                      8: e
                        1324    LOAD_GLOBAL                     6: QMessageBox
                        1334    LOAD_ATTR                       28: critical
                        1354    PUSH_NULL
                        1356    LOAD_FAST                       0: self
                        1358    LOAD_CONST                      15: 'Folder Error'
                        1360    LOAD_CONST                      16: 'Could not create folder: '
                        1362    LOAD_GLOBAL                     31: NULL + str
                        1372    LOAD_FAST                       8: e
                        1374    CALL                            1
                        1382    FORMAT_SIMPLE
                        1384    BUILD_STRING                    2
                        1386    CALL                            3
                        1394    POP_TOP
                        1396    POP_EXCEPT
                        1398    LOAD_CONST                      0: None
                        1400    STORE_FAST                      8: e
                        1402    DELETE_FAST                     8: e
                        1404    RETURN_CONST                    0: None
                        1406    LOAD_CONST                      0: None
                        1408    STORE_FAST                      8: e
                        1410    DELETE_FAST                     8: e
                        1412    RERAISE                         1
                        1414    RERAISE                         0
                        1416    COPY                            3
                        1418    POP_EXCEPT
                        1420    RERAISE                         1
                        1422    PUSH_EXC_INFO
                        1424    WITH_EXCEPT_START
                        1426    TO_BOOL
                        1434    POP_JUMP_IF_TRUE                1 (to 1438)
                        1438    RERAISE                         2
                        1440    POP_TOP
                        1442    POP_EXCEPT
                        1444    POP_TOP
                        1446    POP_TOP
                        1448    JUMP_BACKWARD_NO_INTERRUPT      360 (to 732)
                        1452    COPY                            3
                        1454    POP_EXCEPT
                        1456    RERAISE                         1
                        1458    PUSH_EXC_INFO
                        1460    LOAD_GLOBAL                     26: Exception
                        1470    CHECK_EXC_MATCH
                        1472    POP_JUMP_IF_FALSE               46 (to 1566)
                        1476    STORE_FAST                      8: e
                        1478    LOAD_GLOBAL                     6: QMessageBox
                        1488    LOAD_ATTR                       28: critical
                        1508    PUSH_NULL
                        1510    LOAD_FAST                       0: self
                        1512    LOAD_CONST                      22: 'File Error'
                        1514    LOAD_CONST                      23: 'Error saving Lua script: '
                        1516    LOAD_GLOBAL                     31: NULL + str
                        1526    LOAD_FAST                       8: e
                        1528    CALL                            1
                        1536    FORMAT_SIMPLE
                        1538    BUILD_STRING                    2
                        1540    CALL                            3
                        1548    POP_TOP
                        1550    POP_EXCEPT
                        1552    LOAD_CONST                      0: None
                        1554    STORE_FAST                      8: e
                        1556    DELETE_FAST                     8: e
                        1558    RETURN_CONST                    0: None
                        1560    LOAD_CONST                      0: None
                        1562    STORE_FAST                      8: e
                        1564    DELETE_FAST                     8: e
                        1566    RERAISE                         1
                        1568    RERAISE                         0
                        1570    COPY                            3
                        1572    POP_EXCEPT
                        1574    RERAISE                         1
                        1576    PUSH_EXC_INFO
                        1578    WITH_EXCEPT_START
                        1580    TO_BOOL
                        1588    POP_JUMP_IF_TRUE                1 (to 1592)
                        1592    RERAISE                         2
                        1594    POP_TOP
                        1596    POP_EXCEPT
                        1598    POP_TOP
                        1600    POP_TOP
                        1602    JUMP_BACKWARD_NO_INTERRUPT      226 (to 1152)
                        1604    COPY                            3
                        1606    POP_EXCEPT
                        1608    RERAISE                         1
                        1610    PUSH_EXC_INFO
                        1612    LOAD_GLOBAL                     26: Exception
                        1622    CHECK_EXC_MATCH
                        1624    POP_JUMP_IF_FALSE               68 (to 1762)
                        1628    STORE_FAST                      8: e
                        1630    LOAD_GLOBAL                     6: QMessageBox
                        1640    LOAD_ATTR                       8: warning
                        1660    PUSH_NULL
                        1662    LOAD_FAST                       0: self
                        1664    LOAD_CONST                      26: 'Zip Error'
                        1666    LOAD_CONST                      27: 'Zip archive appears corrupted: '
                        1668    LOAD_GLOBAL                     31: NULL + str
                        1678    LOAD_FAST                       8: e
                        1680    CALL                            1
                        1688    FORMAT_SIMPLE
                        1690    BUILD_STRING                    2
                        1692    CALL                            3
                        1700    POP_TOP
                        1702    LOAD_GLOBAL                     60: logging
                        1712    LOAD_ATTR                       62: exception
                        1732    PUSH_NULL
                        1734    LOAD_CONST                      28: 'Zip archive error:'
                        1736    CALL                            1
                        1744    POP_TOP
                        1746    POP_EXCEPT
                        1748    LOAD_CONST                      0: None
                        1750    STORE_FAST                      8: e
                        1752    DELETE_FAST                     8: e
                        1754    RETURN_CONST                    0: None
                        1756    LOAD_CONST                      0: None
                        1758    STORE_FAST                      8: e
                        1760    DELETE_FAST                     8: e
                        1762    RERAISE                         1
                        1764    RERAISE                         0
                        1766    COPY                            3
                        1768    POP_EXCEPT
                        1770    RERAISE                         1
                        1772    PUSH_EXC_INFO
                        1774    LOAD_GLOBAL                     26: Exception
                        1784    CHECK_EXC_MATCH
                        1786    POP_JUMP_IF_FALSE               44 (to 1876)
                        1790    STORE_FAST                      8: e
                        1792    LOAD_GLOBAL                     60: logging
                        1802    LOAD_ATTR                       8: warning
                        1822    PUSH_NULL
                        1824    LOAD_CONST                      29: 'Failed to delete folder %s: %s'
                        1826    LOAD_FAST                       7: target_folder
                        1828    LOAD_GLOBAL                     31: NULL + str
                        1838    LOAD_FAST                       8: e
                        1840    CALL                            1
                        1848    CALL                            3
                        1856    POP_TOP
                        1858    POP_EXCEPT
                        1860    LOAD_CONST                      0: None
                        1862    STORE_FAST                      8: e
                        1864    DELETE_FAST                     8: e
                        1866    JUMP_BACKWARD_NO_INTERRUPT      336 (to 1198)
                        1870    LOAD_CONST                      0: None
                        1872    STORE_FAST                      8: e
                        1874    DELETE_FAST                     8: e
                        1876    RERAISE                         1
                        1878    RERAISE                         0
                        1880    COPY                            3
                        1882    POP_EXCEPT
                        1884    RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: remove_game_handler
                    Qualified Name: LuaScriptMaker.remove_game_handler
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 8
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'input_remove'
                        'text'
                        'strip'
                        'QMessageBox'
                        'warning'
                        'steam_dir'
                        'remove_game'
                        'information'
                        'len'
                    [Locals+Names]
                        'self'
                        'identifier'
                        'removed'
                    [Constants]
                        None
                        'Input Error'
                        'Please enter a Game Name or AppID.'
                        'Directory Error'
                        'Please set the Steam directory first.'
                        'Removal Completed'
                        'Removed '
                        ' item(s) from your Steam installation.'
                        'Not Found'
                        'No game found matching the identifier.'
                    [Disassembly]
                        0       RESUME                          0
                        2       LOAD_FAST                       0: self
                        4       LOAD_ATTR                       0: input_remove
                        24      LOAD_ATTR                       3: text
                        44      CALL                            0
                        52      LOAD_ATTR                       5: strip
                        72      CALL                            0
                        80      STORE_FAST                      1: identifier
                        82      LOAD_FAST                       1: identifier
                        84      TO_BOOL
                        92      POP_JUMP_IF_TRUE                25 (to 144)
                        96      LOAD_GLOBAL                     6: QMessageBox
                        106     LOAD_ATTR                       8: warning
                        126     PUSH_NULL
                        128     LOAD_FAST                       0: self
                        130     LOAD_CONST                      1: 'Input Error'
                        132     LOAD_CONST                      2: 'Please enter a Game Name or AppID.'
                        134     CALL                            3
                        142     POP_TOP
                        144     RETURN_CONST                    0: None
                        146     LOAD_FAST                       0: self
                        148     LOAD_ATTR                       10: steam_dir
                        168     TO_BOOL
                        176     POP_JUMP_IF_TRUE                25 (to 228)
                        180     LOAD_GLOBAL                     6: QMessageBox
                        190     LOAD_ATTR                       8: warning
                        210     PUSH_NULL
                        212     LOAD_FAST                       0: self
                        214     LOAD_CONST                      3: 'Directory Error'
                        216     LOAD_CONST                      4: 'Please set the Steam directory first.'
                        218     CALL                            3
                        226     POP_TOP
                        228     RETURN_CONST                    0: None
                        230     LOAD_FAST                       0: self
                        232     LOAD_ATTR                       13: remove_game
                        252     LOAD_FAST                       1: identifier
                        254     CALL                            1
                        262     STORE_FAST                      2: removed
                        264     LOAD_FAST                       2: removed
                        266     TO_BOOL
                        274     POP_JUMP_IF_FALSE               38 (to 352)
                        278     LOAD_GLOBAL                     6: QMessageBox
                        288     LOAD_ATTR                       14: information
                        308     PUSH_NULL
                        310     LOAD_FAST                       0: self
                        312     LOAD_CONST                      5: 'Removal Completed'
                        314     LOAD_CONST                      6: 'Removed '
                        316     LOAD_GLOBAL                     17: NULL + len
                        326     LOAD_FAST                       2: removed
                        328     CALL                            1
                        336     FORMAT_SIMPLE
                        338     LOAD_CONST                      7: ' item(s) from your Steam installation.'
                        340     BUILD_STRING                    3
                        342     CALL                            3
                        350     POP_TOP
                        352     RETURN_CONST                    0: None
                        354     LOAD_GLOBAL                     6: QMessageBox
                        364     LOAD_ATTR                       14: information
                        384     PUSH_NULL
                        386     LOAD_FAST                       0: self
                        388     LOAD_CONST                      8: 'Not Found'
                        390     LOAD_CONST                      9: 'No game found matching the identifier.'
                        392     CALL                            3
                        400     POP_TOP
                        402     RETURN_CONST                    0: None
                'identifier'
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: remove_game
                    Qualified Name: LuaScriptMaker.remove_game
                    Arg Count: 2
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 10
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'set'
                        'Path'
                        'str'
                        'isdigit'
                        'fetch_depot_ids_from_steamdb'
                        'get_library_folders'
                        'glob'
                        'read_text'
                        'lower'
                        'parse_appmanifest'
                        'get'
                        'steam_dir'
                        'exists'
                        'iterdir'
                        'name'
                        'save_dir'
                        'is_dir'
                        'shutil'
                        'rmtree'
                        'append'
                        'log_removal'
                        'Exception'
                    [Locals+Names]
                        'self'
                        'identifier'
                        'process_appid'
                        'main_appid'
                        'depot_ids'
                        'depot'
                        'libraries'
                        'lib'
                        'manifest_path'
                        'content'
                        'app_data'
                        'appid'
                        'stplugin'
                        'file'
                        'depotcache'
                        'save_path'
                        'folder'
                        'e'
                        'processed_ids'
                        'remove_extra_files'
                        'remove_from_stplugin'
                        'removed_items'
                        'safe_delete'
                    [Constants]
                        None
                        'file_path'
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: safe_delete
                            Qualified Name: LuaScriptMaker.remove_game.<locals>.safe_delete
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 9
                            Flags: 0x00000013 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED)
                            [Names]
                                'exists'
                                'unlink'
                                'append'
                                'str'
                                'log_removal'
                                'Exception'
                            [Locals+Names]
                                'file_path'
                                'e'
                                'removed_items'
                                'self'
                            [Constants]
                                None
                                'Removed file: '
                                'Error removing file '
                                ': '
                            [Disassembly]
                                0       COPY_FREE_VARS                  2
                                2       RESUME                          0
                                4       LOAD_FAST                       0: file_path
                                6       LOAD_ATTR                       1: exists
                                26      CALL                            0
                                34      TO_BOOL
                                42      POP_JUMP_IF_FALSE               64 (to 172)
                                46      NOP
                                48      LOAD_FAST                       0: file_path
                                50      LOAD_ATTR                       3: unlink
                                70      CALL                            0
                                78      POP_TOP
                                80      LOAD_DEREF                      2: removed_items
                                82      LOAD_ATTR                       5: append
                                102     LOAD_GLOBAL                     7: NULL + str
                                112     LOAD_FAST                       0: file_path
                                114     CALL                            1
                                122     CALL                            1
                                130     POP_TOP
                                132     LOAD_DEREF                      3: self
                                134     LOAD_ATTR                       9: log_removal
                                154     LOAD_CONST                      1: 'Removed file: '
                                156     LOAD_FAST                       0: file_path
                                158     FORMAT_SIMPLE
                                160     BUILD_STRING                    2
                                162     CALL                            1
                                170     POP_TOP
                                172     RETURN_CONST                    0: None
                                174     RETURN_CONST                    0: None
                                176     PUSH_EXC_INFO
                                178     LOAD_GLOBAL                     10: Exception
                                188     CHECK_EXC_MATCH
                                190     POP_JUMP_IF_FALSE               42 (to 276)
                                194     STORE_FAST                      1: e
                                196     LOAD_DEREF                      3: self
                                198     LOAD_ATTR                       9: log_removal
                                218     LOAD_CONST                      2: 'Error removing file '
                                220     LOAD_FAST                       0: file_path
                                222     FORMAT_SIMPLE
                                224     LOAD_CONST                      3: ': '
                                226     LOAD_GLOBAL                     7: NULL + str
                                236     LOAD_FAST                       1: e
                                238     CALL                            1
                                246     FORMAT_SIMPLE
                                248     BUILD_STRING                    4
                                250     CALL                            1
                                258     POP_TOP
                                260     POP_EXCEPT
                                262     LOAD_CONST                      0: None
                                264     STORE_FAST                      1: e
                                266     DELETE_FAST                     1: e
                                268     RETURN_CONST                    0: None
                                270     LOAD_CONST                      0: None
                                272     STORE_FAST                      1: e
                                274     DELETE_FAST                     1: e
                                276     RERAISE                         1
                                278     RERAISE                         0
                                280     COPY                            3
                                282     POP_EXCEPT
                                284     RERAISE                         1
                        'folder'
                        'appid'
                        'ext'
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: remove_extra_files
                            Qualified Name: LuaScriptMaker.remove_game.<locals>.remove_extra_files
                            Arg Count: 3
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 3
                            Flags: 0x00000013 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED)
                            [Names]
                            [Locals+Names]
                                'folder'
                                'appid'
                                'ext'
                                'target'
                                'safe_delete'
                            [Constants]
                                None
                            [Disassembly]
                                0       COPY_FREE_VARS                  1
                                2       RESUME                          0
                                4       LOAD_FAST_LOAD_FAST             1: folder, appid
                                6       FORMAT_SIMPLE
                                8       LOAD_FAST                       2: ext
                                10      FORMAT_SIMPLE
                                12      BUILD_STRING                    2
                                14      BINARY_OP                       11 (/)
                                18      STORE_FAST                      3: target
                                20      LOAD_DEREF                      4: safe_delete
                                22      PUSH_NULL
                                24      LOAD_FAST                       3: target
                                26      CALL                            1
                                34      POP_TOP
                                36      RETURN_CONST                    0: None
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: remove_from_stplugin
                            Qualified Name: LuaScriptMaker.remove_game.<locals>.remove_from_stplugin
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 4
                            Flags: 0x00000013 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED)
                            [Names]
                                'Path'
                                'steam_dir'
                                'exists'
                                'iterdir'
                                'name'
                            [Locals+Names]
                                'appid'
                                'stplugin'
                                'file'
                                'safe_delete'
                                'self'
                            [Constants]
                                None
                                'config'
                                'stplug-in'
                            [Disassembly]
                                0       COPY_FREE_VARS                  2
                                2       RESUME                          0
                                4       LOAD_GLOBAL                     1: NULL + Path
                                14      LOAD_DEREF                      4: self
                                16      LOAD_ATTR                       2: steam_dir
                                36      CALL                            1
                                44      LOAD_CONST                      1: 'config'
                                46      BINARY_OP                       11 (/)
                                50      LOAD_CONST                      2: 'stplug-in'
                                52      BINARY_OP                       11 (/)
                                56      STORE_FAST                      1: stplugin
                                58      LOAD_FAST                       1: stplugin
                                60      LOAD_ATTR                       5: exists
                                80      CALL                            0
                                88      TO_BOOL
                                96      POP_JUMP_IF_FALSE               49 (to 196)
                                100     LOAD_FAST                       1: stplugin
                                102     LOAD_ATTR                       7: iterdir
                                122     CALL                            0
                                130     GET_ITER
                                132     FOR_ITER                        28 (to 190)
                                136     STORE_FAST                      2: file
                                138     LOAD_FAST_LOAD_FAST             2: appid, file
                                140     LOAD_ATTR                       8: name
                                160     CONTAINS_OP                     0 (in)
                                164     POP_JUMP_IF_TRUE                2 (to 170)
                                168     JUMP_BACKWARD                   20 (to 130)
                                172     LOAD_DEREF                      3: safe_delete
                                174     PUSH_NULL
                                176     LOAD_FAST                       2: file
                                178     CALL                            1
                                186     POP_TOP
                                188     JUMP_BACKWARD                   30 (to 130)
                                192     END_FOR
                                194     POP_TOP
                                196     RETURN_CONST                    0: None
                                198     RETURN_CONST                    0: None
                        [Code]
                            File Name: LuaMaker_NahBro3.py
                            Object Name: process_appid
                            Qualified Name: LuaScriptMaker.remove_game.<locals>.process_appid
                            Arg Count: 1
                            Pos Only Arg Count: 0
                            KW Only Arg Count: 0
                            Stack Size: 10
                            Flags: 0x00000013 (CO_OPTIMIZED | CO_NEWLOCALS | CO_NESTED)
                            [Names]
                                'add'
                                'get_library_folders'
                                'exists'
                                'parse_acf_file'
                                'shutil'
                                'rmtree'
                                'append'
                                'str'
                                'log_removal'
                                'Exception'
                                'steam_dir'
                                'Path'
                                'glob'
                                'os'
                                'listdir'
                                're'
                                'match'
                            [Locals+Names]
                                'appid'
                                'libraries'
                                'found'
                                'lib'
                                'manifest_path'
                                'installdir'
                                'game_install_dir'
                                'e'
                                'steam_path'
                                'depotcache'
                                'file'
                                'stats'
                                'ach'
                                'processed_ids'
                                'remove_extra_files'
                                'remove_from_stplugin'
                                'removed_items'
                                'safe_delete'
                                'self'
                            [Constants]
                                None
                                False
                                'appmanifest_'
                                '.acf'
                                True
                                'common'
                                'Removed installation folder: '
                                'Error removing installation folder '
                                ': '
                                '.lua'
                                '.st'
                                'depotcache'
                                '_*.manifest'
                                'appcache'
                                'stats'
                                '.*_'
                                '(?:_\\d+)?\\.bin$'
                                'achievements'
                            [Disassembly]
                                0       COPY_FREE_VARS                  6
                                2       RESUME                          0
                                4       LOAD_FAST                       0: appid
                                6       LOAD_DEREF                      13: processed_ids
                                8       CONTAINS_OP                     0 (in)
                                12      POP_JUMP_IF_FALSE               1 (to 16)
                                16      RETURN_CONST                    0: None
                                18      LOAD_DEREF                      13: processed_ids
                                20      LOAD_ATTR                       1: add
                                40      LOAD_FAST                       0: appid
                                42      CALL                            1
                                50      POP_TOP
                                52      LOAD_DEREF                      18: self
                                54      LOAD_ATTR                       3: get_library_folders
                                74      CALL                            0
                                82      STORE_FAST                      1: libraries
                                84      LOAD_CONST                      1: False
                                86      STORE_FAST                      2: found
                                88      LOAD_FAST                       1: libraries
                                90      GET_ITER
                                92      FOR_ITER                        189 (to 472)
                                96      STORE_FAST                      3: lib
                                98      LOAD_FAST                       3: lib
                                100     LOAD_CONST                      2: 'appmanifest_'
                                102     LOAD_FAST                       0: appid
                                104     FORMAT_SIMPLE
                                106     LOAD_CONST                      3: '.acf'
                                108     BUILD_STRING                    3
                                110     BINARY_OP                       11 (/)
                                114     STORE_FAST                      4: manifest_path
                                116     LOAD_FAST                       4: manifest_path
                                118     LOAD_ATTR                       5: exists
                                138     CALL                            0
                                146     TO_BOOL
                                154     POP_JUMP_IF_TRUE                2 (to 160)
                                158     JUMP_BACKWARD                   35 (to 90)
                                162     LOAD_CONST                      4: True
                                164     STORE_FAST                      2: found
                                166     LOAD_GLOBAL                     7: NULL + parse_acf_file
                                176     LOAD_FAST                       4: manifest_path
                                178     CALL                            1
                                186     STORE_FAST                      5: installdir
                                188     LOAD_FAST                       5: installdir
                                190     TO_BOOL
                                198     POP_JUMP_IF_FALSE               98 (to 396)
                                202     LOAD_FAST                       3: lib
                                204     LOAD_CONST                      5: 'common'
                                206     BINARY_OP                       11 (/)
                                210     LOAD_FAST                       5: installdir
                                212     BINARY_OP                       11 (/)
                                216     STORE_FAST                      6: game_install_dir
                                218     LOAD_FAST                       6: game_install_dir
                                220     LOAD_ATTR                       5: exists
                                240     CALL                            0
                                248     TO_BOOL
                                256     POP_JUMP_IF_FALSE               69 (to 396)
                                260     NOP
                                262     LOAD_GLOBAL                     8: shutil
                                272     LOAD_ATTR                       10: rmtree
                                292     PUSH_NULL
                                294     LOAD_FAST                       6: game_install_dir
                                296     CALL                            1
                                304     POP_TOP
                                306     LOAD_DEREF                      16: removed_items
                                308     LOAD_ATTR                       13: append
                                328     LOAD_GLOBAL                     15: NULL + str
                                338     LOAD_FAST                       6: game_install_dir
                                340     CALL                            1
                                348     CALL                            1
                                356     POP_TOP
                                358     LOAD_DEREF                      18: self
                                360     LOAD_ATTR                       17: log_removal
                                380     LOAD_CONST                      6: 'Removed installation folder: '
                                382     LOAD_FAST                       6: game_install_dir
                                384     FORMAT_SIMPLE
                                386     BUILD_STRING                    2
                                388     CALL                            1
                                396     POP_TOP
                                398     LOAD_DEREF                      17: safe_delete
                                400     PUSH_NULL
                                402     LOAD_FAST                       4: manifest_path
                                404     CALL                            1
                                412     POP_TOP
                                414     LOAD_DEREF                      14: remove_extra_files
                                416     PUSH_NULL
                                418     LOAD_FAST_LOAD_FAST             48: lib, appid
                                420     LOAD_CONST                      9: '.lua'
                                422     CALL                            3
                                430     POP_TOP
                                432     LOAD_DEREF                      14: remove_extra_files
                                434     PUSH_NULL
                                436     LOAD_FAST_LOAD_FAST             48: lib, appid
                                438     LOAD_CONST                      10: '.st'
                                440     CALL                            3
                                448     POP_TOP
                                450     LOAD_DEREF                      15: remove_from_stplugin
                                452     PUSH_NULL
                                454     LOAD_FAST                       0: appid
                                456     CALL                            1
                                464     POP_TOP
                                466     LOAD_CONST                      4: True
                                468     STORE_FAST                      2: found
                                470     JUMP_BACKWARD                   191 (to 90)
                                474     END_FOR
                                476     POP_TOP
                                478     LOAD_DEREF                      18: self
                                480     LOAD_ATTR                       20: steam_dir
                                500     TO_BOOL
                                508     POP_JUMP_IF_FALSE               286 (to 1084)
                                514     LOAD_GLOBAL                     23: NULL + Path
                                524     LOAD_DEREF                      18: self
                                526     LOAD_ATTR                       20: steam_dir
                                546     CALL                            1
                                554     STORE_FAST                      8: steam_path
                                556     LOAD_FAST                       8: steam_path
                                558     LOAD_CONST                      11: 'depotcache'
                                560     BINARY_OP                       11 (/)
                                564     STORE_FAST                      9: depotcache
                                566     LOAD_FAST                       9: depotcache
                                568     LOAD_ATTR                       5: exists
                                588     CALL                            0
                                596     TO_BOOL
                                604     POP_JUMP_IF_FALSE               35 (to 676)
                                608     LOAD_FAST                       9: depotcache
                                610     LOAD_ATTR                       25: glob
                                630     LOAD_FAST                       0: appid
                                632     FORMAT_SIMPLE
                                634     LOAD_CONST                      12: '_*.manifest'
                                636     BUILD_STRING                    2
                                638     CALL                            1
                                646     GET_ITER
                                648     FOR_ITER                        11 (to 672)
                                652     STORE_FAST                      10: file
                                654     LOAD_DEREF                      17: safe_delete
                                656     PUSH_NULL
                                658     LOAD_FAST                       10: file
                                660     CALL                            1
                                668     POP_TOP
                                670     JUMP_BACKWARD                   13 (to 646)
                                674     END_FOR
                                676     POP_TOP
                                678     LOAD_FAST                       8: steam_path
                                680     LOAD_CONST                      13: 'appcache'
                                682     BINARY_OP                       11 (/)
                                686     LOAD_CONST                      14: 'stats'
                                688     BINARY_OP                       11 (/)
                                692     STORE_FAST                      11: stats
                                694     LOAD_FAST                       11: stats
                                696     LOAD_ATTR                       5: exists
                                716     CALL                            0
                                724     TO_BOOL
                                732     POP_JUMP_IF_FALSE               73 (to 880)
                                736     LOAD_GLOBAL                     26: os
                                746     LOAD_ATTR                       28: listdir
                                766     PUSH_NULL
                                768     LOAD_FAST                       11: stats
                                770     CALL                            1
                                778     GET_ITER
                                780     FOR_ITER                        47 (to 876)
                                784     STORE_FAST                      10: file
                                786     LOAD_GLOBAL                     30: re
                                796     LOAD_ATTR                       32: match
                                816     PUSH_NULL
                                818     LOAD_CONST                      15: '.*_'
                                820     LOAD_FAST                       0: appid
                                822     FORMAT_SIMPLE
                                824     LOAD_CONST                      16: '(?:_\\d+)?\\.bin$'
                                826     BUILD_STRING                    3
                                828     LOAD_FAST                       10: file
                                830     CALL                            2
                                838     TO_BOOL
                                846     POP_JUMP_IF_TRUE                2 (to 852)
                                850     JUMP_BACKWARD                   37 (to 778)
                                854     LOAD_DEREF                      17: safe_delete
                                856     PUSH_NULL
                                858     LOAD_FAST_LOAD_FAST             186: stats, file
                                860     BINARY_OP                       11 (/)
                                864     CALL                            1
                                872     POP_TOP
                                874     JUMP_BACKWARD                   49 (to 778)
                                878     END_FOR
                                880     POP_TOP
                                882     LOAD_FAST                       8: steam_path
                                884     LOAD_CONST                      13: 'appcache'
                                886     BINARY_OP                       11 (/)
                                890     LOAD_CONST                      17: 'achievements'
                                892     BINARY_OP                       11 (/)
                                896     STORE_FAST                      12: ach
                                898     LOAD_FAST                       12: ach
                                900     LOAD_ATTR                       5: exists
                                920     CALL                            0
                                928     TO_BOOL
                                936     POP_JUMP_IF_FALSE               73 (to 1084)
                                940     LOAD_GLOBAL                     26: os
                                950     LOAD_ATTR                       28: listdir
                                970     PUSH_NULL
                                972     LOAD_FAST                       12: ach
                                974     CALL                            1
                                982     GET_ITER
                                984     FOR_ITER                        47 (to 1080)
                                988     STORE_FAST                      10: file
                                990     LOAD_GLOBAL                     30: re
                                1000    LOAD_ATTR                       32: match
                                1020    PUSH_NULL
                                1022    LOAD_CONST                      15: '.*_'
                                1024    LOAD_FAST                       0: appid
                                1026    FORMAT_SIMPLE
                                1028    LOAD_CONST                      16: '(?:_\\d+)?\\.bin$'
                                1030    BUILD_STRING                    3
                                1032    LOAD_FAST                       10: file
                                1034    CALL                            2
                                1042    TO_BOOL
                                1050    POP_JUMP_IF_TRUE                2 (to 1056)
                                1054    JUMP_BACKWARD                   37 (to 982)
                                1058    LOAD_DEREF                      17: safe_delete
                                1060    PUSH_NULL
                                1062    LOAD_FAST_LOAD_FAST             202: ach, file
                                1064    BINARY_OP                       11 (/)
                                1068    CALL                            1
                                1076    POP_TOP
                                1078    JUMP_BACKWARD                   49 (to 982)
                                1082    END_FOR
                                1084    POP_TOP
                                1086    LOAD_FAST                       2: found
                                1088    RETURN_VALUE
                                1090    PUSH_EXC_INFO
                                1092    LOAD_GLOBAL                     18: Exception
                                1102    CHECK_EXC_MATCH
                                1104    POP_JUMP_IF_FALSE               43 (to 1192)
                                1108    STORE_FAST                      7: e
                                1110    LOAD_DEREF                      18: self
                                1112    LOAD_ATTR                       17: log_removal
                                1132    LOAD_CONST                      7: 'Error removing installation folder '
                                1134    LOAD_FAST                       6: game_install_dir
                                1136    FORMAT_SIMPLE
                                1138    LOAD_CONST                      8: ': '
                                1140    LOAD_GLOBAL                     15: NULL + str
                                1150    LOAD_FAST                       7: e
                                1152    CALL                            1
                                1160    FORMAT_SIMPLE
                                1162    BUILD_STRING                    4
                                1164    CALL                            1
                                1172    POP_TOP
                                1174    POP_EXCEPT
                                1176    LOAD_CONST                      0: None
                                1178    STORE_FAST                      7: e
                                1180    DELETE_FAST                     7: e
                                1182    JUMP_BACKWARD_NO_INTERRUPT      394 (to 398)
                                1186    LOAD_CONST                      0: None
                                1188    STORE_FAST                      7: e
                                1190    DELETE_FAST                     7: e
                                1192    RERAISE                         1
                                1194    RERAISE                         0
                                1196    COPY                            3
                                1198    POP_EXCEPT
                                1200    RERAISE                         1
                        'appmanifest_*.acf'
                        'utf-8'
                        (
                            'encoding'
                        )
                        ''
                        'config'
                        'stplug-in'
                        'depotcache'
                        'Removed exported folder: '
                        'Error removing exported folder '
                        ': '
                        'No game found matching the identifier.'
                    [Disassembly]
                        0       MAKE_CELL                       0: self
                        2       MAKE_CELL                       18: processed_ids
                        4       MAKE_CELL                       19: remove_extra_files
                        6       MAKE_CELL                       20: remove_from_stplugin
                        8       MAKE_CELL                       21: removed_items
                        10      MAKE_CELL                       22: safe_delete
                        12      RESUME                          0
                        14      BUILD_LIST                      0
                        16      STORE_DEREF                     21: removed_items
                        18      LOAD_GLOBAL                     1: NULL + set
                        28      CALL                            0
                        36      STORE_DEREF                     18: processed_ids
                        38      LOAD_CONST                      1: 'file_path'
                        40      LOAD_GLOBAL                     2: Path
                        50      BUILD_TUPLE                     2
                        52      LOAD_FAST                       21: removed_items
                        54      LOAD_FAST                       0: self
                        56      BUILD_TUPLE                     2
                        58      LOAD_CONST                      2: <CODE> safe_delete
                        60      MAKE_FUNCTION
                        62      SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        64      SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                        66      STORE_DEREF                     22: safe_delete
                        68      LOAD_CONST                      3: 'folder'
                        70      LOAD_GLOBAL                     2: Path
                        80      LOAD_CONST                      4: 'appid'
                        82      LOAD_GLOBAL                     4: str
                        92      LOAD_CONST                      5: 'ext'
                        94      LOAD_GLOBAL                     4: str
                        104     BUILD_TUPLE                     6
                        106     LOAD_FAST                       22: safe_delete
                        108     BUILD_TUPLE                     1
                        110     LOAD_CONST                      6: <CODE> remove_extra_files
                        112     MAKE_FUNCTION
                        114     SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        116     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                        118     STORE_DEREF                     19: remove_extra_files
                        120     LOAD_CONST                      4: 'appid'
                        122     LOAD_GLOBAL                     4: str
                        132     BUILD_TUPLE                     2
                        134     LOAD_FAST                       22: safe_delete
                        136     LOAD_FAST                       0: self
                        138     BUILD_TUPLE                     2
                        140     LOAD_CONST                      7: <CODE> remove_from_stplugin
                        142     MAKE_FUNCTION
                        144     SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        146     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                        148     STORE_DEREF                     20: remove_from_stplugin
                        150     LOAD_CONST                      4: 'appid'
                        152     LOAD_GLOBAL                     4: str
                        162     BUILD_TUPLE                     2
                        164     LOAD_FAST                       18: processed_ids
                        166     LOAD_FAST                       19: remove_extra_files
                        168     LOAD_FAST                       20: remove_from_stplugin
                        170     LOAD_FAST                       21: removed_items
                        172     LOAD_FAST                       22: safe_delete
                        174     LOAD_FAST                       0: self
                        176     BUILD_TUPLE                     6
                        178     LOAD_CONST                      8: <CODE> process_appid
                        180     MAKE_FUNCTION
                        182     SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                        184     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                        186     STORE_FAST                      2: process_appid
                        188     LOAD_FAST                       1: identifier
                        190     LOAD_ATTR                       7: isdigit
                        210     CALL                            0
                        218     TO_BOOL
                        226     POP_JUMP_IF_FALSE               46 (to 320)
                        230     LOAD_FAST                       1: identifier
                        232     STORE_FAST                      3: main_appid
                        234     LOAD_FAST                       2: process_appid
                        236     PUSH_NULL
                        238     LOAD_FAST                       3: main_appid
                        240     CALL                            1
                        248     POP_TOP
                        250     LOAD_DEREF                      0: self
                        252     LOAD_ATTR                       9: fetch_depot_ids_from_steamdb
                        272     LOAD_FAST                       3: main_appid
                        274     CALL                            1
                        282     STORE_FAST                      4: depot_ids
                        284     LOAD_FAST                       4: depot_ids
                        286     GET_ITER
                        288     FOR_ITER                        11 (to 312)
                        292     STORE_FAST                      5: depot
                        294     LOAD_FAST                       2: process_appid
                        296     PUSH_NULL
                        298     LOAD_FAST                       5: depot
                        300     CALL                            1
                        308     POP_TOP
                        310     JUMP_BACKWARD                   13 (to 286)
                        314     END_FOR
                        316     POP_TOP
                        318     JUMP_FORWARD                    603 (to 1528)
                        322     LOAD_DEREF                      0: self
                        324     LOAD_ATTR                       11: get_library_folders
                        344     CALL                            0
                        352     STORE_FAST                      6: libraries
                        354     LOAD_FAST                       6: libraries
                        356     GET_ITER
                        358     FOR_ITER                        125 (to 610)
                        362     STORE_FAST                      7: lib
                        364     LOAD_FAST                       7: lib
                        366     LOAD_ATTR                       13: glob
                        386     LOAD_CONST                      9: 'appmanifest_*.acf'
                        388     CALL                            1
                        396     GET_ITER
                        398     FOR_ITER                        101 (to 602)
                        402     STORE_FAST                      8: manifest_path
                        404     NOP
                        406     LOAD_FAST                       8: manifest_path
                        408     LOAD_ATTR                       15: read_text
                        428     LOAD_CONST                      10: 'utf-8'
                        430     LOAD_CONST                      11: ('encoding',)
                        432     CALL_KW                         1
                        434     LOAD_ATTR                       17: lower
                        454     CALL                            0
                        462     STORE_FAST                      9: content
                        464     LOAD_FAST                       1: identifier
                        466     LOAD_ATTR                       17: lower
                        486     CALL                            0
                        494     LOAD_FAST                       9: content
                        496     CONTAINS_OP                     0 (in)
                        500     POP_JUMP_IF_TRUE                2 (to 506)
                        504     JUMP_BACKWARD                   55 (to 396)
                        508     LOAD_GLOBAL                     19: NULL + parse_appmanifest
                        518     LOAD_FAST                       8: manifest_path
                        520     CALL                            1
                        528     STORE_FAST                      10: app_data
                        530     LOAD_FAST                       10: app_data
                        532     LOAD_ATTR                       21: get
                        552     LOAD_CONST                      4: 'appid'
                        554     LOAD_CONST                      12: ''
                        556     CALL                            2
                        564     STORE_FAST                      11: appid
                        566     LOAD_FAST                       11: appid
                        568     TO_BOOL
                        576     POP_JUMP_IF_TRUE                2 (to 582)
                        580     JUMP_BACKWARD                   93 (to 396)
                        584     LOAD_FAST                       2: process_appid
                        586     PUSH_NULL
                        588     LOAD_FAST                       11: appid
                        590     CALL                            1
                        598     POP_TOP
                        600     JUMP_BACKWARD                   103 (to 396)
                        604     END_FOR
                        606     POP_TOP
                        608     JUMP_BACKWARD                   127 (to 356)
                        612     END_FOR
                        614     POP_TOP
                        616     LOAD_GLOBAL                     3: NULL + Path
                        626     LOAD_DEREF                      0: self
                        628     LOAD_ATTR                       22: steam_dir
                        648     CALL                            1
                        656     LOAD_CONST                      13: 'config'
                        658     BINARY_OP                       11 (/)
                        662     LOAD_CONST                      14: 'stplug-in'
                        664     BINARY_OP                       11 (/)
                        668     STORE_FAST                      12: stplugin
                        670     LOAD_FAST                       12: stplugin
                        672     LOAD_ATTR                       25: exists
                        692     CALL                            0
                        700     TO_BOOL
                        708     POP_JUMP_IF_FALSE               77 (to 864)
                        712     LOAD_FAST                       12: stplugin
                        714     LOAD_ATTR                       27: iterdir
                        734     CALL                            0
                        742     GET_ITER
                        744     FOR_ITER                        57 (to 860)
                        748     STORE_FAST                      13: file
                        750     LOAD_FAST                       1: identifier
                        752     LOAD_ATTR                       17: lower
                        772     CALL                            0
                        780     LOAD_FAST                       13: file
                        782     LOAD_ATTR                       28: name
                        802     LOAD_ATTR                       17: lower
                        822     CALL                            0
                        830     CONTAINS_OP                     0 (in)
                        834     POP_JUMP_IF_TRUE                2 (to 840)
                        838     JUMP_BACKWARD                   49 (to 742)
                        842     LOAD_DEREF                      22: safe_delete
                        844     PUSH_NULL
                        846     LOAD_FAST                       13: file
                        848     CALL                            1
                        856     POP_TOP
                        858     JUMP_BACKWARD                   59 (to 742)
                        862     END_FOR
                        864     POP_TOP
                        866     LOAD_GLOBAL                     3: NULL + Path
                        876     LOAD_DEREF                      0: self
                        878     LOAD_ATTR                       22: steam_dir
                        898     CALL                            1
                        906     LOAD_CONST                      15: 'depotcache'
                        908     BINARY_OP                       11 (/)
                        912     STORE_FAST                      14: depotcache
                        914     LOAD_FAST                       14: depotcache
                        916     LOAD_ATTR                       25: exists
                        936     CALL                            0
                        944     TO_BOOL
                        952     POP_JUMP_IF_FALSE               77 (to 1108)
                        956     LOAD_FAST                       14: depotcache
                        958     LOAD_ATTR                       27: iterdir
                        978     CALL                            0
                        986     GET_ITER
                        988     FOR_ITER                        57 (to 1104)
                        992     STORE_FAST                      13: file
                        994     LOAD_FAST                       1: identifier
                        996     LOAD_ATTR                       17: lower
                        1016    CALL                            0
                        1024    LOAD_FAST                       13: file
                        1026    LOAD_ATTR                       28: name
                        1046    LOAD_ATTR                       17: lower
                        1066    CALL                            0
                        1074    CONTAINS_OP                     0 (in)
                        1078    POP_JUMP_IF_TRUE                2 (to 1084)
                        1082    JUMP_BACKWARD                   49 (to 986)
                        1086    LOAD_DEREF                      22: safe_delete
                        1088    PUSH_NULL
                        1090    LOAD_FAST                       13: file
                        1092    CALL                            1
                        1100    POP_TOP
                        1102    JUMP_BACKWARD                   59 (to 986)
                        1106    END_FOR
                        1108    POP_TOP
                        1110    LOAD_DEREF                      0: self
                        1112    LOAD_ATTR                       30: save_dir
                        1132    TO_BOOL
                        1140    POP_JUMP_IF_FALSE               192 (to 1526)
                        1144    LOAD_GLOBAL                     3: NULL + Path
                        1154    LOAD_DEREF                      0: self
                        1156    LOAD_ATTR                       30: save_dir
                        1176    CALL                            1
                        1184    STORE_FAST                      15: save_path
                        1186    LOAD_FAST                       15: save_path
                        1188    LOAD_ATTR                       27: iterdir
                        1208    CALL                            0
                        1216    GET_ITER
                        1218    FOR_ITER                        151 (to 1522)
                        1222    STORE_FAST                      16: folder
                        1224    LOAD_FAST                       16: folder
                        1226    LOAD_ATTR                       33: is_dir
                        1246    CALL                            0
                        1254    TO_BOOL
                        1262    POP_JUMP_IF_TRUE                2 (to 1268)
                        1266    JUMP_BACKWARD                   26 (to 1216)
                        1270    LOAD_FAST                       1: identifier
                        1272    LOAD_ATTR                       17: lower
                        1292    CALL                            0
                        1300    LOAD_FAST                       16: folder
                        1302    LOAD_ATTR                       28: name
                        1322    LOAD_ATTR                       17: lower
                        1342    CALL                            0
                        1350    CONTAINS_OP                     0 (in)
                        1354    POP_JUMP_IF_TRUE                2 (to 1360)
                        1358    JUMP_BACKWARD                   72 (to 1216)
                        1362    NOP
                        1364    LOAD_GLOBAL                     34: shutil
                        1374    LOAD_ATTR                       36: rmtree
                        1394    PUSH_NULL
                        1396    LOAD_FAST                       16: folder
                        1398    CALL                            1
                        1406    POP_TOP
                        1408    LOAD_DEREF                      21: removed_items
                        1410    LOAD_ATTR                       39: append
                        1430    LOAD_GLOBAL                     5: NULL + str
                        1440    LOAD_FAST                       16: folder
                        1442    CALL                            1
                        1450    CALL                            1
                        1458    POP_TOP
                        1460    LOAD_DEREF                      0: self
                        1462    LOAD_ATTR                       41: log_removal
                        1482    LOAD_CONST                      16: 'Removed exported folder: '
                        1484    LOAD_FAST                       16: folder
                        1486    LOAD_ATTR                       28: name
                        1506    FORMAT_SIMPLE
                        1508    BUILD_STRING                    2
                        1510    CALL                            1
                        1518    POP_TOP
                        1520    JUMP_BACKWARD                   153 (to 1216)
                        1524    END_FOR
                        1526    POP_TOP
                        1528    LOAD_DEREF                      21: removed_items
                        1530    TO_BOOL
                        1538    POP_JUMP_IF_TRUE                17 (to 1574)
                        1542    LOAD_DEREF                      0: self
                        1544    LOAD_ATTR                       41: log_removal
                        1564    LOAD_CONST                      19: 'No game found matching the identifier.'
                        1566    CALL                            1
                        1574    POP_TOP
                        1576    LOAD_DEREF                      21: removed_items
                        1578    RETURN_VALUE
                        1580    PUSH_EXC_INFO
                        1582    POP_TOP
                        1584    POP_EXCEPT
                        1586    JUMP_BACKWARD                   597 (to 396)
                        1592    COPY                            3
                        1594    POP_EXCEPT
                        1596    RERAISE                         1
                        1598    PUSH_EXC_INFO
                        1600    LOAD_GLOBAL                     42: Exception
                        1610    CHECK_EXC_MATCH
                        1612    POP_JUMP_IF_FALSE               53 (to 1720)
                        1616    STORE_FAST                      17: e
                        1618    LOAD_DEREF                      0: self
                        1620    LOAD_ATTR                       41: log_removal
                        1640    LOAD_CONST                      17: 'Error removing exported folder '
                        1642    LOAD_FAST                       16: folder
                        1644    LOAD_ATTR                       28: name
                        1664    FORMAT_SIMPLE
                        1666    LOAD_CONST                      18: ': '
                        1668    LOAD_GLOBAL                     5: NULL + str
                        1678    LOAD_FAST                       17: e
                        1680    CALL                            1
                        1688    FORMAT_SIMPLE
                        1690    BUILD_STRING                    4
                        1692    CALL                            1
                        1700    POP_TOP
                        1702    POP_EXCEPT
                        1704    LOAD_CONST                      0: None
                        1706    STORE_FAST                      17: e
                        1708    DELETE_FAST                     17: e
                        1710    JUMP_BACKWARD                   248 (to 1216)
                        1714    LOAD_CONST                      0: None
                        1716    STORE_FAST                      17: e
                        1718    DELETE_FAST                     17: e
                        1720    RERAISE                         1
                        1722    RERAISE                         0
                        1724    COPY                            3
                        1726    POP_EXCEPT
                        1728    RERAISE                         1
                [Code]
                    File Name: LuaMaker_NahBro3.py
                    Object Name: restart_steam
                    Qualified Name: LuaScriptMaker.restart_steam
                    Arg Count: 1
                    Pos Only Arg Count: 0
                    KW Only Arg Count: 0
                    Stack Size: 9
                    Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
                    [Names]
                        'os'
                        'system'
                        'time'
                        'sleep'
                        'Path'
                        'steam_dir'
                        'exists'
                        'subprocess'
                        'Popen'
                        'str'
                        'QMessageBox'
                        'information'
                        'warning'
                        'Exception'
                        'critical'
                    [Locals+Names]
                        'self'
                        'steam_exe'
                        'e'
                    [Constants]
                        None
                        'taskkill /IM steam.exe /F'
                        3
                        'steam.exe'
                        'Steam Restarted'
                        'Steam has been restarted.'
                        'Steam Not Found'
                        'Steam executable not found in the specified directory.'
                        'Error'
                        'Error restarting Steam: '
                    [Disassembly]
                        0       RESUME                          0
                        2       NOP
                        4       LOAD_GLOBAL                     0: os
                        14      LOAD_ATTR                       2: system
                        34      PUSH_NULL
                        36      LOAD_CONST                      1: 'taskkill /IM steam.exe /F'
                        38      CALL                            1
                        46      POP_TOP
                        48      LOAD_GLOBAL                     4: time
                        58      LOAD_ATTR                       6: sleep
                        78      PUSH_NULL
                        80      LOAD_CONST                      2: 3
                        82      CALL                            1
                        90      POP_TOP
                        92      LOAD_GLOBAL                     9: NULL + Path
                        102     LOAD_FAST                       0: self
                        104     LOAD_ATTR                       10: steam_dir
                        124     CALL                            1
                        132     LOAD_CONST                      3: 'steam.exe'
                        134     BINARY_OP                       11 (/)
                        138     STORE_FAST                      1: steam_exe
                        140     LOAD_FAST                       1: steam_exe
                        142     LOAD_ATTR                       13: exists
                        162     CALL                            0
                        170     TO_BOOL
                        178     POP_JUMP_IF_FALSE               57 (to 294)
                        182     LOAD_GLOBAL                     14: subprocess
                        192     LOAD_ATTR                       16: Popen
                        212     PUSH_NULL
                        214     LOAD_GLOBAL                     19: NULL + str
                        224     LOAD_FAST                       1: steam_exe
                        226     CALL                            1
                        234     BUILD_LIST                      1
                        236     CALL                            1
                        244     POP_TOP
                        246     LOAD_GLOBAL                     20: QMessageBox
                        256     LOAD_ATTR                       22: information
                        276     PUSH_NULL
                        278     LOAD_FAST                       0: self
                        280     LOAD_CONST                      4: 'Steam Restarted'
                        282     LOAD_CONST                      5: 'Steam has been restarted.'
                        284     CALL                            3
                        292     POP_TOP
                        294     RETURN_CONST                    0: None
                        296     LOAD_GLOBAL                     20: QMessageBox
                        306     LOAD_ATTR                       24: warning
                        326     PUSH_NULL
                        328     LOAD_FAST                       0: self
                        330     LOAD_CONST                      6: 'Steam Not Found'
                        332     LOAD_CONST                      7: 'Steam executable not found in the specified directory.'
                        334     CALL                            3
                        342     POP_TOP
                        344     RETURN_CONST                    0: None
                        346     PUSH_EXC_INFO
                        348     LOAD_GLOBAL                     26: Exception
                        358     CHECK_EXC_MATCH
                        360     POP_JUMP_IF_FALSE               46 (to 454)
                        364     STORE_FAST                      2: e
                        366     LOAD_GLOBAL                     20: QMessageBox
                        376     LOAD_ATTR                       28: critical
                        396     PUSH_NULL
                        398     LOAD_FAST                       0: self
                        400     LOAD_CONST                      8: 'Error'
                        402     LOAD_CONST                      9: 'Error restarting Steam: '
                        404     LOAD_GLOBAL                     19: NULL + str
                        414     LOAD_FAST                       2: e
                        416     CALL                            1
                        424     FORMAT_SIMPLE
                        426     BUILD_STRING                    2
                        428     CALL                            3
                        436     POP_TOP
                        438     POP_EXCEPT
                        440     LOAD_CONST                      0: None
                        442     STORE_FAST                      2: e
                        444     DELETE_FAST                     2: e
                        446     RETURN_CONST                    0: None
                        448     LOAD_CONST                      0: None
                        450     STORE_FAST                      2: e
                        452     DELETE_FAST                     2: e
                        454     RERAISE                         1
                        456     RERAISE                         0
                        458     COPY                            3
                        460     POP_EXCEPT
                        462     RERAISE                         1
                (
                    'added_ids'
                    'btn_change_steam'
                    'btn_clear'
                    'btn_export_all'
                    'btn_pause'
                    'btn_preview'
                    'btn_remove'
                    'btn_restart'
                    'btn_save'
                    'btn_select_save'
                    'btn_set_game'
                    'combo_theme'
                    'dlc_ids'
                    'export_paused'
                    'exporter_tab'
                    'game_dir'
                    'input_dkey'
                    'input_dlc'
                    'input_manifest'
                    'input_primary'
                    'input_remove'
                    'input_secondary'
                    'label_console'
                    'label_dkey'
                    'label_dlc'
                    'label_game'
                    'label_manifest'
                    'label_preview'
                    'label_primary'
                    'label_remove'
                    'label_save_dir'
                    'label_secondary'
                    'label_steam'
                    'remover_tab'
                    'save_dir'
                    'script_lines'
                    'steam_dir'
                    'tabs'
                    'text_console'
                    'text_preview'
                    'text_remove_console'
                )
            [Disassembly]
                0       MAKE_CELL                       0: __class__
                2       RESUME                          0
                4       LOAD_NAME                       0: __name__
                6       STORE_NAME                      1: __module__
                8       LOAD_CONST                      0: 'LuaScriptMaker'
                10      STORE_NAME                      2: __qualname__
                12      LOAD_CONST                      1: 84
                14      STORE_NAME                      3: __firstlineno__
                16      LOAD_NAME                       4: getattr
                18      PUSH_NULL
                20      LOAD_NAME                       5: sys
                22      LOAD_CONST                      2: 'frozen'
                24      LOAD_CONST                      3: False
                26      CALL                            3
                34      TO_BOOL
                42      POP_JUMP_IF_FALSE               29 (to 102)
                46      LOAD_NAME                       6: Path
                48      PUSH_NULL
                50      LOAD_NAME                       5: sys
                52      LOAD_ATTR                       14: executable
                72      CALL                            1
                80      LOAD_ATTR                       16: parent
                100     STORE_NAME                      9: BASE_PATH
                102     JUMP_FORWARD                    32 (to 168)
                104     LOAD_NAME                       6: Path
                106     PUSH_NULL
                108     LOAD_NAME                       10: __file__
                110     CALL                            1
                118     LOAD_ATTR                       23: resolve
                138     CALL                            0
                146     LOAD_ATTR                       16: parent
                166     STORE_NAME                      9: BASE_PATH
                168     LOAD_NAME                       9: BASE_PATH
                170     LOAD_CONST                      4: 'config.json'
                172     BINARY_OP                       11 (/)
                176     STORE_NAME                      12: CONFIG_PATH
                178     LOAD_FAST                       0: __class__
                180     BUILD_TUPLE                     1
                182     LOAD_CONST                      5: <CODE> __init__
                184     MAKE_FUNCTION
                186     SET_FUNCTION_ATTRIBUTE          8 (MAKE_FUNCTION_CLOSURE)
                188     STORE_NAME                      13: __init__
                190     LOAD_CONST                      6: <CODE> load_config
                192     MAKE_FUNCTION
                194     STORE_NAME                      14: load_config
                196     LOAD_CONST                      7: <CODE> save_config
                198     MAKE_FUNCTION
                200     STORE_NAME                      15: save_config
                202     LOAD_CONST                      8: <CODE> build_ui
                204     MAKE_FUNCTION
                206     STORE_NAME                      16: build_ui
                208     LOAD_CONST                      9: <CODE> log_console
                210     MAKE_FUNCTION
                212     STORE_NAME                      17: log_console
                214     LOAD_CONST                      10: <CODE> log_removal
                216     MAKE_FUNCTION
                218     STORE_NAME                      18: log_removal
                220     LOAD_CONST                      11: <CODE> clear_draft
                222     MAKE_FUNCTION
                224     STORE_NAME                      19: clear_draft
                226     LOAD_CONST                      12: <CODE> toggle_export_pause
                228     MAKE_FUNCTION
                230     STORE_NAME                      20: toggle_export_pause
                232     LOAD_CONST                      13: <CODE> update_theme
                234     MAKE_FUNCTION
                236     STORE_NAME                      21: update_theme
                238     LOAD_CONST                      14: <CODE> auto_detect_steam_dir
                240     MAKE_FUNCTION
                242     STORE_NAME                      22: auto_detect_steam_dir
                244     LOAD_CONST                      15: <CODE> change_steam_directory
                246     MAKE_FUNCTION
                248     STORE_NAME                      23: change_steam_directory
                250     LOAD_CONST                      16: <CODE> select_save_directory
                252     MAKE_FUNCTION
                254     STORE_NAME                      24: select_save_directory
                256     LOAD_CONST                      17: <CODE> select_game_directory
                258     MAKE_FUNCTION
                260     STORE_NAME                      25: select_game_directory
                262     LOAD_CONST                      18: 'return'
                264     LOAD_NAME                       26: set
                266     BUILD_TUPLE                     2
                268     LOAD_CONST                      19: <CODE> get_library_folders
                270     MAKE_FUNCTION
                272     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                274     STORE_NAME                      27: get_library_folders
                276     LOAD_CONST                      20: <CODE> auto_fill_fields
                278     MAKE_FUNCTION
                280     STORE_NAME                      28: auto_fill_fields
                282     LOAD_CONST                      21: <CODE> update_preview
                284     MAKE_FUNCTION
                286     STORE_NAME                      29: update_preview
                288     LOAD_CONST                      22: 'primary'
                290     LOAD_NAME                       30: str
                292     LOAD_CONST                      18: 'return'
                294     LOAD_NAME                       30: str
                296     BUILD_TUPLE                     4
                298     LOAD_CONST                      23: <CODE> get_game_name_from_primary
                300     MAKE_FUNCTION
                302     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                304     STORE_NAME                      31: get_game_name_from_primary
                306     LOAD_CONST                      24: <CODE> get_dkey
                308     MAKE_FUNCTION
                310     STORE_NAME                      32: get_dkey
                312     LOAD_CONST                      25: 'appid'
                314     LOAD_NAME                       30: str
                316     LOAD_CONST                      18: 'return'
                318     LOAD_NAME                       30: str
                320     BUILD_TUPLE                     4
                322     LOAD_CONST                      26: <CODE> get_manifest_for_appid
                324     MAKE_FUNCTION
                326     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                328     STORE_NAME                      33: get_manifest_for_appid
                330     LOAD_CONST                      27: <CODE> get_manifest
                332     MAKE_FUNCTION
                334     STORE_NAME                      34: get_manifest
                336     LOAD_CONST                      28: <CODE> copy_manifest_files
                338     MAKE_FUNCTION
                340     STORE_NAME                      35: copy_manifest_files
                342     LOAD_CONST                      29: <CODE> copy_fallback_manifest
                344     MAKE_FUNCTION
                346     STORE_NAME                      36: copy_fallback_manifest
                348     LOAD_CONST                      30: <CODE> copy_bin_files
                350     MAKE_FUNCTION
                352     STORE_NAME                      37: copy_bin_files
                354     LOAD_CONST                      31: <CODE> copy_achievement_bin_files
                356     MAKE_FUNCTION
                358     STORE_NAME                      38: copy_achievement_bin_files
                360     LOAD_CONST                      32: <CODE> create_zip_archive
                362     MAKE_FUNCTION
                364     STORE_NAME                      39: create_zip_archive
                366     LOAD_CONST                      33: <CODE> process_dlc_ids
                368     MAKE_FUNCTION
                370     STORE_NAME                      40: process_dlc_ids
                372     LOAD_CONST                      34: <CODE> fetch_dlc_ids
                374     MAKE_FUNCTION
                376     STORE_NAME                      41: fetch_dlc_ids
                378     LOAD_CONST                      25: 'appid'
                380     LOAD_NAME                       30: str
                382     LOAD_CONST                      18: 'return'
                384     LOAD_NAME                       42: list
                386     BUILD_TUPLE                     4
                388     LOAD_CONST                      35: <CODE> fetch_depot_ids_from_steamdb
                390     MAKE_FUNCTION
                392     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                394     STORE_NAME                      43: fetch_depot_ids_from_steamdb
                396     LOAD_CONST                      36: <CODE> process_primary_appid
                398     MAKE_FUNCTION
                400     STORE_NAME                      44: process_primary_appid
                402     LOAD_CONST                      22: 'primary'
                404     LOAD_NAME                       30: str
                406     LOAD_CONST                      37: 'gamename'
                408     LOAD_NAME                       30: str
                410     LOAD_CONST                      18: 'return'
                412     LOAD_NAME                       6: Path
                414     LOAD_CONST                      38: None
                416     BINARY_OP                       7 (|)
                420     BUILD_TUPLE                     6
                422     LOAD_CONST                      39: <CODE> export_game
                424     MAKE_FUNCTION
                426     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                428     STORE_NAME                      45: export_game
                430     LOAD_CONST                      40: <CODE> export_all_installed_games
                432     MAKE_FUNCTION
                434     STORE_NAME                      46: export_all_installed_games
                436     LOAD_CONST                      41: <CODE> handle_preview
                438     MAKE_FUNCTION
                440     STORE_NAME                      47: handle_preview
                442     LOAD_CONST                      42: <CODE> handle_save
                444     MAKE_FUNCTION
                446     STORE_NAME                      48: handle_save
                448     LOAD_CONST                      43: <CODE> save_lua_script
                450     MAKE_FUNCTION
                452     STORE_NAME                      49: save_lua_script
                454     LOAD_CONST                      44: <CODE> remove_game_handler
                456     MAKE_FUNCTION
                458     STORE_NAME                      50: remove_game_handler
                460     LOAD_CONST                      45: 'identifier'
                462     LOAD_NAME                       30: str
                464     LOAD_CONST                      18: 'return'
                466     LOAD_NAME                       42: list
                468     BUILD_TUPLE                     4
                470     LOAD_CONST                      46: <CODE> remove_game
                472     MAKE_FUNCTION
                474     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
                476     STORE_NAME                      51: remove_game
                478     LOAD_CONST                      47: <CODE> restart_steam
                480     MAKE_FUNCTION
                482     STORE_NAME                      52: restart_steam
                484     LOAD_CONST                      48: ('added_ids', 'btn_change_steam', 'btn_clear', 'btn_export_all', 'btn_pause', 'btn_preview', 'btn_remove', 'btn_restart', 'btn_save', 'btn_select_save', 'btn_set_game', 'combo_theme', 'dlc_ids', 'export_paused', 'exporter_tab', 'game_dir', 'input_dkey', 'input_dlc', 'input_manifest', 'input_primary', 'input_remove', 'input_secondary', 'label_console', 'label_dkey', 'label_dlc', 'label_game', 'label_manifest', 'label_preview', 'label_primary', 'label_remove', 'label_save_dir', 'label_secondary', 'label_steam', 'remover_tab', 'save_dir', 'script_lines', 'steam_dir', 'tabs', 'text_console', 'text_preview', 'text_remove_console')
                486     STORE_NAME                      53: __static_attributes__
                488     LOAD_FAST                       0: __class__
                490     COPY                            1
                492     STORE_NAME                      54: __classcell__
                494     RETURN_VALUE
        'LuaScriptMaker'
        [Code]
            File Name: LuaMaker_NahBro3.py
            Object Name: main
            Qualified Name: main
            Arg Count: 0
            Pos Only Arg Count: 0
            KW Only Arg Count: 0
            Stack Size: 4
            Flags: 0x00000003 (CO_OPTIMIZED | CO_NEWLOCALS)
            [Names]
                'QApplication'
                'sys'
                'argv'
                'setStyleSheet'
                'LuaScriptMaker'
                'show'
                'exit'
                'exec'
            [Locals+Names]
                'app'
                'dark_style'
                'window'
            [Constants]
                None
                '\n        QWidget { background-color: #121212; color: #e0e0e0; }\n        QLineEdit, QTextEdit { background-color: #1e1e1e; color: #e0e0e0; border: 1px solid #444444; }\n        QPushButton { background-color: #1a1a1a; color: #e0e0e0; padding: 5px; border: none; }\n        QPushButton:hover { background-color: #2a2a2a; }\n        QPushButton:pressed { background-color: #3a3a3a; }\n        QLabel { color: #e0e0e0; }\n    '
            [Disassembly]
                0       RESUME                          0
                2       LOAD_GLOBAL                     1: NULL + QApplication
                12      LOAD_GLOBAL                     2: sys
                22      LOAD_ATTR                       4: argv
                42      CALL                            1
                50      STORE_FAST                      0: app
                52      LOAD_CONST                      1: '\n        QWidget { background-color: #121212; color: #e0e0e0; }\n        QLineEdit, QTextEdit { background-color: #1e1e1e; color: #e0e0e0; border: 1px solid #444444; }\n        QPushButton { background-color: #1a1a1a; color: #e0e0e0; padding: 5px; border: none; }\n        QPushButton:hover { background-color: #2a2a2a; }\n        QPushButton:pressed { background-color: #3a3a3a; }\n        QLabel { color: #e0e0e0; }\n    '
                54      STORE_FAST                      1: dark_style
                56      LOAD_FAST                       0: app
                58      LOAD_ATTR                       7: setStyleSheet
                78      LOAD_FAST                       1: dark_style
                80      CALL                            1
                88      POP_TOP
                90      LOAD_GLOBAL                     9: NULL + LuaScriptMaker
                100     CALL                            0
                108     STORE_FAST                      2: window
                110     LOAD_FAST                       2: window
                112     LOAD_ATTR                       11: show
                132     CALL                            0
                140     POP_TOP
                142     LOAD_GLOBAL                     2: sys
                152     LOAD_ATTR                       12: exit
                172     PUSH_NULL
                174     LOAD_FAST                       0: app
                176     LOAD_ATTR                       15: exec
                196     CALL                            0
                204     CALL                            1
                212     POP_TOP
                214     RETURN_CONST                    0: None
        '__main__'
    [Disassembly]
        0       RESUME                          0
        2       LOAD_CONST                      0: 0
        4       LOAD_CONST                      1: None
        6       IMPORT_NAME                     0: sys
        8       STORE_NAME                      0: sys
        10      LOAD_CONST                      0: 0
        12      LOAD_CONST                      1: None
        14      IMPORT_NAME                     1: re
        16      STORE_NAME                      1: re
        18      LOAD_CONST                      0: 0
        20      LOAD_CONST                      1: None
        22      IMPORT_NAME                     2: json
        24      STORE_NAME                      2: json
        26      LOAD_CONST                      0: 0
        28      LOAD_CONST                      1: None
        30      IMPORT_NAME                     3: shutil
        32      STORE_NAME                      3: shutil
        34      LOAD_CONST                      0: 0
        36      LOAD_CONST                      1: None
        38      IMPORT_NAME                     4: requests
        40      STORE_NAME                      4: requests
        42      LOAD_CONST                      0: 0
        44      LOAD_CONST                      1: None
        46      IMPORT_NAME                     5: ctypes
        48      STORE_NAME                      5: ctypes
        50      LOAD_CONST                      0: 0
        52      LOAD_CONST                      1: None
        54      IMPORT_NAME                     6: logging
        56      STORE_NAME                      6: logging
        58      LOAD_CONST                      0: 0
        60      LOAD_CONST                      1: None
        62      IMPORT_NAME                     7: os
        64      STORE_NAME                      7: os
        66      LOAD_CONST                      0: 0
        68      LOAD_CONST                      1: None
        70      IMPORT_NAME                     8: zipfile
        72      STORE_NAME                      8: zipfile
        74      LOAD_CONST                      0: 0
        76      LOAD_CONST                      1: None
        78      IMPORT_NAME                     9: time
        80      STORE_NAME                      9: time
        82      LOAD_CONST                      0: 0
        84      LOAD_CONST                      1: None
        86      IMPORT_NAME                     10: subprocess
        88      STORE_NAME                      10: subprocess
        90      LOAD_CONST                      0: 0
        92      LOAD_CONST                      1: None
        94      IMPORT_NAME                     11: sourcedefender
        96      STORE_NAME                      11: sourcedefender
        98      LOAD_CONST                      0: 0
        100     LOAD_CONST                      2: ('Path',)
        102     IMPORT_NAME                     12: pathlib
        104     IMPORT_FROM                     13: Path
        106     STORE_NAME                      13: Path
        108     POP_TOP
        110     LOAD_CONST                      0: 0
        112     LOAD_CONST                      3: ('QApplication', 'QMainWindow', 'QWidget', 'QVBoxLayout', 'QHBoxLayout', 'QGridLayout', 'QLabel', 'QLineEdit', 'QPushButton', 'QTextEdit', 'QFileDialog', 'QMessageBox', 'QComboBox', 'QTabWidget')
        114     IMPORT_NAME                     14: PyQt6.QtWidgets
        116     IMPORT_FROM                     15: QApplication
        118     STORE_NAME                      15: QApplication
        120     IMPORT_FROM                     16: QMainWindow
        122     STORE_NAME                      16: QMainWindow
        124     IMPORT_FROM                     17: QWidget
        126     STORE_NAME                      17: QWidget
        128     IMPORT_FROM                     18: QVBoxLayout
        130     STORE_NAME                      18: QVBoxLayout
        132     IMPORT_FROM                     19: QHBoxLayout
        134     STORE_NAME                      19: QHBoxLayout
        136     IMPORT_FROM                     20: QGridLayout
        138     STORE_NAME                      20: QGridLayout
        140     IMPORT_FROM                     21: QLabel
        142     STORE_NAME                      21: QLabel
        144     IMPORT_FROM                     22: QLineEdit
        146     STORE_NAME                      22: QLineEdit
        148     IMPORT_FROM                     23: QPushButton
        150     STORE_NAME                      23: QPushButton
        152     IMPORT_FROM                     24: QTextEdit
        154     STORE_NAME                      24: QTextEdit
        156     IMPORT_FROM                     25: QFileDialog
        158     STORE_NAME                      25: QFileDialog
        160     IMPORT_FROM                     26: QMessageBox
        162     STORE_NAME                      26: QMessageBox
        164     IMPORT_FROM                     27: QComboBox
        166     STORE_NAME                      27: QComboBox
        168     IMPORT_FROM                     28: QTabWidget
        170     STORE_NAME                      28: QTabWidget
        172     POP_TOP
        174     LOAD_CONST                      0: 0
        176     LOAD_CONST                      4: ('QIntValidator', 'QFont')
        178     IMPORT_NAME                     29: PyQt6.QtGui
        180     IMPORT_FROM                     30: QIntValidator
        182     STORE_NAME                      30: QIntValidator
        184     IMPORT_FROM                     31: QFont
        186     STORE_NAME                      31: QFont
        188     POP_TOP
        190     LOAD_CONST                      0: 0
        192     LOAD_CONST                      5: ('Qt', 'QThread')
        194     IMPORT_NAME                     32: PyQt6.QtCore
        196     IMPORT_FROM                     33: Qt
        198     STORE_NAME                      33: Qt
        200     IMPORT_FROM                     34: QThread
        202     STORE_NAME                      34: QThread
        204     POP_TOP
        206     LOAD_NAME                       6: logging
        208     LOAD_ATTR                       70: basicConfig
        228     PUSH_NULL
        230     LOAD_CONST                      6: 'error_log.txt'
        232     LOAD_NAME                       6: logging
        234     LOAD_ATTR                       72: WARNING
        254     LOAD_CONST                      7: '%(asctime)s - %(levelname)s - %(message)s'
        256     LOAD_CONST                      8: ('filename', 'level', 'format')
        258     CALL_KW                         3
        260     POP_TOP
        262     LOAD_CONST                      9: 'acf_path'
        264     LOAD_NAME                       13: Path
        266     LOAD_CONST                      10: 'return'
        268     LOAD_NAME                       37: str
        270     LOAD_CONST                      1: None
        272     BINARY_OP                       7 (|)
        276     BUILD_TUPLE                     4
        278     LOAD_CONST                      11: <CODE> parse_acf_file
        280     MAKE_FUNCTION
        282     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
        284     STORE_NAME                      38: parse_acf_file
        286     LOAD_CONST                      9: 'acf_path'
        288     LOAD_NAME                       13: Path
        290     LOAD_CONST                      10: 'return'
        292     LOAD_NAME                       39: dict
        294     BUILD_TUPLE                     4
        296     LOAD_CONST                      12: <CODE> parse_appmanifest
        298     MAKE_FUNCTION
        300     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
        302     STORE_NAME                      40: parse_appmanifest
        304     LOAD_CONST                      9: 'acf_path'
        306     LOAD_NAME                       13: Path
        308     LOAD_CONST                      10: 'return'
        310     LOAD_NAME                       37: str
        312     BUILD_TUPLE                     4
        314     LOAD_CONST                      13: <CODE> get_manifest_from_acf
        316     MAKE_FUNCTION
        318     SET_FUNCTION_ATTRIBUTE          4 (MAKE_FUNCTION_ANNOTATIONS)
        320     STORE_NAME                      41: get_manifest_from_acf
        322     LOAD_BUILD_CLASS
        324     PUSH_NULL
        326     LOAD_CONST                      14: <CODE> SteamAPI
        328     MAKE_FUNCTION
        330     LOAD_CONST                      15: 'SteamAPI'
        332     CALL                            2
        340     STORE_NAME                      42: SteamAPI
        342     LOAD_BUILD_CLASS
        344     PUSH_NULL
        346     LOAD_CONST                      16: <CODE> LuaScriptMaker
        348     MAKE_FUNCTION
        350     LOAD_CONST                      17: 'LuaScriptMaker'
        352     LOAD_NAME                       16: QMainWindow
        354     CALL                            3
        362     STORE_NAME                      43: LuaScriptMaker
        364     LOAD_CONST                      18: <CODE> main
        366     MAKE_FUNCTION
        368     STORE_NAME                      44: main
        370     LOAD_NAME                       45: __name__
        372     LOAD_CONST                      19: '__main__'
        374     COMPARE_OP                      88 (==)
        378     POP_JUMP_IF_FALSE               8 (to 396)
        382     LOAD_NAME                       44: main
        384     PUSH_NULL
        386     CALL                            0
        394     POP_TOP
        396     RETURN_CONST                    1: None
        398     RETURN_CONST                    1: None
