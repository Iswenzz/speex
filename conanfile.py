from conans import ConanFile, CMake


class speex(ConanFile):
    name = "speex"
    version = "1.2.1"
    license = "COPYING"
    url = "https://gitlab.xiph.org/xiph/speex"
    description = "Speex voice codec."

    generators = "cmake"
    exports_sources = (
        "include/*",
        "libspeex/*",
        "config.h",
        "CMakeLists.txt",
        "COPYING",
        "INSTALL",
        "README",
    )

    settings = "os", "arch", "compiler", "build_type"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("COPYING, INSTALL, README")
        self.copy("config.h")
        self.copy("*.h", src="include", dst="include")
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["speex"]
