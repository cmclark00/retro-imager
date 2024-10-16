# Retro-Imager

**Retro-Imager** is a fork of the official Raspberry Pi Imager, specially tailored for retro gaming handhelds and the custom firmwares that power them. This project simplifies the process of flashing custom firmware images to your retro handheld devices, allowing you to quickly get set up and start gaming.

## Supported Devices & Custom Firmwares

At present, **Retro-Imager** supports:
**muOS** and **Rocknix**. 
More devices and firmwares will be added in future releases!

## Features

- **Easy-to-use interface**: Retro-Imager retains the familiar look and feel of Raspberry Pi Imager, making it accessible to anyone.
- **Handheld Focus**: Tailored specifically for retro handheld gaming devices, eliminating unnecessary options for general-purpose single-board computers.
- **Custom Firmware Support**: Flash custom OS images like muOS and Rocknix quickly and easily.
- **Firmware Recommendations**: The top-most firmware option for each device is our recommended choice, ensuring optimal performance and compatibility.

## Getting Started

### Prerequisites

- A computer running Linux (x86_64) or Windows (x86_64)
- A microSD card reader
- A microSD card (at least 8GB, though larger is recommended)

### Installation

1. Download the most recent release from the [GitHub releases page](https://github.com/cmclark00/retro-imager/releases).
2. Extract the files (if necessary) and run the application on your system:
   - For Linux: Make the file executable and run it.
     ```bash
     chmod +x retro-imager.AppImage
     ./retro-imager.AppImage
     ```
   - For Windows: Double-click the `.exe` file.

### Using Retro-Imager

1. Launch Retro-Imager.
2. Select your device from the list (e.g., RG35XX Plus, RG28XX, RGB30).
3. Choose the custom firmware you would like to install. The top-most option is the recommended firmware for your selected device.
4. Insert your microSD card into your computer.
5. Select the correct device from the list and click "Write".
6. Safely remove the microSD card and insert it into your retro gaming handheld.

## Contributing

We welcome contributions! Whether you're improving code, fixing bugs, or expanding firmware support, your help is appreciated.

To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeature
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
5. Open a Pull Request.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
