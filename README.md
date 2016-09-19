Purpose
=======

To download and backup photos stored in https://www.dailyconnect.com.

Build
=====

    cd src
    docker build -t tylo42/daily_connect_download .

Run
===

Before this can work, a cookies.txt file must be placed in the the directory that will be cross mounted.

Replace <Input/output directory> with the directory outside of the container for cross mounting and <YYMMDD> with the date intended for download. Files will be downloaded to the cross mounted directory.

    docker run -v <Input/ouput directory>:/share -it --rm tylo42/daily_connect_download <YYMMDD>


