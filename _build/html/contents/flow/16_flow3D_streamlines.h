
<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture 6 - Groundwater flow equation &#8212; Groundwater I</title>
    
  <link rel="stylesheet" href="../../_static/css/index.73d71520a4ca3b99cfee5594769eaaae.css">

    
  <link rel="stylesheet"
    href="../../_static/vendor/fontawesome/5.13.0/css/all.min.css">
  <link rel="preload" as="font" type="font/woff2" crossorigin
    href="../../_static/vendor/fontawesome/5.13.0/webfonts/fa-solid-900.woff2">
  <link rel="preload" as="font" type="font/woff2" crossorigin
    href="../../_static/vendor/fontawesome/5.13.0/webfonts/fa-brands-400.woff2">

    
      
  <link rel="stylesheet"
    href="../../_static/vendor/open-sans_all/1.44.1/index.css">
  <link rel="stylesheet"
    href="../../_static/vendor/lato_latin-ext/1.44.1/index.css">

    
    <link rel="stylesheet" href="../../_static/sphinx-book-theme.2d2078699c18a0efb88233928e1cf6ed.css" type="text/css" />
    <link rel="stylesheet" href="../../_static/pygments.css" type="text/css" />
    <link rel="stylesheet" type="text/css" href="../../_static/togglebutton.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/copybutton.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/mystnb.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/sphinx-thebe.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/myfile.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/panels-main.c949a650a448cc0ae9fd3441c0e17fb0.css" />
    <link rel="stylesheet" type="text/css" href="../../_static/panels-variables.06eb56fa6e07937060861dad626602ad.css" />
    
  <link rel="preload" as="script" href="../../_static/js/index.3da636dd464baa7582d2.js">

    <script id="documentation_options" data-url_root="../../" src="../../_static/documentation_options.js"></script>
    <script src="../../_static/jquery.js"></script>
    <script src="../../_static/underscore.js"></script>
    <script src="../../_static/doctools.js"></script>
    <script src="../../_static/language_data.js"></script>
    <script src="../../_static/togglebutton.js"></script>
    <script src="../../_static/clipboard.min.js"></script>
    <script src="../../_static/copybutton.js"></script>
    <script src="https://unpkg.com/thebelab@0.3.3/lib/index.js"></script>
    <script >var togglebuttonSelector = '.toggle, .admonition.dropdown, .tag_hide_input div.cell_input, .tag_hide-input div.cell_input, .tag_hide_output div.cell_output, .tag_hide-output div.cell_output, .tag_hide_cell.cell, .tag_hide-cell.cell';</script>
    <script src="../../_static/sphinx-book-theme.be0a4a0c39cd630af62a2fcf693f3f06.js"></script>
    <script async="async" src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script type="text/x-mathjax-config">MathJax.Hub.Config({"tex2jax": {"inlineMath": [["\\(", "\\)"]], "displayMath": [["\\[", "\\]"]], "processRefs": false, "processEnvironments": false}})</script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js"></script>
    <script src="https://unpkg.com/@jupyter-widgets/html-manager@^0.18.0/dist/embed-amd.js"></script>
    <script async="async" src="https://unpkg.com/thebelab@latest/lib/index.js"></script>
    <script >
        const thebe_selector = ".thebe,.cell"
        const thebe_selector_input = "pre,.cell_input div.highlight"
        const thebe_selector_output = ".output,.cell_output"
    </script>
    <script async="async" src="../../_static/sphinx-thebe.js"></script>
    <link rel="index" title="Index" href="../../genindex.html" />
    <link rel="search" title="Search" href="../../search.html" />

    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="docsearch:language" content="en" />



  </head>
  <body data-spy="scroll" data-target="#bd-toc-nav" data-offset="80">
    

    <div class="container-xl">
      <div class="row">
          
<div class="col-12 col-md-3 bd-sidebar site-navigation show" id="site-navigation">
    
        <div class="navbar-brand-box">
<a class="navbar-brand text-wrap" href="../../index.html">
  
  <img src="../../_static/logo3.png" class="logo" alt="logo">
  
  
  <h1 class="site-logo" id="site-title">Groundwater I</h1>
  
</a>
</div>

<form class="bd-search d-flex align-items-center" action="../../search.html" method="get">
  <i class="icon fas fa-search"></i>
  <input type="search" class="form-control" name="q" id="search-input" placeholder="Search this book..." aria-label="Search this book..." autocomplete="off" >
</form>

<nav class="bd-links" id="bd-docs-nav" aria-label="Main navigation">
  <ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../../intro.html">
   The Interactive Groundwater-I Book
  </a>
 </li>
</ul>
<p class="caption">
 <span class="caption-text">
  Background
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../background/00_general.html">
   About this Groundwater Course and Contents
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../background/03_basic_hydrogeology.html">
   Lecture 1 - Course Introduction/Water Cycle
  </a>
 </li>
