#!/usr/bin/env python

from os.path import join, dirname


def main():
    try:
        from robot.libdoc import libdoc
    except Exception as ex:
        err_msg = "Robot Framework 2.7 or later required for generating documentation"
        raise RuntimeError(err_msg) from ex

    libdoc(join(dirname(__file__), '..', 'src', 'BrowserMobProxyLibrary'),
           join(dirname(__file__), 'BrowserMobProxyLibrary.html'))


if __name__ == '__main__':
    main()
