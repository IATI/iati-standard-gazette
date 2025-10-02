==========================================================
iati-docs-base: Template repo for IATI documentation sites
==========================================================

Includes:

* IATI documentation Sphinx theme
* Scaffolding for translation
* Instructions on how to create a new IATI documentation site
* The "kitchen sink" comprehensive demonstration of Sphinx features rendered using the theme

For more information on using the `IATI documentation site Sphinx theme <https://github.com/IATI/sphinx-theme>`_ , see `the theme documentation <https://iati-sphinx-theme.readthedocs-hosted.com/en/latest/>`_

Creating a new IATI Documentation website
=========================================

Create the repo
---------------

In order to create a new repo using this as a template, you need permission to create new repos in the IATI GitHub organisation. If you don't have this, talk to `an organisation owner <https://github.com/orgs/IATI/people>`_.

If you have this permission, then click the "Use this template" button on the repo to create a new repo, using this as a template. 

Configure the docs site
-----------------------

Go through docs/conf.py and replace all references to "IATI Validator" with the name of whatever you're documenting. 

Set up ReadTheDocs
------------------

Then, set up the repo on ReadTheDocs by `logging in to app.readthedocs.com <https://app.readthedocs.com/dashboard/>`_ using GitHub. Permissions on ReadTheDocs are set via GitHub so you have to log in using GitHub, otherwise you won't be able to access anything.

Once logged in, click Add Project and follow through the flow to add the project. If you get a banner saying "Failed to add deploy key to project Failed to add deploy key to GitHub project, ensure you have the correct permissions and try importing again.", you can ignore it(!) 

Repeat the Add Project flow again for each language that you're adding translations for, using the same repo and following the convention of appending -fr/-es etc at the end of each project name, and setting the Language of the project to the appropriate value. 

Then, go to the Settings of the English version of the docs, click "translations" in the menu, and add the extra projects you just created as Translations of the first. 

Finally, go through each of the projects that you've just created, go to their Settings, and ensure that the Privacy Level is set to Public and that the "Build pull requests for this project" box is checked. 

Write your content
------------------

You're now ready to write your content - see other documentation sites for examples of layouts and structure, and look at the "kitchen sink" for examples of Sphinx features. All content must be written in `ReStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ .

See the "Contributing" section, below, for best practices on how to work on your content.

Don't forget to remove the Kitchen Sink and these setup instructions before starting work on your own documentation. The content in the other sections below can stay as it's relevant to anyone wanting to work on the documentation in the future. 

Building the Documentation
==========================

"Building" is the process of running a piece of software to turn the text files into a website, and making them available as a navigable website. 

There are three ways to build the documentation:

* Build it locally
* Using ReadTheDocs
* If you use VS Code, using the included compile script

Using ReadTheDocs
-----------------

ReadTheDocs will automatically build when a new Pull Request is opened on GitHub, whenever a new commit is pushed to an open Pull Request, or when a Pull Request is merged.

View the docs locally with live preview
---------------------------------------
  
Assuming a unix based system:

.. code-block:: bash

  # Make sure you have python3 venv, e.g. for Ubuntu
  # If you're not sure, try creating a venv, and see if it errors
  sudo apt-get install python3-venv
  
  # Create a venv
  python3 -m venv .ve    
  
  # Enter the venv, needs to be run for every new shell
  source .ve/bin/activate
  
  # Install requirements
  pip install -r requirements_dev.txt
  
  # Run sphinx-autobuild
  sphinx-autobuild docs docs/_build/html

Then go to http://localhost:8000/ in a browser.
When you save changes to a file, it should update in the browser automatically.
To change the language, edit the `language` variable in `docs/conf.py`.

Using VS Code
-------------

A devcontainer.json and launch.json are supplied which add sphinx-autobuild as a Run option

Contributing
============

In order to contribute to this documentation, create a new branch and make your suggested changes. Then, open a Pull Request; this will build a preview of your changes and let you see what the complete site will look like. 

Formatting
----------

The Python code in this repository uses the python [black](https://github.com/psf/black) formatter.
If editing in VSCode, the project is set up to format automatically on save.
To format manually, run `black .`:

Translations
============

The process for getting documentation translated is:

* Extract English strings into a .pot file
* Send the .pot file for translation
* Recieve .po files from the translation process
* Check the .po files into the repo
* Re-run the build process with the translations

Extract Strings
---------------

.. code-block:: bash

  cd docs
  make gettext
  # .pot files are in _build/locale

Send for translation & Receive translations
-------------------------------------------

Nothing automated here, sorry. Ask @robredpath for details. 

Check the files into the repo
-----------------------------

Place the files into `docs/locale/fr/LC_MESSAGES/` (replacing fr with the appropriate langauge code as required)

Re-run the build
----------------

On ReadTheDocs, projects that are translations don't auto-build on Pull Request. If you want to preview the documentation in another language, you can create a Version via the RTD interface and set it up to build the branch that you're working on. Translated versions will automatically rebuild when the Pull Request is merged, however. 

If building locally: 

.. code-block:: bash

  cd docs
  make -e SPHINXOPTS="-D language='fr'" dirhtml

Built docs are in `docs/_build/dirhtml`.
