#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-google_cloud_secret_manager
Version  : 2.15.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/5e/c4/aeae60d3b32fe03ab91340b96f12a4f783bc20d0a16c79e0b3fa5cd308f4/google-cloud-secret-manager-2.15.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/5e/c4/aeae60d3b32fe03ab91340b96f12a4f783bc20d0a16c79e0b3fa5cd308f4/google-cloud-secret-manager-2.15.0.tar.gz
Summary  : Google Cloud Secret Manager API client library
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_cloud_secret_manager-license = %{version}-%{release}
Requires: pypi-google_cloud_secret_manager-python = %{version}-%{release}
Requires: pypi-google_cloud_secret_manager-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Python Client for Secret Manager API
====================================
|stable| |pypi| |versions|

%package license
Summary: license components for the pypi-google_cloud_secret_manager package.
Group: Default

%description license
license components for the pypi-google_cloud_secret_manager package.


%package python
Summary: python components for the pypi-google_cloud_secret_manager package.
Group: Default
Requires: pypi-google_cloud_secret_manager-python3 = %{version}-%{release}

%description python
python components for the pypi-google_cloud_secret_manager package.


%package python3
Summary: python3 components for the pypi-google_cloud_secret_manager package.
Group: Default
Requires: python3-core
Provides: pypi(google_cloud_secret_manager)
Requires: pypi(google_api_core)
Requires: pypi(grpc_google_iam_v1)
Requires: pypi(proto_plus)
Requires: pypi(protobuf)

%description python3
python3 components for the pypi-google_cloud_secret_manager package.


%prep
%setup -q -n google-cloud-secret-manager-2.15.0
cd %{_builddir}/google-cloud-secret-manager-2.15.0
pushd ..
cp -a google-cloud-secret-manager-2.15.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673386322
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_cloud_secret_manager
cp %{_builddir}/google-cloud-secret-manager-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_cloud_secret_manager/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-google_cloud_secret_manager/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
