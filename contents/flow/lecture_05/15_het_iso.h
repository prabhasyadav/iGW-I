
<!DOCTYPE html>

<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lecture 5. Aquifer Heterogeneity and Anisotropy &#8212; Groundwater I</title>
    
  <link rel="stylesheet" href="../../../_static/css/index.73d71520a4ca3b99cfee5594769eaaae.css">

    
  <link rel="stylesheet"
    href="../../../_static/vendor/fontawesome/5.13.0/css/all.min.css">
  <link rel="preload" as="font" type="font/woff2" crossorigin
    href="../../../_static/vendor/fontawesome/5.13.0/webfonts/fa-solid-900.woff2">
  <link rel="preload" as="font" type="font/woff2" crossorigin
    href="../../../_static/vendor/fontawesome/5.13.0/webfonts/fa-brands-400.woff2">

    
      
  <link rel="stylesheet"
    href="../../../_static/vendor/open-sans_all/1.44.1/index.css">
  <link rel="stylesheet"
    href="../../../_static/vendor/lato_latin-ext/1.44.1/index.css">

    
    <link rel="stylesheet" href="../../../_static/sphinx-book-theme.2d2078699c18a0efb88233928e1cf6ed.css" type="text/css" />
    <link rel="stylesheet" href="../../../_static/pygments.css" type="text/css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/togglebutton.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/copybutton.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/mystnb.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/sphinx-thebe.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/myfile.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/panels-main.c949a650a448cc0ae9fd3441c0e17fb0.css" />
    <link rel="stylesheet" type="text/css" href="../../../_static/panels-variables.06eb56fa6e07937060861dad626602ad.css" />
    
  <link rel="preload" as="script" href="../../../_static/js/index.3da636dd464baa7582d2.js">

    <script id="documentation_options" data-url_root="../../../" src="../../../_static/documentation_options.js"></script>
    <script src="../../../_static/jquery.js"></script>
    <script src="../../../_static/underscore.js"></script>
    <script src="../../../_static/doctools.js"></script>
    <script src="../../../_static/language_data.js"></script>
    <script src="../../../_static/togglebutton.js"></script>
    <script src="../../../_static/clipboard.min.js"></script>
    <script src="../../../_static/copybutton.js"></script>
    <script src="../../../_static/custom.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/"></script>
    <script >var togglebuttonSelector = '.toggle, .admonition.dropdown, .tag_hide_input div.cell_input, .tag_hide-input div.cell_input, .tag_hide_output div.cell_output, .tag_hide-output div.cell_output, .tag_hide_cell.cell, .tag_hide-cell.cell';</script>
    <script src="../../../_static/sphinx-book-theme.be0a4a0c39cd630af62a2fcf693f3f06.js"></script>
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
    <script async="async" src="../../../_static/sphinx-thebe.js"></script>
    <link rel="index" title="Index" href="../../../genindex.html" />
    <link rel="search" title="Search" href="../../../search.html" />
    <link rel="next" title="Lecture 6: Steady-State Groundwater flow in 3D" href="../lecture_06/16_darcy_law_3D.html" />
    <link rel="prev" title="Lecture 4 - Darcy’s Law and Conductivity" href="../lecture_04/14_darcy_law_K.html" />

    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="docsearch:language" content="en" />



  </head>
  <body data-spy="scroll" data-target="#bd-toc-nav" data-offset="80">
    

    <div class="container-xl">
      <div class="row">
          
<div class="col-12 col-md-3 bd-sidebar site-navigation show" id="site-navigation">
    
        <div class="navbar-brand-box">
<a class="navbar-brand text-wrap" href="../../../index.html">
  
  <img src="../../../_static/logo3.png" class="logo" alt="logo">
  
  
  <h1 class="site-logo" id="site-title">Groundwater I</h1>
  
</a>
</div>

<form class="bd-search d-flex align-items-center" action="../../../search.html" method="get">
  <i class="icon fas fa-search"></i>
  <input type="search" class="form-control" name="q" id="search-input" placeholder="Search this book..." aria-label="Search this book..." autocomplete="off" >
</form>

<nav class="bd-links" id="bd-docs-nav" aria-label="Main navigation">
  <ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../../../intro.html">
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
  <a class="reference internal" href="../../background/00_general.html">
   About this Groundwater Course and Contents
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../background/03_basic_hydrogeology.html">
   Lecture 1 - Course Introduction/Water Cycle
  </a>
 </li>
</ul>
<p class="caption">
 <span class="caption-text">
  Flow
 </span>
</p>
<ul class="current nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../lecture_02/12_subsurface_structure.html">
   Lecture 2 - Subsurface Structure
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../lecture_03/13_gw_storage.html">
   Lecture 3-  Groundwater as a reservoir
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../lecture_04/14_darcy_law_K.html">
   Lecture 4 - Darcy’s Law and Conductivity
  </a>
 </li>
 <li class="toctree-l1 current active">
  <a class="current reference internal" href="#">
   Lecture 5. Aquifer Heterogeneity and Anisotropy
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../lecture_06/16_darcy_law_3D.html">
   Lecture 6: Steady-State Groundwater flow in 3D
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../lecture_07/17_quantify_flow.html">
   Lecture 07 - Quantifying 3D Groundwater Flow
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../lecture_08/18_wells.html">
   Lecture 08 - Wells*
  </a>
 </li>
</ul>
<p class="caption">
 <span class="caption-text">
  Transport
 </span>
</p>
<ul class="nav sidenav_l1">
 <li class="toctree-l1">
  <a class="reference internal" href="../../transport/lecture_09/21_conservative_transport.html">
   Lecture 9-  Conservative Transport
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../transport/lecture_10/22_reactive_transport.html">
   Lecture 10:  Reactive Mass Transport
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
  <a class="reference internal" href="../../tutorials/tutorial_01/01_python.html">
   Tutorial 1 - Python Programming language
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_01/02_jupyter.html">
   Tutorial 1 - JUPYTER Notebook Interface for Python
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_01/02_jupyter.html#installing-python-and-jupyter-notebook-in-your-system">
   Installing Python and JUPYTER notebook in your system
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_02/tutorial_02.html">
   Tutorial 2 - Aquifer and Storage Properties
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_03/tutorial_03.html">
   Tutorial 3 - Darcy Law and Conductivity
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_04/tutorial_04.html">
   Tutorial 4 - Effective K &amp; Recitation
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_05/tutorial_05.html">
   Tutorial 5 - Tutorial problems aquifer heterogeneity/anisotropy
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_06/tutorial_06.html">
   Tutorial 6 - Tutorial Problems on Flow in Confined/Unconfined Aquifer
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_07/tutorial_07.html">
   Tutorial 7 - Wells
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_08/tutorial_08.html">
   Tutorial 8 - Conservative transport
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tutorials/tutorial_09/tutorial_09.html">
   Tutorial 9 - Reactive transport
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
  <a class="reference internal" href="../../tools/decay.html">
   Simulating Mass Budget
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tools/sieve_analysis.html">
   Simulating Seive Analysis
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tools/effective_K.html">
   Simulating Effective hydraulic conductivity
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tools/uniform_flow_and_well.html">
   Uniform Flow and Well*
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tools/aniso2D.html">
   Simulating the Anisotropy and flow direction
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tools/type_curve_fit.html">
   Type curve and fitting pumping data tool
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tools/1D_advection_dispersion.html">
   Tool for simulating 1D Conservative Transport (Laboratory Column)
  </a>
 </li>
 <li class="toctree-l1">
  <a class="reference internal" href="../../tools/Kinetics_degradation.html">
   Simulating Kinetics and Degradation
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
  <a class="reference internal" href="../../questions/GW_exam_2019_20.html">
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
        <a class="dropdown-buttons" href="../../../_sources/contents/flow/lecture_05/15_het_iso.ipynb"><button type="button"
                class="btn btn-secondary topbarbtn" title="Download source file" data-toggle="tooltip"
                data-placement="left">.ipynb</button></a>
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
            href="https://github.com/prabhasyadav/iGW-I/issues/new?title=Issue%20on%20page%20%2Fcontents/flow/lecture_05/15_het_iso.html&body=Your%20issue%20content%20here."><button
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

