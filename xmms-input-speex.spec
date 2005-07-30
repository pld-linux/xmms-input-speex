Summary:	Speex input plugin for XMMS
Summary(pl):	Wtyczka wej¶ciowa dls XMMS-a odtwarzaj±ca pliki w formacie speex
Name:		xmms-input-speex
Version:	0.9.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	speex-xmms-%{version}.tar.gz
# Source0-md5:	788ec657f2d0078396b396a1fb804ff9
Patch0:		%{name}-utf8.patch
BuildRequires:	libogg-devel
BuildRequires:	speex-devel >= 1.0
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speex input plugin for XMMS.

%description -l pl
Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±ca pliki w formacie speex.

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
