# Style Transfer Application

## live Link: https://stylizer.streamlit.app

## Overview
This project implements a neural style transfer application that allows users to combine the content of one image with the artistic style of another. The application uses deep learning techniques to generate visually appealing images that maintain the content of the original photo while adopting the artistic style of a reference image.

## Features
- **Content-Style Separation**: Preserves the content of the input image while applying the style of the reference image
- **Customizable Parameters**: Control the style transfer intensity and other parameters
- **Fast Processing**: Optimized for efficient style transfer
- **High-Quality Output**: Generates high-resolution stylized images

## Requirements
- Python 3.7+
- TensorFlow 2.x
- NumPy
- Pillow
- Matplotlib (for visualization)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/surajmaity/ML_projects/tree/main/Style_transfer_app
   ```
2. Navigate to the project directory:
   ```bash
   cd Style_transfer_app
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Prepare your content and style images in the `images/` directory
2. Run the main script:
   ```bash
   python style_transfer.py --content <content_image> --style <style_image> --output <output_image>
   ```
3. View the generated image in the `outputs/` directory

## Parameters
- `--content`: Path to the content image
- `--style`: Path to the style image
- `--output`: Path to save the output image
- `--iterations`: Number of optimization iterations (default: 1000)
- `--content_weight`: Weight for content loss (default: 1e4)
- `--style_weight`: Weight for style loss (default: 1e-2)

## Research Paper
This implementation is based on the paper:
"Exploring the Structure of a Real-time, Arbitrary Neural Artistic Stylization Network" by Golnaz Ghiasi, Honglak Lee, Manjunath Kudlur, Vincent Dumoulin, Jonathon Shlens
Published in 2017, this paper presents a real-time approach to neural style transfer using feed-forward networks.

Paper Link: https://arxiv.org/pdf/1705.06830

## Dataset
The model can be used with any images, but for training and testing, we recommend using:
- **COCO Dataset** (Common Objects in Context): Used for content images
  - Website: https://cocodataset.org/
  - Contains over 200,000 labeled images
- **WikiArt Dataset**: Used for style images
  - Website: https://www.wikiart.org/
  - Contains over 80,000 artworks from various artists and styles



