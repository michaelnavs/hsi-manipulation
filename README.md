<!-- PROJECT LOGO -->
<br />
<p align="center">
  <img src="./logo.png" alt="Logo" width="80">

  <h3 align="center">HSI Manipulation</h3>

  <p align="center">
      Learning to read and load HSI dataset
  </p>
</p>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- Add demo here!! -->

Part of my NSF Research work, I was tasked with creating a script to read and
load HSI dataset. From there, my research advisor wanted me show the spectral
signature plot of a random pixel on the image. Once I was able to plot the
spectral signature of a random pixel, I was told to only plot the spectral signature
between wavelengths of 460-530. After that, I calculated the slope and plotted
the line of best fit for the data.

### Built With

- [Spectral](http://www.spectralpython.net/)

<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

- python3.8

  ```sh
  sudo apt update
  sudo apt install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt install python3.8
  ```

- pip3
  ```sh
  sudo apt install python3-pip
  ```

### Installation

2. Clone the repo
   ```sh
   git clone https://github.com/michaelnavs/analyzing-hsi.git
   ```
3. Create virtual environment
   ```sh
   python3 -m venv venv
   ```
4. Activate virtual environmnt
   ```sh
   source venv/bin/activate
   ```
5. Install required packages
   ```sh
   pip install -r requirements.txt
   ```
6. Run main script with desired pixel row and column value respectively
   ```
   python main.py 1 2
   ```
