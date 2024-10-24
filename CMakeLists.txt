# Minimum CMake version required
cmake_minimum_required(VERSION 3.10)

# Project name and supported languages
project(hackaton LANGUAGES C CXX)

# Include directories
include_directories(src/c src/cpp)

# Source files
file(GLOB C_SOURCES "src/c/*.c")
file(GLOB CPP_SOURCES "src/cpp/*.cpp")

# Executable target
add_executable(projet_exe ${C_SOURCES} ${CPP_SOURCES})

target_link_libraries(projet_exe ncurses)
