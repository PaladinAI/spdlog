from conans import ConanFile
from conans import tools

class SpdlogConan(ConanFile):
    name = "spdlog"
    version = "1.1.0"
    description = "Fast C++ logging library."
    url = "https://github.com/gabime/spdlog"
    license = "MIT"
    exports_sources = "include/*"

    def package(self):
        self.copy("*.h", src="include", dst="include")
        self.copy("*ostream.cc", src="include", dst="include")
        self.copy("*format.cc", src="include", dst="include")

    def package_info(self):
        self.info.header_only()
