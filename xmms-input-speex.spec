Summary:	Speex input plugin for XMMS
Summary(pl):	Wtyczka wej�ciowa formatu speex dla XMMS
Name:		xmms-input-speex
Version:	0.8.0
Release:	3
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.speex.org/download/speex-xmms-nightly.tar.gz
# Source0-md5:	788ec657f2d0078396b396a1fb804ff9
URL:		http://www.speex.org/projects.html
BuildRequires:	libogg-devel
BuildRequires:	speex-devel >= 1.0
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Speex input plugin for XMMS.

%description -l pl
Wtyczka wej�ciowa formatu speex dla XMMS.

%prep
%setup -q -n speex-xmms

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

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
