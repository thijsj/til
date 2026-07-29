# Create a smaller PDF

If your PDF file is too large due to high-resolution images or other content, you can reduce its size using the following method:

`convert -density 120 -quality 95 -compress jpeg input.pdf output.pdf`
