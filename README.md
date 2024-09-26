# HiPS Server Installation

This repository provides the necessary tools and instructions to set up a basic HiPS (Hierarchical Progressive Survey) server using Pan-STARRS images.

## Contents

1. [Prerequisites](#prerequisites)
2. [Download Pan-STARRS Images](#download-pan-starrs-images)
3. [Generate HiPS Server](#generate-hips-server)
4. [Additional Information](#additional-information)

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- **Java**: Ensure you have Java installed. You can download it from [here](https://www.java.com/en/download/).

## Download Pan-STARRS Images

To download the Pan-STARRS images in the r filter, use the provided script:

1. Clone the repository or download the `MAST_PS1_Download.py` script.
2. Run the following command in your terminal:

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

## Additional Information

For more details on how to use the generated HiPS server, please refer to the documentation provided by the HiPS community or the Aladin website.

If you encounter any issues, feel free to open an issue in this repository.

Happy coding!