<div class="dropdown-buttons-trigger">
    <button id="dropdown-buttons-trigger" class="btn btn-secondary topbarbtn"
        aria-label="Launch interactive content"><i class="fas fa-rocket"></i></button>
    <div class="dropdown-buttons">
        
        <a class="binder-button" href="https://mybinder.org/v2/gh/prabhasyadav/iGW-I/main?urlpath=tree/contents/flow/lecture_05/15_het_iso.ipynb"><button type="button"
                class="btn btn-secondary topbarbtn" title="Launch Binder" data-toggle="tooltip"
                data-placement="left"><img class="binder-button-logo"
                    src="../../../_static/images/logo_binder.svg"
                    alt="Interact on binder">Binder</button></a>
        
        
        
        <button type="button" class="btn btn-secondary topbarbtn"
            onclick="initThebeSBT()" title="Launch Thebe" data-toggle="tooltip" data-placement="left"><i
                class="fas fa-play"></i><span style="margin-left: .4em;">Live Code</span></button>
        
    </div>
</div>

    </div>

    <!-- Table of contents -->
    <div class="d-none d-md-block col-md-2 bd-toc show">
        
        <div class="tocsection onthispage pt-5 pb-3">
            <i class="fas fa-list"></i> Contents
        </div>
        <nav id="bd-toc-nav">
            <ul class="nav section-nav flex-column">
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#motivation">
   Motivation
  </a>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#heterogeneity">
   Heterogeneity
  </a>
  <ul class="nav section-nav flex-column">
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#effective-hydraulic-conductivity">
     Effective Hydraulic Conductivity
    </a>
   </li>
  </ul>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#layered-systems">
   Layered Systems
  </a>
  <ul class="nav section-nav flex-column">
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#case-i-flow-parallel-to-layering">
     Case I - Flow Parallel to Layering
    </a>
   </li>
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#example-problem">
     Example problem
    </a>
   </li>
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#case-2-flow-perpendicular-to-layering">
     Case 2 - Flow Perpendicular to Layering
    </a>
   </li>
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#id1">
     Example problem
    </a>
   </li>
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#summary-effective-conductivity-of-layered-aquifers">
     Summary: Effective Conductivity of Layered Aquifers
    </a>
   </li>
  </ul>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#hydraulic-resistance">
   Hydraulic Resistance
  </a>
  <ul class="nav section-nav flex-column">
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#id2">
     Example problem
    </a>
   </li>
  </ul>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#aquifer-anisotropy">
   Aquifer Anisotropy
  </a>
  <ul class="nav section-nav flex-column">
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#anisotropy-and-scale-effects">
     Anisotropy and scale effects
    </a>
   </li>
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#indices-and-functional-arguments-to-describe-anisotropy">
     Indices and functional arguments to describe anisotropy
    </a>
   </li>
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#concept-of-the-hydraulic-conductivity-ellipse">
     Concept of the hydraulic conductivity ellipse
    </a>
   </li>
   <li class="toc-h3 nav-item toc-entry">
    <a class="reference internal nav-link" href="#id3">
     Example problem
    </a>
   </li>
  </ul>
 </li>
 <li class="toc-h2 nav-item toc-entry">
  <a class="reference internal nav-link" href="#combining-heterogeneity-and-anisotropy">
   Combining Heterogeneity and Anisotropy
  </a>
 </li>
</ul>

        </nav>
        
    </div>
</div>
    <div id="main-content" class="row">
        <div class="col-12 col-md-9 pl-md-3 pr-md-0">
        
              <div>
                
  <div class="section" id="lecture-5-aquifer-heterogeneity-and-anisotropy">
