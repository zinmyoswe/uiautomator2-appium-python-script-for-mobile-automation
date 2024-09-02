from androguard.core import apk

class APKAnalyzer:
    def __init__(self, apk_path):
        # Load the APK file using Androguard
        self.apk = apk.APK(apk_path)

    def get_package_name(self):
        # Extract package name
        return self.apk.get_package()

    def get_version_name(self):
        # Extract version name
        return self.apk.get_androidversion_name()

    def get_version_code(self):
        # Extract version code
        return self.apk.get_androidversion_code()

    def get_permissions(self):
        # Extract permissions
        return self.apk.get_permissions()

    def analyze(self):
        # Return all metadata in a dictionary
        metadata = {
            "Package Name": self.get_package_name(),
            "Version Name": self.get_version_name(),
            "Version Code": self.get_version_code(),
            "Permissions": self.get_permissions()
        }
        return metadata

if __name__ == "__main__":
    apk_path = "test_apk/susi-ai-master-app-playStore-release.apk"  # Change this path to your APK file
    analyzer = APKAnalyzer(apk_path)
    metadata = analyzer.analyze()

    # Print metadata
    for key, value in metadata.items():
        print(f"{key}: {value}")
