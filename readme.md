# How to Use the Cover Image Scripts

These scripts process input images, add circular masks with specified radii, and save the resulting images in the `outputs` or `covered_images` folders.

## Prerequisites
- Python installed on your system.
- Basic knowledge of using the terminal or command prompt.

## Steps:

### 1. Open Terminal in the Code Folder
Right-click the folder containing the code files and select "Open in Terminal" to open a terminal window in the code directory.

### 2. Create a New Virtual Environment
Create a new Python virtual environment named `cover` using the following command:

```bash
python -m venv cover
```

### 3. Activate the Virtual Environment
Activate the virtual environment. On Windows, use:

```bash
.\cover\Scripts\activate
```

On macOS and Linux, use:

```bash
source cover/bin/activate
```

### 4. Install Required Packages
Install the necessary packages from the `requirements.txt` file using the following command:

```bash
pip install -r requirements.txt
```

### 5. Run the Scripts

#### For `cover_tripod.py`:

Run the Python script `cover_tripod.py` with the following command, providing the path to the input image, the radius of the circular mask in pixels, and specify the processing device (optional, default is 'cuda'):

```bash
python cover_tripod.py -i <path_to_image> -r <radius> --device <device>
```

Replace `<path_to_image>` with the path to your input image file, `<radius>` with the desired radius of the circular mask in pixels, and `<device>` with either 'cuda' or 'cpu' to specify the processing device (optional).

#### For `cover_tripod_multiple.py`:

Run the Python script `cover_tripod_multiple.py` with the following command, providing the path to the input image folder, the radius of the circular mask in pixels, and specify the processing device (optional, default is 'cuda'):

```bash
python cover_tripod_multiple.py -i <path_to_image_folder> -r <radius> --device <device>
```

Replace `<path_to_image_folder>` with the path to your input image folder, `<radius>` with the desired radius of the circular mask in pixels, and `<device>` with either 'cuda' or 'cpu' to specify the processing device (optional).

### 6. Check Output
The processed images will be saved in the `outputs` or `covered_images` folder, depending on the script you run.

---

Feel free to reach out if you have any questions or encounter any issues. Happy coding!