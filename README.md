## Build process setup

[![CircleCI](https://circleci.com/gh/aursu/rpmbuild-perl-modules.svg?style=svg)](https://circleci.com/gh/aursu/rpmbuild-perl-modules)

[ ![perl-MD5](https://api.bintray.com/packages/aursu/custom/perl-MD5/images/download.svg) ](https://bintray.com/aursu/custom/perl-MD5/_latestVersion)

[ ![perl-Crypt-Blowfish](https://api.bintray.com/packages/aursu/custom/perl-Crypt-Blowfish/images/download.svg) ](https://bintray.com/aursu/custom/perl-Crypt-Blowfish/_latestVersion)

[ ![perl-Mcrypt](https://api.bintray.com/packages/aursu/custom/perl-Mcrypt/images/download.svg) ](https://bintray.com/aursu/custom/perl-Mcrypt/_latestVersion)

[ ![perl-UUID](https://api.bintray.com/packages/aursu/custom/perl-UUID/images/download.svg) ](https://bintray.com/aursu/custom/perl-UUID/_latestVersion)

[ ![perl-CryptX](https://api.bintray.com/packages/aursu/custom/perl-CryptX/images/download.svg) ](https://bintray.com/aursu/custom/perl-CryptX/_latestVersion)

Sections `Prerequisites` and `Setup` should be done only once per build host

### Requirements

* Docker CE 17.12.0+ (https://docs.docker.com/install/)
* Docker Compose 1.10+ (https://github.com/docker/compose/releases/)

### Perl Modules Requirements

No specific requirements

### Prerequisites

1. `Docker` should be installed on build host following these instructions:

    https://docs.docker.com/install/linux/docker-ce/centos/#set-up-the-repository

    and

    https://docs.docker.com/install/linux/docker-ce/centos/#install-docker-ce-1

2. `Docker Compose` should be installed on build host following instructions:

    https://docs.docker.com/compose/install/#install-compose

3. Add your build user into docker group (required to manage docker):

    ```
    usermod -aG docker <username>
    ```

    and relogin

4. Start Docker daemon

    ```
    systemctl enable docker
    systemctl start docker
    ```

5. Port 80 on build host should be free (stop nginx/httpd or move to different
port)

### Setup

1. Clone build repo with submodules (perl-modules is just an example - it could be
any build repo):

    ```
    git clone --recursive git@github.com:aursu/rpmbuild-perl-modules.git
    cd rpmbuild-perl-modules
    ```

2. Setup build environment:

    2.1. Setup rpmbuild base images

    ```
    docker-compose -f rpmbuild/docker-compose.yml pull
    ```

### Build process


1. Build base image

    ```
    docker-compose -f docker-compose.base.yml build
    ```

2. Build packages

    ```
    docker-compose up --build -d
    ```

    command above will start all build serrvices in background. But it is possible
to run any of them or run in foreground etc

3. Wait until command `docker-compose ps` returns all services in state 'Exit 0'

### Access RPM packages

Use `docker cp` command from paths
`/home/centos-6/rpmbuild/RPMS` and `/home/centos-7/rpmbuild/RPMS`

### Complete build

To complete all build processes run commands:

```
docker-compose down
docker-compose -f docker-compose.base.yml down
docker-compose -f rpmbuild/docker-compose.yml down
```

These commands will stop and remove all containers but not build images (see
`docker images` and `docker rmi` commands manuals)
