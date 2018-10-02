from conans import ConanFile
from conans import tools

class SpdlogConan(ConanFile):
    name = "spdlog"
    version = "0.14.0"
    description = "https://gitlab.axis-canada.com/3rdparty/spdlog."
    url = "https://github.com/gabime/spdlog"
    license = "MIT"
    exports_sources = "include/*"
    no_copy_source = True

    def package(self):
        self.copy("*.h", src="include", dst="include")
        self.copy("*ostream.cc", src="include", dst="include")
        self.copy("*format.cc", src="include", dst="include")

    def package_info(self):
        self.info.header_only()
