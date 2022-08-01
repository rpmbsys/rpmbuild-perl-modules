

# rpmbuild-perl-modules 

## Build process setup

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

### Setup

1. Clone build repo with submodules (perl-modules is just an example - it could be
any build repo):

    ```
    git clone --recursive git@github.com:aursu/rpmbuild-perl-modules.git
    cd rpmbuild-perl-modules
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
