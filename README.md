# Pi-Thon

A Pythonic starter for your Raspberry Pi projects with GPIO support, pre-configured linting, type checking, and testing.

## Features

- **GPIO Libraries**: RPi.GPIO and gpiozero for hardware control
- **Code Quality**: Ruff for linting and formatting
- **Type Safety**: mypy for static type checking
- **Testing**: pytest with coverage reporting
- **Git Hooks**: pre-commit for automated code quality checks
- **Camera Support**: picamera2 ready to use
- **Configuration Management**: python-dotenv for environment variables

## Prerequisites

- Raspberry Pi (any model with GPIO)
- Python 3.11 or higher
- Git

## Quick Start

### 1. Create Your Project

1. Click the **"Use this template"** button at the top of this page
2. Name your new repository
3. Clone your new repository:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-PROJECT-NAME.git
cd YOUR-PROJECT-NAME
```

4. Update project information in `pyproject.toml`:
   - Change `name` to your project name
   - Update `authors` with your information
   - Update repository URLs in `[project.urls]`

### 2. System Setup (Raspberry Pi only)

**If you're setting this up outside a Pi for development, skip to step 3**

First, update your system packages:

```bash
sudo apt update
sudo apt upgrade -y
```

Install Python development tools: (These may come installed with your OS)

```bash
sudo apt install -y python3-pip python3-venv git
```

#### Optional - Install ZSH and Oh My ZSH

```bash
# Install ZSH
sudo apt-get update && sudo apt-get install zsh

# Set default to ZSH
chsh -s $(which zsh)

# Install Oh My ZSH
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Install autosuggestions plugin
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

# Install syntax highlighting plugin
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

Then edit the RC file:

```bash
nano ~/.zshrc
```

Add these plugins:

```zsh
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
```

### 3. Setup Virtual Environment and Dependencies

Create and activate a virtual environment:

```bash
make venv
source venv/bin/activate
```

Install dependencies:

```bash
# On Mac (development only - skips Pi hardware libraries)
make install-dev

# On Raspberry Pi (includes hardware libraries)
make install-pi
```

### 4. Configure Pre-commit Hooks

Install pre-commit hooks:

```bash
make install-hooks
```

Update hook versions to latest (recommended for new projects):

```bash
make update-deps
```

Optional - run hooks to verify setup:

```bash
make pre-commit
```

### 5. Configure Environment Variables

Create a `.env` file for your configuration:

```bash
cp .env.example .env
```

Edit `.env` with your settings (GPIO pins, API keys, etc.)

## Project Structure

```
YOUR-PROJECT-NAME/
├── .vscode/                # VSCode settings
├── examples/               # Example scripts and wiring diagrams
│   ├── blink.py           # Basic LED blink example
│   ├── blink_env.py       # Advanced example with env vars
│   └── button.py          # Button input example
├── src/                    # Your application code
│   └── your_package/
├── tests/                  # Test files
│   └── test_example.py    # Example test file
├── typings/                # Custom type stubs for libraries without types
├── .editorconfig           # Editor configuration
├── .env.example            # Environment variable template
├── .gitignore              # Git ignore rules
├── .pre-commit-config.yaml # Pre-commit hooks
├── LICENSE                 # MIT License
├── Makefile                # Development commands
├── pyproject.toml          # Project configuration
└── README.md               # This file
```

## Development Workflow

### Quick Reference

```bash
make help          # Show all available commands
make format        # Format code with Ruff
make lint          # Check code with Ruff
make lint-fix      # Auto-fix linting issues
make typecheck     # Type check with mypy
make test          # Run tests
make test-cov      # Run tests with coverage report
make check         # Run all checks (lint + typecheck + test)
make pre-commit    # Run pre-commit hooks manually
```

### Running Code Quality Tools

```bash
# Format and lint your code
make format
make lint-fix

# Type check
make typecheck

# Run everything at once
make check
```

### Running Tests

```bash
# Run all tests
make test

# Run with coverage report
make test-cov
# Coverage report will be in htmlcov/index.html

# Run specific test file
pytest tests/test_example.py
```

