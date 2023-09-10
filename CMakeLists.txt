cmake_minimum_required(VERSION 3.16.0)
project(speex VERSION 1.2.1 LANGUAGES C)
set_property(GLOBAL PROPERTY USE_FOLDERS ON)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_STATIC_LIBRARY_PREFIX "lib")
set(CMAKE_C_FLAGS "-g -O2 -fvisibility=hidden -Wall")
add_definitions(-DHAVE_CONFIG_H)

# Macros
set_property(GLOBAL PROPERTY SPEEX_PROJECT_SOURCE_DIR "${PROJECT_SOURCE_DIR}")

# Headers
set(SPEEX_CONFIG "${PROJECT_SOURCE_DIR}/config.h")
set(SPEEX_HEADER_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include")
file(GLOB_RECURSE SPEEX_HEADER_FILES "${SPEEX_HEADER_DIR}/*.h")

# Build
add_subdirectory(libspeex)

# Install
install(TARGETS speex LIBRARY DESTINATION lib)
install(DIRECTORY include/ DESTINATION include FILES_MATCHING PATTERN "*.h")
