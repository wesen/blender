*****************************
Blender Institute Render Farm
*****************************

This renderfarm has been used for the short film Sintel and currently used for
the Mango Open Movie.

It is in-house software that has never been used outside the blender institute
yet, but could be with minor changes as long as the setup is quite similar to
our own.


Requirements
============

* Linux (debian / ubuntu used here)

* SSH over and LAN to issue commands to nodes (won't run over the internet).

* Subversion (to manage assets).

* Blender (for rendering).

* Exr Tools (exrheader to extract info from final frames).

* Python3.2 (which the render-farm is written in).


Running The Farm
================


Master
------

This is main script that runs the farm. nodes are checked and assigned jobs,
the script manages updating svn on the nodes, running jobs, killing jobs and
showing the web site.

Run with:

.. code-block:: bash

	./new_master.py



Slide Show (Generating)
-----------------------

This isn't essential but is nice to have images from the farm show up in the
web interface.

Run with:

.. code-block:: bash

	./slideshow/preview_images_update.py


Slide Show (Viewing)
--------------------

This sill show up in the web front-end interface but you may want to run
full screen. There are 2 options.


Display ./slideshow/lastframe.html in a full screen in a browser.


Run MPlayer in a loop with:

.. code-block:: bash

	./slideshow/slideshow.sh


AVI Generation
--------------

Once you get the EXR frames back from the farm its convenient to be able to
play them back in an AVI, for this we have a script which finds finished
jobs and renders out half resolution AVI-JPEG's.


.. code-block:: bash

	./master_avi_gen__loop.sh


This script simply calls ./master_avi_gen.py in a loop.


TODO - explain master_ui.c
TODO - explain new_blender_setup.py a bit?

