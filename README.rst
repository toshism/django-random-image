Django Random Image
=================

Django Random Image is a simple app to load a random image from a specified directory.

It's trivially simple but I've needed it a few times so I thought maybe others have too.

Installation
************

Add 'random_image' to INSTALLED_APPS.

Settings
************

All settings are optional

**RANDOM_IMAGE_DIR**

Default: Not defined

A path to the directory from which to load the random images. Relative to MEDIA_ROOT.

Note: Passing a path to the template tag will always override the RANDOM_IMAGE_DIR setting.

**RANDOM_IMAGE_EXTENSIONS**

Default: ['.jpg','.jpeg','.png','.gif']

A list containing extensions to be considered when choosing a random image.


Usage
************

Pass in a path to the image directory::

    {% load random_image %}
    <img src="{{ MEDIA_URL}}{% random_image "path/to/image/dir" %}">

The path to the image directory should be relative to MEDIA_ROOT.

or if you have added RANDOM_IMAGE_DIR to your settings file::

   {% load random_image  %}
   <img src="{{ MEDIA_URL }}{% random_image %}">


That's it! Simple as it gets.
