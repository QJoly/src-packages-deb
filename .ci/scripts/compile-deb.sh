#!/bin/bash


function build_deb {
    echo "Build .deb files"
    base_dir=$(pwd)
    for folder in $(ls); do
        echo "Build all .debs for $folder"
        cd $folder
        for version in $(ls); do
            echo "Build $version"
            dpkg-deb --build $version
            cd $base_dir/$folder
        done
        cd $base_dir 
    done
    cd $base_dir
}

build_deb
echo "All .deb are compiled."
ARCH=$(dpkg --print-architecture)
find . -iname "**${ARCH}.deb" -exec dpkg -i {} \;
