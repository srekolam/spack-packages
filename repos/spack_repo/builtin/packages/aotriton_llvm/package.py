# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import re

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

_versions = {
    "86b69c31-ubuntu": {
        "apt": (
            "b596c493d8f16e1c40026d16024fdcb3225dc09c5c7d8493833dff774677f67b",
            "https://oaitriton.blob.core.windows.net/public/llvm-builds/llvm-86b69c31-ubuntu-x64.tar.gz",
        ),
    },
}

class AotritonLlvm(Package):
    """FIXME: Put a proper description of your package here."""

    pkg_type = "apt"
    for ver, packages in _versions.items():
        pkg = packages.get(pkg_type)
        if pkg:
            version(ver, sha256=pkg[0], url=pkg[1], expand=False)

    def install(self, spec, prefix):
        for file in os.listdir("."):
            os.system(f"tar xvf {file}")
        install_tree(f"llvm-{spec.version}-x64/", prefix)
