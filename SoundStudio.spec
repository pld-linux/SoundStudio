Summary:	Tk sound editor, with record, playback, and mixer facilities
Summary(pl):	Edytor d¼wiêku z mo¿liwo¶ci± nagrywania, odtwarzania i miksowania
Name:		SoundStudio
Version:	1.0.6
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/studio/%{name}-%{version}.tar.gz
# Source0-md5:	673314c074f719460cf08ed27f2b954b
Source1:	%{name}.desktop
Source2:	studio.xpm
Patch0:		%{name}.patch
Patch1:		%{name}-endian.patch
URL:		http://studio.sourceforge.net/
Requires:	tcl >= 7.4
Requires:	tk >= 4.0
Requires:	sox >= 11
Requires:	/bin/more
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch1 -p1

%build
MYFILES=%{_libdir}/%{name} \
SOX_CMD="set SOX_CMD [exec which sox]" \
CC="%{__cc} %{rpmcflags}" \
./build default

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir}/mini,%{_libdir}/%{name},%{_bindir}} \
	$RPM_BUILD_ROOT%{_applnkdir}/Multimedia

install studio reset_dsp $RPM_BUILD_ROOT%{_bindir}
install fader maxmin studio_mixer studio_tool $RPM_BUILD_ROOT%{_libdir}/%{name}
install *.tk *.ico $RPM_BUILD_ROOT%{_libdir}/%{name}
install help1.hlp v12.au StudioHelp $RPM_BUILD_ROOT%{_libdir}/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/mini/studio.xpm
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
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
%{_applnkdir}/Multimedia/SoundStudio.desktop
