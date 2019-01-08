FROM aursu/rpmbuild:7-build

USER root
RUN yum -y install \
        perl-Crypt-CBC \
        perl-ExtUtils-MakeMaker \
    && yum clean all && rm -rf /var/cache/yum

COPY SOURCES ${BUILD_TOPDIR}/SOURCES
COPY SPECS ${BUILD_TOPDIR}/SPECS

RUN chown -R $BUILD_USER ${BUILD_TOPDIR}/{SOURCES,SPECS}

USER $BUILD_USER