</ul>
<p class="caption">
 <span class="caption-text">
  Flow
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="lecture_02/12_subsurface_structure.html">
   Lecture 2 - Subsurface Structure
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="lecture_03/13_gw_storage.html">
   Lecture 3-  Groundwater as a reservoir
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="lecture_04/14_darcy_law_K.html">
   Lecture 4 - Darcy’s Law and Conductivity
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="lecture_05/15_het_iso.html">
   Lecture 5. Aquifer Heterogeneity and Anisotropy
  </a>
 </li>
</ul>
<p class="caption">
 <span class="caption-text">
  Tutorials
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../tutorials/tutorial_01/01_python.html">
   Tutorial 1 - Python Programming language
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../tutorials/tutorial_01/02_jupyter.html">
   Tutorial 1 - JUPYTER Notebook Interface for Python
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../tutorials/tutorial_01/02_jupyter.html#installing-python-and-jupyter-notebook-in-your-system">
   Installing Python and JUPYTER notebook in your system
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../tutorials/tutorial_02/tutorial_02.html">
   Tutorial 2
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../tutorials/tutorial_03/tutorial_03.html">
   Tutorial 3
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../tutorials/tutorial_04/tutorial_04.html">
   Tutorial 4
  </a>
 </li>
</ul>
<p class="caption">
 <span class="caption-text">
  Tools
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../tools/decay.html">
   Simulating Mass budget
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../tools/sieve_analysis.html">
   Simulating Seive Analysis
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../tools/effective_K.html">
   Simulating Effective hydraulic conductivity
  </a>
 </li>
</ul>
<p class="caption">
 <span class="caption-text">
  Question pool
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../questions/GW_exam_2019_20.html">
   Groundwater Exam Solution -  2019-2020
  </a>
 </li>
</ul>

</nav>

 <!-- To handle the deprecated key -->

<div class="navbar_extra_footer">
  Powered by <a href="https://jupyterbook.org">Jupyter Book</a>
</div>

</div>


          


          
<main class="col py-md-3 pl-md-4 bd-content overflow-auto" role="main">
    
    <div class="row topbar fixed-top container-xl">
    <div class="col-12 col-md-3 bd-topbar-whitespace site-navigation show">
    </div>
    <div class="col pl-2 topbar-main">
        
        <button id="navbar-toggler" class="navbar-toggler ml-0" type="button" data-toggle="collapse"
            data-toggle="tooltip" data-placement="bottom" data-target=".site-navigation" aria-controls="navbar-menu"
            aria-expanded="true" aria-label="Toggle navigation" aria-controls="site-navigation"
            title="Toggle navigation" data-toggle="tooltip" data-placement="left">
            <i class="fas fa-bars"></i>
            <i class="fas fa-arrow-left"></i>
            <i class="fas fa-arrow-up"></i>
        </button>
        
        <div class="dropdown-buttons-trigger">
    <button id="dropdown-buttons-trigger" class="btn btn-secondary topbarbtn" aria-label="Download this page"><i
            class="fas fa-download"></i></button>

    
    <div class="dropdown-buttons">
        <!-- ipynb file if we had a myst markdown file -->
        
        <!-- Download raw file -->
        <a class="dropdown-buttons" href="../../_sources/contents/flow/16_flow3D_streamlines.md"><button type="button"
                class="btn btn-secondary topbarbtn" title="Download source file" data-toggle="tooltip"
                data-placement="left">.md</button></a>
        <!-- Download PDF via print -->
        <button type="button" id="download-print" class="btn btn-secondary topbarbtn" title="Print to PDF"
            onClick="window.print()" data-toggle="tooltip" data-placement="left">.pdf</button>
    </div>
    
</div>
        <!-- Source interaction buttons -->

<div class="dropdown-buttons-trigger">
    <button id="dropdown-buttons-trigger" class="btn btn-secondary topbarbtn"
        aria-label="Connect with source repository"><i class="fab fa-github"></i></button>
    <div class="dropdown-buttons sourcebuttons">
        <a class="repository-button"
            href="https://github.com/prabhasyadav/iGW-I"><button type="button" class="btn btn-secondary topbarbtn"
                data-toggle="tooltip" data-placement="left" title="Source repository"><i
                    class="fab fa-github"></i>repository</button></a>
        <a class="issues-button"
            href="https://github.com/prabhasyadav/iGW-I/issues/new?title=Issue%20on%20page%20%2Fcontents/flow/16_flow3D_streamlines.html&body=Your%20issue%20content%20here."><button
                type="button" class="btn btn-secondary topbarbtn" data-toggle="tooltip" data-placement="left"
                title="Open an issue"><i class="fas fa-lightbulb"></i>open issue</button></a>
        
    </div>
