Summary: tk sound editor, with record, playback, and mixer facilities 
Name: SoundStudio
Version: 0.9.1
Release: 2
Group: Applications/Sound
Copyright: GPL
Source: http://www.elec-eng.leeds.ac.uk/staff/een6njb/Software/Studio/SoundStudio-0.9.1.tar.gz
URL: http://www.elec-eng.leeds.ac.uk/staff/een6njb/Software/Studio/screens.html
Source1: SoundStudio.wmconfig
Source2: studio.xpm
Patch0: SoundStudio.patch
BuildRoot: /var/tmp/SoundStudio-root
Requires: tcl >= 7.4, tk >= 4.0, sox >= 11, /bin/more


%description
Sound Studio provides a graphical user interface for manipulating
digitised sound. It allows you to record, play and edit sound files
in various formats, such as Microsoft's wav files, Sun's audio files
(.au) and Creative Lab's .voc format.
It also provides access to a sound card's built-in mixer to adjust
recording levels and output volumes. Also Sound Studio provides you
with information about the sample and allows conversion into other
formats, sampling rates etc.

%prep
%setup -q
%patch0 -p1 -b .patch

%build
./install

%install
rm -fr ${RPM_BUILD_ROOT}

mkdir -p ${RPM_BUILD_ROOT}/etc/X11/wmconfig
mkdir -p ${RPM_BUILD_ROOT}/usr/share/icons/mini
install -m755 -d ${RPM_BUILD_ROOT}/usr/lib/${RPM_PACKAGE_NAME}
install -m755 -d ${RPM_BUILD_ROOT}/usr/bin
install -m555 studio reset_dsp ${RPM_BUILD_ROOT}/usr/bin
install -m555 maxmin studio_mixer studio_tool ${RPM_BUILD_ROOT}/usr/lib/${RPM_PACKAGE_NAME}
install -m444 *.tk *.ico ${RPM_BUILD_ROOT}/usr/lib/${RPM_PACKAGE_NAME}
install -m444 help1.hlp matra.wav test.au woof.wav ${RPM_BUILD_ROOT}/usr/lib/${RPM_PACKAGE_NAME}
install -m 644 $RPM_SOURCE_DIR/SoundStudio.wmconfig  $RPM_BUILD_ROOT/etc/X11/wmconfig/SoundStudio
install -m 644 $RPM_SOURCE_DIR/studio.xpm $RPM_BUILD_ROOT/usr/share/icons/mini/studio.xpm

%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc COPYING README StudioHelp studio-${RPM_PACKAGE_VERSION}.lsm  DOCS/*
/usr/bin/studio
/usr/bin/reset_dsp
/usr/lib/SoundStudio
/etc/X11/wmconfig/SoundStudio
/usr/share/icons/mini/studio.xpm

%changelog 
* Sun May  9 1999 Peter Hanecak <hanecak@megaloman.sk>
- changes to allow non-root users to build too (%install)

* Wed Oct 06 1998 Michael Maher <mike@redhat.com>
- rebuilt package for 5.2, fixed RPM.

* Wed May 19 1998 Michael Maher <mike@redhat.com>
- built package
