Summary:	tk sound editor, with record, playback, and mixer facilities 
Name:		SoundStudio
Version:	0.9.1
Release:	2
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
License:	GPL
Source0:	http://www.elec-eng.leeds.ac.uk/staff/een6njb/Software/Studio/%{name}-%{version}.tar.gz
URL:		http://www.elec-eng.leeds.ac.uk/staff/een6njb/Software/Studio/screens.html
Source1:	%{name}.wmconfig
Source2:	studio.xpm
Patch0:		%{name}.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	tcl >= 7.4, tk >= 4.0, sox >= 11, /bin/more

%description
Sound Studio provides a graphical user interface for manipulating
digitised sound. It allows you to record, play and edit sound files in
various formats, such as Microsoft's wav files, Sun's audio files
(.au) and Creative Lab's .voc format. It also provides access to a
sound card's built-in mixer to adjust recording levels and output
volumes. Also Sound Studio provides you with information about the
sample and allows conversion into other formats, sampling rates etc.

%prep
%setup -q
%patch0 -p1 -b .patch

%build
./install

%install
rm -rf $RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/X11/wmconfig
install -d ${RPM_BUILD_ROOT}%{_datadir}/icons/mini
install -m755 -d ${RPM_BUILD_ROOT}%{_libdir}/${RPM_PACKAGE_NAME}
install -m755 -d ${RPM_BUILD_ROOT}%{_bindir}
install -m555 studio reset_dsp ${RPM_BUILD_ROOT}%{_bindir}
install -m555 maxmin studio_mixer studio_tool ${RPM_BUILD_ROOT}%{_libdir}/${RPM_PACKAGE_NAME}
install -m444 *.tk *.ico ${RPM_BUILD_ROOT}%{_libdir}/${RPM_PACKAGE_NAME}
install -m444 help1.hlp matra.wav test.au woof.wav ${RPM_BUILD_ROOT}%{_libdir}/${RPM_PACKAGE_NAME}
install $RPM_SOURCE_DIR/SoundStudio.wmconfig $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/SoundStudio
install $RPM_SOURCE_DIR/studio.xpm $RPM_BUILD_ROOT%{_datadir}/icons/mini/studio.xpm

%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc COPYING README StudioHelp studio-${RPM_PACKAGE_VERSION}.lsm  DOCS/*
%attr(755,root,root) %{_bindir}/studio
%attr(755,root,root) %{_bindir}/reset_dsp
%{_libdir}/SoundStudio
%{_sysconfdir}/X11/wmconfig/SoundStudio
%{_datadir}/icons/mini/studio.xpm
