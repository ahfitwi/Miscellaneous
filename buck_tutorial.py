"""
https://buck.build/rule/prebuilt_python_library.html

#-------------------------------
1. prebuilt_python_library()
#-------------------------------
This is liable to change in the future.

A prebuilt_python_library() rule is used to include prebuilt python packages 
into the output of a top-level python_binary or python_test rule.

These prebuilt libraries can either be whl files or eggs

whls for most packages are available for download from PyPI. The whl used 
may be downloaded with remote_file. However, Buck does not attempt to infer 
dependency information from pip, so that information will have to be imparted 
by the user.

To create an egg for a package, run python setup.py bdist_egg in the package 
source distribution.

Arguments
    # name (required)
        The short name for this build target.

    # binary_src (required)
        The path to the .whl or .egg to use. Note: .egg files have a very particular 
        naming convention that must be followed - otherwise pex will not find the 
        dependency properly at runtime!

    # deps (defaults to [])
        Other prebuilt_python_library() rules which this library depends on. These 
        may also be python_library rules if you want to depend on a source-based copy 
        of the library.

    # exclude_deps_from_merged_linking (defaults to False)
        When linking the top-level binary with a merged [python].native_link_strategy, 
        do not merge or re-link any native transitive deps of this library. This is useful 
        if this library wraps prebuilt native extensions which cannot be re-linked as part 
        of library merging.

    # visibility (defaults to [])
        List of build target patterns that identify the build rules that can include this 
        rule as a dependency, for example, by listing it in their deps or exported_deps 
        attributes. For more information, see visibility.

    # licenses (defaults to [])
        Set of license files for this library. To get the list of license files for a given 
        build rule and all of its dependencies, you can use buck query.

    # labels (defaults to [])
        Set of arbitrary strings which allow you to annotate a build rule with tags that can 
        be searched for over an entire dependency tree using buck query attrfilter().
"""

# Examples: A simple prebuilt_python_library with no external dependencies.
remote_file(
  name = "requests-download",
  url = "https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl",
  sha1 = "e1fc28120002395fe1f2da9aacea4e15a449d9ee",
  out = "requests-2.22.0-py2.py3-none-any.whl",
)

prebuilt_python_library(
  name = "requests",
  binary_src = ":requests-download",
)

# A slightly more complex example
prebuilt_python_library(
  name = "greenlet",
  binary_src = "greenlet-0.4.7-py2.7-macosx-10.10-x86_64.egg",
)

prebuilt_python_library(
  name = "gevent",
  binary_src = "gevent-1.0.2-py2.7-macosx-10.10-x86_64.egg",
  deps = [
    ":greenlet",
  ],
)

"""
#-------------------------------
2. python_binary()
#-------------------------------
This is liable to change in the future.

A python_binary() rule is used to build a PEX file—an executable Python package—that includes Python sources and resources from all transitive python_library dependencies.
Arguments
    # name (required)
        The short name for this build target. Also, the output PEX file will have this name as its
        base filename with an additional .pex extension.

    # main_module (required)
        The python module that should be the entry point of the binary. This should be a module 
        name within a python_library that this binary depends on. Note that module names take 
        base_module of the library into account. This property is mutually exclusive with main, 
        and should be preferred to main, which is deprecated.

    # main (defaults to None)
        This property is deprecated. Use a python_library dependency and main_module instead

        The Python file which serves as the entry point for the PEX. The interpreter initiates 
        execution of the PEX with the code in this file.

    # base_module (defaults to None)
        This property is deprecated.

        The package in which the main module should reside in its final location in the binary. 
        If unset, Buck uses the project-relative directory that contains the BUCK file.

    # platform (defaults to None)
        The name of the Python platform flavor to build against by default as defined in the 
        [python] section of .buckconfig.

    # deps (defaults to [])
        A list of python_library rules that specify Python modules to include in the PEX file—
        including all transitive dependencies of these rules.

    # preload_deps (defaults to [])
        A list of C/C++ library dependencies that need to be loaded before any other libraries 
        when the PEX starts up. This requires dynamic loader support, such as LD_PRELOAD, found 
        on most systems. This list is order- sensitive and the preload libraries listed here are
        passed down to the dynamic linker in the same order.

    # package_style (defaults to None)
        Used to override the global packaging style that is set in [[python].package_style].

    # linker_flags (defaults to [])
        Additional linker flags that should be applied to any linking which is specific to this 
        rule. Note that whether these flags are used is dependent on the native link strategy 
        selected in.buckconfig and currently applies only to the merged [python].native_link_strategy; 
        the separate link strategy pulls in shared libraries that are linked in the context of the 
        rules that own them, such as cxx_library.

    # visibility (defaults to [])
        List of build target patterns that identify the build rules that can include this rule as a 
        dependency, for example, by listing it in their deps or exported_deps attributes. For more 
        information, see visibility.

    # licenses (defaults to [])
        Set of license files for this library. To get the list of license files for a given build rule 
        and all of its dependencies, you can use buck query.

    # labels (defaults to [])
        Set of arbitrary strings which allow you to annotate a build rule with tags that can be searched 
        for over an entire dependency tree using buck query attrfilter().
"""

