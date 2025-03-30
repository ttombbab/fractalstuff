# fractalstuff
# Fractal Compression and Multi-Julia Set Inspired Image Reconstruction

This project explores a novel approach to image representation and potential compression inspired by the mathematical properties of multi-Julia sets.

## Background

While working on fractal compression techniques, I stumbled upon an interesting mathematical space. This space utilizes a custom number type consisting of three components: (real, imaginary, imaginary). The implementation of this number type can be found in the `newnum.py` file.

I experimented with applying an iterative formula similar to the one used for generating Multibrot sets: `$Z \leftarrow z^5 + C$ , Typically, this formula uses complex numbers raised to the power of 2 or other integers. In this project, the formula is adapted to the custom (real, $Z \leftarrow z^5 + C$imaginary, imaginary) number type and raised to the fifth power.

## Observations

When the results of these calculations are projected onto a two-dimensional plane, the resulting patterns bear a striking resemblance to real-world images, such as the intricate structure of a pomegranate seed.

## The Challenge

Initially, I faced a roadblock in determining how to map a real-world image to a corresponding fractal space. This challenge led me to put this line of research on the back burner.

## Inspiration from Neural Networks

Recently, I was listening to a video discussing the reconstruction of datasets from neural network weights. This sparked a new idea:

What if the attractors of multi-Julia sets could be treated as the "weights" in a neural network? Could we then reconstruct data (potentially images) from these fractal attractors?

## Next Steps (Current Thinking)

This project represents an initial exploration of this concept. The current focus is on:

* Further understanding the properties of the custom (real, imaginary, imaginary) number space.
* Investigating the relationship between the parameters of the multi-Julia set (specifically with the power of 5 and the 'c' value) and the resulting patterns.
* Exploring the feasibility of using multi-Julia set attractors as a basis for image reconstruction, potentially drawing inspiration from techniques used in neural network weight analysis.

## Code

The core implementation of the custom number type is in `newnum.py`
example images.

## Contributing
Here's the video link; https://youtu.be/JAzTr5hIVpI?si=VhSKH8g1nCbrmT1x
