# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.cmake import CMakePackage, generator
from spack_repo.builtin.build_systems.compiler import CompilerPackage
from spack_repo.builtin.packages.llvm.package import LlvmDetection

from spack.package import *


class LlvmAotriton(CMakePackage, LlvmDetection, CompilerPackage):
    """FIXME: Put a proper description of your package here."""

    url = "https://github.com/llvm/llvm-project/archive/llvmorg-7.1.0.tar.gz"
    git = "https://github.com/llvm/llvm-project"
    version("21.1.4", sha256="3a0921d78be74302cb054da1dad59e706814d8fed3a6ac9b532e935825a0715c")
    version("0.10", commit="3c709802d31b5bc5ed3af8284b40593ff39b9eec")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("cmake@3.13.4:", type="build")
    depends_on("python", type="build")
    depends_on("z3", type="link")
    depends_on("zlib-api", type="link")
    depends_on("ncurses+termlib", type="link")
    depends_on("libxml2", type="link")
    depends_on("py-pybind11")
    depends_on("pkgconfig", type="build")

    generator("ninja")

    root_cmakelists_dir = "llvm"

    def _standard_flag(self, *, language, standard):
        flags = {
            "cxx": {"11": "-std=c++11", "14": "-std=c++14", "17": "-std=c++17"},
            "c": {"99": "-std=c99", "11": "-std=c1x"},
        }
        return flags[language][standard]

    def cmake_args(self):
        llvm_projects = ["llvm", "mlir"]
        args = [
            self.define("LLVM_ENABLE_Z3_SOLVER", "OFF"),
            self.define("CMAKE_BUILD_TYPE", "Release"),
            self.define("LLVM_REQUIRES_RTTI", True),
            self.define("LLVM_ENABLE_LIBXML2", False),
            self.define("LLVM_ENABLE_RTTI", "ON"),
            self.define("CMAKE_INSTALL_LIBDIR", "lib"),
            self.define("CMAKE_CXX_STANDARD", 17),
            self.define("LLVM_BUILD_UTILS", "ON"),
            self.define("LLVM_TARGETS_TO_BUILD", "host;NVPTX;AMDGPU"),
            self.define("MLIR_ENABLE_BINDINGS_PYTHON", "ON"),
            self.define("LLVM_ENABLE_TERMINFO", "OFF")
        ]
        args.append(self.define("LLVM_ENABLE_PROJECTS", llvm_projects))
        return args
                                                   
