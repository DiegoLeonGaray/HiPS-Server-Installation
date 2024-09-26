# HiPS Server Installation

This repository provides the necessary tools and instructions to set up a basic HiPS (Hierarchical Progressive Survey) server using Pan-STARRS images.

## Contents

1. [Prerequisites](#prerequisites)
2. [Download Pan-STARRS Images](#download-pan-starrs-images)
3. [Generate HiPS Server](#generate-hips-server)
4. [Generate Multiresolution Images](#generate-multiresolution-images)
5. [Additional Information](#additional-information)

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- **Java**: Ensure you have Java installed. You can download it from [here](https://www.java.com/en/download/).

## Download Pan-STARRS Images

To download the Pan-STARRS images in the r filter, run the following command in your terminal:

```bash
python MAST_PS1_Download.py
```

This script will download all the images sequentially and store them in a folder named `mastDownload`.

## Generate HiPS Server

Once the images are downloaded, you'll need to generate the HiPS server using the Aladin package.

### What is AladinBeta.jar?

**Aladin** is a software tool designed for the visualization of astronomical images and catalogues. The `AladinBeta.jar` package contains the code necessary to create the HiPS server that represents the sky portion covered by the images in the `mastDownload` folder.

### Running the HiPS Generation Command

To generate the HiPS server, open your terminal and navigate to the directory containing the `AladinBeta.jar` file and the `mastDownload` folder. Run the following command:

```bash
java -Xmx16g -jar AladinBeta.jar -hipsgen maxThread=20 in=mastDownload out=HiPS id=ALeRCE INDEX TILES CHECKCODE DETAILS
```

- **Parameters**:
  - `out=HiPS`: This defines the name of the folder that will contain the generated HiPS server.
  - `id=ALeRCE`: This provides an identification ID for the HiPS server.

- **Flags**:
  - **INDEX**: Enables the creation of an index file for efficient access to HiPS tiles, containing metadata about the HiPS structure.
  - **TILES**: Generates the actual tiles for the HiPS, essential for visualization.
  - **CHECKCODE**: Performs a consistency check on the generated HiPS data to ensure files meet specifications and are error-free.
  - **DETAILS**: Provides detailed logging during the generation process, useful for debugging.

## Generate Multiresolution Images

This repository also includes a code called `hips2delight`, which contains the function `fits_cutout`. This function takes the following parameters:

- **Central celestial coordinates** of the image.
- **HiPS order**.
- **Size in pixels** of the image to be returned.

The function returns an HDUList object that characterizes the generated FITS file. This code allows for the generation of multiresolution images required by the DELIGHT algorithm to predict the position of the host galaxy for a given supernova alert.

## Additional Information

For more details on how to use the generated HiPS server, please refer to the [official user manual](https://aladin.cds.unistra.fr/hips/HipsgenManual.pdf) provided by the Aladin website.



