Start sketching blog post on angular - One way to do web apps in Angular and Django. (It may not be *the* right way but it has worked out great and we learned alot and would probably do some things differently the next time)
    workflow and UI design process
    assigning a URL routing scheme to the comp frames
    factories with hardcoded data (nope we didn't do TDD)
    controllers and views: how to stay DRY?
    web map
        the doozy. Needed fine grained control over vector layers, styling, editing, drawing and selection tools. Directives exist but are not full featured enough. Need a two way data binding and a complete directive that exposes all of the OpenLayers API via a controller's $scope.... Lots of work. Instead, create a map model in POJS (plain old javascript) to manage the state of the map. It's probably more akin to knockout's ViewModel with lots of public functions to e.g. select and edit features or manage layers. These functions get called within controllers. Yep the controllers manipulate the DOM and are no longer loosely coupled or testable without mocks. Faster than writing directives which force you to reinvent the wheel to work with existing javascript libraries. Basically the choice to use angular boils down to this: has someone written a directive that does EXACTLY what I need? If so, choose Angular in a heartbeat. If there's no direct or obvious way to get two-way binding between your DOM Elements and your $scope (because your DOM elements are wrapped behind an existing javascript library), consider alternatives. There are tons of great libraries out there but, to use them in Angular, developers are forced to write directives to bind this library's objects to the scope. Writing directives seems hacky and confusing at first glance and I can't imagine it being much fun to write. But people write directives now for ..... [cite] if it's commonly used, chances are someone has written a module with an angular directive for it. Wasted work or useful abstraction? It depends - it certainly raises the barrier for early adopters who have to spend a great deal of time on reimplimenting details within a framework that purports to make things easier.  

    Functionality first 
    hook into backend
    hurdles: auth, deployment, map
    design -> css

    [] how we built a website
    domain
        spatial data
        conceptual model
        bayes net and calibration
    user experience
        workflow
        design comps process
        html and css implementation
    front end
        Angular
        Bootstrap
        OL3
        Grunt/Bower/Yeoman
    back end
        GeoDjango
        Unit tests
        DRF
        Bayesian Belief Network
        DB
        KeyValue store
        tiles
        Nginx, uwsgi
    devops
        git workflow
        continuous integration
        ansible
        venv, vagrant
        AWS
