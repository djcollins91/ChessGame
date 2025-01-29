cmake_minimum_required(VERSION 3.10)  # Minimum CMake version requirement
project(vo_epipolar_project)  # Set project name

#Set the C++ standard (if applicable)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(OpenCV REQUIRED)


add_executable(vo_epipolar_project src/vo_epipolar.cpp)


target_link_libraries(vo_epipolar_project ${OpenCV_LIBS})