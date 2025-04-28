# port-scanner

This is a simple Python-based port scanner that allows users to scan a range of ports on a specified target IP address. It helps identify open ports within a given range, which is useful for security assessments, penetration testing, and network management.

## Features
- **Scan a range of ports**: Enter a start and end port to scan.
- **Timeout handling**: Each connection attempt has a timeout, so the scanner doesn’t hang indefinitely.
- **Port status display**: The script will display whether a port is open or closed.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ItsAkanksha1/port-scanner.git
   ```

2. Navigate to the project directory:
   ```bash
   cd port-scanner
   ```

3. Ensure you have Python installed (Python 3.x recommended).

4. Install the required Python libraries (if any, though this project uses built-in libraries):
   ```bash
   pip install -r requirements.txt  # Optional, if you create a requirements.txt
   ```

## Usage

1. Run the port scanner script:
   ```bash
   python port_scanner.py
   ```

2. Enter the target IP address, the starting port, and the ending port when prompted.

3. The script will then scan the specified ports on the target IP and display the results.

### Example:
   ```bash
   Enter target IP address: 192.168.1.1
   Enter start port: 80
   Enter end port: 100
   ```

   The script will display open ports between port 80 and port 100 on `192.168.1.1`.

## Contributing

If you would like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. Please ensure your contributions align with the project's goals and adhere to the following guidelines:

- Follow best practices for code style and documentation.
- Add tests for any new features you introduce.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is built using Python and its `socket` library.
- Thanks to all contributors who improve and maintain open-source tools like Python.
```
