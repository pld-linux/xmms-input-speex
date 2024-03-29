Summary:	Speex input plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wejściowa dls XMMS-a odtwarzająca pliki w formacie speex
Name:		xmms-input-speex
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://jzb.rapanden.dk/pub/speex-xmms-%{version}.tar.gz
# Source0-md5:	223a8c8fc7f073c7a7bd4fe6736ed0ee
Patch0:		%{name}-utf8.patch
BuildRequires:	libogg-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	speex-devel >= 1.0
BuildRequires:	xmms-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speex input plugin for XMMS.

%description -l pl.UTF-8
Wtyczka wejściowa dla XMMS-a odtwarzająca pliki w formacie speex.

%prep
%setup -q -n speex-xmms
%patch0 -p1

%build
%{__make} \
	CC="%{__cc} %{rpmcflags} -I%{_includedir}/speex -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_input_plugindir}

install libspeex.so $RPM_BUILD_ROOT%{xmms_input_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{xmms_input_plugindir}/*
