# picture-frame-photo-booth

This is a project that I've seen a hundred times, but I've never really managed to pull off myself. I took an old monitor from recycling, pulled off the frame, and turned it into a shadow-box photo frame.

Behind it, I'll be putting a Raspberry Pi, camera, switch, and a spiral pushbutton. The idea is to have a photobooth hanging on my 9-year-old's wall, with a capability to take and display animated GIFs.

The flow is something like the following:

- Two 'modes' set with a hardware switch. Mode 1 is 'take a picture'. Mode 2 is 'show a slideshow'. 

For Mode 1, the Pi would start with a full-screen image with instructions ('push the button, make a picture!'). Pressing the button would: a) show a preview from the camera; b) take a picture with a sound, repeat for 5 pictures; c) stich the pictures together with graphicsmagick or similar; d) display the animated GIF a few times; return to instruction screen.

A little more detail. The picture itself is, I imagine, a stitch of the camera image + a white matte-looking 'frame', so the whole thing looks a bit more museum photograph-like. I'd like to be saving the entire archive of animated pictures, which I can then pick up, via the app Hazel, to the Mac Mini on my network.

For Mode 2, the Pi would run a light-weight image display (chromium browser in kiosk mode, for example), with animated GIF images randomly rotated from a local file.
