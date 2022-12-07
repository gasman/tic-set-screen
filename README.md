# tic-set-screen

A command line tool for replacing the cover image of a TIC-80 .tic cartridge file

## About

As of TIC-80 version 0.90, the cover image for a cartridge is saved as a dump of the screen data. This is displayed using the cartridge's built-in palette, which will be the default Sweetie16 (or DB16) palette if a custom palette has not been explicitly set up through the TIC-80 sprite editor. Notably, poking the palette memory from a running program does _not_ write those palette changes back to the cartridge file.

[This is problematic for many size-coded / byte battle / byte jam releases](https://github.com/nesbox/TIC-80/issues/1552), as they consist only of code and no supporting data - a program that sets a custom palette will end up with a cover image displayed in false colours. Additionally, there's no way to capture scanline-level palette changes performed with SCN or OVR.

In the absence of a "proper" fix, `tic-set-screen` allows you to supply an arbitrary 16-colour image, and generates a new .tic cartridge file with the screen and palette chunks modified to use that as the cover image.

(Note that, since the cartridge's built-in palette is changed, a program that only pokes some of the palette memory and relies on default values for the rest could end up looking different. If this is a problem, you can still use `tic-set-screen` to prepare a metadata cart for uploading to tic80.com.)

## Installation

With Python 3.7 or above installed, run:

```sh
pip install tic-set-screen
```

(Depending on your Python setup, the command may be `pip3` rather than `pip`. You can also install it into a Python virtual environment, if that's your jam.)

## Usage

```sh
tic-set-screen input_cart.tic cover_image.png output_cart.tic
```

The cover image must be 240x136 and use a maximum of 16 colours. It can be PNG, GIF, or [any other format recognised by Pillow](https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html).
