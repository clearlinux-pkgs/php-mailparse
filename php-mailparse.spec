#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-mailparse
Version  : 3.1.1
Release  : 9
URL      : https://pecl.php.net/get/mailparse-3.1.1.tgz
Source0  : https://pecl.php.net/get/mailparse-3.1.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-mailparse-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
# mailparse library for PHP 7
Mailparse is an extension for parsing and working with email messages.

%package lib
Summary: lib components for the php-mailparse package.
Group: Libraries

%description lib
lib components for the php-mailparse package.


%prep
%setup -q -n mailparse-3.1.1
cd %{_builddir}/mailparse-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/mailparse.so
