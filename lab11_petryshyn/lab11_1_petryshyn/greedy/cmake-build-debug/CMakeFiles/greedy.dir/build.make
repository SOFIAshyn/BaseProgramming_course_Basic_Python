# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Users/sofia.petryshyn/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/183.4284.156/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/sofia.petryshyn/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/183.4284.156/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/greedy.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/greedy.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/greedy.dir/flags.make

CMakeFiles/greedy.dir/main.c.o: CMakeFiles/greedy.dir/flags.make
CMakeFiles/greedy.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/greedy.dir/main.c.o"
	/Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/greedy.dir/main.c.o   -c /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/main.c

CMakeFiles/greedy.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/greedy.dir/main.c.i"
	/Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/main.c > CMakeFiles/greedy.dir/main.c.i

CMakeFiles/greedy.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/greedy.dir/main.c.s"
	/Library/Developer/CommandLineTools/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/main.c -o CMakeFiles/greedy.dir/main.c.s

# Object files for target greedy
greedy_OBJECTS = \
"CMakeFiles/greedy.dir/main.c.o"

# External object files for target greedy
greedy_EXTERNAL_OBJECTS =

greedy: CMakeFiles/greedy.dir/main.c.o
greedy: CMakeFiles/greedy.dir/build.make
greedy: CMakeFiles/greedy.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable greedy"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/greedy.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/greedy.dir/build: greedy

.PHONY : CMakeFiles/greedy.dir/build

CMakeFiles/greedy.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/greedy.dir/cmake_clean.cmake
.PHONY : CMakeFiles/greedy.dir/clean

CMakeFiles/greedy.dir/depend:
	cd /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/cmake-build-debug /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/cmake-build-debug /Users/sofia.petryshyn/Desktop/c_lab/lab_11/greedy/cmake-build-debug/CMakeFiles/greedy.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/greedy.dir/depend

