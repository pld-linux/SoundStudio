Summary:	tk sound editor, with record, playback, and mixer facilities 
Summary(pl):	Edytor d¼wiêku z mo¿liwo¶ci± nagrywania, odtwarzania i miksowania
Name:		SoundStudio
Version:	1.0.5
Release:	1
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
License:	GPL
Source0:	http://prdownloads.sourceforge.net/studio/%{name}-%{version}.tar.gz
Source1:	%{name}.wmconfig
Source2:	studio.xpm
Patch0:		%{name}.patch
URL:		http://studio.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	tcl >= 7.4, tk >= 4.0, sox >= 11, /bin/more

%description
Sound Studio provides a graphical user interface for manipulating
digitized sound. It allows you to record, play and edit sound files in
various formats, such as Microsoft's wav files, Sun's audio files
(.au) and Creative Lab's .voc format. It also provides access to a
sound card's built-in mixer to adjust recording levels and output
volumes. Also Sound Studio provides you with information about the
sample and allows conversion into other formats, sampling rates etc.

%description -l pl
Sound Studio daje graficzny interfejs do obrabiania cyfrowego d¼wiêku.
Pozwala na nagrywanie, odtwarzanie i edycjê plików d¼wiêkowych
w ró¿nych formatach: Microsoft .wav, Sun .au, Creative Labs .voc.
Daje tak¿e dostêp do miksera karty d¼wiêkowej. Pozwala na konwersjê do
innych formatów i czêstotliwo¶ci próbkowania.

%prep
%setup -q -n SoundStudio
%patch0 -p1

%build
MYFILES=%{_libdir}/%{name} SOX_DIR=/usr/bin OPT="%{rpmcflags}" ./build default

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/mini,%{_libdir}/%{name},%{_bindir}}
install studio reset_dsp $RPM_BUILD_ROOT%{_bindir}
install fader maxmin studio_mixer studio_tool $RPM_BUILD_ROOT%{_libdir}/%{name}
install *.tk *.ico $RPM_BUILD_ROOT%{_libdir}/%{name}
install help1.hlp v12.au StudioHelp $RPM_BUILD_ROOT%{_libdir}/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/mini/studio.xpm

# change it to .desktop
#install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/X11/wmconfig
#install $RPM_SOURCE_DIR/SoundStudio.wmconfig $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/SoundStudio

gzip -9nf README

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/studio
%attr(755,root,root) %{_bindir}/reset_dsp
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/fader
%attr(755,root,root) %{_libdir}/%{name}/maxmin
%attr(755,root,root) %{_libdir}/%{name}/studio_mixer
%attr(755,root,root) %{_libdir}/%{name}/studio_tool
%{_libdir}/%{name}/*.tk
%{_libdir}/%{name}/*.ico
%{_libdir}/%{name}/*.hlp
%{_libdir}/%{name}/*.au
%{_libdir}/%{name}/StudioHelp
%{_pixmapsdir}/mini/studio.xpm
#%{_sysconfdir}/X11/wmconfig/SoundStudio
