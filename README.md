<!-- start header -->
# PloomberPieplineTemplate
<!-- end header -->





## Description
<!-- start description -->
The purpose of this template is to serve as a useful starting point for any data science pipeline that I want to begin. Most importantly it contains things which I find particularly useful when creating data science pipelines/models that will exist for a long time, such as step-by-step and FAQ documents generation via (nbconvert) and final report generation using python-ppttx which use plotly for graphs as well as pipeline/DAG plotting via ploombers API so that one can very easily see the end-to-end flow of ones project. It also contains things such as `RunMe` and `InstallMe` notebooks which I have found useful for development and in making things more accessible for less technical audiences. It illustrates a lot of the benefits that I think adoption of Ploomber brings about in my use cases and thus can be seen as a sort of "everything/all-in-one/showcase-every-feature-that-ploomber-can-do" project.  
Hopefully its useful to other as well
<!-- end description -->

## Getting the Project/CodeBase Setup
### Install VsCode 
I use VsCode to edit my code. This repo contains helpful configuration settings and recommended extensions in the `.vscode` folder so i'd recommend using VsCode as well if you want the most semaless experience. I don't test anything with other IDE's but it might work on others, however don't quote me on that.
you can find the download for VsCode here 
[https://code.visualstudio.com/Download](https://code.visualstudio.com/Download)
Once VsCode is installed you should be able to clone the repository from github


### Install uv
We'll use uv for package managemnt and dependency resolution. 
so first we need to install it. 
to do this we can use the command line script below
[Script_WingetInstallUv.bat](Script_WingetInstallUv.bat)

### Install all packages
Next we need to install all the packages/dependecies we use (e.g. pandas, plotly, etc).
Its best practise to do this in a virtual environment. Luckily `uv` does a lot of this for us using its uv sync command. 
To do this we can run the command line script below
[Script_UvSync.bat](Script_UvSync.bat)



