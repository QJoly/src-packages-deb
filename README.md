This Github project is a debian Package Collection.

You can build each package with the following command:

```bash
dpkg-deb --build <package>
```

Example:

```bash
dpkg-deb --build packages/hello-world/hello-world_1.0.0-1_all 
#dpkg-deb: building package 'hello-world' in 'packages/hello-world/hello-world_1.0.0-1_all.deb'.
```


## LICENSE

Licensed under the MIT License.

Please respect the license of each package.