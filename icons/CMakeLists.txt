set(ICON48
fcitx5-lekhika-test.png    
fcitx5-lekhika.png)

install(FILES
    ${ICON48}
    DESTINATION share/icons/hicolor/48x48/apps)

foreach(icon ${ICON48})
    string(REPLACE "fcitx5-" "" icon_new ${icon})
    install(FILES ${icon} RENAME ${icon_new} DESTINATION share/fcitx/imicon)
endforeach()
