# Algorithm-Visualizer
This code uses Python and the open-source GTK graphics library to create a responsive algorithm visualizer on Linux. 

## Installing Dependencies
First, you will need to install system-level dependencies

For Ubuntu/Debian/Mint, run:
```
sudo apt update
sudo apt install -y build-essential pkg-config libcairo2-dev libgirepository1.0-dev python3-dev gir1.2-gtk-3.0
```
For Arch Linux, run:
```
sudo pacman -Syu
sudo pacman -S base-devel pkg-config cairo gobject-introspection python gtk3
```
For Fedora, run:
```
sudo dnf update
sudo dnf install @development-tools pkg-config cairo-devel gobject-introspection-devel python3-devel gtk3
```

Once you've installed the system-level dependencies, you'll need to install Python dependencies:
```
pip install -r requirements.txt
```

## Running the program
Run: 
```
python3 main.py
```
