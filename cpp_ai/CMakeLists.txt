cmake_minimum_required(VERSION 3.20)
project(rat-trig
  VERSION 0.1.0
  DESCRIPTION "Rational Trigonometry - A C++20 implementation of Norman Wildberger's rational trigonometry"
  LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Options
option(BUILD_SHARED_LIBS "Build shared library" ON)
option(BUILD_TESTS "Build tests" ON)
option(BUILD_EXAMPLES "Build examples" ON)

# Include directories
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Library
add_library(rat-trig
  src/trigonom.cpp
)

target_include_directories(rat-trig PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>
)

# Tests
if(BUILD_TESTS)
  enable_testing()
  
  # Download doctest if not found
  if(NOT TARGET doctest)
    include(FetchContent)
    FetchContent_Declare(
      doctest
      GIT_REPOSITORY https://github.com/doctest/doctest.git
      GIT_TAG v2.4.11
    )
    FetchContent_MakeAvailable(doctest)
  endif()

  add_executable(tests
    tests/test_trigonom.cpp
    tests/test_cross.cpp
    tests/test_dot.cpp
    tests/test_quad.cpp
    tests/test_spread.cpp
    tests/test_spread_law.cpp
    tests/test_triple_quad_formula.cpp
  )

  target_link_libraries(tests PRIVATE rat-trig doctest)
  target_include_directories(tests PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)

  add_test(NAME rat-trig-tests COMMAND tests)
endif()

# Examples
if(BUILD_EXAMPLES)
  add_executable(fibonacci
    examples/fibonacci.cpp
  )
  target_link_libraries(fibonacci PRIVATE rat-trig)

  add_executable(basic_usage
    examples/basic_usage.cpp
  )
  target_link_libraries(basic_usage PRIVATE rat-trig)
endif()

# Installation
install(TARGETS rat-trig
  EXPORT rat-trig-targets
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# Export targets
install(EXPORT rat-trig-targets
  FILE rat-trig-config.cmake
  NAMESPACE rat-trig::
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/rat-trig
)