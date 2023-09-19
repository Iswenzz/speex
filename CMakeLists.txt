cmake_minimum_required(VERSION 3.16.0)
project(speex VERSION 1.2.1 LANGUAGES C)
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS_INIT} -g -O2 -fvisibility=hidden -Wall")
set(CMAKE_STATIC_LIBRARY_PREFIX "lib")
add_definitions(-DHAVE_CONFIG_H)

# Macros
set_property(GLOBAL PROPERTY SPEEX_PROJECT_SOURCE_DIR "${PROJECT_SOURCE_DIR}")

# Headers
set(SPEEX_CONFIG "${PROJECT_SOURCE_DIR}/config.h")
set(SPEEX_HEADER_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include")
file(GLOB_RECURSE SPEEX_HEADER_FILES "${SPEEX_HEADER_DIR}/*.h")

# Build
add_subdirectory(libspeex)

target_include_directories(speex INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include/speex>)

# Install
install(TARGETS speex EXPORT speexTargets LIBRARY DESTINATION lib)
install(DIRECTORY include/ DESTINATION include FILES_MATCHING PATTERN "*.h")

# Package
include(CMakePackageConfigHelpers)

export(EXPORT speexTargets
    FILE "${CMAKE_CURRENT_BINARY_DIR}/speexTargets.cmake"
    NAMESPACE speex::)

configure_package_config_file(cmake/speexConfig.cmake.in
	"${CMAKE_CURRENT_BINARY_DIR}/speexConfig.cmake"
	INSTALL_DESTINATION lib/cmake/speex)

install(EXPORT speexTargets
    FILE speexTargets.cmake
    NAMESPACE speex::
    DESTINATION lib/cmake/speex)

install(FILES "${CMAKE_CURRENT_BINARY_DIR}/speexConfig.cmake"
    DESTINATION lib/cmake/speex)