</div>


        <!-- Full screen (wrap in <a> to have style consistency -->
        <a class="full-screen-button"><button type="button" class="btn btn-secondary topbarbtn" data-toggle="tooltip"
                data-placement="bottom" onclick="toggleFullScreen()" aria-label="Fullscreen mode"
                title="Fullscreen mode"><i
                    class="fas fa-expand"></i></button></a>

        <!-- Launch buttons -->

    </div>

    <!-- Table of contents -->
    <div class="d-none d-md-block col-md-2 bd-toc show">
        
        <div class="tocsection onthispage pt-5 pb-3">
            <i class="fas fa-list"></i> Contents
        </div>
        <nav id="bd-toc-nav">
            <ul class="nav section-nav flex-column">
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#prof-liedl-prof-werth-prof-chahar-prabhas-is-to-add-the-text-contents">
   Prof. Liedl/Prof. Werth/Prof. Chahar/Prabhas is to add the text contents.
  </a>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#anne-sophie-is-to-add-the-numerical-contents">
   Anne/Sophie is to add the numerical contents
  </a>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#what-do-you-need-in-this-course">
   What do you need in this course?
  </a>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#how-the-course-will-be-conducted">
   How the course will be conducted?
  </a>
 </li>
</ul>

        </nav>
        
    </div>
</div>
    <div id="main-content" class="row">
        <div class="col-12 col-md-9 pl-md-3 pr-md-0">
        
              <div>
                
  <div class="section" id="lecture-6-groundwater-flow-equation">
<h1>Lecture 6 - Groundwater flow equation<a class="headerlink" href="#lecture-6-groundwater-flow-equation" title="Permalink to this headline">¶</a></h1>
<div class="section" id="prof-liedl-prof-werth-prof-chahar-prabhas-is-to-add-the-text-contents">
<h2>Prof. Liedl/Prof. Werth/Prof. Chahar/Prabhas is to add the text contents.<a class="headerlink" href="#prof-liedl-prof-werth-prof-chahar-prabhas-is-to-add-the-text-contents" title="Permalink to this headline">¶</a></h2>
</div>
<div class="section" id="anne-sophie-is-to-add-the-numerical-contents">
<h2>Anne/Sophie is to add the numerical contents<a class="headerlink" href="#anne-sophie-is-to-add-the-numerical-contents" title="Permalink to this headline">¶</a></h2>
<p>IPYNB code for</p>
<ol class="simple">
<li><p>isochrones and protection zones  Excel sheet</p></li>
<li><p>Excel sheet “anisotropic_aquifer_2D”</p></li>
</ol>
</div>
<div class="section" id="what-do-you-need-in-this-course">
<h2>What do you need in this course?<a class="headerlink" href="#what-do-you-need-in-this-course" title="Permalink to this headline">¶</a></h2>
<p>You will need the following:</p>
<ol class="simple">
<li><p>Laptop/Smartphone with internet connected</p></li>
<li><p>Recommended is installed JUPYTER interface.</p></li>
<li><p>Calculator</p></li>
<li><p>Presence of your mind.</p></li>
</ol>
<div class="highlight-bash notranslate"><div class="highlight"><pre><span></span>pip install jupyter-book
</pre></div>
</div>
</div>
<div class="section" id="how-the-course-will-be-conducted">
<h2>How the course will be conducted?<a class="headerlink" href="#how-the-course-will-be-conducted" title="Permalink to this headline">¶</a></h2>
<p>The course will be conducted in the following manner:</p>
<ol class="simple">
<li><p>Lectures will be presented as a combination of presentation and interactive visuals.</p></li>
<li><p>Tutorials will entirely be based on interactive excercises and visualization</p></li>
<li><p>This is how you set-up internal navigation <span class="xref myst">anatomy of a Jupyter Book</span> section covers the</p></li>
</ol>
</div>
</div>

    <script type="text/x-thebe-config">
    {
        requestKernel: true,
        binderOptions: {
            repo: "prabhasyadav/iGW-I",
            ref: "main",
        },
        codeMirrorConfig: {
            theme: "abcdef",
            mode: "python"
        },
        kernelOptions: {
            kernelName: "python3",
            path: "./contents/flow"
        },
        predefinedOutput: true
    }
    </script>
    <script>kernelName = 'python3'</script>

              </div>
              
        </div>
    </div>
    
    
    <div class='prev-next-bottom'>
        

    </div>
    <footer class="footer mt-5 mt-md-0">
    <div class="container">
      <p>
        
          By P. K. Yadav, T. Reimann and several others<br/>
        
      </p>
    </div>
  </footer>
</main>


      </div>
    </div>

    
  <script src="../../_static/js/index.3da636dd464baa7582d2.js"></script>


    
  </body>
</html>