FILE(GLOB PY_FILES *.py)
FILE(GLOB DESCR_FILES description/*.txt)
FILE(GLOB HELP_FILES help/*.html)

INSTALL(FILES ${PY_FILES} DESTINATION ${SEXTANTE_PLUGIN_DIR}/taudem)
INSTALL(FILES ${DESCR_FILES} DESTINATION ${SEXTANTE_PLUGIN_DIR}/taudem/description)
INSTALL(FILES ${HELP_FILES} DESTINATION ${SEXTANTE_PLUGIN_DIR}/taudem/help)