<h1>Lecture 5. Aquifer Heterogeneity and Anisotropy<a class="headerlink" href="#lecture-5-aquifer-heterogeneity-and-anisotropy" title="Permalink to this headline">¶</a></h1>
<p><em>(The contents presented in this section were re-developed principally by <a class="reference external" href="http://web.iitd.ac.in/~chahar/">Prof. B. R. Chahar</a> and Dr. P. K. Yadav. The original contents are from Prof. Rudolf Liedl)</em></p>
<hr class="docutils" />
<div class="section" id="motivation">
<h2>Motivation<a class="headerlink" href="#motivation" title="Permalink to this headline">¶</a></h2>
<p>The last lecture introduces aquifer properties such hydraulic conductivity, storativity, porosity. The key assumption in that lecture was that the aquifer is an 1D unit, e.g., the Darcy column, and that its properties do not vary in space. In contrast to these, an aquifer is more accurately represented by a 3D system and its properties vary both in space and directions. In fact variations of hydraulic conductivity (<span class="math notranslate nohighlight">\(K\)</span>), a most critical aquifer quantity, are dominant in most cases. Variations of <span class="math notranslate nohighlight">\(K\)</span> can be observed at very small spatial scales and directions. Thus, aquifer properties that depends on <span class="math notranslate nohighlight">\(K\)</span> also varies. Consequently, aquifer properties such as <span class="math notranslate nohighlight">\(K\)</span> takes a tensor form- a quantity whose magnitude is space and direction dependent.</p>
<p>In the picture below (<a class="reference internal" href="#aquifer-het"><span class="std std-numref">Fig. 1</span></a>) the 3-D spatial variability of aquifer properties is illustrated by a 2-D vertical cross-section. The picture of the outcrop show some form of a layered system, with each layer likely possessing individual subsurface properties.</p>
<div class="figure align-center" id="aquifer-het">
<a class="reference internal image-reference" href="../../../_images/L5_f1.png"><img alt="../../../_images/L5_f1.png" src="../../../_images/L5_f1.png" style="width: 615.3px; height: 209.29999999999998px;" /></a>
<p class="caption"><span class="caption-number">Fig. 1 </span><span class="caption-text">Aquifer Heterogeneity</span><a class="headerlink" href="#aquifer-het" title="Permalink to this image">¶</a></p>
</div>
</div>
<div class="section" id="heterogeneity">
<h2>Heterogeneity<a class="headerlink" href="#heterogeneity" title="Permalink to this headline">¶</a></h2>
<p>A solid or a porous medium is <strong>homogeneous</strong> if its property do not vary in space. In contrast, the porous medium is <strong>heterogeneous</strong>, or also sometime termed inhomogeneous, if at least one of its properties varies in space. In groundwater studies, heterogeneity or homogeneity is generally associated with hydraulic conductivity <span class="math notranslate nohighlight">\((K)\)</span> of the aquifer. In many practical applications, properties such as strativity and porosity are treated as spatially constant or homogeneous. This is usually done for two reasons:</p>
<ul class="simple">
<li><p>the spatial variability of hydraulic conductivity is much more pronounced than that of storativity and porosity, and</p></li>
<li><p>very limited data are available of the spatial variability of storativity and porosity.</p></li>
</ul>
<p>Thus, an aquifer is:</p>
<blockquote>
<div><p>homogeneous if <span class="math notranslate nohighlight">\(K (x, y, z) = K\)</span>, and</p>
</div></blockquote>
<blockquote>
<div><p>heterogeneous if <span class="math notranslate nohighlight">\(K (x, y, z) \neq K\)</span></p>
</div></blockquote>
<p>For heterogeneous aquifer it is not required that <span class="math notranslate nohighlight">\(K\)</span> is varying in all directions, i.e., varying of <span class="math notranslate nohighlight">\(K\)</span> can be restricted to one or two spatial coordinates.</p>
<p>Heterogeneity in aquifer can exist in many configurations. But they are broadly categorized to the following three classes:</p>
<blockquote>
<div><p><strong>layered heterogeneity</strong>: common in sedimentary systems and unconsolidated deposits.</p>
</div></blockquote>
<blockquote>
<div><p><strong>discontinuous heterogeneity</strong>: due to presence of faults, e.g., at the contact between overburden-bedrock.</p>
</div></blockquote>
<blockquote>
<div><p><strong>trending heterogeneity</strong>: Common in the aquifers with active sedimentation processes</p>
</div></blockquote>
<p>Aquifer properties such as storativity and porosity are affected by heterogeneity but they are often considered spatially constant in practical applications. This is because</p>
<ul class="simple">
<li><p>The spatial variability of hydraulic conductivity is much more pronounced than any other aquifer property, and</p></li>
<li><p>Only limited spatial variability data are available for storativity or porosity.</p></li>
</ul>
<p>Heterogeneity play a significant role in controlling the flow of groundwater, but its quantification is more relevant to the transport of chemicals in groundwater.</p>
<div class="section" id="effective-hydraulic-conductivity">
<h3>Effective Hydraulic Conductivity<a class="headerlink" href="#effective-hydraulic-conductivity" title="Permalink to this headline">¶</a></h3>
<p>It is possible to represent the spatial distribution of
hydraulic conductivity in a heterogeneous aquifer by an <em>average</em>
value such that steady-state groundwater discharge remains the
same as in the heterogeneous case. Such obtained <em>average</em> <span class="math notranslate nohighlight">\(K\)</span> value is termed as <strong>effective hydraulic conductivity</strong>. In other words, it can be mentioned that the effective hydraulic conductivity characterizes a
fictitious homogeneous aquifer with the same discharge and the
same overall head difference under steady-state conditions as some
heterogeneous aquifer to be investigated.</p>
<p>The quantification of <em>effective hydraulic conductivity</em> is straight-forward for perfectly layered systems, which can be seen as an idealized representation of natural layering. In more natural systems with complex heterogeneous configurations, cumbersome mathematical derivations are required to obtain effective <span class="math notranslate nohighlight">\(K\)</span>.</p>
<p>In the next few sections, effective hydraulic conductivity for ideal layered system is derived.</p>
</div>
</div>
<div class="section" id="layered-systems">
<h2>Layered Systems<a class="headerlink" href="#layered-systems" title="Permalink to this headline">¶</a></h2>
<div class="section" id="case-i-flow-parallel-to-layering">
<h3>Case I - Flow Parallel to Layering<a class="headerlink" href="#case-i-flow-parallel-to-layering" title="Permalink to this headline">¶</a></h3>
<p>A confined aquifer consisting of <span class="math notranslate nohighlight">\(n\)</span> layers is considered. In the set-up (see <a class="reference internal" href="#flow-parallel"><span class="std std-numref">Fig. 2</span></a>), the layer boundaries are parallel to each other and groundwater flow is parallel to the layering.</p>
<div class="figure align-center" id="flow-parallel">
<a class="reference internal image-reference" href="../../../_images/L5_f2.png"><img alt="../../../_images/L5_f2.png" src="../../../_images/L5_f2.png" style="width: 233.0px; height: 370.5px;" /></a>
<p class="caption"><span class="caption-number">Fig. 2 </span><span class="caption-text">Flow parallel to layering</span><a class="headerlink" href="#flow-parallel" title="Permalink to this image">¶</a></p>
</div>
<p>The analysis is required to consider the aquifer as a <em>single entire aquifer unit</em> and a set of <em>layered aquifer unit</em>. Data of both units are to be considered.</p>
<div class="sphinx-bs container pb-4 docutils">
<div class="row docutils">
<div class="d-flex col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2 docutils">
<div class="card w-100 shadow docutils">
<div class="card-header text-center docutils">
<p class="card-text"><strong>Data for a single entire aquifer unit are:</strong></p>
</div>
<div class="card-body text-justify docutils">
<ul class="simple">
<li><p class="card-text"><span class="math notranslate nohighlight">\(W\)</span> = width (extension perpendicular to cross-section, see figure)</p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(L\)</span> = flow distance along the layer</p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(\Delta h\)</span> = total head loss corresponding to flow length</p></li>
<li><p class="card-text">Q = the total discharge.</p></li>
</ul>
</div>
</div>
</div>
<div class="d-flex col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2 docutils">
<div class="card w-100 shadow docutils">
<div class="card-header text-center docutils">
<p class="card-text"><strong>Data for set of layered aquifer unit are:</strong></p>
</div>
<div class="card-body text-justify docutils">
<ul class="simple">
<li><p class="card-text"><span class="math notranslate nohighlight">\(i\)</span> = layer numbers <span class="math notranslate nohighlight">\((i = 1,2,3 ..., n)\)</span></p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(m_i\)</span> = thickness of <span class="math notranslate nohighlight">\(i^{th}\)</span> layer</p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(K_i\)</span> = conductivity of <span class="math notranslate nohighlight">\(i^{th}\)</span> layer</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p>With these informations available, using volumetric budget and Darcy’s law the <em>effective hydraulic conductivity</em> <span class="math notranslate nohighlight">\(K\)</span> can be quantified from the following steps:</p>
<p>I. Total thickness: <span class="math notranslate nohighlight">\(m = \sum\limits_{i=1}^n m_i\)</span></p>
<p>II. Volumetric budget: <span class="math notranslate nohighlight">\(Q =  \sum\limits_{i=1}^n Q_i\)</span></p>
<p>III. Head loss in <span class="math notranslate nohighlight">\(i^{th}\)</span> layer: <span class="math notranslate nohighlight">\(\Delta h_i = \Delta h\)</span></p>
<p>IV. Darcy’s law for <span class="math notranslate nohighlight">\(i^{th}\)</span> layer: <span class="math notranslate nohighlight">\(Q_i = - wm_iK_i\frac{\Delta h}{L} \)</span></p>
<p>V. Darcy’s law for the homogeneous aquifer to replace the layered system: <span class="math notranslate nohighlight">\(Q = -wmK\frac{\Delta h}{L}\)</span></p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>As flow is parallel to the layering, the head loss in individual layer equals the total head loss (step. 3)</p>
</div>
<p>Summing the discharge in each layer (step 4) will result to the discharge of the homogeneous aquifer (step 5), i.e., we can equate step 4 and step 5 as:</p>
<div class="math notranslate nohighlight">
\[
- w \cdot m \cdot K \cdot \frac{\Delta h}{L} = \sum\limits_{i=1}^n\bigg(- w \cdot m_i \cdot K_i\cdot\frac{\Delta h}{L}\bigg)
\]</div>
<p>Constant quantities from the right-hand side can be taken out of summation and equated with the left side. This leads to:</p>
<div class="math notranslate nohighlight">
\[
{- w}\cdot m \cdot K \cdot \frac{\Delta h}{L} = {- w} \cdot \frac{\Delta h}{L} \cdot \sum\limits_{i=1}^n( m_iK_i)
\]</div>
<p>providing</p>
<div class="math notranslate nohighlight">
\[
m\cdot K = \sum\limits_{i=1}^n( m_iK_i)
\]</div>
<p>As a result, the effective hydraulic conductivity of a layered system when the flow is parallel to the layering equals</p>
<div class="math notranslate nohighlight">
\[
K = \frac{\sum\limits_{i=1}^n(m_i K_i)}{m}
\]</div>
<p>In the above equation, effective hydraulic conductivity <span class="math notranslate nohighlight">\(K\)</span> is obtained as the <em>weighted arithmetic average</em> of layer conductivities <span class="math notranslate nohighlight">\(K_i\)</span>. Weights correspond to relative thickness <span class="math notranslate nohighlight">\(m_i/m\)</span>. Thus, the <em>largest term</em> in the sum contributes most to the arithmetic average. Thus, the effective hydraulic conductivity <span class="math notranslate nohighlight">\(K\)</span> can be approximated from</p>
<div class="math notranslate nohighlight">
\[
K \approx \frac{\max (m_i\cdot K_i)}{m}
\]</div>
</div>
<div class="section" id="example-problem">
<h3>Example problem<a class="headerlink" href="#example-problem" title="Permalink to this headline">¶</a></h3>
<div class="admonition-flow-parallel-to-layering admonition">
<p class="admonition-title">Flow parallel to layering</p>
<p>Calculate the effective hydraulic conductivity of the layer system consisting of 3 layers if the flow is parallel to the stratification.</p>
</div>
<div class="cell docutils container">
<div class="cell_input docutils container">
<div class="highlight-ipython3 notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\033</span><span class="s2">[1m Provided are: </span><span class="se">\033</span><span class="s2">[0m </span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="c1">#Thickness of i-th layer [m]</span>
<span class="n">m1</span> <span class="o">=</span> <span class="mi">3</span> 
<span class="n">m2</span> <span class="o">=</span> <span class="mf">2.5</span>
<span class="n">m3</span> <span class="o">=</span> <span class="mf">1.75</span>

