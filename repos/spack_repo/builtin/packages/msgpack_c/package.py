# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class MsgpackC(CMakePackage):
    """A small, fast binary interchange format convertible to/from JSON"""

    homepage = "http://www.msgpack.org"
    url = "https://github.com/msgpack/msgpack-c/archive/cpp-3.0.1.tar.gz"

    license("BSL-1.0")
    version("7.0.0", sha256="070881ebea9208cf7e731fd5a46a11404025b2f260ab9527e32dfcb7c689fbfc")
    version("6.1.1", sha256="d7b119f292365d41403b41b40c2fefd82ebd81241e3c658fafe0e638fa54604a")
    version("6.1.0", sha256="5e63e4d9b12ab528fccf197f7e6908031039b1fc89cd8da0e97fbcbf5a6c6d3a")
    version("6.0.0", sha256="d02f7ffd28b1d38ab9f5f758c4744fadfae92150461fb8154c98ac49226cff90")
    version("5.0.0", sha256="bd6b8e255f0a62cf8f50f1d292f979ac8ea9a4aa121938679d6f419d6df70ea3")
    version("3.0.1", sha256="1b834ab0b5b41da1dbfb96dd4a673f6de7e79dbd7f212f45a553ff9cc54abf3b")
    version("3.1.1", sha256="bda49f996a73d2c6080ff0523e7b535917cd28c8a79c3a5da54fc29332d61d1e")
    version("3.0.1", sha256="1b834ab0b5b41da1dbfb96dd4a673f6de7e79dbd7f212f45a553ff9cc54abf3b")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("boost", when="@4:")
    depends_on("cmake@2.8.0:", type="build")
    depends_on("cmake@3.1.0:", type="build", when="@4:")
    depends_on("googletest", type="test")

    def cmake_args(self):
        args = [
            self.define("CMAKE_CXX_FLAGS", "-Wno-implicit-fallthrough"),
            self.define("CMAKE_C_FLAGS", "-Wno-implicit-fallthrough"),
            self.define("MSGPACK_BUILD_TESTS", self.run_tests),
        ]
        return args
