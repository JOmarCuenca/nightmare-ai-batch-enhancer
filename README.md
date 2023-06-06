# Nightmare AI image enhancer batch uploader wrapper

Simple CLI utility to batch upload images to the nightmare AI API.

# How to use

## Installation

I recommend creating a dedicated environment for this application.

### Environment

```bash
python3 -m venv env
source env/bin/activate
```

### Required libraries

A `requirements.txt` file provides all the required libraries in order to work properly.

```bash
pip install -r requirements.txt
```

Also very important is that the API needs an API key provided in a `.key` file. by default the main code looks for `api.key` file. but the `.key` file can be provided in the params manually.

## Usage

The CLI utility needs some parameter in order to work properly,

```bash
python3 main.py <IMG DIR - IMG FILE>
```

## Params

- `-v` : Verbose
- `--scale` : The amount of scale to enhance the image **Default 4**
- `--api-path` : The path of the API key file, **Default api.key**
- `--output` : Directory or name to use output the resulting file.
- `--face-enhance` : Enables the Nigthmare AI **face enhance** feature, **Default disabled**

# Links

[Nightmare AI](https://replicate.com/nightmareai/real-esrgan)

# Disclaimer

This is only a wrapper, as the API as of June 5, 2023, only uploads the image, and returns a weblink on where to download the image, and only accepts 1 image at a time.

So this wrapper is meant to be used if you mean to upload like an entire dir full of images and download them at the same time.

This repo is still under development.