set(TABLE_NAME
  lekhika
  )

set(MB_FILE)
set(CONF_FILE)

foreach(table ${TABLE_NAME})
  fcitx5_translate_desktop_file("${table}.conf.in" "${table}.conf")
  add_custom_command(OUTPUT "${table}.main.dict"
    DEPENDS "${table}.txt"
    COMMAND LibIME::tabledict ARGS "${CMAKE_CURRENT_SOURCE_DIR}/${table}.txt"
    "${CMAKE_CURRENT_BINARY_DIR}/${table}.main.dict")
  set(MB_FILE ${MB_FILE} "${CMAKE_CURRENT_BINARY_DIR}/${table}.main.dict")
  set(CONF_FILE ${CONF_FILE} "${CMAKE_CURRENT_BINARY_DIR}/${table}.conf")
endforeach()
add_custom_target(table_data ALL DEPENDS ${MB_FILE})

install(FILES ${CONF_FILE} DESTINATION "${FCITX_INSTALL_PKGDATADIR}/inputmethod")
install(FILES ${MB_FILE} DESTINATION "${FCITX_INSTALL_PKGDATADIR}/table")
