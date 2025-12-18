-- xmake.lua for rat-trig C++ project
set_project("rat-trig")
set_version("0.1.0")
set_languages("cxx20")

-- Options
option("shared", {description = "Build shared library", default = true})
option("tests", {description = "Build tests", default = true})
option("examples", {description = "Build examples", default = true})

-- Library
target("rat-trig")
    set_kind("$(kind)")
    add_headerfiles("include/(rat_trig/**.hpp)")
    add_files("src/trigonom.cpp")
    add_includedirs("include", {public = true})
    
    if is_plat("windows") then
        add_defines("_USE_MATH_DEFINES")
    end

-- Tests
if has_config("tests") then
    add_requires("doctest")
    
    target("tests")
        set_kind("binary")
        add_files("tests/*.cpp")
        add_deps("rat-trig")
        add_packages("doctest")
        add_includedirs("include")
end

-- Examples
if has_config("examples") then
    target("fibonacci")
        set_kind("binary")
        add_files("examples/fibonacci.cpp")
        add_deps("rat-trig")
        add_includedirs("include")
    
    target("basic_usage")
        set_kind("binary")
        add_files("examples/basic_usage.cpp")
        add_deps("rat-trig")
        add_includedirs("include")
end

-- Default target
if is_mode("debug") then
    set_symbols("debug")
    set_optimize("none")
elseif is_mode("release") then
    set_optimize("fastest")
    set_strip("all")
end