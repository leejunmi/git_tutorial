#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "mip" for configuration ""
set_property(TARGET mip APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(mip PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_NOCONFIG "C;CXX"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libmip.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS mip )
list(APPEND _IMPORT_CHECK_FILES_FOR_mip "${_IMPORT_PREFIX}/lib/libmip.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
