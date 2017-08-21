# {{cookiecutter.project_name}} #

{{cookiecutter.project_short_description}}

-------------------------------------------------------------------------------

Install
-------

The latest [`{{cookiecutter.project_slug}}` release][3] is available as a
[Conda][2] package from the [`{{cookiecutter.github_username}}`][4] channel.

To install `{{cookiecutter.project_slug}}` in an **activated Conda environment**, run:

    conda install -c {{cookiecutter.github_username}} -c conda-forge {{cookiecutter.project_slug}}

-------------------------------------------------------------------------------

## Upload firmware ##

To upload the pre-compiled firmware included in the Python package, from an
**activated Conda environment** run the following command:

    python -m {{cookiecutter.project_module_name}}.bin.upload

-------------------------------------------------------------------------------

Conda package contents
----------------------

The `{{cookiecutter.project_slug}}` Conda package includes:

 - `{{cookiecutter.project_module_name}}.SerialProxy` **Python class** providing a high-level interface to
   the `{{cookiecutter.project_slug}}` hardware.
 - **Compiled firmware binary** for the `{{cookiecutter.project_slug}}` hardware.

The installed components (relative to the root of the Conda environment) are
shown below:

    ├───Lib
    │   └───site-packages
    │       └───{{cookiecutter.project_module_name}} (Python package)
    │
    └───Library
        └───bin
            └───platformio
                └───{{cookiecutter.project_slug}} (compiled firmware binaries)
                    │   platformio.ini   (PlatformIO environment information)
                    │
                    └───default
                        firmware.hex

-------------------------------------------------------------------------------

## Usage ##

After uploading the firmware to the board, the
`{{cookiecutter.project_module_name}}.Proxy` class can be used to interact with
the Arduino device.

See the session log below for example usage.

### Example interactive session ###

    >>> import {{cookiecutter.project_module_name}}

Connect to {{cookiecutter.project_slug}}:

    >>> proxy = {{cookiecutter.project_module_name}}.SerialProxy()

Query the number of bytes free in device RAM.

    >>> proxy.ram_free()
    409

Query descriptive properties of device.

    >>> proxy.properties
    base_node_software_version                               0.9.post8.dev141722557
    name                                                                    {{cookiecutter.project_slug}}
    manufacturer                                                           {{cookiecutter.hardware_manufacturer}}
    url                                                                  http://...
    software_version                                                            0.1
    dtype: object

Use Arduino API methods interactively.

    >>> # Set pin 13 as output
    >>> proxy.pin_mode(13, 1)
    >>> # Turn led on
    >>> proxy.digital_write(13, 1)
    >>> # Turn led off
    >>> proxy.digital_write(13, 0)


-------------------------------------------------------------------------------

Develop
-------

**The firmware C++ code** is located in the `src` directory.  The **key
functionality** is **defined in the `{{cookiecutter.project_module_name}}::Node` class in the file
`Node.h`**.


### Adding new remote procedure call (RPC) methods ###

New methods may be added to the Python API by adding new methods to the
`{{cookiecutter.project_module_name}}::Node` C++ class in the file `Node.h`.


### Set up development environment (within a Conda environment) ###

 1. **Clone `{{cookiecutter.project_slug}}`** source code from [GitHub repository][5].
 2. Create the `.pioenvs` directory if it doesn't already exist.
 3. Run the following command within the root of the cloned repository to
    **install run-time dependencies** and link working copy of firmware
    binaries and Python package for run-time use:

        paver develop_link

 4. **Restart terminal and reactivate Conda environment (e.g., `activate` if
    Conda was installed with default settings).**

Step **4** is necessary since at least one of the installed dependencies sets
environment variables, which are only initialized on subsequent activations of
the Conda environment (i.e., they do not take effect immediately within the
running environment).


### Build firmware ###

Run the following command within the root of the cloned repository to **build
the firmware**:

    paver build_firmware

The compiled firmware binary is available under the `.pioenvs` directory, as
shown below:

    └───.pioenvs
        └───default
                firmware.hex


### Flash/upload firmware ###

To flash/upload a compiled firmware to the hardware, run the following command
from the root of the repository:

    pio run --target upload --target nobuild


### Unlink development working copy ###

Run the following command within the root of the cloned repository to unlink
working copy of firmware binaries and Python package:

    paver develop_unlink

This will allow, for example, installation of a main-line release of the
`{{cookiecutter.project_slug}}` Conda package.

-------------------------------------------------------------------------------

License
-------

This project is licensed under the terms of the [MIT License](/LICENSE)

-------------------------------------------------------------------------------

Contributors
------------

 - {{cookiecutter.full_name}} ([@{{cookiecutter.github_username}}](https://github.com/{{cookiecutter.github_username}}))


[1]: https://www.arduino.cc/en/Reference/HomePage
[2]: http://www.scons.org/
[3]: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}
