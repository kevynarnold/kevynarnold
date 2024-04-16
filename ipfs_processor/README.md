# IPFS Processor

IPFS Processor is a Python package designed to handle image files by converting them to PNG format, embedding metadata directly into the images, and generating corresponding JSON files with extensive metadata. This package is particularly useful for projects involving digital asset management, where maintaining image integrity and metadata is crucial.

## Features

Image Conversion: Converts images from various formats to PNG.
Metadata Embedding: Embeds metadata such as description, compiler details, and custom dates directly into PNG files.
JSON Metadata: Generates JSON files for each image containing metadata and IPFS links.
Edition Tracking: Automatically increments edition numbers for image series.
Random Date Generation: Assigns random dates to each image's metadata for enhanced uniqueness.
Installation

Ensure you have Python 3.6 or higher installed on your machine. You can install IPFS Processor directly from the source:

```
# Clone the repository
git clone https://github.com/yourusername/ipfs_processor.git

# Navigate to the cloned directory
cd ipfs_processor

# Install the package
pip install .
```

## Configuration

Before running the package, configure your paths and metadata settings in the config.yaml file located in the ipfs_processor directory.
```
input_dir: '/path/to/input/directory'
output_png_dir: '/path/to/output/png/directory'
output_json_dir: '/path/to/output/json/directory'
cid: 'your_default_cid'
edition: '1'
description: 'Saint Lucia - Let Her Inspire You'
compiler: 'KevynArnold'
date_format: '%Y-%m-%d'
```

## Usage

After configuration, run the package from your terminal:
```
# Activate your Python environment if you have one
source /path/to/your/env/bin/activate

# Run the IPFS Processor
ipfs_processor
```

## Output

PNG images will be saved in the output_png_dir with embedded metadata.
JSON files containing the metadata and IPFS links will be saved in output_json_dir.
Dependencies

- Pillow: For image processing.
- PyYAML: For reading YAML configuration files.
- piexif: For handling EXIF data in images.
Make sure all dependencies are installed using pip:
```
pip install Pillow PyYAML piexif
```

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with your proposed changes.