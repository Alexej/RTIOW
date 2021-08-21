
# My implementation of Ray Tracing in One Weekend by Peter Shirley
https://raytracing.github.io/books/RayTracingInOneWeekend.html#diffusematerials/fixingshadowacne

Highly recommend running it with pypy, final scene took around 30mins with pypy and 12 threads.

* Todo
    * add arg parser, had to remove previous stuff(also without argparser animate_script won't work)
    * improve animate_script, add multiple paths/trajectories
    * add rectangles, polygons, obj files, likely will implement most of this stuff on my next rt try
    * implement the second book
    * fix formatting script
    * fix paths in scripts
    * add scenes folder for the animate_script
    * add exceptions
    * add tests
    * add camera position class
    * overall improve/rework raytracing code for better readability
    * add comments / docs
    * name all variables according to pep8 or whatever, remove underscores from arguments
    * profiling (cprofile), speed improvement


giving props to another RTIOW repo for joblib

## Final Scene
![final_scene](https://user-images.githubusercontent.com/49614339/130330611-13bfc94e-6c56-49ad-8bb0-e1c34529647c.png)


## Animated Scene
![video3](https://user-images.githubusercontent.com/49614339/130331032-933480ce-7b56-4dc0-986e-e7dacb857950.gif)