### GPIO Access

Most GPIO operations require root privileges. Run your scripts with sudo:

```bash
sudo python3 your_script.py
```

Alternatively, add your user to the gpio group:

```bash
sudo usermod -a -G gpio $USER
# Log out and back in for changes to take effect
```

## Common GPIO Pins

| Pin       | Function               | Notes                        |
| --------- | ---------------------- | ---------------------------- |
| 18        | PWM0                   | Good for LED control, servos |
| 12        | PWM0                   | Alternative PWM pin          |
| 23, 24    | GPIO                   | General purpose I/O          |
| 2, 3      | I2C (SDA, SCL)         | For sensors and displays     |
| 10, 9, 11 | SPI (MOSI, MISO, SCLK) | For high-speed devices       |

**Warning**: Always check your specific Raspberry Pi model's pinout. Use 3.3V logic levels unless using a level shifter.

## Example Usage

Pi-Thon includes several ready-to-run examples in the `examples/` directory:

- **`blink.py`** - Basic LED blink with proper cleanup and error handling
- **`blink_env.py`** - Advanced example using environment variables, type hints, and input validation
- **`button.py`** - Button input controlling an LED with event-driven programming

### Running Examples

```bash
# Basic LED blink
python3 examples/blink.py

# Advanced example with .env configuration
python3 examples/blink_env.py

# Button-controlled LED
python3 examples/button.py
```

See the individual example files for wiring diagrams and detailed comments.

## Development on Non-Pi Systems

Pi-Thon includes type stubs in the `typings/` directory that enable you to write and type-check GPIO code on your development machine (Mac, Linux, Windows) before deploying to your Raspberry Pi.

### How It Works

The type stubs provide type information for `gpiozero` and `RPi.GPIO` without requiring the actual libraries to be installed. This means:

- ✅ **Full IDE support**: Autocomplete, inline documentation, and type hints work in VSCode
- ✅ **Type checking passes**: `make typecheck` works on any system
- ✅ **Code runs unchanged**: Deploy the same code to your Pi without modifications
- ✅ **Catch errors early**: Find type errors before running on hardware

### Development Workflow

1. **Write code on your Mac/PC** with full IDE support:

   ```python
   from gpiozero import LED  # Type hints work!
   from time import sleep

   led = LED(17)  # IDE knows what methods are available
   led.on()       # Autocomplete works!
   ```

2. **Run type checking locally**:

   ```bash
   make typecheck  # Passes even without GPIO hardware
   ```

3. **Deploy to Raspberry Pi**:

   ```bash
   # On your Pi, install with hardware dependencies
   make install-pi

   # Run your code
   python3 your_script.py
   ```

### Extending Type Stubs

The included stubs cover the most common GPIO components. If you need additional components, you can extend the stubs in `typings/gpiozero.pyi` or `typings/RPi/GPIO.pyi`. Just add the class or function signature - the implementation isn't needed since these are only for type checking!

## Troubleshooting

### Import Errors

If you get import errors for GPIO libraries, make sure you're running on a Raspberry Pi and have installed the dependencies:

```bash
pip install RPi.GPIO gpiozero
```

### Permission Errors

If you get permission errors accessing GPIO:

```bash
sudo usermod -a -G gpio $USER
# Then log out and back in
```

### mypy Errors for GPIO Libraries

The Raspberry Pi libraries don't have type stubs. These are configured to be ignored in `pyproject.toml`, but if you see warnings, they're expected and won't affect functionality.

## Additional Resources

- [Raspberry Pi GPIO Pinout](https://pinout.xyz/)
- [gpiozero Documentation](https://gpiozero.readthedocs.io/)
- [RPi.GPIO Documentation](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/)
- [Adafruit Learning Guides](https://learn.adafruit.com/)

## Contributing

1. Create a feature branch
2. Make your changes
3. Ensure all tests pass and pre-commit hooks succeed
4. Submit a pull request

## License

MIT License - see LICENSE file for details