<span class="c1">#conductivity of i-th layer [m/s]</span>
<span class="n">K1</span> <span class="o">=</span> <span class="mf">3.5e-3</span>
<span class="n">K2</span> <span class="o">=</span> <span class="mf">2e-2</span>
<span class="n">K3</span> <span class="o">=</span> <span class="mf">5e-4</span>


<span class="c1">#intermediate calculation</span>
<span class="n">m</span> <span class="o">=</span> <span class="n">m1</span><span class="o">+</span><span class="n">m2</span><span class="o">+</span><span class="n">m3</span>

<span class="c1">#solution</span>
<span class="n">K</span> <span class="o">=</span> <span class="p">(</span><span class="n">m1</span><span class="o">*</span><span class="n">K1</span><span class="o">+</span><span class="n">m2</span><span class="o">*</span><span class="n">K2</span><span class="o">+</span><span class="n">m3</span><span class="o">*</span><span class="n">K3</span><span class="p">)</span><span class="o">/</span><span class="n">m</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;thickness of layer 1 = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">m1</span><span class="p">),</span> <span class="s2">&quot;m</span><span class="se">\n</span><span class="s2">thickness of layer 2 = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">m2</span><span class="p">),</span><span class="s2">&quot;m</span><span class="se">\n</span><span class="s2">thickness of layer 3 = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">m3</span><span class="p">),</span> <span class="s2">&quot;m</span><span class="se">\n\n</span><span class="s2">conductivity of layer 1 = </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K1</span><span class="p">),</span>
      <span class="s2">&quot;m/s</span><span class="se">\n</span><span class="s2">conductivity of layer 2 = </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K2</span><span class="p">),</span> <span class="s2">&quot;m/s</span><span class="se">\n</span><span class="s2">conductivity of layer 3 </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K3</span><span class="p">),</span> <span class="s2">&quot;m/s&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n\033</span><span class="s2">[1mSolution:</span><span class="se">\033</span><span class="s2">[0m</span><span class="se">\n</span><span class="s2">The resulting hydraulic conductivity of the layer system is </span><span class="se">\033</span><span class="s2">[1m</span><span class="si">{:02.1e}</span><span class="s2"> m/s</span><span class="se">\033</span><span class="s2">[0m.&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K</span><span class="p">))</span>
</pre></div>
</div>
</div>
<div class="cell_output docutils container">
<div class="output stream highlight-myst-ansi notranslate"><div class="highlight"><pre><span></span><span class=" -Color -Color-Bold"> Provided are: </span> 

thickness of layer 1 = 3 m
thickness of layer 2 = 2.5 m
thickness of layer 3 = 1.75 m

conductivity of layer 1 = 3.5e-03 m/s
conductivity of layer 2 = 2.0e-02 m/s
conductivity of layer 3 5.0e-04 m/s

<span class=" -Color -Color-Bold">Solution:</span>
The resulting hydraulic conductivity of the layer system is <span class=" -Color -Color-Bold">8.5e-03 m/s</span>.
</pre></div>
</div>
</div>
</div>
</div>
<div class="section" id="case-2-flow-perpendicular-to-layering">
<h3>Case 2 - Flow Perpendicular to Layering<a class="headerlink" href="#case-2-flow-perpendicular-to-layering" title="Permalink to this headline">¶</a></h3>
<p>In the second case the the flow <em>perpendicular</em> to the layering is considered. Just as in the <em>parallel</em> flow case, the aquifer in this case also is a confined aquifer with <span class="math notranslate nohighlight">\(n\)</span> layers (see <a class="reference internal" href="#flow-perpendicular"><span class="std std-numref">Fig. 3</span></a>).</p>
<div class="figure align-center" id="flow-perpendicular">
<a class="reference internal image-reference" href="../../../_images/L5_f3.png"><img alt="../../../_images/L5_f3.png" src="../../../_images/L5_f3.png" style="width: 211.5px; height: 364.0px;" /></a>
<p class="caption"><span class="caption-number">Fig. 3 </span><span class="caption-text">Flow perpendicular to layering</span><a class="headerlink" href="#flow-perpendicular" title="Permalink to this image">¶</a></p>
</div>
<div class="sphinx-bs container pb-4 docutils">
<div class="row docutils">
<div class="d-flex col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2 docutils">
<div class="card w-100 shadow docutils">
<div class="card-header text-center docutils">
<p class="card-text"><strong>Data for a single entire aquifer unit are:</strong></p>
</div>
<div class="card-body text-justify docutils">
<ul class="simple">
<li><p class="card-text"><span class="math notranslate nohighlight">\(A\)</span> = total cross-sectional area</p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(\Delta h\)</span> = total head loss</p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(Q\)</span> = total discharge</p></li>
</ul>
</div>
</div>
</div>
<div class="d-flex col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2 docutils">
<div class="card w-100 shadow docutils">
<div class="card-header text-center docutils">
<p class="card-text">And, the available data for the <em>layered units</em> are:</p>
</div>
<div class="card-body text-justify docutils">
<ul class="simple">
<li><p class="card-text"><span class="math notranslate nohighlight">\(i\)</span> = layer number <span class="math notranslate nohighlight">\(i\)</span> <span class="math notranslate nohighlight">\((i = 1,2,3, \ldots, n)\)</span></p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(m_i\)</span> = thickness of <span class="math notranslate nohighlight">\(i^{th}\)</span> layer</p></li>
<li><p class="card-text"><span class="math notranslate nohighlight">\(K_i\)</span> = Hydraulic conductivity of <span class="math notranslate nohighlight">\(i^{th}\)</span> layer</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p>These data combined with <em>equation of continuity</em> and <em>Darcy’s Law</em> can be used to obtain the effective hydraulic conductivity of the system in which flow is perpendicular to the layers. The following steps are required:</p>
<p>I. Total thickness: <span class="math notranslate nohighlight">\(m = \sum\limits_{i=1}^n m_i \)</span></p>
<p>II.   Equation of continuity: <span class="math notranslate nohighlight">\(Q_i = Q\)</span></p>
<p>II.  Cross-sectional area for layer: <span class="math notranslate nohighlight">\(A_i = A \)</span></p>
<p>IV. Decomposition of head loss: <span class="math notranslate nohighlight">\(\Delta h = \sum\limits_{i=1}^n \Delta h_i \)</span></p>
<p>V. Darcy’s law for layer <span class="math notranslate nohighlight">\(i\)</span>:</p>
<div class="math notranslate nohighlight">
\[Q_i = - A_i K_i \frac{\Delta h_i}{m_i}\]</div>
<div class="math notranslate nohighlight">
\[\Delta h_i = -\frac{Q_i m_i}{A_i K_i} = - \frac{Q m_i}{A K_i}\]</div>
<p>VI. Similarly the Darcy’s law for the homogeneous aquifer to replace the layered system:</p>
<div class="math notranslate nohighlight">
\[Q = - A K \frac{\Delta h}{m}\]</div>
<div class="math notranslate nohighlight">
\[\Delta h = - \frac{Q m}{A K }\]</div>
<p>VII. The head loss from step 4 can be equated with the sum of head loss of each layered unit (from step 5), i.e.,</p>
<div class="math notranslate nohighlight">
\[
\frac{Q\cdot m}{A\cdot K}
=\sum\limits_{i=1}^n\frac{Q\cdot m}{A\cdot K}
\]</div>
<p>The constants <span class="math notranslate nohighlight">\(Q\)</span> and <span class="math notranslate nohighlight">\(A\)</span> can be taken out of the summation, this leads to</p>
<div class="math notranslate nohighlight">
\[
\frac{ {-Q}\cdot m}{ A\cdot K}
=\frac{ {-Q}}{A}\sum\limits_{i=1}^n\frac{m_i}{K_i}
\]</div>
<p>As a result, the effective hydraulic conductivity of a layered system for a flow perpendicular to the layering equals</p>
<div class="math notranslate nohighlight">
\[
K = \frac{m}{\sum\limits_{i=1}^n\frac{m_i}{K_i}}
\]</div>
<p>In the above equation, effective hydraulic conductivity <span class="math notranslate nohighlight">\(K\)</span> is obtained as the <em>weighted harmonic average</em> of layer conductivities <span class="math notranslate nohighlight">\(K_i\)</span>. Weights
correspond to relative thicknesses <span class="math notranslate nohighlight">\(m_i/m\)</span>. Thus, the largest term in the sum contributes most to
the harmonic average and therefore, the effective hydraulic conductivity can be approximated from</p>
<div class="math notranslate nohighlight">
\[
K \approx \frac{m}{{\max\big(\frac{m_i}{K_i}}\big)}
\]</div>
</div>
<div class="section" id="id1">
<h3>Example problem<a class="headerlink" href="#id1" title="Permalink to this headline">¶</a></h3>
<div class="admonition-flow-perpendicular-to-layering admonition">
<p class="admonition-title">Flow perpendicular to layering</p>
<p>Calculate the effective hydraulic conductivity of the layer system consisting of 3 layers if the flow is perpendicular to the layering.</p>
</div>
<div class="cell docutils container">
<div class="cell_input docutils container">
<div class="highlight-ipython3 notranslate"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\033</span><span class="s2">[1m Provided are:</span><span class="se">\033</span><span class="s2">[0m&quot;</span><span class="p">)</span>

<span class="c1">#Thickness of i-th layer [m]</span>
<span class="n">m1</span> <span class="o">=</span> <span class="mi">3</span> 
<span class="n">m2</span> <span class="o">=</span> <span class="mf">2.5</span>
<span class="n">m3</span> <span class="o">=</span> <span class="mf">1.75</span>

<span class="c1">#conductivity of i-th layer [m/s]</span>
<span class="n">K1</span> <span class="o">=</span> <span class="mf">3.5e-3</span>
<span class="n">K2</span> <span class="o">=</span> <span class="mf">2e-2</span>
<span class="n">K3</span> <span class="o">=</span> <span class="mf">5e-4</span>

<span class="c1">#intermediate calculation</span>
<span class="n">m</span> <span class="o">=</span> <span class="n">m1</span><span class="o">+</span><span class="n">m2</span><span class="o">+</span><span class="n">m3</span>

<span class="c1">#solution</span>
<span class="n">K</span> <span class="o">=</span> <span class="n">m</span><span class="o">/</span><span class="p">(</span><span class="n">m1</span><span class="o">/</span><span class="n">K1</span><span class="o">+</span><span class="n">m2</span><span class="o">/</span><span class="n">K2</span><span class="o">+</span><span class="n">m3</span><span class="o">/</span><span class="n">K3</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;thickness of layer 1 = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">m1</span><span class="p">),</span> <span class="s2">&quot;m</span><span class="se">\n</span><span class="s2">thickness of layer 2 = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">m2</span><span class="p">),</span><span class="s2">&quot;m</span><span class="se">\n</span><span class="s2">thickness of layer 3 = </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">m3</span><span class="p">),</span> <span class="s2">&quot;m</span><span class="se">\n\n</span><span class="s2">conductivity of layer 1 = </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K1</span><span class="p">),</span>
      <span class="s2">&quot;m/s</span><span class="se">\n</span><span class="s2">conductivity of layer 2 = </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K2</span><span class="p">),</span> <span class="s2">&quot;m/s</span><span class="se">\n</span><span class="s2">conductivity of layer 3 </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K3</span><span class="p">),</span> <span class="s2">&quot;m/s&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n\033</span><span class="s2">[1mSolution:</span><span class="se">\033</span><span class="s2">[0m</span><span class="se">\n</span><span class="s2">The resulting hydraulic conductivity of the layer system is </span><span class="se">\033</span><span class="s2">[1m</span><span class="si">{:02.1e}</span><span class="s2"> m/s</span><span class="se">\033</span><span class="s2">[0m.&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K</span><span class="p">))</span>
</pre></div>
</div>
</div>
<div class="cell_output docutils container">
<div class="output stream highlight-myst-ansi notranslate"><div class="highlight"><pre><span></span><span class=" -Color -Color-Bold"> Provided are:</span>
thickness of layer 1 = 3 m
thickness of layer 2 = 2.5 m
thickness of layer 3 = 1.75 m

conductivity of layer 1 = 3.5e-03 m/s
conductivity of layer 2 = 2.0e-02 m/s
conductivity of layer 3 5.0e-04 m/s

<span class=" -Color -Color-Bold">Solution:</span>
The resulting hydraulic conductivity of the layer system is <span class=" -Color -Color-Bold">1.6e-03 m/s</span>.
</pre></div>
</div>
</div>
</div>
</div>
<div class="section" id="summary-effective-conductivity-of-layered-aquifers">
<h3>Summary: Effective Conductivity of Layered Aquifers<a class="headerlink" href="#summary-effective-conductivity-of-layered-aquifers" title="Permalink to this headline">¶</a></h3>
<ul class="simple">
<li><p><strong>For flow parallel to layering:</strong> <br>
Effective hydraulic conductivity equals the <em>weighted arithmetic mean</em> of layer conductivities.</p></li>
<li><p><strong>Flow perpendicular to layering:</strong> <br>
Effective hydraulic conductivity equals the <em>weighted harmonic mean</em> of layer conductivities.</p></li>
<li><p><strong>Weights</strong> in both cases are given by relative layer thicknesses <span class="math notranslate nohighlight">\(m_i/m\)</span></p></li>
<li><p>It can be mathematically shown that the harmonic mean of a set of
positive numbers cannot exceed the arithmetic mean of the same set. Both means are identical only if all numbers in the set are identical.
Apart from this very special case, we have</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<blockquote>
<div><p><em><strong><em>harmonic mean &lt; arithmetic mean.</em></strong></em></p>
</div></blockquote>
</div>
<p>This implies that the flow direction perpendicular to the layering is associated with a smaller effective hydraulic conductivity than the flow direction parallel to the layering.</p>
</div>
</div>
<div class="section" id="hydraulic-resistance">
<h2>Hydraulic Resistance<a class="headerlink" href="#hydraulic-resistance" title="Permalink to this headline">¶</a></h2>
<p>The <em>Hydraulic Resistance</em> <span class="math notranslate nohighlight">\((R)\)</span> provide an alternative approach to express conductivity. It is defined as a reciprocal to hydraulic conductivity <span class="math notranslate nohighlight">\((K)\)</span>, i.e.,</p>
<div class="math notranslate nohighlight">
\[
R = \frac{1}{K}
\]</div>
<p>This implies that large <span class="math notranslate nohighlight">\(K\)</span> corresponds to small <span class="math notranslate nohighlight">\(R\)</span> and vice-versa. Considerations about effective hydraulic conductivities of layered
aquifers can be transferred to hydraulic resistances by recalling
that the arithmetic mean of positive numbers coincides with the
harmonic mean of reciprocal numbers and vice versa. This can be used in the following manner:</p>
<ul class="simple">
<li><p><strong>For <em>flow parallel to layering</em>:</strong></p></li>
</ul>
<p>As Effective hydraulic conductivity equals the weighted arithmetic mean of layer conductivities, the reciprocal of this, i.e., the effective hydraulic resistance, will equal the weighted harmonic mean of layer resistances.</p>
<p>Furthermore, if all layer thicknesses are identical <span class="math notranslate nohighlight">\((m_i =\)</span> const.) and flow is parallel to layering, the largest discharge passes through the layer with
highest hydraulic conductivity (smallest hydraulic resistance). In this case, the discharge through each layer is proportional to layer conductivity or inversely proportional to layer resistance.</p>
<ul class="simple">
<li><p><strong>For <em>flow perpendicular to layering</em>:</strong></p></li>
</ul>
<p>In this case the effective hydraulic conductivity equals the weighted harmonic
mean of layer conductivities. This leads to Effective hydraulic resistance equaling the weighted arithmetic mean of layer resistances.</p>
<p>Similar to the <em>flow parallel to the layering,</em> if all layer thicknesses are identical (<span class="math notranslate nohighlight">\(m_i =\)</span> const.) and flow is perpendicular to layering, the largest hydraulic gradient is across the layer with lowest hydraulic conductivity (highest hydraulic resistance). In this case, the <em>head gradient</em> across each layer is proportional to layer resistance or inversely proportional to layer conductivity.</p>
<div class="section" id="id2">
<h3>Example problem<a class="headerlink" href="#id2" title="Permalink to this headline">¶</a></h3>
<div class="admonition-hydraulic-resistance admonition">
<p class="admonition-title">Hydraulic Resistance</p>
<p>Find the hydraulic resistance with the given hydraulic counductivity</p>
</div>
<div class="cell docutils container">
<div class="cell_input docutils container">
<div class="highlight-ipython3 notranslate"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\033</span><span class="s2">[1m Provided are:</span><span class="se">\033</span><span class="s2">[0m </span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="n">K</span> <span class="o">=</span> <span class="mf">5e-4</span> <span class="c1"># m/s, hydraulic conductivity</span>

<span class="c1">#solution</span>
<span class="n">R</span> <span class="o">=</span> <span class="mi">1</span><span class="o">/</span><span class="n">K</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Hydraulic conductivity = </span><span class="si">{:02.1e}</span><span class="s2"> m/s&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n\033</span><span class="s2">[1mSolution:</span><span class="se">\033</span><span class="s2">[0m</span><span class="se">\n\n</span><span class="s2">The resulting hydraulic resistance is </span><span class="se">\033</span><span class="s2">[1m</span><span class="si">{:02.1e}</span><span class="s2"> s/m</span><span class="se">\033</span><span class="s2">[0m.&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">R</span><span class="p">))</span>
</pre></div>
</div>
</div>
<div class="cell_output docutils container">
<div class="output stream highlight-myst-ansi notranslate"><div class="highlight"><pre><span></span><span class=" -Color -Color-Bold"> Provided are:</span> 

Hydraulic conductivity = 5.0e-04 m/s

<span class=" -Color -Color-Bold">Solution:</span>

The resulting hydraulic resistance is <span class=" -Color -Color-Bold">2.0e+03 s/m</span>.
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="aquifer-anisotropy">
<h2>Aquifer Anisotropy<a class="headerlink" href="#aquifer-anisotropy" title="Permalink to this headline">¶</a></h2>
<p>A solid or a porous medium is <strong>isotropic</strong> if its (all) properties are independent of <em>direction.</em> Conversely, a solid or a porous medium is <strong>anisotropic</strong> if at least one of its property is dependent on direction. Thus, isotropic (or anisotropic) property of porous media refines the concept of homogeneity (or heterogeneity). The key difference being that anisotropy of aquifer is associated only with hydraulic conductivity as other aquifer properties like storativity or porosity cannot depend on direction. Groundwater flow (and more so solute transport) is affected by anisotropy. However, in unconsolidated aquifers the impact of heterogeneity is usually more important.</p>
<p>Figure below (<a class="reference internal" href="#iso-anisotropy"><span class="std std-numref">Fig. 4</span></a>) explains the concept of isotropy more clearly. The direction dependency of <span class="math notranslate nohighlight">\(K\)</span> is represented by the arrows diagram.</p>
<div class="figure align-center" id="iso-anisotropy">
<a class="reference internal image-reference" href="../../../_images/L5_f4.png"><img alt="../../../_images/L5_f4.png" src="../../../_images/L5_f4.png" style="width: 637.2px; height: 421.6px;" /></a>
<p class="caption"><span class="caption-number">Fig. 4 </span><span class="caption-text">Isotropy and Anisotropy in aquifers</span><a class="headerlink" href="#iso-anisotropy" title="Permalink to this image">¶</a></p>
</div>
<div class="section" id="anisotropy-and-scale-effects">
<h3>Anisotropy and scale effects<a class="headerlink" href="#anisotropy-and-scale-effects" title="Permalink to this headline">¶</a></h3>
<p>The effective hydraulic conductivity of layered aquifers was shown earlier to depend on the orientation of the flow direction relative to layering, i.e., parallel versus perpendicular. On a larger scale, it may not be possible to identify or resolve heterogeneities associated with example thin layers, small lenses, shape and orientation of grains (see figure above). Nevertheless, <span class="math notranslate nohighlight">\(K\)</span> is found to be direction-dependent when groundwater flow is quantified at the larger scale. In these case, small-scale heterogeneity (e.g., due to layering) expresses itself as anisotropy of hydraulic conductivity at the larger scale.</p>
</div>
<div class="section" id="indices-and-functional-arguments-to-describe-anisotropy">
<h3>Indices and functional arguments to describe anisotropy<a class="headerlink" href="#indices-and-functional-arguments-to-describe-anisotropy" title="Permalink to this headline">¶</a></h3>
<p>One could consider heterogeneity as a property of entirety. While function arguments point towards heterogeneity, <em>indices</em> are
used to express that hydraulic conductivity depends on direction. Considering a 3-D Cartesian coordinate system, the directional dependent hydraulic conductivity can be represented by <span class="math notranslate nohighlight">\(K_x\)</span>, <span class="math notranslate nohighlight">\(K_y\)</span> and <span class="math notranslate nohighlight">\(K_z\)</span> in parallel with the <span class="math notranslate nohighlight">\(x-\)</span>, <span class="math notranslate nohighlight">\(y-\)</span> and <span class="math notranslate nohighlight">\(z-\)</span>axis, respectively. Within these, one could distinguish between horizontal conductivities (<span class="math notranslate nohighlight">\(K_x\)</span> and <span class="math notranslate nohighlight">\(K_y\)</span>) with the vertical conductivity <span class="math notranslate nohighlight">\(K_z\)</span>. More often, anisotropy is observed only between horizontal and vertical directions (i.e., along <span class="math notranslate nohighlight">\(x\)</span> or <span class="math notranslate nohighlight">\(y\)</span> and <span class="math notranslate nohighlight">\(z\)</span> directions), while isotropy is observed along horizontal directions (<span class="math notranslate nohighlight">\(x\)</span> and <span class="math notranslate nohighlight">\(y\)</span> direction). Thus, symbols <span class="math notranslate nohighlight">\(K_h\)</span> representing <span class="math notranslate nohighlight">\(K_x = K_y\)</span> and <span class="math notranslate nohighlight">\(K_v\)</span> representing <span class="math notranslate nohighlight">\(K_z\)</span> can be used to denote horizontal and vertical hydraulic conductivity, respectively.</p>
</div>
<div class="section" id="concept-of-the-hydraulic-conductivity-ellipse">
<h3>Concept of the hydraulic conductivity ellipse<a class="headerlink" href="#concept-of-the-hydraulic-conductivity-ellipse" title="Permalink to this headline">¶</a></h3>
<p>Let us consider an aquifer with horizontal conductivity <span class="math notranslate nohighlight">\(K_h\)</span> and vertical hydraulic conductivity <span class="math notranslate nohighlight">\(K_v\)</span>. Let us assume that the flow in the aquifer is in some arbitrary direction characterized by the angle <span class="math notranslate nohighlight">\(\theta\)</span> between the flow direction and horizontal plane (see <a class="reference internal" href="#k-ellipse"><span class="std std-numref">Fig. 5</span></a>).</p>
<div class="figure align-center" id="k-ellipse">
<a class="reference internal image-reference" href="../../../_images/L5_f5.png"><img alt="../../../_images/L5_f5.png" src="../../../_images/L5_f5.png" style="width: 469.70000000000005px; height: 249.15000000000003px;" /></a>
<p class="caption"><span class="caption-number">Fig. 5 </span><span class="caption-text">hydraulic conductivity ellipse</span><a class="headerlink" href="#k-ellipse" title="Permalink to this image">¶</a></p>
</div>
<p>In this case, it can be shown that the effective hydraulic conductivity <span class="math notranslate nohighlight">\(K\)</span> is</p>
<div class="math notranslate nohighlight">
\[
K = \frac{1}{\frac{\cos^2\theta}{K_h}+\frac{\sin^2\theta}{K_v}} 
\]</div>
<p>If the angle <span class="math notranslate nohighlight">\(\theta\)</span> is varied, the above equation defines an ellipse (also called “hydraulic conductivity ellipse”) with semi-axes equal to <span class="math notranslate nohighlight">\(\surd{K_h}\)</span> and <span class="math notranslate nohighlight">\(\surd{K_v}\)</span>, respectively. The square root of <span class="math notranslate nohighlight">\(K\)</span> can be visualised by the length of a line segment parallel to the direction of flow. This line segment extends from the centre to the perimeter of the ellipse.</p>
</div>
<div class="section" id="id3">
<h3>Example problem<a class="headerlink" href="#id3" title="Permalink to this headline">¶</a></h3>
<div class="admonition-hydraulic-resistance admonition">
<p class="admonition-title">Hydraulic Resistance</p>
<p>Find resulting hydraulic conductivity from provided horizontal and vertical conductivities.</p>
</div>
<div class="cell docutils container">
<div class="cell_input docutils container">
<div class="highlight-ipython3 notranslate"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n\033</span><span class="s2">[1mProvided are:</span><span class="se">\033</span><span class="s2">[0m</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="n">Kh</span> <span class="o">=</span>  <span class="mf">1e-3</span> <span class="c1">#horizontal hydraulic conductivity [m/s]</span>
<span class="n">Kv</span> <span class="o">=</span>  <span class="mf">1e-4</span> <span class="c1">#vertical hydraulic conductivity [m/s]</span>
<span class="n">theta</span> <span class="o">=</span> <span class="mi">50</span> <span class="c1">#angle between flow direction ans horizontal plane [°]</span>

<span class="c1">#solution</span>
<span class="n">K</span> <span class="o">=</span> <span class="mi">1</span> <span class="o">/</span><span class="p">((</span><span class="n">np</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">theta</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="o">/</span><span class="n">Kh</span><span class="p">)</span><span class="o">+</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">theta</span><span class="p">)</span><span class="o">**</span><span class="mi">2</span><span class="o">/</span><span class="n">Kv</span><span class="p">))</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;horizontal hydraulic conductivity = </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">Kh</span><span class="p">),</span> <span class="s2">&quot;m/s</span><span class="se">\n</span><span class="s2">&quot;</span> <span class="s2">&quot;vertical hydraulic conductivity = </span><span class="si">{:02.1e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">Kv</span><span class="p">),</span> <span class="s2">&quot;m/s</span><span class="se">\n</span><span class="s2">&quot;</span>
      <span class="s2">&quot;angle = </span><span class="si">{}</span><span class="s2">°</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">theta</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\033</span><span class="s2">[1mSolution:</span><span class="se">\033</span><span class="s2">[0m</span><span class="se">\n\n</span><span class="s2">The resulting hydraulic conductivity is </span><span class="se">\033</span><span class="s2">[1m</span><span class="si">{:02.1e}</span><span class="s2"> m/s</span><span class="se">\033</span><span class="s2">[0m.&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">K</span><span class="p">))</span>
</pre></div>
</div>
</div>
<div class="cell_output docutils container">
<div class="output stream highlight-myst-ansi notranslate"><div class="highlight"><pre><span></span><span class=" -Color -Color-Bold">Provided are:</span>

horizontal hydraulic conductivity = 1.0e-03 m/s
vertical hydraulic conductivity = 1.0e-04 m/s
angle = 50°

<span class=" -Color -Color-Bold">Solution:</span>

The resulting hydraulic conductivity is <span class=" -Color -Color-Bold">6.2e-04 m/s</span>.
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="combining-heterogeneity-and-anisotropy">
<h2>Combining Heterogeneity and Anisotropy<a class="headerlink" href="#combining-heterogeneity-and-anisotropy" title="Permalink to this headline">¶</a></h2>
<p>The distinction between_Homogeneous, Heterogeneous, isotropic_ and <em>anisotropic</em> aquifer or any combination of them can be more clearly understood from the figure (for vertical <span class="math notranslate nohighlight">\(x-z\)</span> plane).</p>
<div class="figure align-center" id="het-aniso">
<a class="reference internal image-reference" href="../../../_images/L5_f6.png"><img alt="../../../_images/L5_f6.png" src="../../../_images/L5_f6.png" style="width: 705.6500000000001px; height: 523.0500000000001px;" /></a>
<p class="caption"><span class="caption-number">Fig. 6 </span><span class="caption-text">Heterogeneity and Anisotropy in aquifer</span><a class="headerlink" href="#het-aniso" title="Permalink to this image">¶</a></p>
</div>
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
            path: "./contents/flow/lecture_05"
        },
        predefinedOutput: true
    }
    </script>
    <script>kernelName = 'python3'</script>

              </div>
              
        </div>
    </div>
    
    
    <div class='prev-next-bottom'>
        
    <a class='left-prev' id="prev-link" href="../lecture_04/14_darcy_law_K.html" title="previous page">Lecture 4 - Darcy’s Law and Conductivity</a>
    <a class='right-next' id="next-link" href="../lecture_06/16_darcy_law_3D.html" title="next page">Lecture 6: Steady-State Groundwater flow in 3D</a>

    </div>
    <footer class="footer mt-5 mt-md-0">
    <div class="container">
      <p>
        
          By P. K. Yadav, T. Reimann and several others<br/>
        
          <div class="extra_footer">
            <div>
<a href="https://creativecommons.org/licenses/by/4.0/"><img src="https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png"></a>
    All content on this site (unless otherwise specified) is licensed under the <a href="https://creativecommons.org/licenses/by/4.0/">CC BY-NC-SA 4.0 license</a>
</div>

          </div>
      </p>
    </div>
  </footer>
</main>


      </div>
    </div>

    
  <script src="../../../_static/js/index.3da636dd464baa7582d2.js"></script>


    
  </body>
</html>