# HiPS Server Installation

This repository provides the necessary tools and instructions to set up a basic HiPS (Hierarchical Progressive Survey) server using Pan-STARRS images.

## Contents

1. [Prerequisites](#prerequisites)
2. [Download Pan-STARRS Images](#download-pan-starrs-images)
3. [Generate HiPS Server](#generate-hips-server)
4. [HiPS Update](#hips-update)
5. [Additional Information](#additional-information)

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- **Java**: Ensure you have Java installed. You can download it from [here](https://www.java.com/en/download/).

## Download Pan-STARRS Images

To download Pan-STARRS images, you can use the script `MAST_PS1_Download.py`. The script have two important functions:

- **get_observations(collection="PS1", filters_list=["r"], ra_range=[30, 35],dec_range=[10, 15])**:

  This function filter the observations according to the `collection`, `filter`, `ra_range`, and `dec_range` parameters.
  - `collection=PS1`: Name of the mission or collection. Default value **"PS1"**.
  - `filters_list=["r"]`: List of filters to use for the search. Defalut value **["r"]**.
  - `ra_range=[0, 360]`: Right ascension range [min, max]. Default value **[0, 360]**.
  - `dec_range=[10, 15]`: Declination range [min, max]. Default value **[0, 90]**.

- **download_products_in_batches(products, batch_size=200)**:

  This function downloads the products in smaller batches to avoid exceeding download limits.
  - `products`: List of filtered observations products.
  - `batch_size`: The batch size to download the products in.

  

For example, to download the Pan-STARRS images with default parameters (northern hemisphere observations), run the following command in your terminal:

```bash
python MAST_PS1_Download.py
```

The main function sequentially downloads all images of the northern hemisphere and store them in a folder named `mastDownload`.

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

## HiPS Update

Updating a HiPS is usually done to add new images without having to completely restart the calculation. Usually you no longer have the original images and you just want to add new ones. The safest method is to create a new HiPS with the new images, and then concatenate it to the original HiPS.

### Concatenation of 2 HiPS

Hipsgen allows to concatenate 2 HiPS thanks to the "CONCAT" action. These 2 HiPS must necessarily have the same HiPS order. First, another HiPS server must be generated using the instructions in section 3. Suppose this second HiPS server is generated with the name "HiPS2", and suppose the first generated HiPS server has the name "HiPS". The concatenation is done by integrating the first HiPS into the second. 

To concatenate the "HiPS" server into the "HiPS2" server, open your terminal and navigate to the directory containing the `AladinBeta.jar` file and the `mastDownload2` folder (Assuming this folder contains the new images). Run the following command:

```bash
java -Xmx16g -jar AladinBeta.jar -hipsgen maxThread=20 in=HiPS out=HiPS2 id=HiPS_C CONCAT CHECKCODE DETAILS
```

- **Parameters**:
  - `in=HiPS`: Path name of the first HiPS server generated. This server will be integrated into the second one.
  - `out=HiPS2`: Path name of the second HiPS server generated. This server will receive the integration of the first one
  - `id=HiPS_C`: This provides an identification ID for the resulting HiPS server.

- **Flags**:
  - **CONCAT**: Action that allows the concatenation of the server indicated in the "in" parameter, together with the server indicated in the "out" parameter. The HiPS server indicated in "in" is integrated within the HiPS server indicated in "out".
  - **CHECKCODE**: Performs a consistency check on the generated HiPS data to ensure files meet specifications and are error-free.
  - **DETAILS**: Provides detailed logging during the generation process, useful for debugging.


## Additional Information

For more details on how to use the generated HiPS server, please refer to the [official user manual](https://aladin.cds.unistra.fr/hips/HipsgenManual.pdf) provided by the Aladin website.



