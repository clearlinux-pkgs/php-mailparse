#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-mailparse
Version  : 3.1.6
Release  : 70
URL      : https://pecl.php.net/get/mailparse-3.1.6.tgz
Source0  : https://pecl.php.net/get/mailparse-3.1.6.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-mailparse-lib = %{version}-%{release}
Requires: php-mailparse-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# mailparse library for PHP
Mailparse is an extension for parsing and working with email messages.

%package lib
Summary: lib components for the php-mailparse package.
Group: Libraries
Requires: php-mailparse-license = %{version}-%{release}

%description lib
lib components for the php-mailparse package.


%package license
Summary: license components for the php-mailparse package.
Group: Default

%description license
license components for the php-mailparse package.


%prep
%setup -q -n mailparse-3.1.6
cd %{_builddir}/mailparse-3.1.6
pushd ..
cp -a mailparse-3.1.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-mailparse
cp %{_builddir}/mailparse-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-mailparse/b5469c326673cd097cc5e081bf40b1d9c0577644 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/mailparse.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-mailparse/b5469c326673cd097cc5e081bf40b1d9c0577644
