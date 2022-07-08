# altiplano

## Clone Repository in local directory

* create a new directory for the proyect
* cd into the directory with the terminal
* execute the following command:

    ~~~Bash
    git clone --recurse-submodules https://github.com/Addval-Connect/altiplano.git
    ~~~

## Push changes to staging

* checkout to the staging branch Altiplano-Staging

    ~~~Bash
    git checkout Altiplano-Staging
    ~~~

* Make the necesary changes
* Commit the changes to the submoduels, if any:

    ~~~Bash
    cd <submodule/path>
    git add .
    git commit -m "Commit message"
    ~~~

* Push the changes from the submodules:

    ~~~Bash
    cd <submodule/path>
    git push
    ~~~

* Comit the version change and other changes to the staging branch:

    ~~~Bash
    git add .
    git commit -m "Commit message"
    ~~~

* Push the changes to the staging branch:

    ~~~Bash
    git push
    ~~~

## Merge changes to production