#Examples: Build a PEX from the Python files in the BUCK directory.

# BUCK
python_binary(
  name = 'tailer',
  main_module = 'tailer',
  deps = [
    ':tailerutils',
  ],
)

python_library(
  name = 'tailerutils',
  # The main module, tailer.py, is specified here.
  # (Separated out from the glob pattern for clarity.)
  srcs = glob(['tailer.py', '*.py']),
)

#Use the platform argument to select the [python#py2] platform as defined in .buckconfig.
#; .buckconfig

[python#py2]
  interpreter = /usr/bin/python2.7

# BUCK
python_binary(
  name = 'bin',
  platform = 'py2',
  main_module = 'main',
  deps = [
    ':bar',
  ],

"""
#-------------------------------
3. python_library()
#-------------------------------
This is liable to change in the future.

A python_library() rule is used to group together Python source files and resources to package 
them into a PEX using a top-level python_binary rule.
Arguments
    # name (required)
        The short name for this build target.

    # srcs (defaults to [])
        The set of Python (.py) files to include in this library.

    # platform_srcs (defaults to [])
        Python-platform-specific source files. These should be specified as a list of pairs where the 
        first element in each pair is an un-anchored regex against which the platform name is matched, 
        and the second element is a list of source files. The regex should use java.util.regex.Pattern 
        syntax. The platform name is a Python platform flavor defined in the [python] section of 
        .buckconfig.

    # resources (defaults to [])
        Static files to be packaged along with the Python sources. These resources can be accessed at 
        runtime using the pkg_resources module distributed with Python's setuptools.

    # platform_resources (defaults to [])
        Python-platform-specific resource files. These should be specified as a list of pairs where the 
        first element in each pair is an un-anchored regex against which the platform name is matched, 
        and the second element is a list of resource files. The regex should use java.util.regex.Pattern 
        syntax. The platform name is a Python platform flavor defined in the [python] section of 
        .buckconfig.

    # base_module (defaults to None)
        The package in which the specified source files and resources should reside in their final 
        location in the top-level binary. If unset, Buck uses the project-relative directory that 
        contains the BUCK file.

    # deps (defaults to [])
        Other python_library() rules that list srcs from which this rule imports modules.

    # exclude_deps_from_merged_linking (defaults to False)
        When linking the top-level binary with a merged [python].native_link_strategy, do not merge 
        or re-link any native transitive deps of this library. This is useful if this library wraps 
        prebuilt native extensions which cannot be re-linked as part of library merging.

    # visibility (defaults to [])
        List of build target patterns that identify the build rules that can include this rule as a 
        dependency, for example, by listing it in their deps or exported_deps attributes. For more 
        information, see visibility.

    # licenses (defaults to [])
        Set of license files for this library. To get the list of license files for a given build rule 
        and all of its dependencies, you can use buck query.

    # labels (defaults to [])
        Set of arbitrary strings which allow you to annotate a build rule with tags that can be searched 
        for over an entire dependency tree using buck query attrfilter().
"""
# Examples: Include Python source files and resource files.

# BUCK 

# A rule that includes a single Python file.
python_library(
  name = 'fileutil',
  srcs = ['fileutil.py'],
  deps = [
    '//third_party/python-magic:python-magic',
  ],
)

# A rule that uses glob() to include all Python source files in the
# directory in which the rule is defined. The rule also specifies a 
# resource file that gets packaged with the source file.
python_library(
  name = 'testutil',
  srcs = glob(['testutil/**/*.py']),
  resources = [
    'testdata.dat',
  ],
)


# Use the platform_srcs and platform_resources arguments to pull in source files 
# and resources only when building for a specific Python platform.

; .buckconfig

[python#py2]
  interpreter = /usr/bin/python2.7

[python#py3]
  interpreter = /usr/bin/python3.4
# BUCK

python_library(
  name = 'utils',
  platform_srcs = [
    ('py2', ['foo.py']),
    ('py3', ['bar.py']),
  ],
  platform_resources = [
    ('py2', ['foo.dat']),
    ('py3', ['bar.dat']),
  ],
)


"""
#-------------------------------
4. python_test()
#-------------------------------
This is liable to change in the future.

A python_test() rule defines a set of .py files that contain tests to run via the Python unit 
testing framework.

If your test requires static files you should specify these in the resources or 
platform_resources arguments. If you do not specify these files, they won't be available 
when your test runs.

Arguments
    # name (required)
        The short name for this build target.

    # srcs (defaults to [])
        The set of Python (.py) files to include in this library.

    # platform_srcs (defaults to [])
        Python-platform-specific source files. These should be specified as a list of pairs where the 
        first element in each pair is an un-anchored regex against which the platform name is matched, 
        and the second element is a list of source files. The regex should use java.util.regex.Pattern 
        syntax. The platform name is a Python platform flavor defined in the [python] section of 
        .buckconfig.

    # resources (defaults to [])
        Static files to be packaged along with the Python sources. These resources can be accessed at 
        runtime using the pkg_resources module distributed with Python's setuptools.

    # platform_resources (defaults to [])
        Python-platform-specific resource files. These should be specified as a list of pairs where the 
        first element in each pair is an un-anchored regex against which the platform name is matched, 
        and the second element is a list of resource files. The regex should use java.util.regex.Pattern 
        syntax. The platform name is a Python platform flavor defined in the [python] section of 
        .buckconfig.

    # base_module (defaults to None)
        The package in which the specified source files and resources should reside in their final 
        location in the top-level binary. If unset, Buck uses the project-relative directory that 
        contains the BUCK file.

    # exclude_deps_from_merged_linking (defaults to False)
        When linking the top-level binary with a merged [python].native_link_strategy, do not merge or 
        re-link any native transitive deps of this library. This is useful if this library wraps 
        prebuilt native extensions which cannot be re-linked as part of library merging.

    # main_module (defaults to None)
        The main module used to run the tests. This parameter is normally not needed, as Buck will provide 
        a default main module that runs all tests. However, you can override this with your own module 
        to perform custom initialization or command line processing. Your custom module can import the
        standard Buck test main as __test_main__, and can invoke it's normal main function as 
        __test_main__.main(sys.argv).

    # platform (defaults to None)
        The name of the Python platform flavor to build against by default as defined in the [python] 
        section of .buckconfig.

    # env (defaults to {})
        A map of environment names and values to set when running the test.

        It is also possible to expand references to other rules within the values of these environment 
        variables, using builtin string parameter macros:

        $(location //path/to:target)
        Expands to the location of the output of the build rule. This means that you can refer to these 
        without needing to be aware of how Buck is storing data on the disk mid-build.

    # deps (defaults to [])
        python_library rules used by the tests in this rules sources.

    # labels (defaults to [])
        A list of labels to be applied to these tests. These labels are arbitrary text strings and have 
        no meaning within buck itself. They can, however, have meaning for you as a test author (e.g., 
        smoke or fast). A label can be used to filter or include a specific python_test() rule when 
        executing buck test.

    # test_rule_timeout_ms (defaults to None)
        If set specifies the maximum amount of time (in milliseconds) in which all of the tests in 
        this rule should complete. This overrides the default rule_timeout if any has been specified 
        in [test].rule_timeout.

    # contacts (defaults to [])
        A list of organizational contacts for this test. These could be individuals who you would 
        contact in the event of a test failure or other issue with the test.

        contacts = [ 'Joe Sixpack', 'Erika Mustermann' ]

    # package_style (defaults to None)
        Used to override the global packaging style that is set in [[python].package_style].

    # preload_deps (defaults to [])
        A list of C/C++ library dependencies that need to be loaded before any other libraries when the 
        PEX starts up. This requires dynamic loader support, such as LD_PRELOAD, found on most systems.
        This list is order- sensitive and the preload libraries listed here are passed down to the 
        dynamic linker in the same order.

    # linker_flags (defaults to [])
        Additional linker flags that should be applied to any linking which is specific to this rule. 
        Note that whether these flags are used is dependent on the native link strategy selected in
        .buckconfig and currently applies only to the merged [python].native_link_strategy; the 
        separate link strategy pulls in shared libraries that are linked in the context of the 
        rules that own them, such as cxx_library.

    # visibility (defaults to [])
        List of build target patterns that identify the build rules that can include this rule as 
        a dependency, for example, by listing it in their deps or exported_deps attributes. For more 
        information, see visibility.

    # licenses (defaults to [])
        Set of license files for this library. To get the list of license files for a given build rule 
        and all of its dependencies, you can use buck query.

    # labels (defaults to [])
        Set of arbitrary strings which allow you to annotate a build rule with tags that can be searched 
        for over an entire dependency tree using buck query attrfilter().
"""
    
#Examples: A rule that includes a single .py file containing tests.
python_test(
  name = 'fileutil_test',
  srcs = ['fileutil_tests.py'],
  deps = [
    ':fileutil',
  ],
)

# A rule that uses glob() to include all sources in the directory which the
# rule is defined.  It also lists a resource file that gets packaged with
# the sources in this rule.
python_library(
  name = 'fileutil',
  srcs = glob(['fileutil/**/*.py']),
  resources = [
    'testdata.dat',
  ],
)

# Here is an example of using the `platform_srcs` and `platform_resources` 
# parameters to pull in sources/resources only when building for a specific 
# Python platform:

; .buckconfig
[python#py2]
  interpreter = /usr/bin/python2.7
[python#py3]
  interpreter = /usr/bin/python3.4
# BUCK
python_test(
  name = 'test',
  platform_srcs = [
    ('py2', ['foo.py']),
    ('py3', ['bar.py']),
  ],
  platform_resources = [
    ('py2', ['foo.dat']),
    ('py3', ['bar.dat']),
  ],
)

# Here is an example of using the `platform` parameter to 
# select the "py2" Python platform as defined in `.buckconfig` above:

# BUCK
python_test(
  name = 'bin',
  platform = 'py2',
  srcs = [
    'foo.py',
  ],
)