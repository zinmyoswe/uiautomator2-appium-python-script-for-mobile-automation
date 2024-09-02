# APKAnalyzer

A Python tool to analyze APK files and extract metadata such as package name, version, and permissions using the `androguard` library.

## Features

- Extracts package name, version name, and version code from an APK file.
- Retrieves the list of permissions required by the APK.
- Easy-to-use command-line interface.

## Requirements

- Python 3.6 or higher
- `androguard` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/APKAnalyzer.git
    cd APKAnalyzer
    ```

2. **Install dependencies:**
    Install the required Python libraries using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Place the APK file in the `test_apk/` directory:**

   Make sure the APK file you want to analyze is located in the `test_apk/` directory.

2. **Run the script:**

   Run the `apk_analyzer.py` script from the terminal or command prompt:

    ```bash
    python apk_analyzer.py
    ```

3. **Output:**

   The script will output metadata such as the package name, version, and permissions of the APK file.

## Example

Here is an example of how the output might look:


