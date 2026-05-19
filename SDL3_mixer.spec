Summary:	Simple DirectMedia Layer - Sample Mixer Library
Summary(pl.UTF-8):	Simple DirectMedia Layer - biblioteka miksująca próbki dźwiękowe
Summary(pt_BR.UTF-8):	SDL3 - Biblioteca para mixagem
Name:		SDL3_mixer
Version:	3.2.2
Release:	2
License:	Zlib-like
Group:		Libraries
#Source0Download: https://github.com/libsdl-org/SDL_mixer/releases
Source0:	https://github.com/libsdl-org/SDL_mixer/releases/download/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	413c8188458ac0405450f67bb98eac35
URL:		https://github.com/libsdl-org/SDL_mixer
BuildRequires:	SDL3-devel >= 3.4.0
BuildRequires:	cmake >= 3.16
BuildRequires:	flac-devel >=	 1.3.0
BuildRequires:	fluidsynth-devel
BuildRequires:	game-music-emu-devel
BuildRequires:	libmpg123-devel
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	libxmp-devel >= 4.2
BuildRequires:	opus-devel
BuildRequires:	opusfile-devel >= 0.2
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	rpmbuild(macros) >= 1.527
BuildRequires:	wavpack-devel >= 4.0
Requires:	SDL3 >= 3.4.0
Suggests:	libxmp >= 4.2
Suggests:	opusfile >= 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and MPG123 MP3
libraries.

%description -l pl.UTF-8
SDL3_mixer to prosty wielokanałowy mikser audio. Obsługuje 4 kanały
16-bitowego dźwięku stereo plus jeden kanał dla muzyki miksowanej
przez popularne biblioteki MikMod MOD, Timitity MIDI i MPG123 MP3.

%description -l pt_BR.UTF-8
Biblioteca que suporta 4 canais de áudio estéreo 16 bit, mais um canal
de música, mixado pelo populares bibliotecas MOD MikMod, MIDI timidity
e MPG123 MP3.

%package devel
Summary:	Header files and more to develop SDL_mixer applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwoju aplikacji używających biblioteki SDL_mixer
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL3-devel >= 3.4.0

%description devel
Header files and more to develop SDL3_mixer applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwoju aplikacji używających biblioteki
SDL3_mixer.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SDL3.

%prep
%setup -q

%build
%cmake -B build \
	-DSDLMIXER_STRICT:BOOL=ON \
	-DSDLMIXER_WERROR:BOOL=ON \
	-DSDLMIXER_INSTALL_MAN:BOOL=ON \
	-DSDLMIXER_EXAMPLES_INSTALL:BOOL=OFF \
	-DSDLMIXER_TESTS_INSTALL:BOOL=OFF \
	-DSDLMIXER_VORBIS_STB:BOOL=OFF \
	-DSDLMIXER_VORBIS_VORBISFILE:BOOL=ON \
	-DSDLMIXER_VORBIS_TREMOR:BOOL=OFF \
	-DSDLMIXER_FLAC_LIBFLAC:BOOL=ON \
	-DSDLMIXER_FLAC_DRFLAC:BOOL=OFF \
	-DSDLMIXER_MP3_MPG123:BOOL=ON \
	-DSDLMIXER_MP3_DRMP3:BOOL=OFF \
	-DSDLMIXER_DEPS_SHARED:BOOL=OFF

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/licenses/SDL3_mixer/LICENSE.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AGENTS.md CHANGES.txt CLAUDE.md LICENSE.txt README.md
%{_libdir}/libSDL3_mixer.so.*.*.*
%ghost %{_libdir}/libSDL3_mixer.so.0

%files devel
%defattr(644,root,root,755)
%{_libdir}/libSDL3_mixer.so
%{_libdir}/cmake/SDL3_mixer
%dir %{_includedir}/SDL3_mixer
%{_includedir}/SDL3_mixer/SDL_mixer.h
%{_pkgconfigdir}/sdl3-mixer.pc
%{_mandir}/man3/*.3.*
%{_mandir}/man3/*.3type.*
